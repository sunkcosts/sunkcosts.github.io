<!--
# Analysis

!!! abstract "Report Abstract"
    TODO: Report abstract

!!! warning "Continuous Development"
    This analytical report and model are subject to change. If you find an issue with the methodology or have a suggestion for an improvement, please submit it in the [GitHub repository]() - either in the [issues]() or [discussions]() sections depending the type of feedback you are submitting.

!!! bug "Deployed Model Issues"
    If the model deployed on the [streamlit share](https://docs.streamlit.io/streamlit-community-cloud/share-your-app) instance is overloaded, you can also run it in a local python environment. See the [[model_quickstart|model quickstart]] page for more info.

??? note "Sunshade Project Context"
    The focus of this report is the economic forecast, however the analysis was performed to contrast the cost of losing Miami to sea level rise with the cost of deploying a space based sunshade for geoengineering purposes. The project proposal was presented in 2022 at the New Worlds space conference in Austin. A modified [slide deck](../file/internal/document.slides.earthshade.pdf) for the proposal is included on this site.

??? tip "Site Navigation Tips"
    You can press the `/` key to jump to quick search. Navigate between pages with the `<` and `>` keys.

??? info "BibTeX Citation"
    ```bibtex
    @misc{SCTM2023,
        title = {Sunk Costs},
        subtitle = {Forecasting the Economic Impact of Sea Level Rise on Miami},
        author = {Hart Traveller and Luke Moloney},
        year = {2023},
        howpublished = {Available at https://sunkcosts.github.io}
        note = {Contact: guider.adopt0l@icloud.com}
    }
    ```

 -->

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

First, let's start by looking at the global SLR trend over the last few decades. We'll use data collected by the [NOAA LSA](https://www.star.nesdis.noaa.gov/socd/lsa/index.php) (Laboratory for Satellite Altimetry) [Jason](https://www.wikiwand.com/en/Jason_satellite_series) satellites.

<!-- ### NOAA Global SLR Trend: year - year -->

We'll start by using the [global mean sea level](https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/LSA_SLR_timeseries_global.php) dataset, specifically: TOPEX and Jason 1, 2, 3 with seasonal signals removed.

??? question "What is the difference between seasonal signals retained and seasonal signals removed?"
    - The difference between datasets with "seasonal signals retained" and "seasonal signals removed" pertains to the treatment of seasonal variations in the data. In the context of sea level data, seasonal signals could include variations caused by thermal expansion, melting glaciers, and other factors that follow a seasonal pattern.
    - Seasonal Signals Retained: This dataset includes the seasonal variations. It reflects the actual measurements taken over time, inclusive of all the fluctuations that occur on a seasonal basis. It can be useful for understanding how different factors contribute to sea level changes over the course of a year.
    - Seasonal Signals Removed: This dataset has been adjusted to remove the seasonal variations, providing a smoother trend over time. By removing the seasonal signals, it's easier to observe long-term trends and compare data across different time periods without the noise of seasonal fluctuations.



<iframe frameBorder="0" border="0" width="100%" background="black" height="500px" src="../../plot/noaa_lsa_global_slr_seasons_normalized.html"></iframe>





<!-- ## Sea Level Rise Trends

    SLR data is provided by the [NOAA LSA](https://www.star.nesdis.noaa.gov/socd/lsa/index.php) (Laboratory for Satellite Altimetry). Specifically, the data was gathered by the following systems:

    - [TOPEX/Poseidon](https://www.wikiwand.com/en/TOPEX/Poseidon)
    - [Jason-1](https://www.wikiwand.com/en/Jason-1)
    - [OSTM/Jason-2](https://www.wikiwand.com/en/OSTM/Jason-2)
    - [Jason-3](https://www.wikiwand.com/en/Jason-3)



### Recent History




### Ancient History




## Regional SLR Trends


 -->






<!--
We'll begin by taking an agnostic position on sea level rise (SLR), avoiding for now questions as to whether it is good or bad.

Instead, we will focus simply on answering whether it is happening, and if it is, to what extent (and in the context of the model forecast: to what extent we can be certain).

*rephrase


*have to note
- global SLR trends to not reflect miami specific SLR trends, there needs to be a modifier parameter specific to the miami model which can be tuned to account for this

*later
- we can use existing dataset to gen model, stratify different levels by year/probability


# Resources

This page indexes the various artifacts produced throughout this project, made available for download and common use.
 -->


 <!--
# Introduction

The structure of this analysis will be one in which we build out a model to forecast the economic impact of climate change on the city of Miami. At each step of the process, we provide a high level view of how the model component in what is hopefully an engaging format, providing information about the data used, premises assumed, parameters accounted for, and limiting caveats. Lower level technical detail and code can be found in the [jupyter notebooks] found in the [documentation], which also includes instructions for [setting up] an environment to reproduce this analysis.



<!-- According to ChatGPT, the following statement is a good opener for this report:

> Miami is situated in Miami-Dade County, on the southeastern coast of Florida. As the effects of climate change continue to manifest, there is growing concern about the potential impact on the city. One of the most pressing issues is the rise in sea level, which threatens to inundate Miami's low-lying areas and cause extensive damage to its infrastructure and property. In addition, the city is likely to experience more frequent and severe extreme weather events, such as hurricanes and flooding, which could further exacerbate the risks posed by rising sea levels.

Let's pause for a moment, as a number of claims were just made or implied which you might be expected to take at face value as the reader.

## Claims

The primary claims are as follows:

1. The sea level is rising.
2. The frequency and intensity of extreme weather events is increasing.
3. These changes may harm life, infrastructure, and property, in the city of Miami.

While they may seem reasonable to many, it is worth verifying whether or not they are actually true. Plus, verifying the accuracy of the assertions is a good entry point into the analytical process used to create this report, and allows us to build out the foundations of the model.

Notably a secondary claim we will also evaluate relates to the "growing concern about the potential impact on the city". Is concern actually growing? We will utilize various computational social science research tools in an attempt to find the answer.

## Objectives

Accordingly, our objectives are as follows:

- Assess whether sea level is rising.
    - *todo note: and also specific to miami, differs cause geo*
- section finish: gen model that given inputs of:
    - parameters to SLR curve from fit to prob distributions from IPCC dataset



- is sea level rise bad? why?
    - given premise that human death, displacement, and suffering is bad -> presumably yes
        - reasonable premises to start with
    - ^ this assumes that SLR would result in these events, would it?
        - presumably, but show quantitatively, allow for model variability
- if SLR results in bad outcomes, how much SLR expected, and how bad are the outcomes expected from given levels of SLR


1. Assess the claims stated above, by:
2. Stratifying them across future scenarios of varying severity, specifically:

3. Build an adjustable model capable of forecasting the economic impact (or lack thereof) of climate change on the city of Miami. The user should be able to adjust the parameters given to the model so as to facilitate exploration of a wide range of possible scenarios.


##


---

## Structure/Format

- SLR
    - global
    - miami specific

- start with sea level rise
    - is it happening?
    - pull, analyze data.
        - * conclusion -> already shown, occurring at accelerated rate, fetch data and statistically validate
    - use available dataset to generate model, forecast given params
        - factor in geographic bias associated with south eastern US coast

- create a model component to forecast sea level rise
    - global sea level rise
    - local factors relevant to miami
- assess: is the sea level rising?
- assess: what are reasonable default parameters for this model component?
- visualize: what do the various parameters for sea level rise look like


## References

# References

## Data Sources

### NOAA LSA




## Papers
  -->