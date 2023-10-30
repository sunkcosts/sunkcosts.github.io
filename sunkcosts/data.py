import pandas as pd
import numpy as np
from netCDF4._netCDF4 import Dataset


def load_clean_lsa_slr_dataset(path):
    lsa = pd.read_csv(path, skiprows=5)
    lsa = lsa.set_index("year")
    lsa = lsa.mean(axis=1)
    lsa = lsa.reset_index()
    lsa.columns = ["year", "gmsl_mm"]
    return lsa


def load_clean_gsl_historical_dataset(path):
    pnas = pd.read_excel(
        "../data/pnas.1517056113.sd03.xls", sheet_name="GSL ML21", skiprows=2
    )
    pnas.drop(["1s"], axis=1, inplace=True)
    pnas.columns = ["year", "gmsl_mm"]
    return pnas


def load_ssp_file(basepath: str, confidence: str, scenario: str):
    assert confidence in {"low", "medium"}
    assert scenario in {"ssp126", "ssp245", "ssp585"}
    # lazy path, make sure matches if you replicate
    # ../data/ar6/global/confidence_output_files
    HARDCODED_SSP_DATAPATH = f"{basepath}/{confidence}_confidence/{scenario}/total_{scenario}_{confidence}_confidence_values.nc"
    # 'dataset is not known member' warning: it is
    data = Dataset(HARDCODED_SSP_DATAPATH)
    years = np.array(data["years"][:])
    slc = np.array(data["sea_level_change"][:])
    return years, slc, data


def load_ssp_scenarios(basepath: str):
    conf = ["low", "medium"]
    scen = ["ssp126", "ssp245", "ssp585"]
    years, ssp126, data126 = load_ssp_file(basepath, "medium", "ssp126")
    years, ssp245, data245 = load_ssp_file(basepath, "medium", "ssp245")
    years, ssp585, data585 = load_ssp_file(basepath, "medium", "ssp585")
    datasets = [ssp126, ssp245, ssp585]

    yearly_dists = list()

    for year in range(len(years)):
        yeardist = list()
        for ds in datasets:
            yeardist = yeardist + ds[:, year].flatten().tolist()
        yearly_dists.append(yeardist)
    year_full = list()
    dist_full = list()
    for i, v in enumerate(years):
        year_full = year_full + [v] * len(yearly_dists[i])
        dist_full = dist_full + yearly_dists[i]

    return (years,)
