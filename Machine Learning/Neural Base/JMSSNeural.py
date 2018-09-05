#JMSSNeural v0.5

# the heaviside step function
def step(signal):
    if signal > 0:
        return 1
    else:
        return 0

# the summation of weights (including bias) and inputs
# note that the last input value (the 'answer') is ignored
# ^^ this assumes that the input values contain an answer!
# so not suitable for feedforward summation
def perceptron_train(input_values, weights):
    # weights 0 is the bias
    total = weights[0]
    i = 0
    while i < len(input_values)-1:
        total += input_values[i] * weights[i + 1]
        i += 1
    return step(total)

# used for feedforward summation
def perceptron(input_values, weights):
    # weights 0 is the bias
    total = weights[0]
    i = 0
    while i < len(input_values):
        total += input_values[i] * weights[i + 1]
        i += 1
    return step(total)

# Train Perceptron weights using gradient descent
def train(dataset, learning_rate, epochs):
    weights = [0.0 for i in range(len(dataset[0]))]
    for epoch in range(epochs):
            sum_error = 0.0
            for row in dataset:
                prediction = perceptron_train(row, weights)
                error = row[-1] - prediction
                sum_error += error**2
                # weight 0 is the bias
                weights[0] = weights[0] + learning_rate * error
                for i in range(len(row)-1):
                    weights[i + 1] = weights[i + 1] + learning_rate * error * row[i]
    return weights
