import os
import numpy as np


# MySQL Constants

MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'PASSWORD'
MYSQL_DB = 'DB_NAME'

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
