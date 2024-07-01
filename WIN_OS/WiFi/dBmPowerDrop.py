def dBm_to_mW(dBm_value):
  """
  This function converts a signal strength in dBm to milliwatts (mW).

  Args:
      dBm_value: The signal strength value in dBm (float).

  Returns:
      The equivalent power in milliwatts (float).
  """
  return 10**(dBm_value / 10)

# Loop through dBm values in steps of -3
for dBm in range(0, -73, -3):  # Adjust the range to start from 0 and end at -72 for inclusive steps
  mw_power = dBm_to_mW(dBm)
  print(f"Signal strength: {dBm} dBm")
  print(f"Equivalent power: {mw_power:.8f} mW")
  print("-" * 20)  # Add a separator line between entries

print(f"Now print in steps of -10 dBm\n")
#now do it in steps of -10 dBm
for dBm in range(0, -90, -10):  # Adjust the range to start from 0 and end at -72 for inclusive steps
  mw_power = dBm_to_mW(dBm)
  print(f"Signal strength: {dBm} dBm")
  print(f"Equivalent power: {mw_power:.8f} mW")
  print("-" * 20)  # Add a separator line between entries