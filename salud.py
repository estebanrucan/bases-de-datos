def centimetros_a_metros(cm):
    return cm / 100

def meses_a_anios(meses):
    return meses / 12

def IMC(kg, m):
    imc = kg / m ** 2
    return imc

def fc_maxima(edad):
    return 220 - edad

def porcentaje_grasa(kg, m, edad, sexo):
    if sexo == 'masculino':
        porcentaje_grasa = (1.2 * (kg / m**2)) + (0.23 * edad) - 16.2
    elif sexo == 'femenino':
        porcentaje_grasa = (1.2 * (kg / m**2)) + (0.23 * edad) - 5.4
    else:
        return None
    return porcentaje_grasa