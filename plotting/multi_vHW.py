#!/usr/bin/env python
'''
    This script was written by Samuel Bowerman (Postdoctoral Associate, Luger Lab) on 3/30/2020.

    Its intended purpose is to create publication-quality figures for combined vHW plots that
    contain a discrete collection of data sets. Plotting > 10 data sets in this script can
    create quite a "busy" plot, and users seeking to plot a titration series are thereby
    recommended to use the "titration_gradient.py" script, instead.

    This script is provided "AS IS" and WITHOUT WARRANTY.

    Questions or concerns with the script's performance can be directed to the Luger Lab
    "AUC-analysis" github page: www.github.com/Luger-Lab/AUC-analysis/
'''
import numpy as np
import matplotlib.pyplot as plt
import argparse

#Take the input file from the command line
parser = argparse.ArgumentParser()
parser.add_argument("-i",dest='in_file',help='Path to combo-*.csv file containing traces for plotting.',default='')
args = parser.parse_args()
in_file = args.in_file
if in_file == '':
    in_file = input("Please enter the name of the file containing the multiple vHW traces for plotting > ")
#Load the input file in to an array and convert
in_array= np.genfromtxt(in_file,skip_header=1,dtype=str,delimiter=',')
in_array= np.core.defchararray.replace(in_array,'"','')
in_array= in_array.astype(float)
xmin = 0.8*np.min(in_array[:,::3])
xmax = 1.2*np.max(in_array[:,::3])

#Determine the number of profiles (samples)
Nprof = int(len(in_array[0])/3)

#Get the names of each profile
print("Detected "+str(Nprof)+" samples in the data file.")
names = np.array([],dtype=str)
print("Collecting names for display in figure legend:")
for idx in range(Nprof):
    names = np.append(names,input("Please enter name of sample "+str(idx+1)+" > "))


#Get the Figure Dimensions
figx = float(input("Please enter the figure X-size (inches) > "))
figy = float(input("Please enter the figure Y-size (inches) > "))

#Get marker style
marker_happy = False
markers = np.array(['.','o','v','s','D'],dtype=str)
while not marker_happy:
    print("\n\n\nHere is a list of marker styles:")
    print("\t 1 = dots")
    print("\t 2 = circles")
    print("\t 3 = triangles")
    print("\t 4 = squares")
    print("\t 5 = diamonds")
    mark_idx = int(input("Please select the marker style > ")) - 1
    marker = markers[mark_idx]

    msize = float(input("\nPlease select a marker size (Suggested = 4) > "))
    
    #Make a dummy plot to determine if user likes marker selection
    plt.figure(figsize=(figx,figy))
    for idx in range(Nprof):
        plt.plot(in_array[:,0+3*idx],in_array[:,1+3*idx],marker=marker,markersize=msize,label=names[idx],linestyle='',markeredgecolor='k')
    plt.xlabel('Sedimentation Coefficient (S)')
    plt.xlim(xmin,xmax)
    plt.ylabel('Boundary Fraction (%)')
    plt.tight_layout()

    print("\n\nDisplaying example plot.")

    plt.show()

    happy_str = input("\nAre you satisfied with the markers? (Y/N) > ")
    if happy_str.lower() == 'y':
        marker_happy = True
    plt.close('all')

#Determine where to put the legend
leg_happy = False
while not leg_happy:
    print('\n\nLegend can be set to the following locations:')
    print('\t0  = automatic placement')
    print('\t1  = upper right')
    print('\t2  = upper left')
    print('\t3  = lower left')
    print('\t4  = lower right')
    print('\t5  = right')
    print('\t6  = center left')
    print('\t7  = center right')
    print('\t8  = lower center')
    print('\t9  = upper center')
    print('\t10 = center')

    leg_loc = int(input("\nEnter your preferred legend location >"))

    print("\nDisplaying legend with selection "+str(leg_loc))
    plt.figure(figsize=(figx,figy))
    for idx in range(Nprof):
        plt.plot(in_array[:,0+3*idx],in_array[:,1+3*idx],marker=marker,markersize=msize,label=names[idx],linestyle='',markeredgecolor='k')
    plt.xlabel('Sedimentation Coefficient (S)')
    plt.xlim(xmin,xmax)
    plt.ylabel('Boundary Fraction (%)')
    plt.legend(loc=leg_loc,frameon=False,fontsize=10,handletextpad=0)
    plt.tight_layout()
    plt.show()
    happy_str = input("\nAre you satisfied with the legend location? (Y/N) > ")
    if happy_str.lower() == 'y':
        leg_happy = True
    plt.close('all')

oname = ''
while oname == '':
    oname = input("\n\nOptions set, please provide output name (Example: AUC_plot.pdf) > ")
if oname[-4:] != '.pdf':
    oname = oname+'.pdf'

plt.figure(figsize=(figx,figy))
for idx in range(Nprof):
    plt.plot(in_array[:,3*idx],in_array[:,3*idx],marker=marker,markersize=msize,label=names[idx],linestyle='',markeredgecolor='k')
plt.xlabel('Sedimentation Coefficient (S)')
plt.xlim(xmin,xmax)
plt.ylabel('Boundary Fraction (%)')
plt.legend(loc=leg_loc,frameon=False,fontsize=10,handletextpad=0)
plt.tight_layout()
plt.savefig(oname,format='pdf')
