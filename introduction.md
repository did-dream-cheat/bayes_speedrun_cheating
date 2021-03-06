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

# Introduction

## Motivation

I first became aware of the accusations against Dream via [a blog I follow](https://statmodeling.stat.columbia.edu/2020/12/24/dream-investigation-results-official-report-by-the-minecraft-speedrunning-team/). As a casual Minecraft player who has watched some of Dream's videos, I was drawn to read the Minecraft Speedrunning Team's [report](https://mcspeedrun.com/dream.pdf). It is very well written, in my opinion, and the team has put a lot of time and effort into creating a thorough investigation. Nonetheless, it made several flawed assumptions that create fundamental problems with the analysis.

That same blog post pointed me towards a [rebuttal report](https://drive.google.com/file/d/1yfLURFdDhMfrvI2cFMdYM8f_M_IRoAlM/view), which had been declared "[hilariously bad](https://statmodeling.stat.columbia.edu/2020/12/24/dream-investigation-results-official-report-by-the-minecraft-speedrunning-team/#comment-1622865)" and riddled with "[absurd errors](https://www.reddit.com/r/statistics/comments/kiqosv/d_accused_minecraft_speedrunner_who_was_caught/ggse2er/?utm_source=reddit&utm_medtook%20time%20to%20review%20theium=web2x&context=3)." My primary critiques of the MST's report were not mentioned, oddly, which drew me to read the rebuttal. Photoexcitation's report also made some faulty assumptions, and again the most important ones were missed by the critiques. While not perfect by any means, the second report was better than I was led to believe.

I asked myself if I could create a better report. After some thought, I realized the situation was quite similar to others I've analyzed in the past, and so I started work on what you are currently reading.

## Declaration of Bias

I am a graduate student in computer science, specializing in computer graphics. I have not taken a university-level statistics course, though I have taken two courses on cryptography and information theory, and those subjects rely heavily on probability. Neither taught me anything new about probability; my interest in algorithms and philosophy have led me to casually study the statistics underlying science. I've found that self-study to be of immense use, as all my research has relied on statistical analysis at some level. At best, I can be considered an amateur statistician.

My plan to compensate for my lack of authority is to be more detailed and open. I will walk through all the math I employ, and explain my analysis and logic as I go. Not only is all the code I used available [via GitHub](https://github.com/hjhornbeck/bayes_speedrun_cheating/) under the [GNU Public License 3.0](https://github.com/hjhornbeck/bayes_speedrun_cheating/blob/main/LICENSE), it is present in this document as well. You can edit and replay both the simulations and analysis via a webbrowser, usually with a click of a button. Pages that support it will have a rocket icon along the page header.

**I have not been paid by Dream to write this report, directly or indirectly. I have not been contacted by him or any third party, let alone asked to write this report.** I have enjoyed watching some of his videos, and I believe he is a very talented Minecraft player, but I am indifferent to whether or not his speed runs are considered valid.

**By the same token, I have no relationship with the Minecraft speedrunning community. None of them have contacted or paid me to write this report, directly or via a third party.** I have no plans on becoming a Minecraft speed runner, I'm content to merely build things and do some casual streaming. They have no more influence on me than Dream.

In short, my motivations for writing this report can be boiled down to two points:

1. [I hate p-values](https://www.google.com/search?q=p-values+site%3Afreethoughtblogs.com%2Freprobate).
2. [I enjoy working with conjugate priors](https://freethoughtblogs.com/reprobate/2020/02/19/dear-bob-carpenter/).
