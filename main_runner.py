import argparse
from siganalogies_grabber import dataset_maker

if __name__ == "__main__":
    # Inputs
    # --epochs = epochs to train for
    # --dataset = '2016' or '2019' for siganalogies
    # --language = language
    # --n_analogies = number of analogies

    parser = argparse.ArgumentParser(prog="morpho_analogy",
                                     description='Parsing arguments for both retrieving data and training'
                                     )

    parser.add_argument("--epochs", metavar='ep', type=int, nargs=1,
                        help='number of epochs to train for',
                        default=100
                        )

    parser.add_argument("--dataset", metavar='dataset', type=str,
                        help='2016 or 2016 sigmorphon datset',
                        default=2016)

    parser.add_argument("--language", metavar='language', type=str,
                        help='a language in the siganalogies dataset',
                        default='english')

    parser.add_argument('--n_analogies', metavar='n_analogies', type=int, nargs=1,
                        help='number of analogies to train on',
                        default=100)

    args = parser.parse_args()

    # languages = "english", "finnish", "french", "german", "portuguese", "spanish"
    EPOCHS = args.epochs
    LANGUAGE = args.language
    DATASET = args.dataset
    N_ANALOGIES = args.n_analogies

dataset = dataset_maker(DATASET, LANGUAGE)