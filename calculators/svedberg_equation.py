#!/usr/bin/env python
'''
    This script was written by Samuel Bowerman (Postdoctoral Associate, Luger Lab) on 3/30/2020.
    
    Its intended purpose is to serve as a quick-reference calculator for desired SV-AUC
    quantities according to modeled/fit/theoretical values and the Svedberg equation.

    The script is provided "AS IS" and WITHOUT WARRANTY.

    Questions or concerns with the script's performance can be directed to the Luger Lab
    "AUC-Tools" github page: (address goes here)

    Also, as a brief aside, using this calculator with S_(20,w) (S values corrected to 
    20 degrees Celsius, in water) values means that one should use the density of water
    at 20 C (0.998234 g/cm^3) rather than the density of your buffer solution, when using
    this calculator.
'''

import numpy as np
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-s",help='Sed. coefficient (in S, or 10^-13 seconds).',default=0.0,type=float)
parser.add_argument("-d",help='Diff. Coefficient (in cm^2/s)',default=0.0,type=float)
parser.add_argument("-p",help='Solvent Density (in g/cm^3)',default=0.0,type=float)
parser.add_argument("-mw",help='Theoretical Mol. Weight (in Da)',default=0.0,type=float)
parser.add_argument("-vbar",help='Theoretical v-bar value',default=0.0,type=float)
parser.add_argument("-vbar_range",help='Plot a range of v-bar vs MW values, extending [-vbar_range] in either direction of the supplied vbar value',default=0.0,type=float)
args = parser.parse_args()

RT = 8.314472 * 293.15
op_mode="0"
if ((args.s==0) and (args.d==0) and (args.p==0)) or ((args.vbar==0) and (args.mw==0)):
    while (op_mode != 'a') and (op_mode != 'b'):
        op_mode   = input("Would you like to (A) calculate v-bar when given theoretical mol. weight or (B) calculate mol. weight given theoretical vbar?  (A or B) > ").lower()
        if (op_mode != 'a') and (op_mode != 'b'):
            print("Please select either option (A) or option (B), or enter \"quit\" to close the program.")
            if op_mode=='quit':
                quit()
        elif op_mode == 'a':
            fit_vbar = True
            fit_mw   = False
        elif op_mode == 'b':
            fit_mw   = True
            fit_vbar = False

    sed_coeff   = float(input("What is the observed S value (in S, 10^-13 seconds - for example: 2.67)? > "))
    diff_const  = float(input("What is the modeled Diffusion Constant (in cm^2/s - for example: 0.46912)? > "))
    sol_dens    = float(input("What is the approximate solvent density (in g/cm^3 - for example: 0.998)? > "))
    if fit_vbar and not fit_mw:
        mw      = float(input("What is the theoretical mol. weight of the complex (in Da - for example: 49130)? > "))
    elif fit_mw and not fit_vbar:
        vbar    = float(input("What is the v-bar value (partial specific volume, in cm^3/g - for example: 0.7239)? > "))
        do_range='unset'
        while not ((do_range=='y') or (do_range=='n')):
            do_range= input("Would you like to process a range of v-bar values? (Y/N) > ").lower()
        if do_range=='y':
            vbar_range  = float(input("Please enter the extent from the supplied v-bar value that you would like to sample. > "))
            fit_range   = np.linspace(vbar-vbar_range,vbar+vbar_range,num=100)
            print("Sampling v-bar values from "+str(fit_range[0])+" to "+str(fit_range[-1])+" cm^3/g.")
            plot_range=True
        else:
            plot_range=False
else:
    sed_coeff   = args.s
    diff_const  = args.d
    sol_dens    = args.p
    vbar        = args.vbar
    mw          = args.mw
    if (vbar != 0) and (mw == 0):
        fit_mw  = True
        fit_vbar= False
        if args.vbar_range!=0:
            fit_range = np.linspace(vbar-args.vbar_range,vbar+args.vbar_range,num=100)
            plot_range= True
        else:
            plot_range= False
    elif (mw != 0) and (vbar == 0):
        fit_vbar= True
        fit_mw  = False

if fit_mw and not fit_vbar:
    numerator = sed_coeff * RT
    denom     = diff_const * (1.0 - vbar * sol_dens)

    mass = numerator / denom
    mass = np.around(mass,decimals=0)
    print("\n\n\t\tAccording to the Svedberg Equation and given inputs, MW should be "+str(mass)+" Da.\n\n")
    if plot_range == True:
        print("Plotting range of MW values across given vbar_range.")
        mw_range = sed_coeff*RT/(diff_const*(1.0-fit_range*sol_dens))
        plt.figure(figsize=(3.,3.))
        plt.plot(fit_range,mw_range,color='k')
        plt.xlabel(r'$\rm{\bar{v}}$ ($\rm{cm^3}$/g)')
        plt.ylabel('Mol. Weight (Da)')
        plt.tight_layout()
        plt.show()

elif fit_vbar and not fit_mw:
    # vbar = (1/p) * [1 - (RT*S)/(MW*D)]
    rts_over_md = (RT*sed_coeff)/(mw*diff_const)
    vbar_calc   = (1/sol_dens) * (1 - rts_over_md)
    vbar_calc   = np.around(vbar_calc,decimals=4)
    print("\n\n\t\tAccording to the Svedberg Equation and given inputs, v-bar should be "+str(vbar_calc)+" cm^3/g.\n\n")


