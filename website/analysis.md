# Analysis







<!-- This page is structured as follows:

1. An analysis of global sea level trends.
    - SLR trends in historical context.
2. Exploration into regional differences from global trends.
3. The addition of a regional modifier to our model.
4. The integration of probability distributions into our model.
5. The integration of the aforementioned regional modifier to the probabilistic model.

X. Collection of satellite data
X. Visualization of SIP

- First start with global SLR
    - data source: https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/LSA_SLR_timeseries_global.php
        - from sat:  TOPEX/Poseidon, Jason-1, Jason-2, and Jason-3
- Then look at regional SLR, introduce reasonable modification parameter, ref regional paper
- Then pull probability dataset, build probabilistic model
- Then add modifier parameter for regional variation to probabilistic model
-->

First, let's start by looking at the global SLR trend over the last few decades. We'll use data collected by the [NOAA LSA](https://www.star.nesdis.noaa.gov/socd/lsa/index.php) (Laboratory for Satellite Altimetry) .

<!-- ### NOAA Global SLR Trend: year - year -->

We'll start by using data from the [Jason](https://www.wikiwand.com/en/Jason_satellite_series) satellite series.[^1]

[^1]: [Global sea level time series](https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/LSA_SLR_timeseries_global.php)


!!! question "What is the difference between seasonal signals retained and seasonal signals removed?"
    - The difference between datasets with "seasonal signals retained" and "seasonal signals removed" pertains to the treatment of seasonal variations in the data. In the context of sea level data, seasonal signals could include variations caused by thermal expansion, melting glaciers, and other factors that follow a seasonal pattern.
    - Seasonal Signals Retained: This dataset includes the seasonal variations. It reflects the actual measurements taken over time, inclusive of all the fluctuations that occur on a seasonal basis. It can be useful for understanding how different factors contribute to sea level changes over the course of a year.
    - Seasonal Signals Removed: This dataset has been adjusted to remove the seasonal variations, providing a smoother trend over time. By removing the seasonal signals, it's easier to observe long-term trends and compare data across different time periods without the noise of seasonal fluctuations.



<iframe frameBorder="0" border="0" width="100%" background="black" height="500px" src="../../plot/noaa_lsa_global_slr_seasons_normalized.html"></iframe>




