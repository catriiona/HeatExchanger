# Counterflow Heat Exchanger Simulation

## Overview

This Python script simulates the temperature profile in a counterflow heat exchanger. The simulation uses an Ordinary Differential Equation (ODE) approach to model the heat transfer between hot and cold fluids across multiple layers. The temperature profiles, total heat transfer, log mean temperature difference, and total weight of the heat exchanger are calculated and visualized.

## Code Structure

- **heat_exchanger_simulation Function:**
  - This function takes the overall heat transfer coefficient and layer weight as inputs and returns the temperature profiles, total heat transfer, log mean temperature difference, and total weight.

- **Main Script:**
  - The main script runs the heat_exchanger_simulation function for both steel and aluminum cases, comparing the results.

- **ODE Solver:**
  - The ODE solver integrates the energy balance equation for each layer, calculating the temperature profile of the hot fluid along the length of the heat exchanger.

## Equations

The ODE being solved is derived from the overall energy balance equation for each layer:

\[ \frac{dT}{dx} = -\frac{T - T_c}{R \cdot \dot{m} \cdot C_p} \]

Where:
- \( T \) is the temperature of the hot fluid,
- \( T_c \) is the temperature of the cold fluid,
- \( R \) is the total thermal resistance for all layers,
- \( \dot{m} \) is the mass flow rate,
- \( C_p \) is the specific heat capacity.

## Usage

1. Define the parameters for the heat exchanger, including mass flow rates, inlet temperatures, specific heat capacities, contact area, number of layers, overall heat transfer coefficients, layer length, and layer weight.

2. Run the main script to perform simulations for different materials (e.g., steel and aluminum) and compare the results.

3. View the temperature profiles, total heat transfer, log mean temperature difference, and total weight for each material.

## Dependencies

- Python 3.x
- NumPy
- Matplotlib
- SciPy

## License

This code is provided under the [MIT License](LICENSE).
