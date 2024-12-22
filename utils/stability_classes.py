# source: 
# https://www.researchgate.net/publication/357185624_Crosswind_integrated_concentration_for_various_dispersion_parameter_systems
# https://www.tandfonline.com/doi/abs/10.13182/NT77-A31828

stability_classes = {
    "A": {
        "description": "Very Unstable",
        "a1": -0.0234,
        "a2": 0.3500,
        "b1": 0.8800,
        "b2": 0.1520,
        "b3": 0.1475,
        "conditions": "Strong solar radiation, clear skies, light winds",
        "examples": "Summer afternoons with strong sunlight and low wind speed"
    },
    "B": {
        "description": "Unstable",
        "a1": -0.0147,
        "a2": 0.2480,
        "b1": -0.9850,
        "b2": 0.8200,
        "b3": 0.0168,
        "conditions": "Moderate solar radiation, light to moderate winds",
        "examples": "Spring or fall days with some sunlight and mild wind"
    },
    "C": {
        "description": "Slightly Unstable",
        "a1": -0.0117,
        "a2": 0.1750,
        "b1": -1.1860,
        "b2": 0.8500,
        "b3": 0.0045,
        "conditions": "Weak solar radiation, partly cloudy skies, moderate winds",
        "examples": "Partly cloudy mornings or late afternoons with moderate wind"
    },
    "D": {
        "description": "Neutral",
        "a1": -0.0059,
        "a2": 0.1080,
        "b1": -1.3500,
        "b2": 0.7930,
        "b3": 0.0022,
        "conditions": "Overcast conditions, moderate to high winds, or nighttime",
        "examples": "Cloudy days or nights with steady winds"
    },
    "E": {
        "description": "Slightly Stable",
        "a1": -0.0059,
        "a2": 0.0880,
        "b1": -2.8800,
        "b2": 1.2550,
        "b3": -0.0420,
        "conditions": "Weak turbulence, clear skies at night, low wind speeds",
        "examples": "Calm, clear nights with minimal wind"
    },
    "F": {
        "description": "Very Stable",
        "a1": -0.0029,
        "a2": 0.0540,
        "b1": -3.8000,
        "b2": 1.4190,
        "b3": -0.0550,
        "conditions": "Very weak turbulence, clear and calm night conditions",
        "examples": "Cool, still nights with no cloud cover or wind"
    }
}
