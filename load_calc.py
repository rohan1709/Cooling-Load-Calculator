# Get user input
area = float(input("Enter the area of the building in square meters: "))
occupants = int(input("Enter the number of occupants in the building: "))
building_type = input("Enter the type of building (residential, commercial): ")
T_outdoor = float(input("Enter the outdoor temperature in Celsius: "))
T_indoor = float(input("Enter the indoor desired temperature in Celsius: "))

# Set U value
U = 30

# Calculate cooling load based on building type
if building_type.lower() == "residential":
    cooling_load = 100 * occupants
elif building_type.lower() == "commercial":
    cooling_load = 150 * occupants
else:
    print("Invalid building type. Please enter either 'residential' or 'commercial'.")
    exit()

# Calculate heat transfer due to conduction
Q_conduction = U * area * (T_outdoor - T_indoor)

# Calculate sensible cooling load
sensible_cooling_load = Q_conduction + cooling_load

# Display the final sensible cooling load to the user
print(f"The sensible cooling load is {sensible_cooling_load} units.")
