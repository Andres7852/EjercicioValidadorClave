from .validador import (Validador, ReglaValidacionGanimedes, ReglaValidacionCalisto)

from .errores import (NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, 
                      NoTieneNumeroError, NoTieneCaracterEspecialError)


def main():
    validador_ganimedes = Validador(ReglaValidacionGanimedes())
    validador_calisto = Validador(ReglaValidacionCalisto())

    clave = input("Introduce una clave para validar: ")

    try:
        if validador_ganimedes.es_valida(clave):
            print("La clave es válida según la regla de Ganimedes.")
    except (NoTieneLetraMayusculaError, NoTieneLetraMinusculaError,
            NoTieneNumeroError, NoTieneCaracterEspecialError) as e:
        print(f"Error de validación con la regla de Ganimedes: {str(e)}")

    try:
        if validador_calisto.es_valida(clave):
            print("La clave es válida según la regla de Calisto.")
    except (NoTieneLetraMayusculaError, NoTieneLetraMinusculaError,
            NoTieneNumeroError, NoTieneCaracterEspecialError) as e:
        print(f"Error de validación con la regla de Calisto: {str(e)}")

if __name__ == "__main__":
    main()