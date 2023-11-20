import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def heat_exchanger_simulation(overall_heat_transfer_coefficient, layer_weight):
    # Given parameters
    mass_flow_rate_hot = 0.010  # Mass flow rate of hot fluid (kg/s)
    mass_flow_rate_cold = 0.034  # Mass flow rate of cold fluid (kg/s)
    inlet_temp_hot = 623.15  # Inlet temperature of hot fluid (K)
    inlet_temp_cold = 293.15  # Inlet temperature of cold fluid (K)
    specific_heat_hot = 1078.0  # Specific heat capacity of hot fluid (J/(kg*K))
    specific_heat_cold = 1007.0  # Specific heat capacity of cold fluid (J/(kg*K))
    contact_area = 0.023808  # Contact area for each layer (m^2)
    num_layers = 5  # Number of layers in series
    layer_length = 0.0125  # Length of each layer (m)
    pressure_drop_cold = 15 #(Pa)
    pressure_drop_hot = 5 #(Pa}

    # Calculate thermal resistance for each layer
    thermal_resistances = layer_length / (overall_heat_transfer_coefficient * contact_area)

    # Set initial condition
    initial_condition = [inlet_temp_hot]

    # Define the ODE system
    def heat_exchanger_ode(T, x):
        # Calculate total thermal resistance for all layers
        total_thermal_resistance = np.sum(thermal_resistances)

        # Calculate dT/dx using the thermal resistance approach
        dTdx = -(T - inlet_temp_cold) / (total_thermal_resistance * mass_flow_rate_hot * specific_heat_hot)
        return dTdx

    # Define positions along the heat exchanger
    x_positions = np.linspace(0, num_layers * layer_length, num_layers)

    # Solve the ODE
    result = odeint(heat_exchanger_ode, initial_condition, x_positions)

    # Extract temperatures and convert to Celsius
    temp_hot = result[:, 0] - 273.15
    temp_cold = (inlet_temp_cold + (inlet_temp_hot - result[:, 0]) * (mass_flow_rate_hot / mass_flow_rate_cold) * (specific_heat_hot / specific_heat_cold)) - 273.15

    # Calculate total heat transfer
    total_heat_transfer = mass_flow_rate_hot * specific_heat_hot * (inlet_temp_hot - result[-1, 0])

    # Calculate log mean temperature difference
    delta_T_1 = temp_hot[0] - temp_cold[0]
    delta_T_2 = temp_hot[-1] - temp_cold[-1]
    log_mean_temp_difference = (delta_T_1 - delta_T_2) / np.log(delta_T_1 / delta_T_2)

    # Calculate total weight of the heat exchanger
    total_weight = num_layers * layer_weight
    
    #Calculate total pressure drop
    pressure_total_hot = num_layers * pressure_drop_hot
    pressure_total_cold = num_layers * pressure_drop_cold

    return x_positions, temp_hot, temp_cold, total_heat_transfer, log_mean_temp_difference, total_weight, pressure_total_hot, pressure_total_cold, num_layers, layer_length

# Given parameters for steel
overall_heat_transfer_coefficient_steel = 45.33154074  # Overall heat transfer coefficient for steel (W/(m^2*K))
layer_weight_steel = 0.599  # Weight of each layer for steel (kg)

# Given parameters for aluminium
overall_heat_transfer_coefficient_aluminium = 45.35971499  # Overall heat transfer coefficient for aluminium (W/(m^2*K))
layer_weight_aluminium = 0.255  # Weight of each layer for aluminium (kg)

# Run simulations for steel and aluminium
result_steel = heat_exchanger_simulation(overall_heat_transfer_coefficient_steel, layer_weight_steel)
result_aluminium = heat_exchanger_simulation(overall_heat_transfer_coefficient_aluminium, layer_weight_aluminium)

# Plotting
plt.plot(result_steel[0], result_steel[1], label="Hot Fluid (Steel)", color="red")
plt.plot(result_steel[0], result_steel[2], label="Cold Fluid (Steel)", color="blue")

plt.plot(result_aluminium[0], result_aluminium[1], label="Hot Fluid (aluminium)", color="orange", linestyle="--")
plt.plot(result_aluminium[0], result_aluminium[2], label="Cold Fluid (aluminium)", color="cyan", linestyle="--")

plt.xlabel("Position Along Heat Exchanger (m)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Profile in Counterflow Heat Exchanger")
plt.legend()
plt.show()

print("General information:")
print("Number of layers: {:.0f}".format(result_steel[8]))
print("Height: {:.2f} cm".format(100*result_steel[9]*result_steel[8]))
print("Pressure drop (hot): {:.2f} Pa".format(result_steel[6]))
print("Pressure drop (cold): {:.2f} Pa\n".format(result_steel[7]))


# Display results for steel
print("Results for Steel:")
print("Total Heat Transfer: {:.2f} Watts".format(result_steel[3]))
print("Log Mean Temperature Difference: {:.2f} °C".format(result_steel[4]))
print("Total Weight of the Heat Exchanger: {:.2f} kg".format(result_steel[5]))

# Display results for aluminium
print("\nResults for aluminium:")
print("Total Heat Transfer: {:.2f} Watts".format(result_aluminium[3]))
print("Log Mean Temperature Difference: {:.2f} °C".format(result_aluminium[4]))
print("Total Weight of the Heat Exchanger: {:.2f} kg".format(result_aluminium[5]))
