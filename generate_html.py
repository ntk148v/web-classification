from os import listdir
from os.path import isfile, join

from classification import conf
from classification import utils


def main(pickle_path):
    clf = utils.load(pickle_path)
    html_path = clf.algorithm + '_' + clf.text_extract_type + '.html'
    utils.visualize(clf.X, clf.y, clf.estimator, path=html_path)


if __name__ == '__main__':
    pickle_dir = conf.SAVED_DIR
    pickle_files = [f for f in listdir(pickle_dir) if isfile(join(pickle_dir, f))]

    for f in pickle_files:
        main(pickle_dir + f)
