# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 5))
gs = fig.add_gridspec(7, 15)
# -- col combo plot
hist_observed_col = fig.add_subplot(gs[1:, 6])  # hist_y1
hist_observed_col.get_yaxis().set_ticks([])
hist_calculated_col = fig.add_subplot(gs[0, 0:6])  # hist_x1
hist_calculated_col.get_xaxis().set_ticks([])
scatter_col = fig.add_subplot(gs[1:, 0:6])  # scatter1
scatter_col.grid(color='k', linestyle='--', alpha=0.25)
scatter_col.set_xlabel("calculated column number")
scatter_col.set_ylabel("observed column number")
# -- row combo plot
hist_observed_row = fig.add_subplot(gs[1:, 14])  # hist_y2
hist_observed_row.get_yaxis().set_ticks([])
hist_calculate_row = fig.add_subplot(gs[0, 8:14])  # hist_x2
hist_calculate_row.get_xaxis().set_ticks([])
scatter_row = fig.add_subplot(gs[1:, 8:14])  # scatter2
scatter_row.grid(color='k', linestyle='--', alpha=0.25)
scatter_row.set_xlabel("calculated row number")
scatter_row.set_ylabel("observed row number")

fig.show()