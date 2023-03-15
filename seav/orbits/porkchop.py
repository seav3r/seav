#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

class PorkchopPlot:
    def __init__(
        self,
        tof_range=(0, 500),
        dep_date_range=(1, 366),
        arr_date_range=(1, 366),
        dep_dv_range=(0, 12),
        arr_dv_range=(0, 12),
    ):
        self.tof_range = tof_range
        self.dep_date_range = dep_date_range
        self.arr_date_range = arr_date_range
        self.dep_dv_range = dep_dv_range
        self.arr_dv_range = arr_dv_range

    def generate(self):
        # Define the time of flight and departure and arrival dates
        TOF = np.arange(*self.tof_range, 1)  # Time of flight
        dep_date = np.arange(*self.dep_date_range, 1)  # Departure date
        arr_date = np.arange(*self.arr_date_range, 1)  # Arrival date

        # Define the departure and arrival delta-V values
        dep_dv = np.arange(*self.dep_dv_range, 1)  # Departure delta-V
        arr_dv = np.arange(*self.arr_dv_range, 1)  # Arrival delta-V

        # Define the mesh grid for the time of flight, departure and arrival dates
        TOF_mesh, dep_mesh, arr_mesh = np.meshgrid(TOF, dep_date, arr_date)

        # Calculate the delta-V values for each combination of time of flight,
        # departure and arrival dates
        dv_mesh = np.zeros_like(TOF_mesh)
        for i in range(len(dep_dv)):
            for j in range(len(arr_dv)):
                dv_mesh[:, i, j] = np.sqrt(
                    dep_dv[i] ** 2 + arr_dv[j] ** 2 + (TOF_mesh * 0.1) ** 2
                )

        # Create the porkchop plot
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(1, 1, 1)
        contour = ax.contourf(
            dep_mesh, arr_mesh, dv_mesh.min(axis=0), cmap="plasma"
        )
        cbar = fig.colorbar(contour)
        ax.set_xlabel("Departure Date (day of year)")
        ax.set_ylabel("Arrival Date (day of year)")
        cbar.set_label("Delta-V (km/s)")
        ax.set_title("Porkchop Plot")
        plt.show()