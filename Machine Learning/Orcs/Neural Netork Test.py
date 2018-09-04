from ReadWrite import *
from JMSSNeural import *

operate = FileOperations()

def axon(ax_in):
    output = 1
    if ax_in <= 0:
        output = 0
    return output

def soma(speed, straight_legged, threshold, w1, w2):
    x = 0
    x = straight_legged*w1 + speed*w2 + threshold
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

for i in range(1, len(training_data)):
    print(soma(training_data[i][0],training_data[i][1],weights[0],weights[1],weights[2]))
