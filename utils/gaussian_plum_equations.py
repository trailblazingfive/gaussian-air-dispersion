from stability_classes import stability_classes
import numpy as np

ROUND_VALUE = True
ROUNDING_DIGITS = 4

def sigma_y(x, stability_class):
    if x <= 0:
        return np.nan
    a1 = stability_classes[stability_class]["a1"]
    a2 = stability_classes[stability_class]["a2"]
    sigma = np.float64((a1 * np.log(x) + a2) * x) 
    if ROUND_VALUE:
        return np.round(sigma, ROUNDING_DIGITS)
    else:
        return sigma

def sigma_z(x, stability_class):
    if x <= 0:
        return np.nan
    b1 = stability_classes[stability_class]["b1"]
    b2 = stability_classes[stability_class]["b2"]
    b3 = stability_classes[stability_class]["b3"]
    sigma = np.float64((1.0/2.15) * np.exp(b1 + b2 * np.log(x) + b3 * np.log(x)**2))
    if ROUND_VALUE:
        return np.round(sigma, ROUNDING_DIGITS)
    else:
        return sigma

for i in np.arange(0.1, 10, 0.1):  # Start at 0.1 to avoid log(0)
    sigma_y_value = sigma_y(i, "A")
    sigma_z_value = sigma_z(i, "A")
    print(f"sy={sigma_y_value}, sz={sigma_z_value}")
