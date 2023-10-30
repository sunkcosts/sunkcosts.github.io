# Sunk Costs

<p style="font-size: 2.2em; color: #b4b4b1; margin-top: -0.65em; margin-bottom: 0em;">Forecasting the Economic Impact of Sea Level Rise on Miami</p>

---


## Overview

The objective of this project is to create a simple model that can forecast the economic cost of sea level rise (SLR) on the City of Miami by the year 2100. This report provides an (ideally) engaging introduction to the model, along with secondary analyses not included in the primary model. (1)
{ .annotate }

1.  You can press `Cmd + K` or `Ctrl + K` to open the quick search bar if you want to find something specific across the site.

It is important to point out that this model attempts to forecast cost *in the absence of human intervention*. It seems reasonable to expect this will occur as costs begin to materialize. (1)
{ .annotate }

1.  If would like to experiment with the model yourself you can either visit the web interface, or alternatively follow the setup instructions provided [here]() to run it locally.


## Summary

We recognize that not everyone will have time to read the full report. Accordingly, a concise summary is provided below.


**Key Points**

- Deserunt ad ut commodo labore ullamco quis aliquip.

**Policy Recommendations**

- Fugiat consectetur consequat occaecat sint cupidatat aute deserunt fugiat aute minim esse.


**Cost Scenarios**

Forecasts of economic impact for best case (low cost), baseline (medium cost), and worst case (high cost) scenarios by the year 2100 are included below. (1)
{ .annotate }

1.  Note that these dollar figures are almost certainly incorrect, and also not actually the figures the model returns, but rather figures derived from the output of the model. Regardless, they are included on the basis that decisive predictions - though virtually always wrong (or if right, by chance) - do have a certain psychological appeal.


<div class="grid-container-3" style = "margin-top: -0.6em; margin-bottom: 0em;">
    <div class="grid-item">
        <div class="admonition dollar-green">
            <p class="admonition-title">~X</p>
        </div>
    </div>
    <div class="grid-item">
        <div class="admonition dollar-yellow">
            <p class="admonition-title">~X</p>
        </div>
    </div>
    <div>
        <div class="admonition dollar-red">
            <p class="admonition-title">~X</p>
        </div>
    </div>
</div>

---



## Introduction

Debatably, objectively quantifying cost is [impossible] on an epistemological level. Regardless, we will make an attempt. To do so, we must first establish the "factors" we will consider - Locke's [life, liberty, and property](https://www.crf-usa.org/foundations-of-our-constitution/natural-rights.html#:~:text=%22life%2C%20liberty%2C%20and%20property.%22) might be a good place to start. We'll address these factors in the order of increasing complexity of model representation.

Also before we begin, let's establish the geographic bounds of the region we will evaluate. (1) We'll refer to this as the "Analysis Area" or AA for short.
{ .annotate }

1.  Coordinates for the bounding box are included below.

    ```python
    coordinates = {
        "top_left": {
            "lat": 25.920,
            "lon": -80.350,
        },
        "bottom_right": {
            "lat": 25.655,
            "lon": -80.060,
        },
    }
    ```


<div style="text-align: left; position: relative; top: 4em; left: 1.5em; margin-top: -2em;">
<a class="glightbox" href="./file/main/image.satellite.miami_sample_area_small.png" data-type="image" data-width="100%" data-height="auto" data-desc-position="bottom">
<button class="satellite-button">Satellite Image</button>
</a>
</div>

<div class="frame">
<iframe frameBorder="0" style="width: 100%; max-height: 30em; height: 30em;" src="./file/main/plotly.map.aoa_bounds_mapbox.html"></iframe>
</div>

!!! note "All data visualizations on this site are interactive. Double click a plot to reset to the original zoom."
<!--
<div class="image">
    <img src="./file/report/image.satellite.miami_sample_area_small.png" style="width: 30em;">
    <figcaption>Fig. 1: Miami Geographic Analysis Area</figcaption>
</div>

 -->

## Property

We'll assume that the loss of property due to SLR has a negative economic impact. Before we go into the details of quantifying property value though, lets first focus on sea level rise.

### Historical Sea Level

