# Numerical Verification of Planck's Distribution and the Stefan-Boltzmann Law

A computational thermal radiation module that evaluates Planck's spectral distribution and validates the Stefan-Boltzmann constant ($\sigma$) by numerical quadrature using composite Simpson's 1/3 rule.

---

## Theoretical Formulation

### 1. Planck's Spectral Distribution Law

Planck's law models the hemispherical spectral emissive power of a blackbody emitting into a vacuum:

$$E_{b,\lambda}(\lambda, T) = \frac{C_1}{\lambda^5 \left[ \exp\left(\frac{C_2}{\lambda T}\right) - 1 \right]}$$

Where:
* $\lambda$: Radiation wavelength ($\text{m}$)
* $T$: Absolute temperature of the emitting surface ($\text{K}$)
* $C_1 = 2\pi h c_0^2 = 3.742 \times 10^{-16} \text{ W}\cdot\text{m}^2$ (First radiation constant)
* $C_2 = \frac{h c_0}{k_B} = 1.4388 \times 10^{-2} \text{ m}\cdot\text{K}$ (Second radiation constant)
* $h$: Planck's constant ($6.626 \times 10^{-34} \text{ J}\cdot\text{s}$)
* $k_B$: Boltzmann constant ($1.381 \times 10^{-23} \text{ J/K}$)
* $c_0$: Speed of light in vacuum ($2.998 \times 10^8 \text{ m/s}$)

---

### 2. Derivation of the Stefan-Boltzmann Law

Total emissive power across all wavelengths is the integral of Planck's spectral distribution:

$$E_b(T) = \int_0^\infty E_{b,\lambda}(\lambda, T) \, d\lambda = \sigma T^4$$

Analytically, substituting $x = \frac{C_2}{\lambda T}$ yields:

$$\sigma = \frac{C_1}{C_2^4} \int_0^\infty \frac{x^3}{e^x - 1} \, dx = \frac{C_1 \pi^4}{15 C_2^4} \approx 5.670374 \times 10^{-8} \text{ W}/(\text{m}^2\cdot\text{K}^4)$$

---

### 3. Numerical Quadrature: Composite Simpson's 1/3 Rule

The continuous semi-infinite integral is approximated over a bounded spectral domain $[\lambda_a, \lambda_b] = [0.1\,\mu\text{m}, 1000\,\mu\text{m}]$ discretized into $N$ intervals ($N+1$ grid points, where $N$ is even):

$$E_b(T) \approx \frac{\Delta \lambda}{3} \left[ E_0 + 4 \sum_{j=1,3,5}^{N-1} E_j + 2 \sum_{j=2,4,6}^{N-2} E_j + E_N \right]$$

From the numerical value of $E_b(T)$, the Stefan-Boltzmann constant is recovered:

$$\sigma_{\text{calc}} = \frac{E_b(T)}{T^4}$$

$$\text{Error (\%)} = \left\vert{} \frac{\sigma_{\text{calc}} - \sigma_{\text{theoretical}}}{\sigma_{\text{theoretical}}} \right\vert{} \times 100$$

---

## Repository Structure

```text
plancks_radiation_verification/
├── src/
│   ├── __init__.py          # Package interfaces
│   ├── radiation.py         # Planck equation and numerical integration routines
│   └── visualize.py         # Log-log spectral distribution plotting
├── main.py                  # Driver script
├── requirements.txt         # Project dependencies
└── README.md
```

## Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/hector-0208/plancks_radiation_verification.git
cd plancks_radiation_verification
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run
```bash
python main.py
```
## Results & Verification

Evaluating at $T = 1000\text{ K}$ across the wavelength band $\lambda \in [0.1\,\mu\text{m}, 1000\,\mu\text{m}]$ using $N = 10^4$ sub-intervals:

| Parameter | Value | Unit |
| :--- | :--- | :--- |
| Temperature ($T$) | $1000.0$ | $\text{K}$ |
| Integration Domain | $[0.1, 1000.0]$ | $\mu\text{m}$ |
| Total Emissive Power ($E_b$) | $56697.88$ | $\text{W/m}^2$ |
| Calculated $\sigma$ | $5.6698 \times 10^{-8}$ | $\text{W}/(\text{m}^2\cdot\text{K}^4)$ |
| Theoretical $\sigma$ | $5.6704 \times 10^{-8}$ | $\text{W}/(\text{m}^2\cdot\text{K}^4)$ |
| Relative Error | $\approx 0.0104\%$ | — |

*The residual truncation error ($< 0.02\%$) is due to truncating the upper spectral limit at $\lambda = 1000\,\mu\text{m}$ rather than integrating to $\infty$.*
