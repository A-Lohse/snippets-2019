import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.widgets as wig
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

def philipC(NatUnEm,Ex_inflation,alpha):
    """This function takes values of Natural unemployment, expectec inflation, and the alpha value for the trade-off between those.
        The function then defines the Unemployment rate at inflation level 0.2 and vice verca. This is used to plot the a straigt line
        The deriviations from Makiew and Taylor's macro economics. The function returns unemployment and inflation"""
    Inflation = 0.2
    UnEm = NatUnEm + (Ex_inflation - Inflation)/alpha
    Unemployment = 0.2
    Inflation = Ex_inflation - alpha*(Unemployment - NatUnEm)


    return list([UnEm,Inflation])

def PCplot(NatUnEm,Ex_inflation,alpha=1):
    """This function plots the first two values given to it, as Unemployment and Inflation. 
    It plots it by assuming that the other value is 0.2 (as calculated in philipsC function)"""
    x = philipC(NatUnEm,Ex_inflation,alpha) 
    plt.plot([0.2,x[0]],[x[1],0.2])
    plt.xlabel("Unemployment")
    plt.ylabel("Inflation")
    plt.xlim(0,10)
    plt.ylim(0,10)

#%matplotlib inline
style = {'description_width': 'initial'}
exi_slider = widgets.FloatSlider(min=0,max=10,value=2,step=0.5,description = "Expected inflation",style=style)
alp_slider = widgets.FloatSlider(min=0.1,max=3,value=1,step=0.2,description = "Alpha value for trade-off",style=style)
NUE_slider = widgets.FloatSlider(min=0,max=7,value=2,step=0.5, description ="Natural unemployment",style=style)
interact(PCplot, Ex_inflation =  exi_slider ,NatUnEm = NUE_slider, alpha =  alp_slider)