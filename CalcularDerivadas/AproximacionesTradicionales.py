import numpy as np
from numpy.fft import fft, ifftshift

def AproximacionTradicional(x, dx, orden):
    largo = len(x)
    puntoMedio = int(np.floor(largo / 2))

    y = np.zeros(largo)
    valores = np.array([210, -120, 45, -10, 1])
    #valores = np.array([-56, 28, -8, 1])
    sumaTotal = np.sum(valores)

    for i, valor in enumerate(valores):
        valor /= 2 * (i + 1) * sumaTotal
        y[puntoMedio + i + 1] = -valor
        y[puntoMedio - i - 1] = valor

    y = fft(ifftshift(y / dx))
    return (y) ** orden

def AproximacionIntegralTradiciona(x, dx):
    largo = len(x)
    puntoMedio = int(np.floor(largo / 2))

    y = np.zeros(largo)
    y[:puntoMedio] = dx

    return -fft(ifftshift(y))