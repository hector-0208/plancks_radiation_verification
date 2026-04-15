import matplotlib.pyplot as plt
import numpy as np

from src.radiation import planck_distribution


def plot_spectral_curves(temperatures, lam_min_um=0.1, lam_max_um=1000.0, num_points=1000):
    """
    Plots spectral blackbody emissive power curves across a logarithmic wavelength scale.
    """
    lam_um = np.logspace(np.log10(lam_min_um), np.log10(lam_max_um), num_points)
    lam_m = lam_um * 1e-6

    plt.figure(figsize=(9, 5.5))

    for T in temperatures:
        E_spectral_m = planck_distribution(lam_m, T)
        E_spectral_um = E_spectral_m * 1e-6  # Convert W/m³ to W/(m²·µm)
        plt.plot(lam_um, E_spectral_um, label=f"T = {T} K", lw=2)

    plt.xscale("log")
    plt.yscale("log")
    plt.xlim(lam_min_um, lam_max_um)
    plt.ylim(1e-4, 1e5)
    plt.xlabel(r"Wavelength $\lambda$ ($\mu\mathrm{m}$)", fontsize=11)
    plt.ylabel(r"Spectral Emissive Power $E_{b,\lambda}$ ($\mathrm{W} / (\mathrm{m}^2 \cdot \mu\mathrm{m})$)", fontsize=11)
    plt.title("Planck's Blackbody Spectral Distribution", fontsize=13)
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend(fontsize=10)
    plt.tight_layout()
    plt.show()
