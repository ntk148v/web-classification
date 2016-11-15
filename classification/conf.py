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

K-NN_PARAMS = {
    'n_neighbors': np.range(1, 31, 2).
    'metric': ['euclidean', 'minkowski', 'manhattan']
}
