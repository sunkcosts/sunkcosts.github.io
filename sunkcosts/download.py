from dataclasses import dataclass

datasets = [{"source_entity": ""}]
links = {
    "lsa_jason_constellation": {
        "global_seasonal_signals_removed": "https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/slr/slr_sla_gbl_free_txj1j2_90.csv",
        "regional_atlantic_seasonal_signals_removed": "https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/slr/slr_sla_atl_free_txj1j2_90.csv",
    },
    "ipcc_ar6_global_slp_confidence": {
        "low": {
            "ssp126": "https://github.com/sunkcosts/ar6_slp_global_confidence_data/raw/main/data/low.ssp126.nc",
            "ssp245": "https://github.com/sunkcosts/ar6_slp_global_confidence_data/raw/main/data/low.ssp245.nc",
            "ssp585": "https://github.com/sunkcosts/ar6_slp_global_confidence_data/raw/main/data/low.ssp585.nc",
        },
        "med": {
            "ssp126": "https://github.com/sunkcosts/ar6_slp_global_confidence_data/raw/main/data/med.ssp126.nc",
            "ssp245": "https://github.com/sunkcosts/ar6_slp_global_confidence_data/raw/main/data/med.ssp245.nc",
            "ssp585": "https://github.com/sunkcosts/ar6_slp_global_confidence_data/raw/main/data/med.ssp585.nc",
        },
    },
}


@dataclass
class Dataset:
    name: str
    description: str
    local_path_raw: str
    local_path_clean: str
    web_url: str

    @property
    def original(self):
        pass

    @property
    def clean(self):
        pass

    def download(self):
        pass
