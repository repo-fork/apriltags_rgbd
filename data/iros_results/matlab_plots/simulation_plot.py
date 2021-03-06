import numpy as np
from ss_plotting.make_plots import plot
import matplotlib.pyplot as plt

data_translation = [0.004, 0.014, 0.028, 0.024, 0.022, 0.042, 0.036, 0.038, 0.036, 0.04, 0.068, 0.036, 0.054, 0.074, 0.074, 0.096, 0.07, 0.088, 0.094, 0.104, 0.108, 0.122, 0.13, 0.114, 0.12, 0.148, 0.158, 0.154, 0.166, 0.15, 0.16, 0.176, 0.176, 0.178, 0.194, 0.22, 0.214, 0.16, 0.208, 0.194, 0.196, 0.22, 0.216, 0.234, 0.252, 0.246, 0.254, 0.282, 0.262, 0.236, 0.204, 0.27, 0.262, 0.274, 0.256, 0.26, 0.284, 0.316, 0.27, 0.266, 0.294, 0.278, 0.27, 0.278, 0.298, 0.296, 0.302, 0.324, 0.322, 0.332, 0.3, 0.34, 0.336, 0.352, 0.318, 0.348, 0.368, 0.322, 0.328, 0.312, 0.326, 0.364, 0.378, 0.346, 0.342, 0.348, 0.332, 0.34, 0.37, 0.328, 0.36, 0.344, 0.38, 0.344, 0.324, 0.37, 0.372, 0.394, 0.384, 0.38, 0.36, 0.406, 0.4, 0.406, 0.346, 0.372, 0.372, 0.402, 0.358, 0.368, 0.418, 0.4, 0.368, 0.338, 0.39, 0.396, 0.404, 0.38, 0.406, 0.406, 0.414]

x_trans = np.arange(0.6, 1.8, 0.01)
series = [(x_trans, data_translation)]
series_labels = ['Simulated Data']
series_colors = ['red']

fig, ax = plot(series, 
     series_labels=series_labels,
     series_colors=series_colors,
     linewidth=5)

data_rotation = [0, 0, 0, 0, 0, 0, 0, 0, 0.008, 0.014, 0.046, 0.058, 0.112, 0.14, 0.182, 0.226, 0.328, 0.284, 0.276, 0.346, 0.322, 0.312, 0.36, 0.34, 0.31, 0.3, 0.298, 0.324, 0.296, 0.29, 0.274, 0.254, 0.286, 0.262, 0.254, 0.24, 0.224, 0.23, 0.208, 0.222, 0.216, 0.2, 0.182, 0.194, 0.168, 0.212, 0.178, 0.182, 0.196, 0.152, 0.174, 0.16, 0.16, 0.2, 0.168, 0.164, 0.154, 0.134, 0.156, 0.16, 0.13, 0.154, 0.134, 0.162, 0.144, 0.154, 0.114, 0.124, 0.126, 0.138, 0.144, 0.114, 0.104, 0.11, 0.098, 0.136, 0.098, 0.108, 0.096, 0.096, 0.116, 0.11, 0.12, 0.134, 0.132, 0.114, 0.126, 0.152, 0.136, 0.172]
x_rot = np.arange(90)
series2 = [(x_rot, data_rotation)]
series_labels2 = ['Simulated Data']
series_colors2 = ['red']

fig2, ax2 = plot(series2, 
     series_labels=series_labels2,
     series_colors=series_colors2,
     linewidth=5)

plt.show()