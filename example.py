import datetime
import multiprocessing as mp

from classification import classifier
from classification import utils


ALGORITHM = ['SVM', 'K-NN']
TEXT_EXTRACT = ['TF IDF', 'Bag Of Words']


def run_time(algorithm, text_extract):
    start = datetime.datetime.now()
    print('#### {} + {} + ENG ####' . format(algorithm, text_extract))
    clf = classifier.Classifier(algorithm, text_extract, is_eng=True)
    utils.save(clf, clf.pickle_file)
    finish = datetime.datetime.now()
    print('#### Complete after : {} ####' . format(finish - start))


def main():
    # Modify your classification/conf.py first to use db.
    for a in ALGORITHM:
        for t in TEXT_EXTRACT:
            run_time(a, t)


if __name__ == '__main__':
    mp.set_start_method('forkserver', force=True)
    main()
