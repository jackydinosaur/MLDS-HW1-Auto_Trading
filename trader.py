# You can write code above the if-main block.
from models.trader2 import Trader
import pandas as pd

def load_data(data):
    data = pd.read_csv(data,header=None)
    return data

test_data = pd.read_csv('../testing_data.csv')

if __name__ == "__main__":
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--training", default="training_data.csv", help="input training data file name")
    parser.add_argument("--testing", default="testing_data.csv", help="input testing data file name")
    parser.add_argument("--output", default="output.csv", help="output file name")
    args = parser.parse_args()

    # The following part is an example.
    # You can modify it at will.
    training_data = load_data(args.training)
    trader = Trader()
    trader.train(training_data)

    testing_data = load_data(args.testing).to_numpy()
    position = 0
    with open(args.output, "w") as output_file:
        for day, row in enumerate(testing_data):
            # We will perform your action as the open price in the next day.
            action = trader.predict_action(day, row, position)
            position = action[1]

            if day < 19:
                output_file.write(action[0])
                output_file.write('\n')
            # this is your option, you can leave it empty.
            # trader.re_training()
