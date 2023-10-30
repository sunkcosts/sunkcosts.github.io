from pathlib import Path
import plotly.express as px
from plotly import offline
from plotly import graph_objects as go


DEFAULT_CONFIG = dict(
    {"scrollZoom": False, "displayModeBar": False, "editable": False, "showTips": False}
)


MINIMAL = dict(
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


def create_bounds_map(mapbox_token: str, boundbox, zoom):
    # Define coordinates for the bounding box
    box_coords = [
        boundbox["top_left"],
        {"lat": boundbox["top_left"]["lat"], "lon": boundbox["bottom_right"]["lon"]},
        boundbox["bottom_right"],
        {"lat": boundbox["bottom_right"]["lat"], "lon": boundbox["top_left"]["lon"]},
        boundbox["top_left"],
    ]

    # Create the bounding box scattermapbox object
    trace_box = go.Scattermapbox(
        mode="lines",
        lon=[point["lon"] for point in box_coords],
        lat=[point["lat"] for point in box_coords],
        fill="toself",
        fillcolor="rgba(255, 255, 255, 0.1)",
        hoverinfo="none",
        line=dict(width=2),
    )

    # Setup the layout
    layout = go.Layout(
        autosize=True,
        margin=go.layout.Margin(l=0, r=0, b=0, t=0, pad=0),
        mapbox=dict(
            accesstoken=mapbox_token,
            bearing=0,
            center=dict(
                lat=(boundbox["top_left"]["lat"] + boundbox["bottom_right"]["lat"])
                / 2,  # Center latitude
                lon=(boundbox["top_left"]["lon"] + boundbox["bottom_right"]["lon"])
                / 2,  # Center longitude
            ),
            pitch=0,
            zoom=zoom,
            style="dark",
        ),
    )

    # Create the figure
    fig = go.Figure(data=[trace_box], layout=layout)
    return fig


def save_html(
    fig,
    path: str | Path,
    background_color: str = "black",
    font_color: str = "white",
    config: dict[str, bool] = DEFAULT_CONFIG,
    div_style: str = "",
) -> None:
    """
    code from: https://community.plotly.com/t/show-tell-plotly-graph-background-color-in-html-file-with-css-style/43223

    allows for writing of plotly figures without white bars around edges
    """
    fig.update_layout(
        hovermode="closest",
        plot_bgcolor=background_color,
        paper_bgcolor=background_color,
        font=dict(color=font_color),
    )
    plot_div = offline.plot(
        fig,
        config=config,
        output_type="div",
    )
    plot_div = plot_div.replace("<div>", f"<div style='{div_style}'>", 1)

    html_fig = f"\n<head>\n<body style='background-color:{background_color};'>\n</head>\n<body>{plot_div}\n</body>"
    with open(path, "w") as file:
        file.write(html_fig)
    file.close()


def showfig(fig):
    fig.update_layout(title_x=0.5, margin=dict(l=5, r=5, t=60, b=20))
    fig.show(renderer="notebook", config={"displayModeBar": False, "showTips": False})


def plot_lsa_slr_data(data, xcol, ycol):
    data.columns = [xcol, ycol]
    fig = px.scatter(data, x=xcol, y=ycol, title=f"{ycol} vs. {xcol}", template=MINIMAL)
    fig.update_traces(
        marker=dict(size=1, line=dict(width=2, color="#3d98ff")),
        selector=dict(mode="markers"),
    )
    fig.update_xaxes(range=[1993, 2023])
    showfig(fig)


def plot_lsa_lsr_plus_pnas(lsa, pnas, xcol, ycol):
    lsa.columns = [xcol, ycol]
    pnas.columns = [xcol, ycol]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=pnas[xcol],
            y=pnas[ycol],
            name="Historical: Kopp et al. Model",
            marker=dict(color="#3d98ff"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=lsa[xcol],
            y=lsa[ycol],
            mode="markers",
            name="Recent: LSA Constellation Data",
            marker=dict(color="#CF6E34", size=3),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[1760],
            y=[-110.67],
            mode="markers",
            name="Industrial Revolution Begins (Click Here)",
            marker=dict(color="red", size=14),
        )
    )

    fig.update_layout(
        template=MINIMAL,
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
        xaxis_title=xcol,
        yaxis_title=ycol,
    )
    fig.update_layout(
        title=f"{ycol} vs. {xcol}",
        title_x=0.5,
        margin=dict(l=5, r=5, t=60, b=20),
        legend_bgcolor="rgba(0,0,0,0)",
    )
    fig.update_xaxes(range=[-1010, 2030])
    fig.update_traces(
        visible="legendonly",
        selector=lambda l: l.name == "Industrial Revolution Begins (Click Here)",
    )
    showfig(fig)
