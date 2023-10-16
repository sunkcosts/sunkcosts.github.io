# Analysis

TODO: Analytical Report Structure


## Introduction

According to ChatGPT, the following statement is a good opener for this report:

> Miami is situated in Miami-Dade County, on the southeastern coast of Florida. As the effects of climate change continue to manifest, there is growing concern about the potential impact on the city. One of the most pressing issues is the rise in sea level, which threatens to inundate Miami's low-lying areas and cause extensive damage to its infrastructure and property. In addition, the city is likely to experience more frequent and severe extreme weather events, such as hurricanes and flooding, which could further exacerbate the risks posed by rising sea levels.


### Claim Evaluation

Let's pause for a moment, as a number of claims were just made or implied which you might be expected to take at face value as the reader.

The primary claims are as follows:

1. The sea level is rising.
2. The frequency and intensity of extreme weather events is increasing.
3. These changes may harm life, infrastructure, and property, in the city of Miami.

While they may seem reasonable to many, it is worth verifying whether or not they are actually true. Plus, verifying the accuracy of the assertions is a good entry point into the analytical process used to create this report, and allows us to build out the foundations of the model.

Notably a secondary claim we will also evaluate relates to the "growing concern about the potential impact on the city". Is concern actually growing? We will utilize various computational social science research tools in an attempt to find the answer.

#### Sea Level Rise

First, let's start by looking at the global SLR trend over the last few decades. We'll use [[references#Recent Global Mean SLR|data]] collected by the Laboratory for Satellite Altimetry. Specifically, the global mean sea level, with [[seasonal_signals|seasonal signals]] removed.

If we take the data from the Jason satellite missions and [[lsa_recent_gmsl.ipynb|create a scatterplot]] of mean global sea level across the last ~30 years, we get the following graph.

<iframe frameBorder="0" border="0" width="100%" background="black" height="500px" src="plot/noaa_lsa_global_slr_seasons_normalized.html"></iframe>

This graph shows that global mean sea level is indeed rising, but it is technically possible that it has been rising for some time. While this would not effect our model, as our model simply seeks to compute cost and is agnostic to the causes of SLR, let's nonetheless evaluate the temporal context by zooming out to look at the last few millenia.





---

- this page -> overview of structure
- report -> main report
- model -> explanation of model methodology
- references -> bibliography
- notebooks -> jupyter notebooks with specific code referenced

* the model is not a jupyter notebook but a python module. This python module/model can be rendered as an app.

- details -> tangents and further notes

... documentation section -> steps for getting setup on your machine

## Model Objectives

## Report Objectives

The discrete objectives of this report are to:



## Sea Level Rise Trends



### Recent Global Trends







### Historical Global Trends



### Recent Regional Trends


---

<!-- TODO: add note about the fact that this model is forecasting using existing forecast data, we are not fitting lines to data, for the purpose of prediction at least -->


