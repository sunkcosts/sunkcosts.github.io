# Report

<!-- ## Abstract

TODO -->

## Introduction

According to ChatGPT, the following statement is a good opener for this report.

> Miami is situated in Miami-Dade County, on the southeastern coast of Florida. As the effects of climate change continue to manifest, there is growing concern about the potential impact on the city. One of the most pressing issues is the rise in sea level, which threatens to inundate Miami's low-lying areas and cause extensive damage to its infrastructure and property. In addition, the city is likely to experience more frequent and severe extreme weather events, such as hurricanes and flooding, which could further exacerbate the risks posed by rising sea levels.


Let's pause for a moment, as a number of claims were just made which you might be expected to take at face value as the reader. While they may seem reasonable to many, it is worth verifying whether or not they are actually true before building a model around them. Plus, verifying the accuracy of the assertions is a good entry point into the analytical process used to create this report, and allows us to build out the foundations of the model.

### Claims

For clarification, the distinct assertions we will examine are as follows.

1. Miami is on the southeastern coast of Florida.
2. The sea level is rising (implied).
3. The rising sea level threatens to inundate Miami.
4. This inundation might cause damage to infrastructure and property.
5. The frequency of extreme weather events is increasing.
6. The increased frequency of extreme weather also increases the risk that more damage will occur.
7. There is growing concern about the potential impact on the city.

??? note "Order & Omissions"
    Note that the order has been adjusted so as to facilitate linear organization of the report. Also, the implication that 'the effects of climate change are beginning to manifest' is ignored, as this is meaningless without a definition for what those effects are, which are only provided later in the statement.


#### Claim 1: Geography

There ought be no controversy in respect to the fact that we consider the first claim true absent any analytical evaluation. Nonetheless, it's helpful to establish *exactly* where we are focusing. A satellite image of the geographic region of analysis used in this report is exhibited in Figure 1.

<!-- TODO: Add source for satellite data and link code. -->

<figure markdown>
  <img src="../assets/satellite/miami_sample_area_small.png" width=400>
  <figcaption>Figure 1: Region of Analysis</figcaption>
</figure>


??? question "Coordinates"
    The coordinates included below refer to the top left and bottom right points that form the bounding box, expressed in latitude and longitude.

    ```json
    {
      "top_left": {
        "latitude": 25.958782,
        "longitude": -80.347522
      },
      "bottom_right": {
        "latitude": 25.698782,
        "longitude": -80.087522
      }
    }
    ```

#### Claim 2: SLR Status





## Notes

<!-- # STRUCTURE -->


<!-- ## The Big SIP -->

<!-- ## Key Points -->

<!-- ## Introduction -->

<!-- ## Context -->






<!-- ## Pre-SIP Costs -->

<!-- ## Post-SIP Costs -->

<!-- ## SIP Importance -->

- video of storm surge

<!-- # SIP Satellite Visualization -->


<!-- ## Conclusion -->

<!-- # SIP Temporal Estimation -->

Given the premise that sea levels continue to rise, the question is not if, but rather when the SIP will begin. Probabalistic estimates are crucial given the economic and humanitarian implications of the SIP.

