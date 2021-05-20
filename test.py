# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

from SCD_Reduction.SCDCalibratePanels2Diagnostics import SCDCalibratePanels2DiagnosticsPlot

LoadIsawPeaks('data/SC100K_Monoclinic_C.integrate', OutputWorkspace='pws')
LoadIsawUB('pws', 'data/SC100K_Monoclinic_C.mat')

config = {
    "prefix": "idealTOPAZ",
    "type": "png",
    "saveto": "./tmp",
    }
pws = mtd['pws']

SCDCalibratePanels2DiagnosticsPlot(
    pws,
    ["bank13", "bank14", "bank16"],
    config,
    showPlots=True,
    )
