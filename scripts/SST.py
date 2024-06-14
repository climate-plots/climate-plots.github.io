import numpy as np
import pooch
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd
import datetime
import matplotlib
import calendar


# Atlantic Multidecadal Oscillation

def plot_SST():

    today = datetime.date.today()

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

    # get total number of years in dataset to use later on
    years = list(sst.index.year.unique())

    # define a colourmap over all the years
    cmap = matplotlib.cm.YlOrRd(np.linspace(0,1,len(years)))

    # convert to xarray because I'm more comfortable with that
    ds_sst = xr.Dataset.from_dataframe(sst)

    # plot full time series
    #######################

    plt.figure(figsize=(10,5))
    ax = plt.gca()

    sst.plot(marker='o', ax=ax, legend=False)

    plt.text('1950-01-01', -0.6, 'Climate-Plots.github.io',
        fontsize=12, color='black')

    plt.title('Global Sea Surface Temperature')

    plt.hlines(y=0, xmin=sst.index.min(), xmax=sst.index.max(),
        color='black', linestyle='--', lw=1)

    plt.savefig('../assets/img/SST.png', dpi=200, bbox_inches='tight')

    # plot each year of data on top of each other
    ##############################################

    plt.figure(figsize=(10,5))

    for i, year in enumerate(range(1850, today.year+1)):
        ds_year = ds_sst['Anomaly'].sel(Date=slice('{0}-01-01'.format(year),
                                '{0}-12-31'.format(year)))
        # ds_year.plot(color=cmap[i])
        plt.plot(pd.DatetimeIndex(ds_year.Date).dayofyear, ds_year, color=cmap[i])

    plt.plot(pd.DatetimeIndex(ds_year.Date).dayofyear, ds_year, color='k', linewidth=3)


    plt.pcolormesh([-20,-15], [0,1], [[1978, 2000],[2000,today.year]], cmap='YlOrRd')
    CB = plt.colorbar()
    CB.ax.set_ylabel('Year', fontsize=30)

    plt.text(float(pd.DatetimeIndex(ds_year.Date).dayofyear[-1]+1), ds_year[-1].data, str(today.year), fontsize='large')

    plt.ylabel('Sea surface temperature anomaly (degrees Celsuis)')
    plt.xticks(np.linspace(15,380,13)[:-1], calendar.month_name[1:], rotation=90)
    plt.xlim(-10,376)
    plt.savefig('../assets/img/SST_by_year.png', bbox_inches='tight', dpi=200)

if __name__ == '__main__':
    plot_SST()
