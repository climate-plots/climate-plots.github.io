import uuid
import numpy as np
import os

def set_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)


def set_multiline_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        delimiter = uuid.uuid1()
        print(f'{name}<<{delimiter}', file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)

possible_graphs = [{'name':'AMO', 'image_path':'assets/img/AMO.png',
                        'text':'The Atlantic Multidecadal Oscillation',
                        'media_alt':'Data from https://psl.noaa.gov/data/timeseries/AMO/'},
                   {'name':'Ant_SIE_anom', 'image_path':'assets/img/Ant_SIE_anom.png',
                        'text':'Antarctic sea ice extent anomaly',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'Ant_SIE_climatology', 'image_path':'assets/img/Ant_SIE_climatology.png',
                        'text':'Antarctic sea ice extent climatology',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'Ant_SIE_year_anoms', 'image_path':'assets/img/Ant_SIE_year_anoms.png',
                        'text':'Antarctic sea ice extent anomalies, by year',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'Ant_SIE_by_year', 'image_path':'assets/img/Ant_SIE_by_year.png',
                        'text':'Antarctic sea ice extent, by year',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'Ant_SIE_year_anoms_standardised', 'image_path':'assets/img/Ant_SIE_year_anoms_standardised.png',
                        'text':'Antarctic sea ice extent anomalies converted to standard deviations, by year',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'Global_sea_ice_anom', 'image_path':'assets/img/Global_sea_ice_anom.png',
                        'text':'Global sea ice extent anomaly',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'Global_sea_ice_climatology', 'image_path':'assets/img/Global_sea_ice_climatology.png',
                        'text':'Global sea ice extent climatology',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'Global_sea_ice_year_anoms', 'image_path':'assets/img/Global_sea_ice_year_anoms.png',
                        'text':'Global sea ice extent anomalies, by year',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'Global_sea_ice_by_year', 'image_path':'assets/img/Global_sea_ice_by_year.png',
                        'text':'Global sea ice extent, by year',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'Global_sea_ice_year_anoms_standardised', 'image_path':'assets/img/Global_sea_ice_year_anoms_standardised.png',
                        'text':'Global sea ice extent anomalies converted to standard deviations, by year',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'Arctic_SIE_anom', 'image_path':'assets/img/Arctic_SIE_anom.png',
                        'text':'Arctic sea ice extent anomaly',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'Arctic_SIE_climatology', 'image_path':'assets/img/Arctic_SIE_climatology.png',
                        'text':'Arctic sea ice extent climatology',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'Arctic_SIE_year_anoms', 'image_path':'assets/img/Arctic_SIE_year_anoms.png',
                        'text':'Arctic sea ice extent anomalies, by year',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'Arctic_SIE_by_year', 'image_path':'assets/img/Arctic_SIE_by_year.png',
                        'text':'Arctic sea ice extent, by year',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'Arctic_SIE_year_anoms_standardised', 'image_path':'assets/img/Arctic_SIE_year_anoms_standardised.png',
                        'text':'Arctic sea ice extent anomalies converted to standard deviations, by year',
                        'media_alt':'Data from https://nsidc.org/data/g02135/versions/3'},
                   {'name':'IPO', 'image_path':'assets/img/IPO.png',
                        'text':'The Interdecadal Pacific Oscillation',
                        'media_alt':'Data from https://psl.noaa.gov/data/timeseries/IPOTPI/'},
                   {'name':'SAM_annual', 'image_path':'assets/img/SAM_annual.png',
                        'text':'The Southern Annular Mode, annual average',
                        'media_alt':'Data from https://legacy.bas.ac.uk/met/gjma/sam.html'},
                   {'name':'SOI', 'image_path':'assets/img/SOI.png',
                        'text':'The Southern Oscillation index describes El Niño and La Niña events',
                        'media_alt':'Data from https://www.ncei.noaa.gov/access/monitoring/enso/soi'},
                   {'name':'SST', 'image_path':'assets/img/SST.png',
                        'text':'Global average sea surface temperature, monthly',
                        'media_alt':'Data from https://www.ncei.noaa.gov/access/monitoring/global-temperature-anomalies/anomalies'},
                   {'name':'SST', 'image_path':'assets/img/SST_by_year.png',
                        'text':'Global average sea surface temperature plotted by year, monthly',
                        'media_alt':'Data from https://www.ncei.noaa.gov/access/monitoring/global-temperature-anomalies/anomalies'}]


def pick_a_graph():
    upper_lim = len(possible_graphs)
    graph = np.random.randint(upper_lim)

    set_output(name='image_path',
                value=possible_graphs[graph]['image_path'])

    set_output(name='text',
                value=possible_graphs[graph]['text'])

if __name__ == '__main__':
    pick_a_graph()