To provide context, let's take a short detour into historical sea level trends on planet Earth. We'll start by looking at the global sea level trend over the last few decades using data from the [Jason](https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/LSA_SLR_timeseries_global.php) Satellite Missions. The data used for this visualization can be downloaded [here](https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/slr/slr_sla_gbl_free_txj1j2_90.csv) - we're using the set with seasonal signals removed. (1)
{ .annotate }


1.  This is the data with seasonal signals removed. The difference between datasets with "seasonal signals retained" and "seasonal signals removed" pertains to the treatment of seasonal variations in the data. In the context of sea level data, seasonal signals could include variations caused by thermal expansion, melting glaciers, and other factors that follow a seasonal pattern.

    - Seasonal Signals Retained: This dataset includes the seasonal variations. It reflects the actual measurements taken over time, inclusive of all the fluctuations that occur on a seasonal basis. It can be useful for understanding how different factors contribute to sea level changes over the course of a year.
    - Seasonal Signals Removed: This dataset has been adjusted to remove the seasonal variations, providing a smoother trend over time. By removing the seasonal signals, it's easier to observe long-term trends and compare data across different time periods without the noise of seasonal fluctuations.

<div class="frame">
<iframe frameBorder="0" style="width: 100%; height: 35em;" src="./file/main/plotly.graph.lsa_gmsl_scatterplot.html"></iframe>
</div>


