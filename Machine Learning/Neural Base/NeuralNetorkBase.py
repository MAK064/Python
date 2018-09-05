from ReadWrite import *
from JMSSNeural import *

operate = FileOperations()

def axon(ax_in):
    output = 1
    if ax_in < 0:
        output = 0
    return output

def soma(dimension_list, weight_list):
    x = 0
    for line in range(0,len(dimension_list)-1):
        x += dimension_list[line] * weight_list[line+1]
    x += weight_list[0]
    y = axon(x)
    return y

textIn = open("orcs.csv", "r")
Orcs = operate.FileFindLines(textIn)
textIn.close()
training_data = []

for i in range(1,len(Orcs)-1):
    line_data = [float(j) for j in Orcs[i].split(",")]
    training_data.append(line_data)
learn_rate = 0.01
epochs = 7000

weights = train(training_data,learn_rate,epochs)
print(weights)
print(training_data)

for i in range(0, len(training_data)):
    print(soma(training_data[i],weights))
