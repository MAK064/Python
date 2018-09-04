# the soma function for Orcs vs Uruk-Hais
def predict(speed, straight_legged, threshold, w1, w2):
    x = 0
    x = speed * w1 + straight_legged * w2 + threshold
    if x > 0:
        return 1
    else:
        return 0

#import the JMSSNeural functions
from JMSSNeural import *

#this is your training data!
#[speed, straight-leggedness, isorc]
#Extension: read this from your .csv file instead of typing it all in again!
training = [
[0.1,0.2,1],
[0.11,0.3,1],
[0.09,0.32,1],
[0.2,0.09,1],
[0.3,0.32,1],
[0.4,0.36,0],
[0.9,0.5,0],
[0.28,0.71,0],
[0.5,0.42,0],
[0.78,0.37,0]
]

#define your learning rate and number of epochs
#this is up to you!
learning_rate = 0.1
epochs = 50

# this will conduct the training over the specified number of epochs and
# using the learning rate
weights = train(training, learning_rate, epochs)

# show me the answers for the weights
# weights[0] = threshold
# weights[1] = w1
# weights[2] = w2
print("The trained weights are: ", weights)


# now use the weights (outputted from the previous run)
# to PREDICT whether the creature is an orc or not given:
#   a speed and straight-leggedness value
print(predict(speed = 0.28, \
           straight_legged = 0.1, \
           threshold = 0.1, \
           w1 = -0.2, \
           w2 = -0.09199999999999993))