It is of course technically possible that the sea level has been rising for some time. For the sake of curiousity let's zoom out and look at the last few millenia. We'll use data produced by Kopp et al. from [this research](https://doi.org/10.1073/pnas.1517056113) paper on historical global mean sea level. (1) The dataset can be downloaded [here](https://www.pnas.org/doi/suppl/10.1073/pnas.1517056113/suppl_file/pnas.1517056113.sd03.xls). (2)
{ .annotate }

1.  The `1s` column representing confidence is dropped in this visualization to simplify the output. From the paper:

    > Each database entry includes reconstructed RSL, RSL error, age, and age error. For regional reconstructions produced from multiple sites (e.g., ref. 5), we treated each site independently. Where we used publications that previously compiled RSL reconstructions (e.g., refs. 37 and 45), the results were used as presented in the compilation. RSL error was assumed to be a range unless the original publication explicitly stated otherwise or if the reconstruction was generated using a transfer function and a Random Mean SE Standard Error of Prediction was reported, in which case this was treated as a range.

2.  Also, the industrial revolution start date reference taken from wikipedia page on the industrial revolution.

<div class="frame">
<iframe frameBorder="0" style="width: 100%; height: 35em;" src="./file/main/plotly.graph.lsa_kopp_scatterplot.html"></iframe>
</div>

So far we've only found that the sea level _has been rising_ - but will it continue to rise?

### Future Sea Level

Given the immense complexity and myriad factors influencing the sea level, creating a climatic model to forecast future sea level rise is beyond our capabilities.

Thankfully, smarter folks than us have already done this, namely: the IPCC. Of course, predicting the future is difficult if not impossible, so the IPCC provides us with a number of different scenarios in the form of SSPs (previously known as RCPs) through which we can evaluate the possible futures we face. We'll be focusing on SSP 126, 245, and 585, which we'll refer to as the 'best', 'medium', and 'worst' case scenarios.

| SSP | Scenario | Scenario Details                                                                                |
| --- | -------- | ----------------------------------------------------------------------------------------------- |
| 119 | Best     | CO2 emissions cut to net zero around 2050.                                                      |
| 245 | Medium   | CO2 emissions around current levels until 2050, then falling but not reaching net zero by 2100. |
| 585 | Worst    | CO2 emissions triple by 2075.                                                                   |

The data we will use to model the different scenarios comes from the [IPCC AR6](https://doi.org/10.5281/zenodo.6382554) report. It can be downloaded [here](https://zenodo.org/records/6382554/files/ar6.zip?download=1).

It's important to note that our model $M_1$ (for cost) uses a model $M_2$ (for sea level rise) that is fit to the output of a model $M_3$ (that the IPCC created). More details on the $M_2$ to $M_3$ process can be found in this [[ar6_slp_model_methodology.ipynb|informal jupyter notebook]] documenting the process.


<!--
more links:

- [Intergovernmental Panel on Climate Change](https://www.wikiwand.com/en/Intergovernmental_Panel_on_Climate_Change)
- [SSPs](https://www.wikiwand.com/en/Shared_Socioeconomic_Pathways)
- [RCPs](https://www.wikiwand.com/en/Representative_Concentration_Pathway)

Notes:

- sea_level_change units are millimeters
- using medium confidence, high confidence was not an option
- distribution fits are random code I wrote/copied from stackoverflow a while ago, going to assume it works
 -->

### Property Value

<!-- Starting with property, we can imagine that the property cost is a function of the value of the property lost. To estimate the value of the property lost, we need to know the value of property across areas in miami
 -->

Starting with property cost, we'll take the following premises as true. (1)
{ .annotate }

1.  In a number of cases we will assume potentially false premises to be true, as not doing this would significantly increase the complexity of the model, and accordingly is out of scope. We will attempt to point out limitations and issues with each premise though. Then, if the reader would like to replicate, modify, or improve the code associated with the model, they have a headstart on some of the stuff that could be addressed.

!!! premise "If an area is inundated with sea water, we consider the property in that area lost."

!!! premise "If an instance of property is lost, we consider the market value of the property lost to be a cost."

Already, an issue presents itself. Namely, when we are considering the market value of the lost property, at what point it time should we assess its value?

It seems reasonable to assume that when the property has *already* been lost to sea level rise, the property value would be $0. Furthermore, once it becomes evident to the market that a property *will* be lost to SLR in the short term, we would also expect that the the market value would converge to zero.

As such, we should not assess the lost market value by looking at the market value, but rather by looking at what the market value would be in the absence of SLR, comparing it to the market value in the presence of SLR (and specifically, various potential SLR scenarios), and taking the difference between the two.

Unfortunately, this is an unpredictable and dynamic system.




## Life


## Liberty




<!--
## Secondary Analyses

## Policy Recommendations

## Conclusion
-->

<!-- todo: move to sunklib readme -->
<!--

Before you begin, make sure you install the package utilities and configure any necessary API keys.

        !!! info "Dependencies"

            **Required**

            - Python (>= 3.10)

            **Recommended**

            - Visual Studio Code
            - Miniconda


        !!! info "Setup"

            ```bash title="Install the package utilities with pip"
            pip install sunklib
            ```

            ```bash title="Download the necessary resources via the CLI"
            scli download --all
            ```

            ```bash title="Configure the required API tokens with the CLI"
            scli tokens --interactive
            ```

 -->

<!--
!!! tip "You can click on images on the site to open them in a zoomable lightbox."
-->


<!--

-->


<!-- -->




<!--
??? quote "All models are wrong, but some are useful."
    This quote - often attributed to <a href="https://www.wikiwand.com/en/George_E._P._Box">George Box</a> - acknowledges that statistical and scientific models are never a perfect representation of reality. What it would mean for a model to be "right"? By definition, a model is a simplified representation of some other <a href="https://ontobee.org/ontology/BFO?iri=http://purl.obolibrary.org/obo/BFO_0000001#:~:text=An%20entity%20is%20anything%20that%20exists%20or%20has%20existed%20or%20will%20exist.">entity</a> that is not the model. If you are trying to model something perfectly, perhaps the only way to have a "correct" model of an entity (correct insofar as you are able to predict the path through the state space of reality that the modeled entity takes) is to recreate the entity itself, in which case, the simulation of the entity is the entity and is running in real time. Which isn't very helpful.
 -->

<!-- ### Policy Recommendations -->


<!--
<video style="width: 30vw;" controls loop>
   <source src="/file/output_high.mp4" type="video/mp4">
</video>

 -->

 <!-- Notably a secondary claim we will also evaluate relates to the "growing concern about the potential impact on the city". Is concern actually growing? We will utilize various computational social science research tools in an attempt to find the answer.
 -->


<!-- TODO -->
<!--
- AR6 data contains regional data, should use this
    - skipping right now to avoid dealing with netcdf format

 -->