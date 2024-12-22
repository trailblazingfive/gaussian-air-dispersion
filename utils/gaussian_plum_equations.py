import numpy as np
import matplotlib.pyplot as plt
from utils.stability_classes import stability_classes
from collections import namedtuple

Point = namedtuple("Point", ["x", "y", "z"])

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
    
# source:
# https://www.tandfonline.com/doi/abs/10.13182/NT77-A31828 - equation 1

def concentration_of_emission(initial_data, point):
    x, y, z = point
    Q = initial_data["emission"]
    H = initial_data["height"]
    u = initial_data["wind_speed"]
    SC = initial_data["stability_class"]

    mass_part = np.float64(Q/(2*np.pi*sigma_y(x,SC)*sigma_z(x,SC)))

    orthogonal_part = np.float64(np.exp(-np.pow(y,2)/(2*np.pow(sigma_y(x,SC),2))))

    height_part = np.float64(np.exp(-(np.pow(z-H,2)/(2*np.pow(sigma_y(x,SC),2))))+np.exp(-(np.pow(z+H,2)/(2*np.pow(sigma_y(x,SC),2)))))

    concentration = mass_part * orthogonal_part * height_part
    return concentration