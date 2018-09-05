from NeuralNetworkBase import *

training_data = MattNeural.readData("sonar.training-data.csv")
testing_data = MattNeural.readData("sonar.testing-data.csv")

weights = MattNeural.training(training_data, 0.01, 700)
MattNeural.run(testing_data, weights)
