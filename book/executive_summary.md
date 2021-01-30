---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.8.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Executive Summary

I know of two analyses of Dream's recent speedrunning performance, one from the Minecraft Speedrunning Team, the other from Photoexitation. While both make some good points, both also have serious flaws. This document is my attempt to do a better analysis.

In {doc}`critique_of_reports`, I point out a number of issues with those two analyses, the most notable of which are the Minecraft Speedrunning Team's {ref}`reliance on p-values<sec:p_value_misunderstood>` and Photoexcitation's failure to mention that {ref}`Bayesian methods are inherently less likely to conclude Dream cheated<sec:missing_context>`. I walk through the logic and mathematics behind my approach in {doc}`methodology`, which relies heavily on Bayesian statistics and conjugate priors. I implement said math in two Python routines and in {doc}`sim_results` I validate them through simulations, with the goal of allowing anyone to easily run their own analysis.

In {doc}`data_results`, I find the probability of Dream cheating to be much lower than the Minecraft Speedruning Team's report, at least five orders of magnitude lower in fact. I also find his performance to be more consistent with simulated players who modified their version of Minecraft than with simulated players who did not or with comparable real-world Minecraft speedrunners. {doc}`I do not make a definitive conclusion<conclusion>`, though, in deference to the Minecraft speedrunning community. In {doc}`future_work`, I suggest a few ways to extend this analysis.

In {ref}`sec:cheating_techniques` I also point out an apparent oversight in the speedrunning community which could allow for different styles of cheating that could easily be missed. I outline {ref}`how to detect these styles<sec:data_pearl>`.
