from NeuralNetworkBase import *

new_data = [[0.3,0.5],[0.6,0.6]]

data = MattNeural.readData("orcs.csv")
weights = MattNeural.training(data, 0.01, 70)
MattNeural.run(new_data, weights)
