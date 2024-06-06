import uuid
import numpy as np

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
                        'text':'The Atlantic Multidecadal Oscillation'},
                   {'name':'Ant_SIE_anom', 'image_path':'assets/img/Ant_SIE_anom.png',
                        'text':'Antarctic sea ice extent anomaly'},
                   {'name':'Ant_SIE_climatology', 'image_path':'assets/img/Ant_SIE_climatology.png',
                        'text':'Antarctic sea ice extent climatology'},
                   {'name':'Ant_SIE_year_anoms', 'image_path':'assets/img/Ant_SIE_year_anoms.png',
                        'text':'Antarctic sea ice extent anomalies, by year'},
                   {'name':'IPO', 'image_path':'assets/img/IPO.png',
                        'text':'The Interdecadal Pacific Oscillation'},
                   {'name':'SAM_annual', 'image_path':'assets/img/SAM_annual.png',
                        'text':'The Southern Annular Mode, annual average'}]


def pick_a_graph():
    upper_lim = len(possible_graphs)
    graph = np.randint(upper_lim)

    set_output(name='image_path',
                value=possible_graphs[graph]['image_path'])

    set_output(name='text',
                value=possible_graphs[graph]['text'])

if __name__ == '__main__':
    pick_a_graph()
