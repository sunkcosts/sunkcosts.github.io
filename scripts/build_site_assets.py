from sunkcosts.tokens import auth
from sunkcosts.plotly import create_bounds_map, save_html


from sunkcosts.env import AA_BOUNDS, PATH_SITE

# mapbox public used as api key can be found in plotly html
# this key is restricted to working on sunkcosts site
boundmap_fig = create_bounds_map(
    mapbox_token=auth.get("mapbox_public"),
    boundbox=AA_BOUNDS,
    zoom=10,
)

save_html(
    boundmap_fig,
    PATH_SITE / "file/main/plotly.map.aoa_bounds_mapbox.html",
    config=dict(),
    div_style="border-radius: 0.4em; overflow: hidden;",
)
