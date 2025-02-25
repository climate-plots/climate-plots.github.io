import numpy as np
import pooch
import matplotlib.pyplot as plt
import matplotlib
import xarray as xr
import pandas as pd
import datetime
import calendar


def plot_Ant_SIE():

    today = datetime.date.today()

    fname_sie_S = pooch.retrieve(
        url="ftp://sidads.colorado.edu/pub/DATASETS/NOAA/G02135/south/daily/data/S_seaice_extent_daily_v3.0.csv",
        known_hash=None,
        path='./'
    )

    df_SIE = pd.read_csv(fname_sie_S, skipinitialspace=True, header=[0],skiprows=[1])

    # convert to proper datetime index
    df_SIE['Date'] = pd.to_datetime(df_SIE[['Year','Month','Day']])
    df_SIE.set_index('Date', inplace=True)

    # get total number of years in dataset to use later on
    years = list(df_SIE.index.year.unique())

    # define a colourmap over all the years
    cmap = matplotlib.cm.YlOrRd(np.linspace(0,1,len(years)))

    # convert to xarray because I'm more comfortable with that
    ds = xr.Dataset.from_dataframe(df_SIE)

    # calculate daily climatology
    # smooth over two days to deal with two-daily observations in
    # beginning of record
    ds_daily_clim =ds.sel(Date=slice('1981-01-01',
            '2010-12-31')).groupby('Date.dayofyear').mean(
            ).rolling(dayofyear=2).mean()

    # calculate daily anomalies
    ds_anoms = ds.groupby('Date.dayofyear') - ds_daily_clim

    # Calculate standard deviations for anomalies
    ds_std = ds.sel(Date=slice('1981-01-01','2010-12-31')).groupby(
    ds.sel(Date=slice('1981-01-01','2010-12-31')).Date.dt.dayofyear).std()

    ds_anoms_std = ds_anoms.groupby(ds_anoms.Date.dt.dayofyear)/ds_std

    # Harden script to work at beginining of year
    window = np.min([7,df_SIE.index.dayofyear[-1]])

    # plot each year of data on top of each other
    ##############################################

    plt.figure(figsize=(10,5))

    for i, year in enumerate(range(1978, today.year+1)):
        ds_year = ds.Extent.sel(Date=slice('{0}-01-01'.format(year),
                                '{0}-12-31'.format(year))).rolling(Date=window).mean()
        # ds_year.plot(color=cmap[i])
        plt.plot(pd.DatetimeIndex(ds_year.Date).dayofyear, ds_year, color=cmap[i])

    plt.plot(pd.DatetimeIndex(ds_year.Date).dayofyear, ds_year, color='k', linewidth=3)


    plt.pcolormesh([-20,-15], [0,1], [[1978, 2000],[2000,today.year]], cmap='YlOrRd')
    CB = plt.colorbar()
    CB.ax.set_ylabel('Year', fontsize=30)

    plt.text(float(pd.DatetimeIndex(ds_year.Date).dayofyear[-1]), ds_year[-1].data-2, str(today.year), fontsize='large')

    plt.text(15, 0.3, 'Climate-Plots.github.io',
        fontsize=12, color='black')

    plt.ylabel('Sea Ice Extent\n(millions of square kilometres)')
    plt.xticks(np.linspace(15,380,13)[:-1], calendar.month_name[1:], rotation=90)
    plt.xlim(-10,376)
    plt.savefig('../assets/img/Ant_SIE_by_year.png', bbox_inches='tight', dpi=200)

    # plot daily climatology
    ########################
    plt.figure(figsize=(7,4))
    ds_daily_clim['Extent'].plot()
    plt.text(150, 4, 'Climate-Plots.github.io',
        fontsize=12, color='black')
    plt.savefig('../assets/img/Ant_SIE_climatology.png', dpi=200, bbox_inches='tight')
    plt.close()


    # plot daily anomalies
    ######################
    color_lim = np.max([-ds_anoms['Extent'].rolling(Date=window).mean().min(),
                    ds_anoms['Extent'].rolling(Date=window).mean().max()])

    plt.figure(figsize=(13,5))
    ds_anoms.Extent.rolling(Date=window).mean().plot(color='k')
    plt.hlines(0, np.datetime64('1978-09-01'),
                np.datetime64(today) + np.timedelta64(30, 'D'), 'k')
    plt.scatter(ds_anoms['Date'], ds_anoms['Extent'].rolling(Date=window).mean(),
                c=ds_anoms['Extent'].rolling(Date=window).mean(), cmap='RdBu', edgecolors=None,
               vmin= -color_lim, vmax= color_lim)

    plt.text(np.datetime64('1978-09-01'), 2.35,'Antarctic Sea Ice Extent Anomaly', fontsize=20, weight='bold')
    plt.text(np.datetime64('1978-09-01'), 1.9,'Relative to 1981-2010 ($10^{6}$ km$^{2}$)', fontsize=15)
    plt.ylabel('')
    plt.xlabel('')

    plt.xlim(np.datetime64('1978-05-01'),
                np.datetime64(today) + np.timedelta64(180, 'D'))

    # ax = plt.gca()
    # ax.spines[['right', 'top']].set_visible(False)
    # # ax.tick_params(axis='x', which='both', length=0)

    # plt.axis('off')
    # fig = plt.gcf()
    # fig.axes.get_yaxis().set_visible(False)
    plt.text(np.datetime64('1990-01-01'), -2.5, 'Climate-Plots.github.io',
        fontsize=15, color='black')
    plt.savefig('../assets/img/Ant_SIE_anom.png', dpi=300, bbox_inches='tight')
    plt.close()


    # plot each year of anomalies on top of each other
    ##################################################
    plt.figure(figsize=(10,5))

    for i, year in enumerate(range(1978, today.year+1)):
        ds_year = ds_anoms.sel(Date=slice('{0}-01-01'.format(year),
                                '{0}-12-31'.format(year)))
        plt.plot(ds_year.Date.dayofyear, ds_year.Extent, color='grey')

    plt.plot(ds_year.Date.dayofyear, ds_year.Extent, color='red', linewidth=3)

    plt.text(ds_year.Date.dayofyear[-1].data, ds_year.Extent[-1].data-0.3, str(today.year), fontsize='large')

    plt.ylabel('Sea Ice Extent anomaly\n(millions of square kilometres)')
    plt.xticks(np.linspace(15,380,13)[:-1], calendar.month_name[1:], rotation=90)
    plt.hlines(0,-10,376, color='k')
    plt.xlim(-10,376)
    plt.text(2, -2.8, 'Climate-Plots.github.io',
        fontsize=12, color='black')
    plt.savefig('../assets/img/Ant_SIE_year_anoms.png', bbox_inches='tight', dpi=200)
    plt.close()


    # Plot anomalies by standard deviation
    ######################################

    plt.figure(figsize=(10,5))

    for i, year in enumerate(range(1978, today.year+1)):
        ds_year = ds_anoms_std.sel(Date=slice('{0}-01-01'.format(year),
                                '{0}-12-31'.format(year)))
        ds_year_dayofyear = ds_anoms.sel(Date=slice('{0}-01-01'.format(year),
                                '{0}-12-31'.format(year)))
        # ds_year.Extent.plot(color=cmap[i])
        plt.plot(ds_year_dayofyear.Date.dayofyear,
                 (ds_year.swap_dims({'Date': 'dayofyear'}).Extent).rolling(dayofyear=window).mean(),
                 color=cmap[i])

    plt.plot(ds_year_dayofyear.Date.dayofyear,
             (ds_year.swap_dims({'Date': 'dayofyear'}).Extent).rolling(dayofyear=window).mean(),
             color='k', linewidth=3)

    plt.pcolormesh([-20,-15], [0,1], [[1978, 2000],[2000,today.year]], cmap='YlOrRd')
    CB = plt.colorbar()
    CB.ax.set_ylabel('Year', fontsize=30)

    plt.text(ds_year_dayofyear.dayofyear[-1].data+ 10,
             (ds_year.swap_dims({'Date': 'dayofyear'}).Extent).rolling(dayofyear=window).mean()[-1].data,
             str(today.year), fontsize='large')

    plt.ylabel('Sea Ice Extent anomaly\n(Standard deviations from the 1981-2010 climatology)')
    plt.xticks(np.linspace(15,380,13)[:-1], calendar.month_name[1:], rotation=90)
    plt.hlines(0,-10,376)
    plt.xlim(-10,376)
    plt.text(2, -7, 'Climate-Plots.github.io',
    fontsize=12, color='black')
    plt.savefig('../assets/img/Ant_SIE_year_anoms_standardised.png', bbox_inches='tight', dpi=200)

if __name__ == '__main__':
    plot_Ant_SIE()

