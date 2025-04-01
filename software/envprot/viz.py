import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.offsetbox import AnchoredText
import seaborn as sns

def lit_mapper():
    """
    Returns a dictionary mapping sources of the E. coli data with standard colors
    and glyphs. This ensures constant marking of data across plots.
    """
    rng = np.random.default_rng(666)
    colors, _ = get_colors()
    mapper = {
        'Bremer & Dennis 2008': {'m': 'X'},
        'Brunschede et al. 1977': {'m': 's'},
        'Dai et al. 2016': {'m': 'o'},
        'Forchhammer & Lindahl 1971': {'m': 'v'},
        'Li et al. 2014': {'m': 'd'},
        'Schmidt et al. 2016': {'m': '8'},
        'Scott et al. 2010': {'m': '^'},
        'Wu et al. 2021': {'m': '<'},
        'Bremer & Dennis, 1996': {'m': '>'},
        'Dalbow & Young, 1975': {'m': 'P'},
        'Young & Bremer, 1976': {'m': 'h'},
        'Skjold et al. 1973': {'m': '*'},
        'Dong et al. 1996': {'m': 'p'},
        'Dong et al. 1995': {'m': 'v'},
        'Bentley et al. 1990': {'m': 'X'},
        'Erickson et al. 2017': {'m': 'o'},
        'Oldewurtle et al. 2021': {'m': 's'},
        'Mori et al. 2017': {'m': '*'},
        'Sloan and Urban, 1976': {'m': 'h'},
        'Li et al. 2018': {'m': '>'},
        'Korem Kohanim et al. 2018': {'m': 'd'},
        'Panlilio et al. 2021': {'m': 'p'},
        'Basan et al. 2015': {'m': '8'},
        'You et al. 2013': {'m': 'h'},
        'Hernandez & Bremer 1993': {'m': 'X'},
        'Farewell & Neidhart 1998': {'m': 'h'},
        'Kepes & Beguin, 1966': {'m': 'o'},
        'Coffman et al. 1971':  {'m': 's'},
        'Morris & Hansen, 1973': {'m': '*'},
        'Schleif et al. 1973': {'m': 'v'},
        'Lacroute & Stent 1968': {'m': 'p'},
        'Dennis & Bremer 1974': {'m': 's'},
        'Albertson & Nyström 1994': {'m': '^'},
        'Gausing 1972': {'m': '>'},
        'Schleif 1967': {'m': '<'},
        'Hernandez & Bremer 1993': {'m': 'v'},
        'Pedersen 1984': {'m': 'X'},
        'Taheri-Araghi et al. 2015': {'m': 'o'},
        'Pierucci 1978': {'m': 'v'},
        'Grossman et al. 1982': {'m': 'X'},
        'Zaritsky & Woldringh 1978': {'m': '<'},
        'Trueba & Woldringh 1980': {'m': 's'},
        'Zaritsky et al. 1993': {'m': '>'},
        'Si et al. 2017': {'m': '^'},
        'Caglar et al. 2017': {'m': 'h'},
        'Li et al. 2014': {'m': 'p'},
        'Mori et al. 2021': {'m': 'P'},
        'Peebo et al. 2015': {'m': '*'},
        'Schmidt et al. 2016': {'m': 'o'},
        'Soufi et al. 2015': {'m': '8'},
        'Valgepea et al. 2013': {'m': 'd'},
        'Basan et al. 2015': {'m': '^'},
        'Dai et al. 2016': {'m': 'o'},
        'Churchward et al. 1982': {'m': '>'},
        'Neidhardt et al. 1992': {'m': 'v'},
        'Wright & Lockhart 1964': {'m': '<'},
        'Chohji et al. 1976': {'m': 'h'},
        'Dennis & Bremer 1987': {'m': 's'},
        'Dennis & Bremer 1974': {'m': '*'},
        'Arike et al. 2012': {'m': 'X'},
        'Balakrishnan et al. 2022': {'m': 'X'},
        'Kubitschek et al. 1983': {'m': 'h'},
        'Mir et al. 2011': {'m': 'p'},
        'Watson et al. 1976': {'m': '^'},
        'Woldringh et al. 1981': {'m': 'v'},
        'Poole 1977': {'m': '>'},
        'Zhu & Dai 2019': {'m': '.'},
        'Yao et al. 2012': {'m': '<'},
        'Zheng et al. 2020': {'m': 'h'},
        'Martinez-Salas et al. 1981': {'m': '8'}
    }
    # Set colors rooted in blue
    cmap = sns.color_palette(
        f"light:{colors['primary_black']}", n_colors=len(mapper)).as_hex()
    rng.shuffle(cmap)
    counter = 0
    for k, _ in mapper.items():
        mapper[k]['c'] = cmap[counter]
        counter += 1
    return mapper


