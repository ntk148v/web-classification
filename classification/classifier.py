import logging
import numpy as np
# import pickle
# from sklearn.model_selection import train_test_split
# from sklearn.model_selection import GridSearchCV
# from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from classification import utils


LOG = logging.getLogger(__name__)


class Classifier(object):

    """Classifier class"""

    def __init__(self, algorithm, text_extract_type):
        """
        :param str algorithm: choosen algorithm will be used to classify.
        :param str text_extract_type: text extraction (Bag of Words & TF_IDF).
        """
        self.algorithm = algorithm
        self.text_extract_type = text_extract_type

    def load_train_set(self):
        """Load train set from database."""
        query = "SELECT `id`, `content`, `label`, `link` FROM `news_dantri`"
        train_set = utils.get_data_from_db(query, 10000)

        contents = []
        labels = []
        for p in train_set:
            contents.append(p['content'])
            labels.append(p['label'])
        return (contents, labels)

    def _set_estimator(self, params):
        if self.algorithm is 'SVM':
            self.estimator = SVC(kernel=params['kernel'], C=params['C'],
                                 gamma=params['gamma'])
        else:
            self.estimator = KNeighborsClassifier(
                n_neighbors=params['n_neighbors'],
                metric=params['metric'])

    def word_to_vector(self):
        """Convert from text to vector."""
        contents, labels = self.load_train_set()
        if self.text_extract_type is 'Bag Of Words':
            self.X = utils.bag_of_words(contents)
        else:
            self.X = utils.td_idf(contents)

        self.y = np.array(labels)

    def _tunning_parameters(self):
        """Tuning the hyper-parameters of an estimator."""
        self._set_estimator()

    def train(self):
        pass

    def predict(self, X):
        pass

    def evaluate(self, X, y, estimator, test_size=0.4, confusion=False):
        pass

    def save_estimator(self, clf):
        pass

    def load_estimator(self):
        pass
