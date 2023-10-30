from pathlib import Path
from sunkcosts.tokens import auth
from sunkcosts.data import load_clean_lsa_gmsl_dataset, load_clean_gsl_historical_dataset
from sunkcosts.plotly import (
    create_bounds_map,
    save_html,
    create_lsa_gmsl_scatterplot,
    create_lsa_kopp_scatterplot,
)
from sunkcosts.env import AA_BOUNDS, PATH_SITE, PATH_WORKDIR

# mapbox public used as api key can be found in plotly html
# this key is restricted to working on sunkcosts site
DEV = False
mapbox_token = auth.get("mapbox_dev") if DEV else auth.get("mapbox_public")

# ! boundmap fig

boundmap_fig = create_bounds_map(
    mapbox_token=mapbox_token,
    boundbox=AA_BOUNDS,
    zoom=10,
)
save_html(
    boundmap_fig,
    PATH_SITE / "file/main/plotly.map.aoa_bounds_mapbox.html",
    config=dict(),
    div_style="border-radius: 0.4em; overflow: hidden;",
)

# ! lsa scatter


lsa = load_clean_lsa_gmsl_dataset(
    "https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/slr/slr_sla_gbl_free_txj1j2_90.csv"
)
lsa_scatter = create_lsa_gmsl_scatterplot(lsa, "Year", "Sea Level (mm)")
save_html(
    lsa_scatter,
    PATH_SITE / "file/main/plotly.graph.lsa_gmsl_scatterplot.html",
)

# ! lsa and kopp historical

pnas = load_clean_gsl_historical_dataset(PATH_WORKDIR / "data/pnas.1517056113.sd03.xls")
lsa_kopp_scatter = create_lsa_kopp_scatterplot(
    lsa, pnas, "Year (BCE/CE)", "Sea Level (mm)"
)
save_html(
    lsa_kopp_scatter,
    PATH_SITE / "file/main/plotly.graph.lsa_kopp_scatterplot.html",
)
