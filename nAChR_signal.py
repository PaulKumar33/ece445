import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import scipy.integrate as sc
import time
import random


class nAChR_Signal:
    def __init__(self):
        pass

    def Signal_model(self, x, t):
        '''
        this is the main function for the model
        :param x: parameters to run the model.
                    x[0] is the dose concentration
                    x[1] is the a time constant in the drug conc function
                    x[2] is the b time constant ""

        :param t: time window for the simulation
        :return:
        '''
        ##define time constants
        tn = 0
        ts = 0
        tc = 0

        a = x[1]
        b = x[2]

        threshc = x[3]
        threshs = x[4]
        threshn = x[5]

        #define the drug amount variable
        drug = x[0]*sum(np.exp(a*t)*np.exp(b*t))


        ##define mode dynamic variables
        dndt = (1/tn)*((0.5*(1-np.tanh(c-threshc))*n)+An*(1-n))      #0.5*(1-np.tanh(c-theshc)) is Bn
        dsdt = (1/ts)*(B*s+(0.5*(1-np.tanh(n + drug-threshs)))*(1-s))
        dcdt = (1/tc)*(Bc*c+(0.5*(1-np.tanh(s+n-theshc)))*(1-s))



    def Run_model(self):
        pass
