from ReadWrite import *
from JMSSNeural import *

operate = FileOperations()

class MattNeural:
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
        y = MattNeural.axon(x)
        return y

    def readData(file_in):
        textIn = open(file_in, "r")
        Orcs = operate.FileFindLines(textIn)
        textIn.close()
        formatted_data = []
        for i in range(1,len(Orcs)-1):
            line_data = [float(j) for j in Orcs[i].split(",")]
            formatted_data.append(line_data)
        return formatted_data

    def training(data_list, learn_rate = 0.1, epochs = 50):
        weights = train(data_list, learn_rate, epochs)
        print("Weights used: " + str(weights))
        print("\nTraining data used: \n" + str(data_list))
        return weights

    def run(input, weights):
        output = ""
        print("\nResults:\n")
        for i in range(0, len(input)):
            output += str(MattNeural.soma(input[i],weights)) + ("\n")
        print(output)

"""
from NeuralNetworkBase import *

data = MattNeural.readData("orcs.csv")
weights = MattNeural.training(data, 0.01, 7000)
MattNeural.run(data, weights)
"""
