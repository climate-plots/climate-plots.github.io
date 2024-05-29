import numpy as np
import pooch
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd


# Interdecadal Pacific Oscillation (IPO) index

def plot_IPO():

    # specify url
    fname_ipo = pooch.retrieve(
        url="https://psl.noaa.gov/data/timeseries/IPOTPI/tpi.timeseries.ersstv5.data",
        known_hash=None,
    )

    # download and read data
    ipo = pd.read_csv(fname_ipo, skiprows=1, nrows=169, delim_whitespace=True,
        names=['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
       'Oct', 'Nov', 'Dec'])

    # convert time to datetime
    ipo = pd.melt(ipo, id_vars=['Year'], var_name='Month')
    ipo['Date'] = pd.to_datetime(ipo['Year'].astype(str) + '-' + ipo['Month'].astype(str))
    ipo = ipo.sort_values(by=['Date']).drop(columns=['Month', 'Year']).reset_index(drop=['index'])
    ipo = ipo.set_index('Date')
    ipo = ipo.rename(columns={'value':'Interdecadal Pacific Oscillation'})

    plt.figure(figsize=(10,5))
    ax = plt.gca()

    ipo.plot(marker='o', ax=ax, legend=False)

    plt.text('1970-01-01', -2.5, 'Climate-Plots.github.io',
        fontsize=12, color='black')

    plt.title('Interdecadal Pacific Oscillation (IPO) index')

    plt.hlines(y=0, xmin=ipo.index.min(), xmax=ipo.index.max(),
        color='black', linestyle='--', lw=1)

    plt.savefig('../assets/img/IPO.png', dpi=200, bbox_inches='tight')

if __name__ == '__main__':
    plot_IPO()
