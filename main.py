from src.radiation import integrate_emissive_power
from src.visualize import plot_spectral_curves


def main():
    temperatures = [100, 500, 1000]
    plot_spectral_curves(temperatures)

    T_target = 1000.0
    res = integrate_emissive_power(T_target, lam_min=0.1e-6, lam_max=1000e-6, num_points=10001)

    print(" Planck Spectral Integration & Stefan-Boltzmann Verification:-->")
    print(f"Integration Range: {res['lam_range'][0]*1e6:.1f} µm to {res['lam_range'][1]*1e6:.1f} µm")
    print(f"Evaluation Temperature: {T_target:.1f} K")
    print(f"Total Emissive Power (E_b): {res['E_total']:.4f} W/m²")
    print(f"Calculated Stefan-Boltzmann (sigma): {res['sigma_numeric']:.6e} W/(m²·K⁴)")
    print(f"Theoretical Stefan-Boltzmann (sigma): {res['sigma_theoretical']:.6e} W/(m²·K⁴)")
    print(f"Percentage Error: {res['relative_error']:.4f} %")
    
if __name__ == "__main__":
    main()
