
<!-- ## Sea Level Rise Trends

    SLR data is provided by the [NOAA LSA](https://www.star.nesdis.noaa.gov/socd/lsa/index.php) (Laboratory for Satellite Altimetry). Specifically, the data was gathered by the following systems:

    - [TOPEX/Poseidon](https://www.wikiwand.com/en/TOPEX/Poseidon)
    - [Jason-1](https://www.wikiwand.com/en/Jason-1)
    - [OSTM/Jason-2](https://www.wikiwand.com/en/OSTM/Jason-2)
    - [Jason-3](https://www.wikiwand.com/en/Jason-3)

We start by analyzing sea level rise (SLR) trends.


<!-- 1. An analysis of global sea level trends.
    - SLR trends in historical context.
2. Exploration into regional differences from global trends.
3. The addition of a regional modifier to our model.
4. The integration of probability distributions into our model.
5. The integration of the aforementioned regional modifier to the probabilistic model. -->

### Recent History

<!-- This page is structured as follows:


X. Collection of satellite data
X. Visualization of SIP

- First start with global SLR
    - data source: https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/LSA_SLR_timeseries_global.php
        - from sat:  TOPEX/Poseidon, Jason-1, Jason-2, and Jason-3
- Then look at regional SLR, introduce reasonable modification parameter, ref regional paper
- Then pull probability dataset, build probabilistic model
- Then add modifier parameter for regional variation to probabilistic model
-->



<!-- ### NOAA Global SLR Trend: year - year -->




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




## Claims



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

## Global Historical SLR

We'll start by looking at global historical sea level rise (SLR) across the last 30 years.

## Figure 1: Global SLR vs. Time (30 Years)
<p align="center"><iframe frameBorder="0" width="1000px" height="500px" src="https://htmlpreview.github.io/?https://github.com/miamilost/miamilost.github.io/tree/main/docs/assets/historical_global_slr_30_years.html"></iframe></p>

*Fig 1. Data Source: [NOAA STAR Satellite Constellation](https://www.star.nesdis.noaa.gov/star/index.php) • [DOWNLOAD](https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/slr/slr_sla_gbl_free_txj1j2_90.csv)*

Initially one may be tempted to simply take this data and extrapolate it into the future with a simple linear model. This method would likely to be highly inaccurate however; it would not account for the innumerable variables which interact both which each other, and with themselves through complex feedback loops.

The illusory nature of this apparently linear trend becomes evident as we expand our time horizons.

## Figure 2: Global SLR vs. Time (3000 Years)

<p align="center"><iframe frameBorder="0" width="1000px" height="500px" src="https://htmlpreview.github.io/?https://github.com/miamilost/miamilost.github.io/tree/main/docs/assets/historical_global_slr_3000_years.html"></iframe></p>

*Fig 2. Data Source: [Temperature driven global SLR... Kopp et al.](https://www.pnas.org/doi/10.1073/pnas.1517056113) • [DOWNLOAD](https://www.pnas.org/doi/suppl/10.1073/pnas.1517056113/suppl_file/pnas.1517056113.sd03.xls)*

## Miami Adjusted SLR

It is important to note that we used global mean SLR data in this analysis, due to the higher availability of quality data. Critically, this data does not actually reflect the local rate of SLR in Miami and the Eastern coast of Florida, and indeed, local SLR may be up to three times greater than the global mean.

In the 2016 paper: "Increasing flooding hazard in coastal communities due to rising sea level: Case study of Miami Beach, Florida", *Wdowinski et al* found that SLR is actually significantly higher in the Miami area.

> The average pre-2006 rate is 3 ± 2 mm/yr, similar to the global long-term rate of SLR, whereas after 2006 the average rate of SLR in Southeast Florida rose to 9 ± 4 mm/yr. Our results suggest that engineering solutions to SLR should rely on regional SLR rate projections and not only on the commonly used global SLR projections. The accelerated rate of SLR in Southeast Florida and other locations along the US Atlantic coast are significantly higher than the global average rate of SLR.

*source: [Increasing flooding hazard in coastal communities due to SLR](https://www.sciencedirect.com/science/article/abs/pii/S0964569116300278)*


For this reason, this analysis ought to be treated as generally conservative; we expect that our probability estimates likely understate the speed at which major economic damage will materialize.

## Overview

This website is an interactive exploratory analysis that seeks to model the economic impact of sea level rise (SLR) on the city of Miami. The analysis invokes a mix of qualitative and quantitative methods and will be continually updated with improvements to methodology, data, communication, and site architecture.

## Motivation

The motivation of the study is to contrast this economic cost against the price of building a space based sunshade for geoengineering purposes. The latter analysis is not included in here, but will be presented at [New Worlds 2022 Conference](https://www.eventcreate.com/e/new-worlds) by the contributors listed on the authors page. (Most) code used is available in the [GitHub](https://github.com/urthshade/miamilost) repository. Remaining scripts and notebooks will be added and organized in the near future. If you find any issues, please submit them as a GitHub issue.


- post sip costs
- pre sip costs


1. United States Census Bureau. (2021). *Quickfacts: Miami city, Florida*. Retrieved October 19, 2022, from https://www.census.gov/quickfacts/fact/table/miamicityflorida,US/PST045221

## SIP Importance

- video of storm surge

## SIP Satellite Visualization

## SIP Temporal Estimation

Given the premise that sea levels continue to rise, the question is not if, but rather when the SIP will begin. Probabalistic estimates are crucial given the economic and humanitarian implications of the SIP.

We endevoured to perform an analysis to establish some rough quantitative estimates using data from the [IPCC Assessment Report 6](https://www.ipcc.ch/assessment-report/ar6/).

Using the , we can fit a skewed normal probability density function to the distribution of estimates across all scenarios for each temporal interval (in this case: decades out to 2150). We review what this means in greater detail below.

The IPCC produces projections for a number of different scenarios. Each scenario produces a distribution of possible SLR outcomes in 10 year intervals out to 2150. For the analysis here, we've amalgamated data from those with `medium` confidence.

Take for example, the distribution of potential global mean SLR values in the year 2100. If we plot this data on a histogram, we get Figure 5.

---

## Figure 5: Histogram of Projected Outcomes for GMSLR by 2100

<p align="center"><iframe frameBorder="0" width="1000px" height="400px" src="https://htmlpreview.github.io/?https://github.com/miamilost/miamilost.github.io/tree/main/docs/assets/global_mean_slr_2100_model_outcome_dist.html"></iframe></p>

*Fig 5. Data Source: [IPCC AR6 Sea Level Projections](https://zenodo.org/record/5914710) • [DOWNLOAD](https://zenodo.org/record/5914710/files/ar6.zip?download=1)*

---

We can take this distribution and fit a skewed normal probability density function (PDF) to it. You can think of this as a 'line of best fit' that follows the curve traced by the histogram.

## Figure 6:

<p align="center"><iframe frameBorder="0" width="1000px" height="500px" src="https://htmlpreview.github.io/?https://github.com/miamilost/miamilost.github.io/tree/main/docs/assets/skewnorm_dist_2100.html"></iframe></p>

---

The benefit of representing the distribution as a PDF is that we can easily integrate the area under any arbitrary interval, thus computing an estimate of the probability that the true value falls within that interval.

## Figure 7: PDF Interval Integration


---

## Figure 8:

*Remember that the graphs are interactive; you can drag to rotate the graph, scroll to zoom, and ctrl-click and drag to reframe the plot.*

<p align="center"><iframe frameBorder="0" width="1000px" height="500px" src="https://htmlpreview.github.io/?https://github.com/urthshade/miamilost/blob/main/docs/assets/all_dists_to_2100.html"></iframe></p>

---

We set the "SIP starting point" at an SLR of 900 millimeters - under the 1 meter at which we will see a disproportionate increase in coastal inundation, but possibly around the time that major areas of the city and surrounding areas would have to be evacuated (assuming preventative measures are not taken).

To estimate the probability that the SIP will *begin* by a given year, we integrate the area greater than 900mm under the curve, for the PDF for a given year. TLDR, we get the following chart, which illustrates the probability the SIP will begin in any given year. Please keep in mind the points made on the [Miami Adjusted SLR]miami-adj-slr.md page.

## Figure 9: SIP Temporal Probabilities By Year (10 Year Intervals)

## Supplementary Analyses


## Demographics


## Awareness


## Insurance

## Miami: Abrupt SLR Inflection Point (SIP)

Continuing our analysis, let's look at a subset of Florida containing Miami and several surrounding areas. The area of analysis (henceforth: AoA) can be found within the following coordinate bounds (latitude, longitude):

- top left: *[25.958782, -80.347522]*
- bottom right: *[25.698782, -80.087522]*


## Figure 3: Area of Analysis (AoA)

<p align="center">
<img src="miami_sample_area.png" width="500">
</p>

*Fig 3. Data Source: [Mapbox](https://www.mapbox.com/)*

To determine how SLR will effect Miami, we examined the elevation distribution across the AoA.

## Figure 4: Elevation Distribution of AoA

<p align="center"><iframe frameBorder="0" width="1000px" height="400px" src="https://htmlpreview.github.io/?https://github.com/miamilost/miamilost.github.io/tree/main/docs/assets/miami_elevation_dist.html"></iframe></p>

*Fig 4. Data Source: [Mapbox](https://www.mapbox.com/)*

This graph is useful, as it illustrates the rather abrupt increase in the amount of area at an elevation of just around 1 meter. This implies that (assuming there are no preventative measures), there could be an "SLR Inflection Point" (or SIP for short).

The use the term "SIP" encompasses the area out to ~3 meters - at which point the elevation distribution returns to pre-SIP levels. The beginning of the SIP is the focus of our next analysis however. This represents the short period of time where in which coastal inundation may go from being manageable to potentially catastrophic.


## Total cost estimate