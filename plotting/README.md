# AUC Plotting Scripts

This folder contains scripts useful for creating publication-quality images of AUC data, such as plotting multiple van Holde-Weischet traces from UltraScanIII. Below, you will find a list of each program and the data that it is designed to plot.

## multi_vHW.py

The `multi_vHW.py` script is designed to simultaneously plot multiple traces from a 'Combine Distribution Plots (vHW)' module output from UltraScanIII. By default, it uses the "Category 10" color scheme of Vega (https://github.com/vega/vega/wiki/Scales#scale-range-literals) in a cycling manner to plot each trace, so distributions containing more than 10 samples will see redundant color usage. As such, this script is most useful when comparing two or several distinct populations. Users seeking to plot a continuous titration series, either of buffer components (such as salt concentration, as shown in Edwards et al.) or of binding partner, should instead use the `titration_gradient.py` script, which utilizes a continuous color gradient to represent data ranging from low to high concentrations.

The `multi_vHW.py` script uses a very simplified interaction with the user. At runtime, using the `-i` option, users can provide the file from which the traces will be extracted. If no `-i` file is provided, then the program will prompt the user to enter the filename once the script has initialized. Once the input file has been defined, the script will take the user through all the steps needed to create a publication quality figure:

1. The script will then ask the user for the names of each trace in the data set. These names will be displayed in the figure legend.
2. Next, the user will be asked to declare what size the figure will be (in inches).
3. After the figure size has been defined, the script will ask the user to choose a marker system.
  - Once a marker has been selected, users will be prompted for a marker size (in pts), with a suggested value of "4"
  - `multi_vHW.py` will now generate an example figure with the size and markers defined by the user. If the user is not happy with their marker or size selection, they may then return to the marker selection step, whereafter another example figure will be generated. The script will only continue after the user is satisfied with their marker representation.
4. After marker selection, `multi_vHW.py` will ask the users to choose a legend location.
  - Similarly to marker selection, the script will only continue after the user is happy with their selection for the legend location.
5. Once the user is satisfied with their marker and legend location choices, the script will ask for a filename to which the plot will be saved (in PDF format).

An example file ("example_multi_vHW.csv") for exploring this script is provided, and this data comes from Edwards et al. "Practical Analytical Ultracentrifugation: a guide to the application of fluorescence and absorbance AUC to biological macromolecules" *Submitted*.

## titration_gradient.py

The `titration_gradient.py` script is designed to visualize traces from a gradient, such as titrating in binding partner concentrations or increasing salt to induce complex destabilization. Functionally, it works the same as the `multi_vHW.py` script, with the exception of using a color bar to differentiate traces instead of discrete color changes. By default, it uses the "terrain" colormap, but any of the available `matplotlib` colormaps can be used by declaring `-colormap [name of colormap]` at runtime (for a list of acceptable map names, please see: https://matplotlib.org/tutorials/colors/colormaps.html).
