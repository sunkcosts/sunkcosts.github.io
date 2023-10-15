

<style>

.md-content__inner {
    background-color: transparent !important;
    padding: none !important;
    top: -4em;
}
.md-sidebar__scrollwrap {
    display: none !important;
}


html {
    background-image: url("./file/internal/image.background.sunkcosts.jpg");
    height: 100%;
    background-attachment: fixed;t
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}

</style>

<div align="center" markdown>

# **Sunk Costs**

<p></p>

## Forecasting the Economic Impact of Sea Level Rise on Miami

</div>

<!-- TODO: refactor text once full analysis is complete -->
!!! abstract "Abstract"
    <!-- TODO: rephrase -->

    We attempt to forecast the economic impact of sea level rise (SLR) on the city of Miami. Instead of producing a single value, however, we produce a model for which a user may supply values based on what they believe is reasonable. This analysis is structured as a high level overview of the process used to produce the model, and the parameters we associate with possible different future scenarios.

    To crystalize the results of the analysis, we conclude with three major scenarios: best case, medium case [rephrase], and worst case, by the year 2100.

    We find that... [include results here]

!!! tip "You can press `Command + K` or `Control + K` to open and close the quick search bar."



<!-- TODO: add note about the fact that this model is forecasting using existing forecast data, we are not fitting lines to data, for the purpose of prediction at least -->

??? info "Model Access"
    There are two ways to access the model:

    1. You can access the model by going to the [webapp](https://sunkcosts.streamlit.app) deployed on streamlits free share service. There's a potential for exceeding the 1GB memory bandwidth provided by streamlit, and if that occurs, this won't work.
    2. You can run the GUI on your local machine. See the [[documentation/index|documentation]] for more information on this.


<!-- TODO: change items below to collapsible details -->


??? note "Continuous Development"
    This analysis and model are subject to change. If you find an issue with the methodology or have a suggestion for an improvement, please submit it in the [GitHub repository]() - either in the [issues]() or [discussions]() sections depending the type of feedback you are submitting.

??? note "Sunshade Project Context"
    The focus of this report is the economic forecast, however the analysis was performed to contrast the cost of losing Miami to sea level rise with the cost of deploying a space based sunshade for geoengineering purposes. The project proposal was presented in 2022 at the New Worlds space conference in Austin. A modified [slide deck](../file/internal/document.slides.earthshade.pdf) for the proposal is included on this site.

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

<br>

<!-- ## [❯ Read the analytical report](./analysis.md)

<p></p>

## [❯ Open the interactive model](https://sunkcosts.streamlit.app)

<p></p>

## [❯ Review the methodology](sort/index.md)

<p></p>

## [❯ Suggest an improvement](https://www.github.com/sunkcosts/sunkcosts.github.io/discussions)

<p></p>

## [❯ Read the documentation](./docs/index.md)

<p></p>

## [❯ View the source code](https://www.github.com/sunkcosts/sunkcosts.github.io) -->

