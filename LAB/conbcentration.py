# Let's calculate the concentrations [Fe³⁺]_0 and [SCN⁻]_0 for each solution.

import pandas as pd

# Input stock concentrations (M) and volumes (mL)
fe_stock_conc = 0.2  # Fe(NO₃)₃ stock concentration (assumed)
scn_stock_conc = 5*10**-4  # KSCN stock concentration (assumed)

# Total volume (mL) for all solutions (constant for simplicity)
total_volume = 20

# Input data for volumes (mL) from the table
data = {
    "Solution": ["Calibration", "1", "2", "3"],
    "Fe(NO₃)₃ (mL)": [15, 0.5, 1, 1.5],
    "KSCN (mL)": [5, 5, 5, 5],
    "H₂O (mL)": [0, 14.5, 14, 13.5],
    "Absorbance": [0.41, 0.19, 0.26, 0.31]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate [Fe³⁺]_0 and [SCN⁻]_0 using the formula C_f = C_i * V_i / V_total
df["[Fe³⁺]_0 (M)"] = fe_stock_conc * df["Fe(NO₃)₃ (mL)"] / total_volume
df["[SCN⁻]_0 (M)"] = scn_stock_conc * df["KSCN (mL)"] / total_volume

print(df) 