# source: https://www.researchgate.net/publication/357185624_Crosswind_integrated_concentration_for_various_dispersion_parameter_systems

stability_classes = {
    "A": {
        "description": "Very Unstable",
        "a1": 0.22,
        "a2": 0.90,
        "b1": 0.20,
        "b2": 1.00,
        "conditions": "Strong solar radiation, clear skies, light winds",
        "examples": "Summer afternoons with strong sunlight and low wind speed"
    },
    "B": {
        "description": "Unstable",
        "a": 0.16,
        "b": 0.90,
        "c": 0.12,
        "d": 0.91,
        "conditions": "Moderate solar radiation, light to moderate winds",
        "examples": "Spring or fall days with some sunlight and mild wind"
    },
    "C": {
        "description": "Slightly Unstable",
        "a": 0.11,
        "b": 0.86,
        "c": 0.08,
        "d": 0.77,
        "conditions": "Weak solar radiation, partly cloudy skies, moderate winds",
        "examples": "Partly cloudy mornings or late afternoons with moderate wind"
    },
    "D": {
        "description": "Neutral",
        "a": 0.08,
        "b": 0.80,
        "c": 0.06,
        "d": 0.67,
        "conditions": "Overcast conditions, moderate to high winds, or nighttime",
        "examples": "Cloudy days or nights with steady winds"
    },
    "E": {
        "description": "Slightly Stable",
        "a": 0.06,
        "b": 0.78,
        "c": 0.03,
        "d": 0.62,
        "conditions": "Weak turbulence, clear skies at night, low wind speeds",
        "examples": "Calm, clear nights with minimal wind"
    },
    "F": {
        "description": "Very Stable",
        "a": 0.04,
        "b": 0.77,
        "c": 0.016,
        "d": 0.54,
        "conditions": "Very weak turbulence, clear and calm night conditions",
        "examples": "Cool, still nights with no cloud cover or wind"
    }
}
