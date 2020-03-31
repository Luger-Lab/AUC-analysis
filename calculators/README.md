# Calculators for AUC-related Research

This folder contains calculators relevant to predicting and/or interpreting AUC data. Below, you will find a brief description and a short usage explanation for each calculator.

## svedberg_equation.py

The "svedberg_equation.py" script is used to calculate the relationship between theoretical and observed molecular weight and subtle changes in the estimated v-bar. This calculator is designed to serve as a tool to help guide researchers' intuitions, but it is certainly not a good replacement for designing better experiments. Users should not interpret these values as "matter-of-fact", as the diffusion constant is also dependent, in part, on the estimated v-bar value. As such, users should consider this calculator a first-order approximation, at best, for the relationship between v-bar and modeled molecular weight.

The calculator functions in two-modes: (A) using a supplied molecular weight to calculate an associated v-bar value or (B) calculate molecular weight(s) from a user-supplied value (or range of values) for v-bar, in both (A) and (B) using user-supplied values of sedimentation and diffusion coefficients, as well as buffer density. It can be run either interactively or by supplying arguments to the calculator at runtime. A full list of options is given below:

- `-s` : (required) User-defined sedimentation coefficient (in units of S, or 10^13 svedberg)
- `-d` : (required) User-defined diffusion coefficient (in cm^2/s, programs such as UltraScan provide this value in m^2/s)
- `-p` : (required) Calculated (or measured) solvent density (in g/cm^3). If the value of `-s` is supplied as S_{20,w}, then the density of water at 20 degrees Celsius should be used (0.998234 g/cm^3).
- `-mw` : If supplied, the theoretical or observed molecular weight of your solute (in Da), used to calculate the value of v-bar.
- `-vbar`: If supplied, the expected value of v-bar (in cm^3/g), used to calculate the value of molecular weight. If supplied alongside the `-mw` option, it will override the `-mw` value and calculate mass from v-bar, rather than v-bar from mass.
- `-vbar_range` : If supplied, will extend the theoretical v-bar value `-vbar_range` in either direction and generate a plot showing the relationship of v-bar on calculated molecular weights, assuming all other values remain constant.

If one of `-s`, `-d`, or `-p` are not supplied at runtime, then the program will automatically initiate in an interactive mode, where it will prompt the user for each value listed above.
