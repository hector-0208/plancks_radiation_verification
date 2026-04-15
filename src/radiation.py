import numpy as np
from scipy.integrate import simpson

# Radiation Constants
C1 = 3.742e-16   # First radiation constant [W·m²]
C2 = 1.4388e-2   # Second radiation constant [m·K]
SIGMA_THEORETICAL = 5.670374e-8  # Stefan-Boltzmann constant [W/(m²·K⁴)]

def planck_distribution(wavelengths, T):
    """
    Computes spectral blackbody emissive power E_b(lambda, T) [W/m³].
    wavelengths: array-like in meters [m]
    T: Absolute temperature [K]
    """
    numerator = C1
    denominator = (wavelengths**5) * (np.exp(C2 / (wavelengths * T)) - 1.0)
    return numerator / denominator

def integrate_emissive_power(T, lam_min=0.1e-6, lam_max=1000e-6, num_points=10001):
    """
    Numerically integrates E_b(lambda, T) over a finite spectral band
    using composite Simpson's rule to compute total emissive power E_b [W/m²].
    """
    lam_grid = np.linspace(lam_min, lam_max, num_points)
    E_spectral = planck_distribution(lam_grid, T)
    E_total = simpson(y=E_spectral, x=lam_grid)
    sigma_numeric = E_total / (T**4)
    relative_error = abs(sigma_numeric - SIGMA_THEORETICAL) / SIGMA_THEORETICAL * 100

    return {
        "E_total": E_total,
        "sigma_numeric": sigma_numeric,
        "sigma_theoretical": SIGMA_THEORETICAL,
        "relative_error": relative_error,
        "lam_range": (lam_min, lam_max),
    }
