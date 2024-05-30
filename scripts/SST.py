import numpy as np
import pooch
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd


# Atlantic Multidecadal Oscillation

def plot_SST():

    # specify url
    fname_sst = pooch.retrieve(
        url="https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/ocean/all/12/1850-2024.csv",
        known_hash=None,
    )

    # download and read data
    sst = pd.read_csv(fname_sst, skiprows=4, sep=',')

    # convert time to datetime
    sst['Date'] = pd.to_datetime(sst['Date'], format='%Y%m')
    sst.set_index('Date', inplace=True)

    plt.figure(figsize=(10,5))
    ax = plt.gca()

    sst.plot(marker='o', ax=ax, legend=False)

    plt.text('1950-01-01', -0.6, 'Climate-Plots.github.io',
        fontsize=12, color='black')

    plt.title('Global Sea Surface Temperature')

    plt.hlines(y=0, xmin=sst.index.min(), xmax=sst.index.max(),
        color='black', linestyle='--', lw=1)

    plt.savefig('../assets/img/SST.png', dpi=200, bbox_inches='tight')

if __name__ == '__main__':
    plot_SST()
