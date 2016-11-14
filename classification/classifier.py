class Classifier(object):
    """Classifier class"""

    def __init__(self, algorithm, text_extract_type, parameters=None):
    	"""
        :param algorithm(str): choosen algorithm will be used to classify.
        :param text_extract_type(str): text extraction (Bag of Words & TF_IDF).
        :param parameter(dict): parameter for algorithm method.
        """
        self.algorithm = algorithm
        self.text_extract_type = text_extract_type
        self.parameters = parameters

    def _set_estimator(self):
        pass

    def _tunning_parameters(self):
        pass

    def train(self):
        pass

    def predict(self, X):
        pass

    def evaluate(self, X, y, estimator, test_size=0.4, confusion=False):
        pass

