from abc import ABC, abstractmethod

class Classifier(ABC):
    """
    Interface para modelos de classificação.
    Contem métodos para treinamento e inferência.
    """
    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass