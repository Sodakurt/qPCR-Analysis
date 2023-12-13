import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import colorsys

# import csv 
filename = 'result.csv'
df = pd.read_csv(filename)

# Get name of control line
control = 'H1 CTRL'
# other settings for plotting
width = 0.6 # bar width
error_width = 1
error_capsize = 4

# get the right order so control line is first in plot
dfc = df.loc[df['Sample'] == control].reset_index() # get control
dfm = df.loc[df['Sample'] != control].reset_index() # get other lines
df_combined = pd.concat([dfc, dfm]) # concatenate

# pivot data for plotting
dfp = df_combined.pivot_table(index='Target', columns='Sample', values='Fold change', sort=False)

# error bars
# errors should be positive, and defined in the order of lower, upper. Should be shape(line, 2, target)
df_lower = df_combined.pivot_table(index='Target', columns='Sample', values='Lower bound', sort=False) # output is shape(target, line)
df_upper = df_combined.pivot_table(index='Target', columns='Sample', values='Upper bound', sort=False)
# getting the right dimensions
error = np.stack((df_lower.to_numpy().T, df_upper.to_numpy().T), axis=1) #.T transposes and then stack in axis=1 to get (X, 2, Y)

# significance (fuck me)


# function for generating colors going from dark to light blue 
def generate_colors(n):
    hue = 240

    # Start with a dark blue color
    sat_start, val_start = 70, 45
    
    # End with a light blue color
    sat_end, val_end = 33, 85

    # Calculate the step size for varying saturation
    sat_step = (sat_end - sat_start) / (n - 1)

    # Calculate the step size for varying values
    val_step = (val_end - val_start) / (n - 1)

    # Generate the colors
    colors = []
    for i in range(n):
        # Calculate the current saturation
        current_sat = sat_start + i * sat_step

        # Calculate the current value
        current_value = val_start + i * val_step

        # Convert HSV to RGB
        rgb_color = colorsys.hsv_to_rgb(hue / 360, current_sat / 100, current_value / 100)

        # Scale RGB values to the range [0, 1]
        rgb_color = tuple(x for x in rgb_color)

        colors.append(rgb_color)

    return colors

# Generate colors
colors = generate_colors(np.shape(error)[0])

# plotting
fig, ax = plt.subplots()
ax.set_ylim(0, 5)
dfp.plot.bar(yerr=error, ax=ax, error_kw=dict(lw=error_width, capsize=error_capsize, capthick=error_width), rot=0, width=width, color=colors)
plt.xlabel("Markers")
plt.ylabel("Fold change")
plt.title("qPCR")
plt.show()

