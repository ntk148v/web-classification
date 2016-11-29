import os
import numpy as np


# MySQL Constants

MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'PASSWORD'

# Database
DEFAULT_DB_ENGINE = 'MYSQL'
MYSQL_DB = 'DB_NAME'
SQLITE_DB = 'DB_PATH - e.x: /home/user/data.sqlite'

# [Notice]: Depend on DB Engine you choose, queries are different.
# In MySQL, is RAND(), but in SQLite, it is RANDOM().
QUERY = """SELECT `id`, `content`, `type`
        FROM `news`
        ORDER BY RANDOM()
        LIMIT 1000"""
NUMBER_ROWS = 1000
# Tunning Parameters

SVM_PARAMS = [
    {
        'kernel': ['rbf'],
        'gamma': [1e-3, 1e-4],
        'C': [1, 10, 100, 1000]
    },
    {
        'kernel': ['linear'],
        'C': [1, 10, 100, 1000]
    }
]

KNN_PARAMS = {
    'n_neighbors': np.arange(1, 31, 2),
    'metric': ['euclidean', 'minkowski', 'manhattan']
}

# Saved DIR path

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
SAVED_DIR = CURRENT_DIR + '/saved/'

# Vietnam stopwords file

VN_SW = CURRENT_DIR + 'vietnamese-stopwords-dash.txt'
