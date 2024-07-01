import csv
import matplotlib.pyplot as plt

def dBm_to_mW(dBm_value):
  """
  This function converts a signal strength in dBm to milliwatts (mW).

  Args:
      dBm_value: The signal strength value in dBm (float).

  Returns:
      The equivalent power in milliwatts (float).
  """
  return 10**(dBm_value / 10)

# Generate dBm values in steps of -3
dBm_values = range(0, -73, -3)  # Adjust range for inclusivity

# Calculate corresponding mW values
mw_powers = [dBm_to_mW(dBm) for dBm in dBm_values]

# Write data to CSV
with open('dBm_to_mW_data.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['dBm', 'mW'])  # Write header row
  for i, dBm in enumerate(dBm_values):
    writer.writerow([dBm, mw_powers[i]])

# Create the plot
plt.figure(figsize=(8, 5))  # Adjust figure size as needed

plt.plot(dBm_values, mw_powers, marker='o', linestyle='-', color='blue', label='dBm to mW')

# Customize plot elements
plt.xlabel('Signal Strength (dBm)')
plt.ylabel('Equivalent Power (mW)')
plt.title('dBm vs mW Conversion')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()

# Display the plot
plt.show()