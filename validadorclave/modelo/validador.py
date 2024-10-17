from abc import ABC, abstractmethod
import re

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
    def contiene_caracter_especial(self, clave):
        return bool(re.search(r'[@_#$%]', clave))
    
    def es_valida(self, clave):
        if not self._contiene_mayuscula(clave):
            return False
        if not self._contiene_minuscula(clave):
            return False
        if not self._contiene_numero(clave):
            return False
        if not self.contiene_caracter_especial(clave):
            return False
        return True
    

class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(self, clave):
        return 'calisto' in clave.lower()
    
    def es_valida(self, clave):
        if not self._contiene_mayuscula(clave):
            return False
        if not self._contiene_minuscula(clave):
            return False
        if not self._contiene_numero(clave):
            return False
        if not self.contiene_caracter_especial(clave):
            return False
        return True
        
