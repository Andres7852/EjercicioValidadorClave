from abc import ABC, abstractmethod
import re
from .errores import (NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, 
                      NoTieneNumeroError, NoTieneCaracterEspecialError)

class ReglaValidacion(ABC):
    @abstractmethod
    def es_valida(self, clave):
        pass

    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)


class ReglaValidacionGanimedes(ReglaValidacion):
    def _validar_longitud(self, clave):
        return 8 <= len(clave) <= 20

    def contiene_caracter_especial(self, clave):
        return bool(re.search(r'[@_#$%]', clave))
    
    def es_valida(self, clave):
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError
        if not self.contiene_calisto(clave):
            raise NoTieneCaracterEspecialError
        return True
    

class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(self, clave):
        return 'calisto' in clave.lower()
    
    def es_valida(self, clave):
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError
        if not self.contiene_calisto(clave):
            raise NoTieneCaracterEspecialError
        return True
        
class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)