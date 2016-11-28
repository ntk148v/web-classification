import multiprocessing as mp

from classification import classifier
from classification import utils


def main():
    # Modify your classification/conf.py first to use db.
    print('---------------- K-NN + TF IDF + ENG -------------------')
    clf1 = classifier.Classifier('K-NN', 'TF IDF', is_eng=True)
    utils.save(clf1, clf1.pickle_file)
    print('---------------- K-NN + Bag Of Words + ENG --------------')
    clf2 = classifier.Classifier('K-NN', 'Bag Of Words', is_eng=True)
    utils.save(clf2, clf2.pickle_file)
    print('---------------- SVM + TF IDF + ENG ---------------------')
    clf3 = classifier.Classifier('SVM', 'TF IDF', is_eng=True)
    utils.save(clf3, clf3.pickle_file)
    print('---------------- SVM + Bag Of Words + ENG ---------------')
    clf4 = classifier.Classifier('SVM', 'Bag Of Words', is_eng=True)
    utils.save(clf4, clf4.pickle_file)


if __name__ == '__main__':
    mp.set_start_method('forkserver', force=True)
    main()
