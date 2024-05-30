import numpy as np
import pooch
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd


# Southern Oscillation index

def plot_SOI():

    # specify url
    fname_soi = pooch.retrieve(
        url="https://www.cpc.ncep.noaa.gov/data/indices/soi",
        known_hash=None,
    )

    # download and read data
    # the final row with data is pathalogical.
    # The separator disappears because the fill value
    # consumes all the space. Will need to do someting clever.
    # For now, just limit the number of rows.

    soi = pd.read_csv(fname_soi, skiprows=3, nrows=73, delim_whitespace=True)

    soi = pd.melt(soi, id_vars=['YEAR'], var_name='Month')
    soi['Date'] = pd.to_datetime(soi['YEAR'].astype(str) + '-' + soi['Month'].astype(str))
    soi = soi.sort_values(by=['Date']).drop(columns=['Month', 'YEAR']).reset_index(drop=['index'])
    soi = soi.set_index('Date')
    soi = soi.rename(columns={'value':'Southern Oscillation Index'})

    plt.figure(figsize=(10,5))
    ax = plt.gca()

    soi.plot(marker='o', ax=ax, legend=False)

    plt.text('1960-01-01', -6, 'Climate-Plots.github.io',
        fontsize=12, color='black')

    plt.title('Southern Oscillation Index')

    plt.hlines(y=0, xmin=soi.index.min(), xmax=soi.index.max(),
        color='black', linestyle='--', lw=1)

    plt.savefig('../assets/img/SOI.png', dpi=200, bbox_inches='tight')

if __name__ == '__main__':
    plot_SOI()
