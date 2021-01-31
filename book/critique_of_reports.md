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

# A Critique of the Reports

(sec:mst_report)=
## Minecraft Speedrunning Team

The [MST report](https://mcspeedrun.com/dream.pdf) is quite good. The authors go into extensive detail on how Blaze rod drops and Pigmen barters for Ender pearls work, to the point of analyzing how random numbers are generated within Minecraft. They gather data on the performance of other runners, which is vital to help rule out flaws in your analysis: if the analysis shows *all* of the top players are cheating, then either cheating is rampant or something is wrong with your analysis. The report goes into quite a bit of detail on the methods used, and shares code to help with reproducibility. I believe it is a good attempt to "present \[an\] unbiased, rigorous statistical analysis of the data" (pg. 4).

(sec:inadequate_comparisons)=
### Inadequate Comparisons to Other Speedrunners

The MST report links to raw data for five top-tier speedrunners, only one of which is Dream. (pg. 24). Rather than carry out their analysis on all five speed runners, though, only Dream's statistics are considered in depth. Figures 1 and 2, on pages 5 and 6, are the only attempt to compare Dream's performance to that of other top speed runners, and even then only raw data is displayed rather than test statistics. The authors of this report had the means and ability to calculate their test statistic for all five runners, and yet they either did not or did not show it. This leaves them wide open to charges of bias.

Running other speedrunner's performance through their metrics is critical to ensure they are working properly. This is one reason why scientific studies usually have control groups, even though it requires twice the effort of not running a control.

(sec:p_value_misunderstood)=
### P-values are Not What You Think

The biggest flaw with the report is the reliance on p-values to generate its conclusions. I have summarized [many critiques of that statistic elsewhere](https://freethoughtblogs.com/reprobate/2015/12/17/index-post-p-values/), but two points are worth covering in detail here.

This is the definition of the p-value:{cite}`doi:10.7326/0003-4819-130-12-199906150-00008`

> If we assume the null hypothesis is true, and draw an infinite amount of data like what has been observed, what proportion of time would the calculated test metric be equal to or more extreme than the test metric predicted by the null hypothesis?

```{margin} Modus Tollens
* If A is true, B is true.
* B is false.
* Ergo, A is false.
```

On its surface, it's a very strange metric. Why are we basing our decision on data we have not and will never observe? What counts as "extreme"? The core logic relies on both [modus tollens](https://mathworld.wolfram.com/ModusTollens.html) and [the Central Limit Theorem](https://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_Probability/BS704_Probability12.html), which are usually correct but not always so.{cite}`cohen_earth_1994,vanderplas_frequentism_2014` 

```{margin} Central Limit Theorem
The means of sufficiently large samples taken from a larger population will follow a Gaussian distribution centred at the population mean.
```

P-values are not a probability of the null hypothesis being incorrect and cannot be treated as such, yet the MST report declares their final p-value to be an "upper bound on the chance" of Dream getting that lucky (pg. 22). The text which popularized the p-value encourages this mistake.

> The term Goodness of Fit has caused some to fall into the fallacy of believing that the higher the value of P the more satisfactorily is the hypothesis verified. Values over .999 have sometimes been reported which, if the hypothesis were true, would only occur once in a thousand trials. Generally such cases are demonstrably due to the use of inaccurate formula, but occasionally small values of $\chi^2$ beyond the expected range do occur, as in Ex. 4 with the colony numbers obtained in the plating method of bacterial counting. In these cases the hypothesis considered is as definitely disproved as if P had been .001. (pg. 96){cite}`fisher1934statistical`

Sir Ronald Fisher himself sometimes presents the p-value as the odds of the null hypothesis being true or false. Textbook authors carried the error forward.

> What Guilford teaches as the logic of hypothesis testing is Fisher's null hypothesis testing, deeply colored by “Bayesian” terms: Null hypothesis testing is about the probability that the null hypothesis is true. “If the result comes out one way, the hypothesis is probably correct, if it comes out another way, the hypothesis is probably wrong” (p. 156). Null hypothesis testing is said to give degrees of doubt such as “probable” or “very likely” a “more exact meaning” (p. 156). Its logic is explained via headings such as “Probability of hypotheses estimated from the normal curve” (p. 160).
> Guilford’s logic is not consistently Fisherian, nor does it consistently use “Bayesian” language of probabilities of hypotheses. It wavers back and forth and beyond.{cite}`gigerenzer1993superego`

Even experts can misinterpret it.

> In a recent survey of medical residents published in JAMA, 88% expressed fair to complete confidence in interpreting P values, yet only 62% of these could answer an elementary P-value interpretation question correctly. However, it is not just those statistics that testify to the difficulty in interpreting P values. In an exquisite irony, none of the answers offered for the P-value question was correct $\dots$ {cite}`GOODMAN2008135`

(sec:p_values_exaggerate)=
### P-values Exaggerate the Evidence
 
Multiple studies have looked into the predictive power of p-values by simulating experiments.{cite}`hubbard_why_2008,colquhoun2014investigation,halsey_fickle_2015` These should be taken with a grain of salt, as many of them argue p-values exaggerate the evidence relative to Bayesian methods. If you believe hypotheses can only be true or false, and cannot be assigned probability values, then you believe Bayesian methods are invalid and thus cannot be used as a reference. Not all of these simulation studies make the same mistake, though.

> In this article, I investigate p-values in relation to replication. My conclusion is that, if you repeat an experiment, you are likely to obtain a p-value quite different from the p in your original experiment. The p-value is actually a very unreliable measure, and it varies dramatically over replications, even with large sample sizes. Therefore, any p-value gives only very vague information about what is likely to happen on replication, and any single p-value could easily have been quite different, simply because of sampling variability.{cite}`doi:10.1111/j.1745-6924.2008.00079.x`

The evidence is strong enough that some researchers have proposed lowering the default p-value cut-off of 0.05.{cite}`Johnson19313` The theory is that rather than asking scientists to abandon the use of p-values, it is simpler to lower the threshold for significance and thus increase the amount of evidence required to reach that bar. Some fields of science have already made that transition, for instance particle physics and genomics research often require $p < 0.001$ or even $p < 0.0000003$.{cite}`lyons_discovering_2013,Storey9440` If p-values exaggerate the evidence against the null hypothesis, and the null hypothesis is that Dream's drop rate was unmodified, then by using p-values the MST report is exaggerating the evidence against Dream. This alone makes another report worthwhile.

I have other complaints about the MST report, but there's significant overlap between them and what's in the Photoexitation report.

(sec:pe_report)=
## Photoexcitation

The PE report offers a few good critiques. It argues that since Minecraft speedrunners almost always stop after they've earned $k$ items, instead of stopping after $n$ attempts to earn those items, the resulting $k$ and $n$ do not follow the binomial distribution. The MST report does not consider this argument in the context of items picked up, though it does consider it in the context of when a speedrunner stops playing.

The PE report's decision to use Bayesian statistics was correct, as in my opinion it copes better with small sample sizes than frequentist methods such as the p-value. It also used simulations to examine the relevant mechanics of Minecraft, a wise choice that makes it easier to test different possible outcomes in a controlled environment.

(sec:nbinom_overuse)=
### Overuse of the Negative Binomial

```{margin} Minecraft Versions
Minecraft comes in several variations, and some variations make it easy to run arbitrary versions of the game. Each variation and version can have differences; for instance, Piglins delay for eight seconds on Bedrock, rather than six seconds on Java. Version 1.16.1 gave you a $\frac{20}{423}$ chance of an Ender pearl barter, while version 1.16.2 gave you a $\frac{10}{459}$ chance. This analysis assumes the Java variation, version 1.16.1, is being run.
```

Having said that, the simulation within the PE report has a blind spot. First, consider Blaze rods. In order to earn them in Minecraft, you must kill Blazes. While it is possible to kill multiple Blazes at once, the only way that's practical during a speedrun is to use the sweeping edge attack of a sword against one Blaze with multiple other near-death Blazes nearby. On top of the difficulty of achieving that feat, most Minecraft speedrunners never craft a sword. Axes do more damage per strike, are effectively a requirement to gather wood, and some speed running stategies never ask the player to attack groups. Nearly always, then, Minecraft runners kill one Blaze at a time, and thus can easily stop when they meet their quota.

A key part of a random-seed any-percent Minecraft 1.16 speedrun is earning Ender pearls via bartering with Piglins. Unlike Blaze rods, which drop instantly after a Blaze dies, Piglins only give the player an item six seconds after the player gave them a gold bar. This, combined with the low chance of earning Ender pearls via a barter, creates a major time barrier for any speedrunner. Fortunately for the player, they don't have to manually hand over every gold bar and can instead drop a stack of them at the feet of the Piglin.

Runners can speed up this process one of two ways. For their 14 minute 39 second speed run, Couriway bartered [with a half-dozen Piglins simultaneously](https://youtu.be/0auJTuzm_Xc?t=404) and waited until they got enough Ender pearls. By bartering with so many Piglins, though, they no longer had strict control over when to stop and thus we'd expect their barter stats to be more Binomial than Negative Binomial.

Another approach is to multitask. For their 15 minute 51 second speedrun, Dowsky trapped a Piglin in a pit, tossed gold bars into it, and while the Piglin was bartering [ran off to kill Blazes](https://youtu.be/0auJTuzm_Xc?t=404). If the Blaze spawner is far enough away, the player won't be able to see when Ender pearls drop and thus won't be able to stop bartering once their quota is met. Again, these barters would be better modelled by a Binomial than a Negative Binomial.

The simulation code present on page 17 of the PE report only models bartering with a single Piglin that the player can monitor closely. That would be perfectly fine if they could show Dream used that technique exclusively when bartering with Piglins, but the report makes no such effort.

(sec:minecraft_misunderstandings)=
### Misunderstanding Minecraft

The PE report demonstrates other misunderstandings about how Minecraft is played.

> If you consider every Minecraft player, then a ”perfect” ender pearl and blaze drop record (2/2 ender pearl barters and 7/7 blaze rod drops) occurs multiple times per hour, since this has a 1 in 60000 odds and Minecraft is played many millions of times a day. Considering all Minecraft worlds ever played and the multitude of ways in which luck plays a role, even one in a trillion events happen daily. (pg. 5)

I am a Minecraft player. While I haven't tracked my Ender pearl barter stats, I can state with confidence that of the zero attempts I'm made to earn Blaze rods, zero have been successful. This is because I have no interest in reaching "The End" at the moment, nor have I had the inclination to do so in the six months or so I've been playing this game. If I do get that interest, I'm playing on a private server with other people who have long since tracked down a Stronghold on our shared map and set up a minecart route to it. In practice, gathering the materials to make Eyes of Ender is something most Minecraft players rarely do, and they rarely attempt it more than once the entire time they play Minecraft. Only a very small fraction of the Minecraft community attempts to speedrun the game, and only those players routinely hunt for Ender pearls and Blaze rods. One in a trillion events can happen daily, but only if about a trillion attempts are made at those events per day.

This lack of knowledge is understandable, given the author does not appear to be a Minecraft player. Nonetheless, the more you know about a topic, the less likely your analysis of that topic will rest on false premises.

(sec:no_real_world)=
### Lack of a Comparison to Real World Data

This premise leads the PE report to forgo comparisons to other speedrunners.

> Comparison to other runners is not necessary to establish that Dream had very low probability runs. Instead this comparison is more relevant to the interpretation of these low probabilities. For example, it reduces the plausibility that the low probabilities were due to some universal glitch that affects all speedrunners. As the reader is assessing the evidence, the low probability of Dream’s runs and that Dream performed much better than other speedrunners should not be considered as independent pieces of evidence as they both are consequences of the same thing. Any lucky speedrunner chosen because they look lucky will look lucky when compared to other speedrunner
streams that were chosen randomly. (pg. 15)

At the core of statistics is the idea of [a reference class](https://en.wikipedia.org/wiki/Reference_class_problem). By invoking every Minecraft player, the PE report is stating that Dream's performance should be compared to them, or in other words that they are the appropriate class of entities to use as a reference. Here, though, the report argues that Dream's performance should not be compared to that of other top speed runners, because it is too dissimilar; rather than compare Dream to speed runners of similar skill, the PE report states the MST report picked random speed runners.

```{margin} How the MST Report chose their speedrunners.
> However, upon further research, Dream’s observed drop rates are substantially greater than those of other top-level RSG runners—including, Illumina, Benex, Sizzler, and Vadikus. (pg. 3)
```

Setting aside the argument that this is the reverse of reality, it is notable that the report makes no attempt to compare Dream's performance to any real-world reference class. If a perfect Blaze rod and Ender pearl bartering session is indeed a common occurrence, it should be easy to demonstrate that by pointing to a few examples of ordinary Minecraft players achieving those feats. Even if they are rarely recorded, discussion of such events must appear in comment sections or Discord channel messages, and we would expect it to be common knowledge among players of Minecraft.

Conversely, even if other speedrunners are an inappropriate reference class, the comparison would help validate their methodology. The author of this report had the data to do this, thanks to the MST report, and passing it through their simulation was as easy as editing two lines of code, so there was no lack of means or opportunity.

(sec:missing_context)=
### Missing Context

> In this document, I don’t have time to discuss the long-term debate between these different statistical
paradigms and when they should be applied. The short version is that another way of investigating whether the probabilities were modified is to try to determine what probabilities were used. (pg. 5)

By skipping the details, the PE report leaves out an important consequence of using Bayesian statistics. You can simplify Bayesian stats down to

> Given the data before me, what credence do I place on a hypothesis relative to some reference?

"Credence" can be thought of in terms of "belief points:" when I say I give 100:1 odds that Joe Biden will become President of the United States, I am saying that for every one belief point I give to the hypothesis "Joe Biden will not become President" I also give one hundred towards "Joe Biden will become president."
```{margin} Betting Odds
The comparison to betting odds is no accident, the study of statistics began with people trying to figure out either how to cheat at gambling or how to detect said cheating.{cite}`doi:https://doi.org/10.1002/0471667196.ess0845.pub3`
```

Mathematically, "credence" is the output of a [likelihood function](https://en.wikipedia.org/wiki/Likelihood_function). Likelihoods obey all the same rules as probabilities, save one: while probabilities are bounded to stay between 0 and 1, likelihoods only have a lower bound of zero. The inputs to a likelihood function are the data we observe, as well as all parameters of a model capturing our belief in that data. These parameters form a multi-dimensional parameter space. All hypotheses we can make about the data live within that space. These may be point hypotheses ("Dream's Blaze rod drop rate was precisely 0.509583957"), or composite hypotheses that are a weighted subset of all possible point hypotheses ("Dream's Blaze rod drop rate ranged between 0.431 and 0.569"). If the parameter space is discrete ("which side of a six-sided die will appear"), that weighted subset is calculated by summation over all possible parameters; if it is continuous ("Dream's Blaze rod drop rate"), it is calculated by integration over all parameters.

Unfortunately, calculating those integrals directly is impractical for all but the easiest problems. Frustrated statisticians and mathematicians began looking for shortcuts and alternatives, and a number of them were codified into what we now call frequentist statistics. The p-value is one such example: it also relies on likelihood functions, but it assumes the amount of data collected is practically infinite. This allows the problem to be transformed into a simpler one that's much easier to integrate.

This has an important side-effect: the flip-side of p-values exaggerating the evidence is that Bayesian metrics are relatively conservative when given the same evidence. if the default hypothesis is some variation of "Dream played fairly", then Bayesian statistics will be slower to give up on that than frequentist statistics. To put that in bold:

**Bayesian statistics is intrinsically more likely to conclude Dream played fairly, relative to frequentist statistics, given the same evidence.** Whether this is a problem or not depends on how sound you think the premises are behind each system. It's not unfair to invoke p-values if the "fairer" analysis is Bayesian and you reject that system outright. By the same token, a Bayesian analysis of Dream's performance is not biased towards him relative to one that uses p-values, provided you think p-values should not be applied to this problem.

(sec:biased_priors)=
### Biased Priors

You can think of a prior as a likelihood function supplied with zero evidence. It is convenient to define your likelihood function as how your credence changes given one atom of data, because then you can chain together arbitrary numbers of likelihood functions to handle arbitrary amounts of evidence. That chain has to be anchored somewhere, though, so you also need to define the likelihood of a specific choice of parameters absent any evidence. The opposite end of that chain is the posterior, or your credence after accounting for all the evidence.

Some priors are hypothesis-specific. "What are the odds that Dream cheated?" depends on "what are the odds of a speedrunner cheating?". If cheating is common in the speedrunning community, then the odds of a specific speedrunner cheating are high, absent any evidence that could change the odds. Likewise, the odds of a specific speedrunner cheating are low if speedrunners in general rarely cheat, again absent any evidence leading us to one conclusion or another.

This shades our view of the evidence: if we assume cheating is rare, our credence that a specific player cheated remains quite low after seeing one atom of evidence that suggests cheating. Importantly, that amount of credence is less than if we had instead assumed cheating is common. Relative to our prior credence of rare cheating, though, that one atom has shifted our credence more than it would have had we assumed cheating was common. In short, new evidence consistent with what you expected doesn't change your credence much; new evidence that isn't, does.

Some priors apply to all relevant hypotheses. A cheater is much less likely to set their Ender pearl drop rate to 100\% than they are to set it to 25\%. This is also true for a fair player. These two hypotheses are not perfect inverses, but they both share an assumption that extremely good luck is unlikely.

> For those savvy in Bayesian statistics, I use a flat/uniform/tophat prior on the probability boost from 1 to 5 and confirmed that these limits do not significantly affect the interpretation. In this case, this just means calculating the likelihoods on a grid from 1 to 5 and, since the prior is flat, these are equivalent to the relative posterior probabilities. This prior does not include any corrections for biases or any opinion that Dream modified his probabilities. (pg 10)

The prior used in the PE report gives as much credence to Dream earning 20 pearls after 423 barter as it does him earning 100. This is going to exaggerate the likelihood that Dream cheated in the resulting analysis.

(sec:mst_response)=
## Response to the Photoexcitation Report

The Minecraft Speedrunning Team has [responded to the PE report](https://mcspeedrun.com/dream/rebuttal.pdf). The best critique it makes mirrors one of mine.

> Moreover, their estimation of 300 livestreamed runs per day over the past year is highly implausible. Many runs are not livestreamed, and the estimation is based on current numbers, even though Minecraft speedrunning has grown massively in the recent months. 

> At the time of Dream’s run, there were 487 runners who had times in 1.16 - far under 1000 - and the vast majority of these were unpopular or did not stream. Selection bias could only be induced from observed runners, so speedrunners who had no significant viewership watching their attempts should not be included. (pg. 3)

The remaining critiques do not apply to the ones I have of the PE report, and do not need to be discussed here.
