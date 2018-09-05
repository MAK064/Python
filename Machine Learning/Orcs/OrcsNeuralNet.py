from NeuralNetworkBase import *

data = MattNeural.readData("orcs.csv")
weights = MattNeural.training(data, 0.01, 7000)
MattNeural.run(data, weights)
