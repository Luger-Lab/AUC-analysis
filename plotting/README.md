# AUC Plotting Scripts

This folder contains scripts useful for creating publication-quality images of AUC data, such as plotting multiple g(S) traces from UltraScanIII. Below, you will find a list of each program and the data that it is designed to plot.

## multi_vHW.py

The `multi_vHW.py` script is designed to simultaneously plot multiple traces from a 'Combine Distribution Plots (vHW)' module output from UltraScanIII. By default, it uses the "Category 10" color scheme of Vega (https://github.com/vega/vega/wiki/Scales#scale-range-literals) in a cycling manner to plot each trace, so distributions containing more than 10 samples will see redundant color usage. As such, this script is most useful when comparing two or several distinct populations. Users seeking to plot a continuous titration series, either of buffer components (such as salt concentration, as shown in Edwards et al.) or of binding partner, should instead use the `titration_gradient.py` script, which utilizes a continuous color gradient to represent data ranging from low to high concentrations.

## titration_gradient.py

The `titration_gradient.py` script is designed to 
