import numpy as np
import pooch
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd


# Southern Annular Mode (SAM) index

def plot_SAM():

    # specify url
    fname_sam = pooch.retrieve(
        url="http://www.nerc-bas.ac.uk/public/icd/gjma/newsam.1957.2007.txt",
        known_hash=None,
    )

    # download and read data

    sam = pd.read_csv(fname_sam, skiprows=1, delim_whitespace=True,
        names=['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
           'Oct', 'Nov', 'Dec'])

    sam = pd.melt(sam, id_vars=['Year'], var_name=['Month'])
    sam['Date'] = pd.to_datetime(sam['Year'].astype(str) + '-' + sam['Month'].astype(str))
    sam = sam.sort_values(by=['Date']).drop(columns=['Month', 'Year']).reset_index(drop=['index'])
    sam = sam.set_index('Date')
    sam = sam.rename(columns={'value':'Southern Annular Mode'})

    plt.figure(figsize=(10,5))
    ax = plt.gca()

    sam.plot(marker='o', ax=ax, legend=False)

    plt.text('1990-01-01', -8, 'Climate-Plots.github.io',
        fontsize=12, color='black')

    plt.title('Southern Annular Mode (SAM) index')

    plt.hlines(y=0, xmin=sam.index.min(), xmax=sam.index.max(),
        color='black', linestyle='--', lw=1)

    plt.savefig('SAM.png', dpi=200, bbox_inches='tight')

if __name__ == '__main__':
    plot_SAM()
