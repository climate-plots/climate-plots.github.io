import numpy as np
import pooch
import matplotlib.pyplot as plt
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

    # convert to xarray because I'm more comfortable with that
    ds = xr.Dataset.from_dataframe(df_SIE)

    # calculate daily climatology
    ds_daily_clim =ds.sel(Date=slice('1981-01-01','2010-12-31')).groupby('Date.dayofyear').mean()

    # plot daily climatology
    ########################
    plt.figure(figsize=(7,4))
    ds_daily_clim['Extent'].plot()
    plt.text(150, 4, 'Climate-Plots.github.io',
        fontsize=12, color='black')
    plt.savefig('../assets/img/Ant_SIE_climatology.png', dpi=200, bbox_inches='tight')
    plt.close()

    # calculate daily anomalies
    ds_anoms = ds.groupby('Date.dayofyear') - ds_daily_clim

    # plot daily anomalies
    ######################
    plt.figure(figsize=(13,5))
    window=7
    ds_anoms.Extent.rolling(Date=window).mean().plot(color='k')
    plt.hlines(0, np.datetime64('1978-09-01'), np.datetime64('2024-05-01'), 'k')
    plt.scatter(ds_anoms['Date'], ds_anoms['Extent'].rolling(Date=window).mean(),
                c=ds_anoms['Extent'].rolling(Date=window).mean(), cmap='RdBu', edgecolors=None,
               vmin= ds_anoms['Extent'].rolling(Date=window).mean().min(),
               vmax= ds_anoms['Extent'].rolling(Date=window).mean().max())

    plt.text(np.datetime64('1978-09-01'), 2.45,'Antarctic Sea Ice Extent Anomaly', fontsize=20, weight='bold')
    plt.text(np.datetime64('1978-09-01'), 2,'Relative to 1981-2010 ($10^{6}$ km$^{2}$)', fontsize=15)
    plt.ylabel('')
    plt.xlabel('')

    plt.xlim(np.datetime64('1978-05-01'), np.datetime64('2025-01-01'))

    # ax = plt.gca()
    # ax.spines[['right', 'top']].set_visible(False)
    # # ax.tick_params(axis='x', which='both', length=0)

    # plt.axis('off')
    # fig = plt.gcf()
    # fig.axes.get_yaxis().set_visible(False)
    plt.text(np.datetime64('2005-01-01'), -2.5, 'Climate-Plots.github.io',
        fontsize=12, color='black')
    plt.savefig('../assets/img/Ant_SIE_anom.png', dpi=300, bbox_inches='tight')
    plt.close()


    # plot each year of anomalies on top of each other
    ##################################################
    plt.figure(figsize=(10,5))

    for i, year in enumerate(range(1978, today.year+1)):
        ds_year = ds_anoms.sel(Date=slice('{0}-01-01'.format(year),
                                '{0}-12-31'.format(year)))#.rolling(Date=7).mean()
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

if __name__ == '__main__':
    plot_Ant_SIE()

