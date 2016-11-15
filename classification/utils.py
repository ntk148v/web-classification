import logging
from configparser import ConfigParser
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from classification import conf


parser = ConfigParser()
LOG = logging.getLogger(__name__)

parser.read('conf.ini')


def get_stop_words(language):
    pass


def bag_of_words(data):
    """Convert a list of strings (contents) to a BOW representation of it.

    :param str data: list of strings.
    :rtype: scipy.sparse.coo_matrix
    """
    vectorizer = CountVectorizer(stop_words=get_stop_words(),
                                 token_pattern=r'\b[^\W\d_]+\b')
    LOG.info('Convert contents to BOW.')
    return vectorizer.fit_transform(contents)


def td_idf(data):
    """Convert a list of strings (contents) to a TF_IDF representation of it.

    :param str data: list of strings.
    :rtype:
    """
    tf_transformers = TfidfTransformer(use_idf=True).fit(bag_of_words())
    LOG.info('Convert contents to TF-IDF.')
    return tf_transformers


def get_data_from_db(query, rows):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchmany(rows)
            LOG.info('Get data from database.')
            return result
    finally:
        LOG.info('Close database connection.')
        connection.close()


def get_db_connection():
    connection = pymysql.connect(host=conf.MYSQL_HOST,
                                 port=conf.MYSQL_PORT,
                                 user=conf.MYSQL_USER,
                                 password=conf.MYSQL_PASSWORD,
                                 db=conf.MYSQL_DB,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    LOG.info('Connect to db {}' . format(parser.get('mysql', 'db')))
    return connection
