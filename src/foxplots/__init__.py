from pathlib import Path

import seaborn as sns
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter


def load_fonts():
    """Load custom fonts from ~/.fonts."""
    font_dirs = [Path("~/.fonts").expanduser()]
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

    for font_file in font_files:
        font_manager.fontManager.addfont(font_file)


def set_style():
    """Set Seaborn rc params."""
    sns.set(
        style="whitegrid",
        rc={
            "axes.spines.right": False,
            "axes.spines.top": False,
            "font.family": "Lato",
            "axes.titlesize": "x-large",
            "axes.titlepad": 24,
            "axes.titlelocation": "left",
            "axes.labelcolor": "#5b5b5b",
            "xtick.color": "#5b5b5b",
            "ytick.color": "#5b5b5b",
        },
    )


def apply():
    """Apply custom styles and fonts."""
    load_fonts()
    set_style()


def _y_fmt(tick_value, pos):
    """Format a tick."""
    if tick_value > 1e6:
        return f"{tick_value/1e6:.2f}M"

    if tick_value > 0:
        return f"{tick_value/1000:.0f}k"

    return f"{tick_value:,.0f}"


def humanize_y_ticks(ax):
    """Use -k or -M suffix for large numbers on Y axis."""
    if ax.get_ylim()[1] > 10_000:
        ax.yaxis.set_major_formatter(FuncFormatter(_y_fmt))


def pretty_title(ax):
    """Set the right font on left title."""
    ax._left_title.set_family("Playfair Display")


def subtitle(ax, text: str, **kwargs):
    """Add text under the main title."""
    ax.figure.text(
        0.125,
        0.915,
        text,
        size="x-small",
        horizontalalignment="left",
        color="#424242",
        fontweight=300,
        **kwargs,
    )


def footnote(ax, text: str, **kwargs):
    """Add text under the figure."""
    ax.figure.text(
        0.125,
        -0.025,
        text,
        size="x-small",
        horizontalalignment="left",
        color="#424242",
        fontweight=300,
        **kwargs,
    )
