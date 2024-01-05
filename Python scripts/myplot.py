import matplotlib.pyplot as plt
# import matplotlib.lines as mlines
import numpy as np

plot_x = np.arange(0.1, 1.0, 0.05)
filename1='modes_full_vec/structure_n_1310sh2c1SiO2ft0.34ed0.34wg0.1-1.0.dat'
filename2='modes_full_vec/mode_types.dat'
data = np.loadtxt(filename1, delimiter=",", usecols=[1,2,3,4,5,6])
shape_raw = np.loadtxt(filename2, dtype=str, delimiter=",", skiprows=1, usecols=[0,1,2,3,4,5])
for i in range(6):
	shape_raw_1 = shape_raw[:,i]
	mode_0 = data[:,i]	
	for k in range(len(data)):
		mode_0_inv = mode_0[k-1]
		shape_raw_2 = shape_raw_1[k-1][0:3]
		wg_widths_inv = plot_x[k-1]
		# print(mode_0_inv)
		# print(wg_widths_inv)
		# print(shape_raw_2)
		if shape_raw_2=="qTE":
			# plt.plot(wg_widths_inv, mode_0_inv,'-^')
			red_dot, = plt.plot(wg_widths_inv, mode_0_inv, color='red', marker='^', markersize=7)
			plt.plot(plot_x, mode_0, color='black', markersize=1)
			# plt.legend(['Mode0', 'Mode1', 'Mode2', 'Mode3', 'Mode4', 'Mode5'], loc=4)
		elif shape_raw_2=="qTM":
			# plt.plot(wg_widths_inv, mode_0_inv, '-o')
			white_cross, = plt.plot(wg_widths_inv, mode_0_inv, color='blue', marker='o', markersize=7)
			# plt.plot(plot_x, mode_0, color='red', markersize=1)
plt.title("$n_{eff}$ vs Waveguide width")
plt.xlabel("Waveguide width")
plt.ylabel("$n_{eff}$")
plt.legend([red_dot, (red_dot, white_cross)], ["TE mode", "TM mode"], loc='best')
plt.show()