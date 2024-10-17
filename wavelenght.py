# Get input from user

# Output the results, with frequency in scientific notation
for i in [3,4,5]:
    initial = i
    final = 2

    # Calculate wavelength using the Rydberg formula
    rydberg_constant = (1.097 * 10**7) * 4**2 # Rydberg constant in m^-1
    wavelength = 1 / (rydberg_constant * ((1 / final**2) - (1 / initial**2)))

    # Calculate frequency using the speed of light
    speed_of_light = 3 * 10**8  # Speed of light in m/s
    frequency = speed_of_light / wavelength
    print(f" Wavelength: {wavelength:.2e} meters, Frequency: {frequency:.2e} Hz, Initial {initial}")
    

