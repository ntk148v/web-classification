import logging
import nltk
import os
import pickle
import pymysql
import sqlite3
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from classification import conf


nltk.download('stopwords')
LOG = logging.getLogger(__name__)
ENG_STOPWORDS = set(nltk.corpus.stopwords.words('english'))
NON_ENG_STOPWORDS = set(nltk.corpus.stopwords.words()) - ENG_STOPWORDS


def is_english(text):
    """Detect language is English or not (Vietnamese)"""
    text = text.lower()
    words = set(nltk.wordpunct_tokenize(text))
    return len(words & ENG_STOPWORDS) > len(words & NON_ENG_STOPWORDS)


def get_stop_words(is_eng=True):
    """Get language's stopwords

    :param boolean is_eng: True if English.
    """
    if is_eng:
        return 'english'
    else:
        with open(conf.VN_SW) as f:
            vn_stopwords = f.read().splitlines()
        return vn_stopwords


def bag_of_words(data, is_eng=True):
    """Convert a list of strings (contents) to a BOW representation of it.

    :param str data: list of strings.
    :param boolean is_eng: True if English.
    :rtype: scipy.sparse.coo_matrix
    """
    vectorizer = CountVectorizer(stop_words=get_stop_words(is_eng),
                                 token_pattern=r'\b[^\W\d_]+\b')
    LOG.info('Convert contents to BOW.')
    return vectorizer.fit_transform(data)


def td_idf(data, is_eng=True):
    """Convert a list of strings (contents) to a TF_IDF representation of it.

    :param str data: list of strings.
    :param boolean is_eng: True if English.
    :rtype:
    """
    tf_transformers = TfidfTransformer(use_idf=True).fit_transform(
        bag_of_words(data, is_eng))
    LOG.info('Convert contents to TF-IDF.')
    return tf_transformers


def get_data_from_db(query, rows, engine=conf.DB_ENGINE):
    """Connect to database and get data from it.

    :param str query: sql query.
    :param int rows: number of rows.
    :param str engine: database engine.
                       default is MySQL.
    :rtype: list
    """
    # Initialize `connection` var to None. In case we could not
    # create a connection to the database(for ex the disk is full)
    # we would not have a connection var defined.
    connection = None
    try:
        if engine.lower() == 'mysql':
            connection = pymysql.connect(host=conf.MYSQL_HOST,
                                         port=conf.MYSQL_PORT,
                                         user=conf.MYSQL_USER,
                                         password=conf.MYSQL_PASSWORD,
                                         db=conf.DB,
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.
                                         DictCursor)
        elif engine.lower() == 'sqlite':
            connection = sqlite3.connect(conf.DB)
        LOG.info('Connect to {} db - {}' . format(engine, conf.DB))

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchmany(rows)
            LOG.info('Get data from database.')
        return result
    except Exception as e:
        LOG.exception('Failed when connecting to database: {}. ' . format(e))
    finally:
        if connection:
            LOG.info('Close database connection.')
            connection.close()


def save(obj, path):
    if os.path.isfile(path):
        LOG.info('File existed! Use load() method.')
    else:
        pickle.dump(obj, open(path, 'wb'), pickle.HIGHEST_PROTOCOL)


def load(path):
    if not os.path.isfile(path):
        LOG.info('File doesnt existed!')
        raise IOError()
    else:
        return pickle.load(open(path, 'rb'))


def evaluate(self, X, y, estimator, test_size=0.4, confusion=False):
    """Evaluate algorithm.
    :param numpy matrix X: dataset.
    :param numpy matrix y: label matrix.
    :param float test_size: testset's size/alldataset's size.
    :param boolean confusion: use confusion matrix or not.
    """
    LOG.info('Evaluate with test_size is %2.0f%%' % (test_size * 100))
    # Split into a training and testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=test_size)
    estimator.fit(X_train, y_train)
    y_predicted = estimator.predict(X_test)

    if not confusion:
        return classification_report(y_test, y_predicted)
    else:
        return confusion_matrix(y_test, y_predicted)
