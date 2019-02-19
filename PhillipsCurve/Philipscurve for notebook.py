%matplotlib inline
from ipywidgets import fixed, FloatSlider, interact, interactive, interact_manual
import matplotlib.pyplot as plt
import matplotlib.widgets as wig
import numpy as np

def philip_c(nat_un_em, ex_inflation, alpha,pv):
    """This function calculates values for inflation and unemployment. 
        
        The values calculated, are the values for inflation and unemployment, given that the other is 0.2.
        The idea is, that the values can be plottet as a straihgt line that shows the relationship between 
        inflation and unemployment in the short run. The deriviations are from Mankiew and Taylor's macro
        economics. 
        
        Args:
            alpha (float) : The coeffecient for the trade-off between inflation and unemployment. 
            No default value given here, but when the interact function is called, 
            the default value of natural rate of unemployment is 1.
            
            ex_inflation (float) : The expectet inflation rate in percent (2=2%). No default value given,
            but when the interact function is called, the default value of natural rate of unemployment is 2. 
            
            nat_un_em (float) : The natural rate of unemployment in percent (2=2%). No default value given,
            but when the interact function is called, the default value of natural rate of unemployment is 2. 
            
            pv (float) : The value of inflation where unemployment should be calculated, and vice versa
      
      Returns: 
                returns two return values. 
                un_em (float) : The unemployment rate  in percent (2=2%), given the 3 parameters and inflation = 0.2
                inflation (float) : The inflation rate in percent (2=2%), given the 3 parameters and unemployment = 0.2
    """
    inflation = pv
    un_em = nat_un_em + (ex_inflation - inflation)/alpha
    unemployment = pv
    inflation = ex_inflation - alpha*(unemployment - nat_un_em)


    return un_em, inflation

def pc_plot(nat_un_em,ex_inflation,alpha=1,pv=0.2):
    """This function plot two values as a relationship between unemployment and inflation. 
        
        The function plots the unemployment and inflation, given the 3 paramaters, at a given level of the other (pv)
        
        Args:
            alpha (float) : The coeffecient for the trade-off between inflation and unemployment. A default value of 1 is given
            ex_inflation (float) : The expectet inflation rate in percent (2=2%). No default value given, but when the interact function is called, the default value of natural rate of unemployment is 2. 
            nat_un_em (float) : The natural rate of unemployment in percent (2=2%). No default value given, but when the interact function is called, the default value of natural rate of unemployment is 2. 
            pv (float) : The value of inflation where unemployment should be calculated, and vice versa. A default value of 0.2 is given for a nice visualization. 
            
        Returns: 
            A plot
        """
    x = philip_c(nat_un_em,ex_inflation,alpha,pv) 
    plt.plot([pv,x[0]],[x[1],pv])
    plt.xlabel("Unemployment")
    plt.ylabel("Inflation")
    plt.xlim(0,8)
    plt.ylim(0,8)