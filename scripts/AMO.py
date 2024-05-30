import numpy as np
import pooch
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd


# Atlantic Multidecadal Oscillation

def plot_AMO():

    # specify url
    fname_amo = pooch.retrieve(
        url="https://psl.noaa.gov/data/correlation/amon.us.long.data",
        known_hash=None,
    )

    # download and read data
    amo = pd.read_csv(fname_amo, skiprows=3, nrows=72, delim_whitespace=True)

    # convert time to datetime
    amo = pd.read_csv(fname_amo, skiprows=1, nrows=167, delim_whitespace=True,
        names=['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May',
            'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    amo
    amo = pd.melt(amo, id_vars=['Year'], var_name='Month')
    amo['Date'] = pd.to_datetime(amo['Year'].astype(str) + '-' + amo['Month'].astype(str))
    amo = amo.sort_values(by=['Date']).drop(columns=['Month', 'Year']).reset_index(drop=['index'])
    amo = amo.set_index('Date')
    amo = amo.rename(columns={'value':'Atlantic Multi-decadal Oscillation '})


    plt.figure(figsize=(10,5))
    ax = plt.gca()

    amo.plot(marker='o', ax=ax, legend=False)

    plt.text('1950-01-01', -0.6, 'Climate-Plots.github.io',
        fontsize=12, color='black')

    plt.title('Atlantic Multidecadal Oscillation Index')

    plt.hlines(y=0, xmin=amo.index.min(), xmax=amo.index.max(),
        color='black', linestyle='--', lw=1)

    plt.savefig('../assets/img/AMO.png', dpi=200, bbox_inches='tight')

if __name__ == '__main__':
    plot_AMO()
