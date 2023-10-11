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


# plotly dark
import plotly.graph_objects as go


minimal = dict(
    layout=go.Layout(
        {
            "annotationdefaults": {
                "arrowcolor": "#f2f5fa",
                "arrowhead": 0,
                "arrowwidth": 1,
            },
            "autotypenumbers": "strict",
            "coloraxis": {
                "colorbar": {
                    "outlinewidth": 0,
                    "ticks": "",
                    "tickcolor": "rgba(0,0,0,0)",
                }
            },
            "colorscale": {
                "diverging": [
                    [0, "#8e0152"],
                    [0.1, "#c51b7d"],
                    [0.2, "#de77ae"],
                    [0.3, "#f1b6da"],
                    [0.4, "#fde0ef"],
                    [0.5, "#f7f7f7"],
                    [0.6, "#e6f5d0"],
                    [0.7, "#b8e186"],
                    [0.8, "#7fbc41"],
                    [0.9, "#4d9221"],
                    [1, "#276419"],
                ],
                "sequential": [
                    [0.0, "#0d0887"],
                    [0.1111111111111111, "#46039f"],
                    [0.2222222222222222, "#7201a8"],
                    [0.3333333333333333, "#9c179e"],
                    [0.4444444444444444, "#bd3786"],
                    [0.5555555555555556, "#d8576b"],
                    [0.6666666666666666, "#ed7953"],
                    [0.7777777777777778, "#fb9f3a"],
                    [0.8888888888888888, "#fdca26"],
                    [1.0, "#f0f921"],
                ],
                "sequentialminus": [
                    [0.0, "#0d0887"],
                    [0.1111111111111111, "#46039f"],
                    [0.2222222222222222, "#7201a8"],
                    [0.3333333333333333, "#9c179e"],
                    [0.4444444444444444, "#bd3786"],
                    [0.5555555555555556, "#d8576b"],
                    [0.6666666666666666, "#ed7953"],
                    [0.7777777777777778, "#fb9f3a"],
                    [0.8888888888888888, "#fdca26"],
                    [1.0, "#f0f921"],
                ],
            },
            "colorway": [
                "#636efa",
                "#EF553B",
                "#00cc96",
                "#ab63fa",
                "#FFA15A",
                "#19d3f3",
                "#FF6692",
                "#B6E880",
                "#FF97FF",
                "#FECB52",
            ],
            "font": {"color": "#f2f5fa"},
            "geo": {
                "bgcolor": "rgb(17,17,17)",
                "lakecolor": "rgb(17,17,17)",
                "landcolor": "rgb(17,17,17)",
                "showlakes": True,
                "showland": True,
                "subunitcolor": "rgba(0,0,0,1)",
            },
            "hoverlabel": {"align": "left"},
            "hovermode": "closest",
            "mapbox": {"style": "dark"},
            "paper_bgcolor": "rgba(0,0,0,0)",
            "plot_bgcolor": "rgba(0,0,0,0)",
            "polar": {
                "angularaxis": {
                    "gridcolor": "rgba(0,0,0,0)",
                    "linecolor": "rgba(0,0,0,1)",
                    "ticks": "",
                },
                "bgcolor": "rgb(17,17,17)",
                "radialaxis": {
                    "gridcolor": "rgba(0,0,0,0)",
                    "linecolor": "rgba(0,0,0,1)",
                    "ticks": "",
                },
            },
            "scene": {
                "xaxis": {
                    "showspikes": False,
                    "zeroline": False,
                    "showline": False,
                    "showticklabels": True,
                    "backgroundcolor": "rgba(0,0,0,0)",
                    "gridcolor": "rgba(0,0,0,0)",
                    "gridwidth": 2,
                    "linecolor": "rgba(0,0,0,1)",
                    "showbackground": False,
                    "ticks": "",
                    "zerolinecolor": "rgba(0,0,0,1)",
                    "title": "",
                },
                "yaxis": {
                    "showspikes": False,
                    "zeroline": False,
                    "showline": False,
                    "showticklabels": True,
                    "backgroundcolor": "rgba(0,0,0,0)",
                    "gridcolor": "rgba(0,0,0,0)",
                    "gridwidth": 2,
                    "linecolor": "rgba(0,0,0,1)",
                    "showbackground": False,
                    "ticks": "",
                    "zerolinecolor": "rgba(0,0,0,1)",
                    "title": "",
                },
                "zaxis": {
                    "showspikes": False,
                    "zeroline": False,
                    "showline": False,
                    "showticklabels": True,
                    "backgroundcolor": "rgba(0,0,0,0)",
                    "gridcolor": "rgba(0,0,0,0)",
                    "gridwidth": 2,
                    "linecolor": "rgba(0,0,0,1)",
                    "showbackground": False,
                    "ticks": "",
                    "zerolinecolor": "rgba(0,0,0,1)",
                    "title": "",
                },
            },
            "shapedefaults": {"line": {"color": "#f2f5fa"}},
            "sliderdefaults": {
                "bgcolor": "#C8D4E3",
                "bordercolor": "rgb(17,17,17)",
                "borderwidth": 1,
                "tickwidth": 0,
            },
            "ternary": {
                "aaxis": {
                    "gridcolor": "rgba(0,0,0,0)",
                    "linecolor": "rgba(0,0,0,1)",
                    "ticks": "",
                },
                "baxis": {
                    "gridcolor": "rgba(0,0,0,0)",
                    "linecolor": "rgba(0,0,0,1)",
                    "ticks": "",
                },
                "bgcolor": "rgb(17,17,17)",
                "caxis": {
                    "gridcolor": "rgba(0,0,0,0)",
                    "linecolor": "rgba(0,0,0,1)",
                    "ticks": "",
                },
            },
            "title": {"x": 0.05},
            "updatemenudefaults": {"bgcolor": "#506784", "borderwidth": 0},
            "xaxis": {
                "showspikes": False,
                "zeroline": False,
                "showline": False,
                "showticklabels": True,
                "automargin": True,
                "gridcolor": "rgba(0,0,0,0)",
                "linecolor": "rgba(0,0,0,1)",
                "ticks": "",
                "title": {"standoff": 15},
                "zerolinecolor": "rgba(0,0,0,1)",
                "zerolinewidth": 2,
            },
            "yaxis": {
                "showspikes": False,
                "zeroline": False,
                "showline": False,
                "showticklabels": True,
                "automargin": True,
                "gridcolor": "rgba(0,0,0,0)",
                "linecolor": "rgba(0,0,0,1)",
                "ticks": "",
                "title": {"standoff": 15},
                "zerolinecolor": "rgba(0,0,0,1)",
                "zerolinewidth": 2,
            },
        }
    )
)
