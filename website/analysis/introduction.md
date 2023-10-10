# Introduction

According to ChatGPT, the following statement is a good opener for this report:

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


<!-- 1. Assess the claims stated above, by:
2. Stratifying them across future scenarios of varying severity, specifically:

3. Build an adjustable model capable of forecasting the economic impact (or lack thereof) of climate change on the city of Miami. The user should be able to adjust the parameters given to the model so as to facilitate exploration of a wide range of possible scenarios. -->


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