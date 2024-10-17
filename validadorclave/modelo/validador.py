from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_minima=8):
        self.longitud_minima = longitud_minima

    @abstractmethod
    def es_valida(self, clave):
        pass
