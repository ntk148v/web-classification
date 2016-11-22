import logging
import numpy as np
# from sklearn.metrics import classification_report
# from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.multiclass import OneVsOneClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from classification import conf
from classification import utils


LOG = logging.getLogger(__name__)


class Classifier(object):

    """Classifier class"""

    def __init__(self, algorithm, text_extract_type, is_eng=True):
        """
        :param str algorithm: choosen algorithm will be used to classify.
        :param str text_extract_type: text extraction (Bag of Words & TF_IDF).
        :param boolean is_eng: language can be eng or vi.
        """
        self.algorithm = algorithm
        self.text_extract_type = text_extract_type
        self.is_eng = is_eng
        self.estimator = None
        self.pickle_file = conf.SAVED_DIR + self.algorithm + \
            '_' + self.text_extract_type + '-' + self.language + '.pickle'
        self.train()

    def load_train_set(self):
        """Load train set from database."""
        query = "SELECT `id`, `content`, `label`, `link` FROM " +\
                conf.TRAINING_TABLE
        train_set = utils.get_data_from_db(query, 10000)

        contents = []
        labels = []
        for p in train_set:
            contents.append(p['content'])
            labels.append(p['label'])
        return (contents, labels)

    def word_to_vector(self):
        """Convert from text to vector."""
        contents, labels = self.load_train_set()
        if self.text_extract_type == 'Bag Of Words':
            self.X = utils.bag_of_words(contents, self.is_eng)
        else:
            self.X = utils.td_idf(contents, self.is_eng)

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
        self.estimator = OneVsOneClassifier(grid_search.best_estimator_) \
            if self.algorithm == 'SVM' else grid_search.best_estimator_

    def train(self):
        self.word_to_vector()
        if not self.estimator:
            self._tuning_parameters()
        else:
            self.estimator.fit(self.X, self.y)

    def predict(self, X):
        self.estimator.predict(X)

    def evaluate(self, X, y, estimator, test_size=0.4, confusion=False):
        pass
