"""
code from: https://community.plotly.com/t/show-tell-plotly-graph-background-color-in-html-file-with-css-style/43223

allows for writing of plotly figures without white bars around edges
"""

from pathlib import Path
from plotly import offline
from plotly import graph_objects as go

DEFAULT_CONFIG = dict({"scrollZoom": False, "displayModeBar": True, "editable": False})


def save_html(
    fig,
    path: str | Path,
    background_color: str = "black",
    font_color: str = "white",
    config: dict[str, bool] = DEFAULT_CONFIG,
) -> None:
    fig.update_layout(
        hovermode="closest",
        plot_bgcolor=background_color,
        paper_bgcolor=background_color,
        font=dict(color=font_color),
    )
    plot_div = offline.plot(fig, config=config, output_type="div")
    html_fig = f"\n<head>\n<body style='background-color:{background_color};'>\n</head>\n<body>{plot_div}\n</body>"
    with open(path, "w") as file:
        file.write(html_fig)
    file.close()
