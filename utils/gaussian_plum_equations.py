from stability_classes import stability_classes
import numpy as np

ROUND_VALUE = True
ROUNDING_DIGITS = 4

def sigma_y(x, stability_class):
    a = stability_classes[stability_class]["a"]
    b = stability_classes[stability_class]["b"]
    sigma = np.float64(a * np.power(x,b))
    if ROUND_VALUE:
        return np.round(sigma, ROUNDING_DIGITS)
    else:
        return sigma

def sigma_z(x, stability_class):
    c = stability_classes[stability_class]["c"]
    d = stability_classes[stability_class]["d"]
    sigma = np.float64(c * np.power(x,d))
    if ROUND_VALUE:
        return np.round(sigma, ROUNDING_DIGITS)
    else:
        return sigma

for i in np.arange(0,100,0.1):
    sigma_y_value = sigma_y(i, "A")
    sigma_z_value = sigma_z(i, "A")
    print(f"sy={sigma_y_value}, sz={sigma_z_value}")