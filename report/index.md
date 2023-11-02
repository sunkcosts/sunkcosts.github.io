# Sunk Costs

<p style="font-size: 2.2em; color: #b4b4b1; margin-top: -0.65em; margin-bottom: 0em;">Forecasting the Economic Impact of Sea Level Rise on Miami</p>

??? warning "This project is currently under development."
    The site is available as a common reference, however it is worth noting that it is currently unfinished. The site, and the model, will continue to be developed in the near term.

!!! tip "You can press `Cmd + K` or `Ctrl + K` to open the quick search bar if you want to find something specific across the site."

!!! tip "All data visualizations on this site are interactive. Double click a plot to reset to the original zoom."

??? info "Sunshade Project Context"
    The focus of this report is the economic forecast, however the analysis was performed to contrast the cost of losing Miami to sea level rise with the cost of deploying a space based sunshade for geoengineering purposes. The project proposal was presented in 2022 at the New Worlds space conference in Austin. A modified [[document.slides.earthshade.pdf]] for the proposal is included on this site.

??? note "Issues & Continuous Development"
    This analysis and model are subject to change. If you find an issue with the methodology or have a suggestion for an improvement, please submit it in the [GitHub repository]() - either in the [issues]() or [discussions]() sections depending the type of feedback you are submitting.

---

## Overview

<!--

If you would like to replicate the analysis, run the model, review the code, discuss enhancements, or submit any issues you notice (technical, methodological, or otherwise), please see the <a href="https://www.github.com/sunkcosts/sunkcosts.github.io">GitHub</a> repository for more information. You can also click the source/fingerprint quicklink on the top left to go to the repository from anywhere on this page.

 -->

The objective of this project is to create a simple model that can forecast the economic cost of sea level rise (SLR) on the City of Miami by the year 2150. This report provides an (ideally) engaging introduction to the model, along with secondary analyses not included in the primary model.

It is important to point out that this model attempts to forecast cost *in the absence of human intervention*. It seems reasonable to expect this will occur as costs begin to materialize.

<!-- (1)
{ .annotate }

1.  If would like to experiment with the model yourself you can either visit the web interface, or alternatively follow the setup instructions provided [here]() to run it locally. -->

Before we begin, let's establish the geographic bounds of the region we will evaluate. (1) We'll refer to this as the "Analysis Area" or AA for short.
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

## Summary

We recognize that not everyone will have time to read the full report. Accordingly, forecasts of economic impact for best case (low cost), baseline (medium cost), and worst case (high cost) scenarios by the year 2100 are included below. (1) **Currently, only the best and worst case are included. Also note that the videos show SLR at 2100, but the final model will go out to 2150. Also, note that these are currently ballpark figures and will be adjusted as the model is streamlined.**
{ .annotate }

1.  Note that these dollar figures are almost certainly incorrect, and also not actually the figures the model returns, but rather figures derived from the output of the model. Regardless, they are included on the basis that decisive predictions - though virtually always wrong (or if right, by chance) - do have a certain psychological appeal.