def get_colors(all_palettes=False):
    """
    Generates a dictionary of standard colors and returns a sequential color
    palette.

    Parameters
    ----------
    all_palettes : bool
        If True, lists of `dark`, `primary`, and `light` palettes will be returned. If
        False, only the `primary` palette will be returned.
    """
    # Define the colors
    colors = {
        'dark_black': '#2b2b2a',
        'black': '#3d3d3d',
        'primary_black': '#4c4b4c',
        'light_black': '#8c8c8c',
        'pale_black': '#afafaf',
        'dark_blue': '#154577',
        'blue': '#005da2',
        'primary_blue': '#3373ba',
        'light_blue': '#5fa6db',
        'pale_blue': '#8ec1e8',
        'dark_green': '#356835',
        'green': '#488d48',
        'primary_green': '#5cb75b',
        'light_green': '#99d097',
        'pale_green': '#b8ddb6',
        'dark_red': '#79302e',
        'red': '#a3433f',
        'primary_red': '#d8534f',
        'light_red': '#e89290',
        'pale_red': '#eeb3b0',
        'dark_gold': '#84622c',
        'gold': '#b1843e',
        'primary_gold': '#f0ad4d',
        'light_gold': '#f7cd8e',
        'pale_gold': '#f8dab0',
        'dark_purple': '#43355d',
        'purple': '#5d4a7e',
        'primary_purple': '#8066ad',
        'light_purple': '#a897c5',
        'pale_purple': '#c2b6d6'
    }

    # Generate the sequential color palettes.
    keys = ['black', 'blue', 'green', 'red', 'purple', 'gold']
    dark_palette = [colors[f'dark_{k}'] for k in keys]
    primary_palette = [colors[f'primary_{k}'] for k in keys]
    light_palette = [colors[f'light_{k}'] for k in keys]

    # Determine what to return.
    if all_palettes:
        palette = [dark_palette, primary_palette, light_palette]
    else:
        palette = primary_palette

    return [colors, palette]


def matplotlib_style(return_colors=True, return_palette=True, **kwargs):
    """
    Assigns the plotting style for matplotlib generated figures.

    Parameters
    ----------
    return_colors : bool
        If True, a dictionary of the colors is returned. Default is True.
    return_palette: bool
        If True, a sequential color palette is returned. Default is True.
    """
    # Define the matplotlib styles.
    rc = {
        # Axes formatting
        "axes.facecolor": "#f0f3f7",
        "axes.edgecolor": "#ffffff",  # 5b5b5b",
        "axes.labelcolor": "#5b5b5b",
        "axes.spines.right": False,
        "axes.spines.top": False,
        "axes.spines.left": True,
        "axes.spines.bottom": True,
        "axes.axisbelow": True,
        "axes.linewidth": 0.15,
        "axes.grid": True,

        # Formatting of lines and points.
        "lines.linewidth": 0.5,
        "lines.dash_capstyle": "butt",
        "patch.linewidth": 0.25,
        "lines.markeredgecolor": '#f0f3f7',
        "lines.markeredgewidth": 0.5,

        # Grid formatting
        "grid.linestyle": '-',
        "grid.linewidth": 0.5,
        "grid.color": "#FFFFFF",

        # Title formatting
        "axes.titlesize": 8,
        "axes.titleweight": 700,
        "axes.titlepad": 3,
        "axes.titlelocation": "left",

        # Axes label formatting.
        "axes.labelpad": 0,
        "axes.labelweight": 700,
        "xaxis.labellocation": "center",
        "yaxis.labellocation": "center",
        "axes.labelsize": 8,
        "axes.xmargin": 0.03,
        "axes.ymargin": 0.03,

        # Legend formatting
        "legend.fontsize": 6,
        "legend.labelspacing": 0.25,
        "legend.title_fontsize": 6,
        "legend.frameon": True,
        "legend.edgecolor": "#5b5b5b",

        # Tick formatting
        "xtick.color": "#5b5b5b",
        "ytick.color": "#5b5b5b",
        "xtick.labelsize": 6,
        "ytick.labelsize": 6,
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "xtick.major.width": 0.25,
        "ytick.major.width": 0.25,
        "xtick.major.pad": 2,
        "ytick.major.pad": 2,
        "xtick.minor.size": 0,
        "ytick.minor.size": 0,

        # General Font styling
        "font.family": "sans-serif",
        "font.family": "Lato",
        "font.weight": 400,  # Weight of all fonts unless overriden.
        "font.style": "normal",
        "text.color": "#3d3d3d",  # "#5b5b5b",

        # Higher-order things
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "figure.facecolor": "white",
        "figure.dpi": 300,
        "errorbar.capsize": 1,
        "savefig.bbox": "tight",
        "mathtext.default": "regular",
    }
    matplotlib.style.use(rc)

    # Load the colors and palettes.
    colors, palette = get_colors(**kwargs)
    sns.set_palette(palette)

    # Determine what, if anything should be returned
    out = []
    if return_colors == True:
        out.append(colors)
    if return_palette == True:
        out.append(palette)

    if len(out) == 1:
        return out[0]
    else:
        return out