We endevoured to perform an analysis to establish some rough quantitative estimates using data from the [IPCC Assessment Report 6](https://www.ipcc.ch/assessment-report/ar6/).

Using the , we can fit a skewed normal probability density function to the distribution of estimates across all scenarios for each temporal interval (in this case: decades out to 2150). We review what this means in greater detail below.

The IPCC produces projections for a number of different scenarios. Each scenario produces a distribution of possible SLR outcomes in 10 year intervals out to 2150. For the analysis here, we've amalgamated data from those with `medium` confidence.

Take for example, the distribution of potential global mean SLR values in the year 2100. If we plot this data on a histogram, we get Figure 5.

---

<!-- ## Figure 5: Histogram of Projected Outcomes for GMSLR by 2100 -->

<p align="center"><iframe frameBorder="0" width="1000px" height="400px" src="https://htmlpreview.github.io/?https://github.com/miamilost/miamilost.github.io/tree/main/docs/assets/global_mean_slr_2100_model_outcome_dist.html"></iframe></p>

*Fig 5. Data Source: [IPCC AR6 Sea Level Projections](https://zenodo.org/record/5914710) • [DOWNLOAD](https://zenodo.org/record/5914710/files/ar6.zip?download=1)*

---

We can take this distribution and fit a skewed normal probability density function (PDF) to it. You can think of this as a 'line of best fit' that follows the curve traced by the histogram.

<!-- ## Figure 6: -->

<p align="center"><iframe frameBorder="0" width="1000px" height="500px" src="https://htmlpreview.github.io/?https://github.com/miamilost/miamilost.github.io/tree/main/docs/assets/skewnorm_dist_2100.html"></iframe></p>

---

The benefit of representing the distribution as a PDF is that we can easily integrate the area under any arbitrary interval, thus computing an estimate of the probability that the true value falls within that interval.

<!-- ## Figure 7: PDF Interval Integration -->


---

<!-- ## Figure 8: -->

*Remember that the graphs are interactive; you can drag to rotate the graph, scroll to zoom, and ctrl-click and drag to reframe the plot.*

<p align="center"><iframe frameBorder="0" width="1000px" height="500px" src="https://htmlpreview.github.io/?https://github.com/urthshade/miamilost/blob/main/docs/assets/all_dists_to_2100.html"></iframe></p>

---

We set the "SIP starting point" at an SLR of 900 millimeters - under the 1 meter at which we will see a disproportionate increase in coastal inundation, but possibly around the time that major areas of the city and surrounding areas would have to be evacuated (assuming preventative measures are not taken).

To estimate the probability that the SIP will *begin* by a given year, we integrate the area greater than 900mm under the curve, for the PDF for a given year. TLDR, we get the following chart, which illustrates the probability the SIP will begin in any given year. Please keep in mind the points made on the [Miami Adjusted SLR](miami-adj-slr.md) page.

<!-- ## Figure 9: SIP Temporal Probabilities By Year (10 Year Intervals) -->


<!-- # Supplementary Analyses -->


<!-- ## Demographics -->


<!-- ## Awareness -->


<!-- ## Insurance -->

<!-- # Miami: Abrupt SLR Inflection Point (SIP) -->

Continuing our analysis, let's look at a subset of Florida containing Miami and several surrounding areas. The area of analysis (henceforth: AoA) can be found within the following coordinate bounds (latitude, longitude):




<!-- ## Figure 3: Area of Analysis (AoA) -->


*Fig 3. Data Source: [Mapbox](https://www.mapbox.com/)*

To determine how SLR will effect Miami, we examined the elevation distribution across the AoA.

<!-- ## Figure 4: Elevation Distribution of AoA -->

<p align="center"><iframe frameBorder="0" width="1000px" height="400px" src="https://htmlpreview.github.io/?https://github.com/miamilost/miamilost.github.io/tree/main/docs/assets/miami_elevation_dist.html"></iframe></p>

*Fig 4. Data Source: [Mapbox](https://www.mapbox.com/)*

This graph is useful, as it illustrates the rather abrupt increase in the amount of area at an elevation of just around 1 meter. This implies that (assuming there are no preventative measures), there could be an "SLR Inflection Point" (or SIP for short).

The use the term "SIP" encompasses the area out to ~3 meters - at which point the elevation distribution returns to pre-SIP levels. The beginning of the SIP is the focus of our next analysis however. This represents the short period of time where in which coastal inundation may go from being manageable to potentially catastrophic.

<!-- ## Total Cost Estimate -->

<!-- ## Discussion -->

- are people starting to move out?
- what reasons might there be for ignorance?
- how has the news and tone shifted (GDELT)?


<!-- ## Seawall Economic model -->

Model approach:

We model sea level rise (SLR). This allows us to estimate sea sea level rise under different scenarios.

We show that given the topology of miami, it can be expected that while preventive measures to reduce impact can reduce the economic cost in the short term, there will eventually come an inflection point at which point preventive measures that do not address the underlying cause will no longer be effective.

Post inflection, the internal dynamics of the model switch - the factors involved in the computed economic cost change substantially.

*demonstrate inflection point*

- assumption: that this inflection point cannot be overcome with technology, and the city will have to be abandoned
  - counterpoint: assuming sea level rise continues, the question is not when we hit the inflection point, but rather, when.

<!-- # pre-inflection cost factors: -->

- building a sea wall
- insurance costs for increased flood events and property damage
- maintenance costs for infrastructure: eg - improved pumps, desalination or water transport

<!-- # post-inflection cost factors: -->

<!-- ## Direct -->

-

<!-- ## Indirect -->


- qualitative components, estimates,

- property insurance prices increases

- property market value increase

- economic output
- cost of rehousing people
- current investment rates
  - factor in investment rate growth, increased capital inflow to property
  - factor in population growth, inevitable cost of rehousing people
    - The US Government census estimates that as of July 2021 it has a population of 439,890 (United States Census Bureau, 2021).


- given the sudden increase in land area covered, we can expect that at some point, the inflection point will be hit, and the economic damage will acrue very suddenly

- sudden inflection point: SIP
- instead of estimating SLR by 2100, let's estimate the lower and upper bounds and lower temporal bounds for the SIP
- can we use a markov chain to introduce randomness into the system?
    - or monte carlo simulation, or equivalent

- probability distribution of scenario * economic cost of each scenario vs. time


<!-- # Global SLR Model -->

In this section we document the steps used to create a model for the estimation of global sea level rise.





Accordingly, it would be


<!-- ## Reintegrate -->

We do this by first performing a qualitative literature review, in order

<!-- ## Qualitative Review -->



<!-- ## Notes -->

Note that this SLR projection does not mean that sea level has to rise this drastically before many areas become practically unlivable. This is because of the marked increase in high-tide and flood events we would expect to see before the sea level has fully risen.

Note that in the case of Miami, due to the topographical heightmap, we would expect to see a slow and steady progression for some time, followed by a very fast apparent increase in sea level in a very short period.

- show simple linear model
- show linear models given varying time periods
- show rate of change - accordingly, it is better to look at the rate of change and then work back to a model
- [ ] create  an area underwater by time graph to show where the estimated major shift will be, given the different models (more conservative models -> will be later in time)
- [ ] create a model that allows you to plug in a variable representing "severity", accordingly, at this point the model takes in:
  - input:
    - year
    - severity of estimation (0 to 1, where 0 is absolute lower bound estimate, and 1 is absolute upper bound estimate)
  - output:
    - estimated sea level rise


<!-- # Introduction -->


<!-- ## Background -->







Miami is a city on the coast of Southern Florida that as of


- background introduction here

model:
- create global SLR estimation model
- create local SLR estimation model
- use to inform economic cost model
	- variables associated?


<!-- # Pre-SIP Life Cost estimate -->


In the United States, FEMA estimates the statistical value of a single human life at $7,500,000. Of course, assigning a monetary value to the cost of a life may seem somewhat cold. Of course - every life is infinitely valuable from the perspective of the person living within that life. It would not be particularly useful to assign an infinite value to a single human life, as this would inhibit any utilitarian calculations. For instance, if we assigned a value of 'infinity' to each life, then at least on a mathematical basis, a single life would be worth the same as all lives, which is obviously not very useful.

https://www.fema.gov/sites/default/files/2020-08/fema_bca_toolkit_release-notes-july-2020.pdf

According to the most recent New York Times estimate, 114 people died in Florida due to hurricane Ian

source: https://www.nytimes.com/2022/10/21/us/hurricane-ian-victims.html

This works out to a cost of $855,000,000.


In this analysis we attempt to estimate the economic impact of sea level rise on the city of Miami. We do this through a meta-analysis of existing literature, which we use to fit several non-linear models of sea level rise (SLR). This allows us to establish optimistic, neutral, and pessimistic scenarios for the sea level by 2100. We animate these scenarios using topographical and image satellite data. We then use these estimates to inform an economic model to estimate costs.

todo - make a note about how wide margins of uncertainty don't invalidate models, rejecting something because it isn't perfectly accurate, or can't perfectly predict the future is a recipe for failure, and if an analytical model can't make a great prediction, a subjective intuitive model, 95%+ percent of the time will be far, far less accurate.,