<!-- Note that these forecasts currently only factor in [[#Property]] and [[#Life]]. -->

<!--

**Key Points**

- Deserunt ad ut commodo labore ullamco quis aliquip.

-->


<!--

**Policy Recommendations**

- Fugiat consectetur consequat occaecat sint cupidatat aute deserunt fugiat aute minim esse.
 -->


<!-- **Cost Scenarios** -->

<div class="grid-container-3" style = "margin-top: -0.6em; margin-bottom: 0em;">
    <div class="grid-item">
        <div class="admonition dollar-green">
            <p class="admonition-title">~50 Billion</p>
        </div>
        <video style="width: 30vw;" controls>
            <source src="./file/main/video.sim.output_low.mp4" type="video/mp4">
        </video>
    </div>
    <div class="grid-item">
        <div class="admonition dollar-yellow">
            <p class="admonition-title">~300 Billion</p>
        </div>
        <p><i>Visualization will be included in complete version</i></p>
    </div>
    <div class="grid-item">
        <div class="admonition dollar-red">
            <p class="admonition-title">~900 Billion</p>
        </div>
        <video style="width: 30vw;" controls>
            <source src="./file/main/video.sim.output_high.mp4" type="video/mp4">
        </video>
    </div>
</div>


---

## Introduction

Debatably, objectively quantifying cost is impossible on an epistemological level. Regardless, we will make an attempt. To do so, we must first establish the "factors" we will consider - Locke's [life, liberty, and property](https://www.crf-usa.org/foundations-of-our-constitution/natural-rights.html#:~:text=%22life%2C%20liberty%2C%20and%20property.%22) might be a good place to start. We'll address these factors in the order of increasing complexity of model representation.

??? note "Economic Value Subjectivity"

    **Tangible vs. Intangible Assets**

    When we speak of the economic impacts of sea level rise, we often first consider tangible assets – properties, infrastructure, and physical goods that can be directly measured in monetary terms. But how do we categorize and put a value on intangible assets impacted by SLR?

    > A renowned artist has painted a mural on a building's exterior wall in a coastal district of Miami. This mural becomes a significant cultural and tourist attraction. Over the years, its intangible value in terms of cultural identity and tourism appeal grows exponentially. Now, due to SLR, there's a real threat of the building being submerged or destroyed. How do we quantify the loss of this mural?

    If we look at it in terms of the artist's fee and the material costs, the monetary value might be relatively low. However, when factoring in its cultural significance, the lost potential tourism revenue, and its irreplaceability, the value becomes more nebulous.

    **Collective vs. Individual Loss**

    Economic impacts can be felt at both individual and collective levels. For instance:

    > A family-owned restaurant that has been operating for decades at Miami's seafront might face bankruptcy due to SLR causing frequent flooding in the area. On a macro level, the economic loss from this single restaurant might seem insignificant when talking about the entire city's economy. But for the family running it, it's their livelihood, heritage, and perhaps a significant part of their identity.

    Is it justifiable to weigh the city's overall economic health over the devastating loss of a single family's livelihood? It's subjective and varies based on who you ask.

    **Direct vs. Indirect Monetary Loss**

    While direct losses like property damage due to SLR are (relatively) straightforward to quantify, indirect losses can be nebulous.

    > Due to constant threats of flooding, insurance premiums for properties in Miami might skyrocket. This can lead to reduced property values and, subsequently, reduced property tax revenues for the city. The cascading effect might also mean businesses relocating, leading to job losses and reduced economic activity in affected areas.

    While we can quantify the immediate losses due to property damage, how do we adequately measure the long-term economic ripple effects of such events?


<!--
<div class="image">
    <img src="./file/report/image.satellite.miami_sample_area_small.png" style="width: 30em;">
    <figcaption>Fig. 1: Miami Geographic Analysis Area</figcaption>
</div>

-->

## Sea Level

Before we go into the details of quantifying the economic impact, lets' first focus on sea level rise.

### Historical Global Sea Level

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


### Future Global Sea Level

Given the immense complexity and myriad factors influencing the sea level, creating a climatic model to forecast future sea level rise is beyond our capabilities. (1)
{ .annotate }

1.  Interactions between the atmosphere, hydrosphere, geosphere, and even biosphere need to be accounted for, with each having its own set of variables and sub-variables that intertwine in ways that are not always predictable. Small changes in one factor, such as volcanic activity, solar radiation, or even human emissions of greenhouse gases, can have cascading effects throughout the system. What's more, feedback loops – both positive and negative – can amplify or dampen these effects in unforeseen ways.


Thankfully, smarter folks than us have already done this, namely: the IPCC. Of course, predicting the future is difficult if not impossible, so the IPCC provides us with a number of different scenarios in the form of SSPs (previously known as RCPs) through which we can evaluate the possible futures we face. We'll be focusing on SSP 126, 245, and 585, which we'll refer to as the 'best', 'medium', and 'worst' case scenarios.

| SSP | Scenario | Scenario Details                                                                                |
| --- | -------- | ----------------------------------------------------------------------------------------------- |
| 119 | Best     | CO2 emissions cut to net zero around 2050.                                                      |
| 245 | Medium   | CO2 emissions around current levels until 2050, then falling but not reaching net zero by 2100. |
| 585 | Worst    | CO2 emissions triple by 2075.                                                                   |

The data we will use to model the different scenarios comes from the [IPCC AR6](https://doi.org/10.5281/zenodo.6382554) report. It can be downloaded [here](https://zenodo.org/records/6382554/files/ar6.zip?download=1). (1)
{ .annotate }

1.  It's important to note that our model $M_1$ (for cost) uses a model $M_2$ (for sea level rise) that is fit to the output of a model $M_3$ (that the IPCC created). More details on the $M_2$ to $M_3$ process can be found in this [[ar6_slp_model_methodology.ipynb|informal jupyter notebook]] documenting the process.

The IPCC global sea level projections data is split into two confidence levels: 'low' and 'medium'. We'll be using only the medium confidence level. Without going into the details, we can use the IPCC data to model the probability density of given sea levels in each scenario out to the year 2150. An example for the SSP 245 scenario at the year 2100 is included below.


<div class="frame">
<iframe frameBorder="0" style="width: 100%; height: 35em;" src="./file/main/plotly.graph.ssp_245_medium_2100_pdf.html"></iframe>
</div>

If we want to get the probability that the sea level will be in a certain range (1) we can get the area under the curve between two intervals.
{ .annotate }

1.  Again mind you, for this scenario, confidence level, and specific year, from the IPCC estimates, from the skewed normal distribution I fit to the IPCC estimates.

If we display the probability distributions for each decade, for each scenario, we get the following graphs.

<div class="grid-container-3" style = "margin-top: 0em; margin-bottom: 0em;">
    <div class="grid-item">
        <div class="frame">
        <iframe frameBorder="0" style="width: 100%; height: 35em;" src="./file/main/plotly.graph.ssp_126_medium_multi_pdf.html"></iframe>
        </div>
    </div>
    <div class="grid-item">
        <div class="frame">
        <iframe frameBorder="0" style="width: 100%; height: 35em;" src="./file/main/plotly.graph.ssp_245_medium_multi_pdf.html"></iframe>
        </div>
    </div>
    <div>
        <div class="frame">
        <iframe frameBorder="0" style="width: 100%; height: 35em;" src="./file/main/plotly.graph.ssp_585_medium_multi_pdf.html"></iframe>
        </div>
    </div>
</div>

It is easier to see how the probability distributions differ if we graph them against each other on the same plot. This can become visually crowded quite quickly, however, so we've included just scenario 126 and 585 below, from 2080 onwards. *Remember that these visualizations are interactive, so you can click and drag the graph to rotate it and get a better view.*

<div class="frame">
<iframe frameBorder="0" style="width: 100%; height: 60em;" src="./file/main/plotly.graph.126_vs_585_pdf.html"></iframe>
</div>


!!! warning "Sections below are a work-in-progress."


### Regional Differences

**Introduction**

### The Big SIP



## Property

We'll assume that the loss of property due to SLR has a negative economic impact.




<!--
### Property (Infrastructure)

link: https://riskcenter.wharton.upenn.edu/miami-and-the-costs-of-climate-change/

> the Biscayne aquifer—where southeast Florida draws its drinking water—will increasingly suffer from salt-water intrusion, a problem for which there is no foreseen solution other than the investment of billions of dollars in water-treatment facilities.



 -->

<!--

Increasing flooding hazard in coastal communities,  Wdowinski et al.

> The average pre- 2006 rate is 3 ± 2 mm/yr, similar to the global long-term rate of SLR, whereas after 2006 the average rate of SLR in Southeast Florida rose to 9 ± 4 mm/yr. Our results suggest that engineering solutions to SLR should rely on regional SLR rate projections and not only on the commonly used global SLR projections.

Source: Abstract, Page 1
This suggests that global sea level rise is not a good metric for local sea level rise in Miami.

> Miami has been identified as the economically most vulnerable city to SLR in the world (US National climate assessment (Melillo et al., 2014)).

Source: Introduction, Page 2
Useful fact to include.

> The number of rain events increased from 9 events in the 1998e2005 time period to 12 events in the 2006e2013 period, an increase of 33%. A more significant increase appears in the number of tide events, from 2 to 8 events, an increase of 400%. Both analyses indicate a significant increase in tide-induced events after 2006.

Source: Cross-Reference Analysis, Page 3

> In order to evaluate the cause for the post-2006 increase of tide events, we analyze the 16-year long daily HH tide gauge record of the nearby Virginia Key station. Best-fit analyses of the tide gauge data reveal a high SLR rate, in the range of 4.1e4.9 mm/yr, depending on the assumed best-fit model (Fig. S2, Supporting Information, Section S2).

Source: Time series analysis of the Virginia Key tide gauge record, Page 3

> An improved method for estimating the rate of SLR and its changes over time is the Ensemble of Empirical Mode Decomposition (EEMD) (Ji et al., 2014; Wu et al., 2009, 2011), which decomposes a time series naturally into amplitude-frequency modulated oscillatory components (often called modes). We applied the EEMD analysis to the Virginia Key daily HH time series and obtained twelve modes (Fig. S4).

Source: Time series analysis of the Virginia Key tide gauge record, Page 3

> The results of the EEMD analysis indicate an accelerating rate of SLR, which began around 2006 (Fig. 5). During this period of accelerated SLR, the HH level in Virginia Key rose by 8 ± 4 cm (Fig. S7), indicating an average rate of 9 ± 4 mm/yr since 2006. Our analysis also yielded the rate of SLR trend, indicating acceleration in the SLR rate from 3 ± 2 mm/yr in 2006 to 14 ± 5 mm/yr in 2013 (Fig. S7). However, these rates are instantaneous and do not reflect a long period of time. Thus, we prefer using the average of 9 ± 4 mm/yr for the period 2006e2013.

> Park and Sweet (2015) analyzed monthly averaged tide gauge records of three southeast Florida sites (Virginia Key, Vaca key, and Florida Bay) using a similar Empirical Mode Decomposition (EMD) method. Their analysis revealed similar results indicating that the rate of SLR has accelerated from the long term 3.8e3.9 mm/yr to 5.9e7.4 mm/yr after 2003. They also analyzed the Florida Current transport record and found a 3 Sv decline in mean transport since 2006. The results of our EEMD analysis, which indicates a significant acceleration in the rate of SLR since 2006, should be viewed cautiously because (1) the length of the time series, and (2) limitations of the EEMD method. Our time series analysis is based on a 16-year long Virginia Key tide gauge record. Such short tide gauge records are typically not used by long-term SLR studies, because they might be affected by nodal and other long-term cycles (18.61, 8.85, and 4.4 years) as well as by possible decadal-scale oceanic and atmospheric processes (e.g., Chambers et al., 2012). Despite the short length of the Virginia Key time series, the effect of nodal cycle on our estimate is minimal, because the dominant modulation along the US Atlantic coast is the 4.4-year quasi-lunar perigee cycle (Haigh et al., 2011), which has a limited bias on 16-year long time series. Unlike other studies concerning with the long-term SLR rate (e.g., Church and White, 2011), our study focuses on decadal scale variations in the rate of SLR. Thus, the 16-year length of the Virginia Key time series is suitable for such analysis.

Source: Time series analysis of the Virginia Key tide gauge record, Page 4

> Including rain-induced events in our analysis revealed that such events impose a significant hazard, as they occur in the sub-tropical climate of Miami Beach 2e3 times per year (Fig. 3 and Table 1). We also found that increasing sea level also increased the frequency of rain-induced flooding events by 33%, because of higher sea level reduces the effectiveness of gravity-based drainage systems. In 2014, the city of Miami Beach invested millions of dollars replacing some of the ineffective gravity-based drainage system by a pumped-based system. Indeed, the change to pump-based drainage system resulted in reduced flooding events in the city.

Source: Discussion, Page 6
I should look into how much this drainage system cost, and what precipitates its need for replacement; ie: how do we predict how the costs will scale and when the pumps will need to replaced/upgraded, and how long they can be upgraded.

> The accelerated rate of SLR in Southeast Florida (9 ± 4 mm/yr since 2006) and other locations along the US Atlantic coast are significantly higher than the global average rate of SLR, which is estimated for the period of 1993e2012 from satellite data as 3.2 ± 0.4 and from in situ data as 2.8 ± 0.4 (Church et al., 2013). Many areas worldwide have experienced higher than the global average rates of SLR, sometimes as high as 20 mm/yr, as in the western Pacific Ocean (e.g., Nicholls and Cazenave, 2010). Spatial variability in the rate of SLR results from salinity variations, nonuniform ocean warming, changes in ocean circulation, and solid Earth's response to the last deglaciation, and changes in gravitational attraction due to ice melt (Stammer, 2008; Wunsch et al., 2007; Milne et al., 2009; Hay et al., 2015). Moreover, since a coherent decrease in the Gulf Stream has not been detected to date and since current climate change projects do predict a coherent decrease, our model results suggest that additional acceleration is possible. Therefore, it is extremely important to take into account the spatial variability in SLR when preparing a city, as Miami Beach, to adapt to increasing sea levels. Engineering projects, such as increasing efficiency of drainage systems or erection of seawalls, are typically based on globally average forecasts of SLR. Thus, if local rates of SLR are significantly higher than those of the globally average ones, as observed in Miami Beach, planned engineering solutions will provide protection for a shorter time period than planned.

Source: Conclusion, Page 8

# Notes
- Seems much of the flooding was caused by rains, or high tide conditions.
- The increase in high tide flooding events may make areas of Miami unviable far before sea level rise does.


 -->

**Applying to Model**


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


<!--

FEMA Benefit Cost Analysis Toolkit
This document is referenced to provide a waypoint estimation for the monetary value of the Value of Statistical Life (per person) ($7.5M).


 -->


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


<!--

Climate model
- NOAA tide and rain gauge records, and other datasets
- Create dataset of global, and miami specific sea level rise, along with dates

Economic Model
- note that estimates from miami may be biased due to perverse economic incentives
	- show cost estimates by year
		- produced by miami/florida related entities, and external entities
- loss in economic output: eg - tourism
	- what industries will be affected and how?
	- what industries can move? (obv. tourism can't)
- factor probability and cost together, create 2D visualization of estimated cost distribution per year
	- create 3D visualization with 3rd axis as time
	- fit normal distribution model (or other dist if appl.) to model distribution of probabilities and costs
	- the estimated cost should be the mean of the probability distribution multiplied by the mean of the cost distribution (or the mean of the cost x probability dist.)
- factor in rising temperatures, property value declines or health impacts.
- model current real estate investment
	- currently increasing? this means more will be lost in the future - factor into model
- I should look into insurance claim datasets in the area
	- can ask: "Miami-Dade County's Public Works and Waste Management office" for datasets
- Should look into
	- zoning datasets
	- property value estimates
	- total economic output of Miami
	- cost of rehousing people
	- cost of attempting to build/maintain quick fix solutions
		- eg: pumping systems and walls
- Create dataset of miami specific economic cost estimates, along with dates, and the factors used for cost estimate (eg: property, externalities, GDP, etc)
- for meta analysis, include estimate (cost, SLR), year, and the type of source (article, publication, published in journal, government review)


- add leaflet map visualization to app?



- add to SLR map visualizations:
	- year
	- sea level rise height
- remove contact information for luke from miamilost project github pages site

slides
- slide to cover an estimate of the best/worst case scenarios
	- embed the video in the slide
- cost estimate
	- preliminary cost estimate is meta analysis of qualitative literature
- cost model doesn't include
	- pumps
	- hurricanes


-->


<!-- 1. United States Census Bureau. (2021). *Quickfacts: Miami city, Florida*. Retrieved October 19, 2022, from https://www.census.gov/quickfacts/fact/table/miamicityflorida,US/PST045221 -->



<!--
Forecast Caveats

In general when we encounter dilemmas like those listed below, we will address them as follows.

1. Point them out and note the biases and limitations of any given definition or approach, so that they may be refined via feedback and iteration.
2. Add the values as adjustable parameters to the model.

Future Prediction

Predicting the future is impossible (or at least beyond our capabilities). We attempt to account for this by creating a model capable of generating a range of scenarios based on the inputs provided by the user, instead of a single discrete prediction. This is also helpful as creating a formal model lays bare assumptions and premises that may otherwise be overlooked, and allows bad assumptions or premises to be more easily caught by others.

??? note "Prediction Certainty"
    In this report, however, we do also attempt to provide estimates of 'best', 'medium', and 'worst' scenarios, as we assess it may increase general appeal.

Inherent Subjectivity

Even if we could predict the future perfectly, the subjective nature of our reality confounds our ability to arrive at discrete monetary values. To concretize this rather abstract statement, we might ask: what is the value of a human life? Consider the following scenario:

> A father wakes up one morning to the sound a broadcast from the EAS telling him that a flash flood has unexpectedly inundated the area. He rushes downstairs and finds that the lower part of his house is already submerged. In a panic, he recalls that his teenage son had spent the night on the couch in the basement, playing video games on their new xbox.

If we asked this man the monetary value of his sons life, what would he say? We might reasonably expect that no discrete figure would suffice, as he values his son to such an extent that it cannot even be expressed in monetary terms.

Unfortunately, assigning an infinite value to each person would inhibit our ability to estimate the economic cost. Accordingly, we're going with the $7.5M figure provided by the  [[citations#FEMA Benefit Cost Analysis Toolkit|FEMA BCA Toolkit]]. Note that while it is used as statistical estimate for the value of a human life, one can adjust the exact value up and down in the model.

!!! details "More examples of this subjectivity dilemma can be found on the [[economic_value_subjectivity|Economic Value Subjectivity]] page."

??? tangent "Infinite Value Paradox"
    If we assign an infinite value to the life of each person, it follows that one person (with a value of infinity) is worth the exact same as any number of $X$ people, who together are all still worth an infinite amount. If one based one's decisions off this paradigm, one would be too paralyzed to get anything done or make sensible decisions, and the world may be worse of for it.


 -->



<!-- TODO: add note about the fact that this model is forecasting using existing forecast data, we are not fitting lines to data, for the purpose of prediction at least -->

<!--

Notes

*   Black swan events

*   Externalities - other costs besides immediate property damage

*   The problem doesn’t end in 2100

*   Other costs not considered

*   Miami isn’t the only city

*   Flooding isn’t the only problem

*   Increase in climate refugees

*   Increase in terrorism

*   Required increase in defense and intelligence costs to defend against increased threat to national security

*   Attention pulled away from other focuses, resources more thinly distributed

*   Decrease in global food security

References

**
* perverse incentives introduced by real estate tax
* many people are treating this as a problem which has an end in sight. It doesn't. When we hit 2100 things will only get worse. And in the case of Miami, if the city is still habitable at this point, it will inevitably cease to be (if we maintain our current path).
* it is unlikely that any steps that the city of miami, or even the state of florida can take, will be able to address this problem in a way that mitigates catastrophic damage by next century (support needed for claim, or, counterclaim)

Wdowinski, S., Bray, R., Kirtman, B. P., & Wu, Z. (2016). Increasing flooding hazard in coastal communities due to rising sea level: Case study of Miami Beach, Florida. _Ocean & Coastal Management_, _126_, 1–8. https://doi.org/10.1016/j.ocecoaman.2016.03.002


-->


<!--




-->

[//begin]: # "Autogenerated link references for markdown compatibility"
[document.slides.earthshade.pdf]: file/extra/document.slides.earthshade.pdf "document.slides.earthshade.pdf"
[//end]: # "Autogenerated link references"
