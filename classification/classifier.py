import logging
import numpy as np
import pickle
# from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from classification import conf
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
        self.estimator = None
        self.is_saved = False
        self.pickle_file = conf.SAVED_DIR + self.algorithm + \
            '_' + self.text_extract_type + '.pickle'
        self.train()

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

    # def _set_estimator(self, params):
    #     """Set estimator instance.

    #     :param dict params: parameters.
    #     """
    #     if self.algorithm == 'SVM':
    #         if params['kernel'] == 'rbf':
    #             self.estimator = SVC(kernel=params['kernel'], C=params['C'],
    #                                  gamma=params['gamma'])
    #         if params['kernel'] == 'linear':
    #             self.estimator = SVC(kernel=params['kernel'], C=params['C'])
    #     else:
    #         self.estimator = KNeighborsClassifier(
    #             n_neighbors=params['n_neighbors'],
    #             metric=params['metric'])

    def word_to_vector(self):
        """Convert from text to vector."""
        contents, labels = self.load_train_set()
        if self.text_extract_type == 'Bag Of Words':
            self.X = utils.bag_of_words(contents)
        else:
            self.X = utils.td_idf(contents)

        self.y = np.array(labels)

    def _tuning_parameters(self):
        """Tuning the hyper-parameters of an estimator."""

        if self.algorithm == 'SVM':
            tmp_estimator = SVC(C=1)
            pre_tune_params = conf.SVM_PARAMS
        else:
            tmp_estimator = KNeighborsClassifier()
            pre_tune_params = conf.KNN_PARAMS

        grid_search = GridSearchCV(tmp_estimator, pre_tune_params, cv=5)
        grid_search.fit(self.X, self.y)
        LOG.info('Tuning the hyper-parameters of an {} estimator' .
                 format(self.algorithm))
        self.estimator = grid_search.best_estimator_

    def train(self):
        self.word_to_vector()
        if not self.estimator:
            self._tuning_parameters()
        else:
            self.estimator.fit(self.X)

    def predict(self, X):
        self.estimator.predict(X)

    def evaluate(self, X, y, estimator, test_size=0.4, confusion=False):
        pass

    def save(self):
        """Save Classifier object to file with pickle."""
        LOG.info('Saving Classifier object to {}' . format(self.pickle_file))
        pickle.dump(self, open(self.pickle_file, 'wb'))
        self.is_saved = True

    def load(self):
        """Load Classifier object from file with pickle."""
        if self.is_saved:
            LOG.info('Loading saved Classifier object from {}' .
                     format(self.pickle_file))
            return pickle.loads(open(self.pickle_file, 'rb'))
        else:
            LOG.info('Unsaved object, try Classifier.save()')
            return None
