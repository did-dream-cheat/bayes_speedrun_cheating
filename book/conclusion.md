# Conclusion

I will refrain from stating conclusively that Dream boosted his Blaze rod drop and Ender pearl barter rate. To explain why, it is worth discussing stopping rules.

(sec:stopping_rules)=
## Stopping Rules

Both the MST and PE reports invoke stopping rules, though in a way that is not congruent with how they are used within the scientific community.

```{margin} P-values 
As I mentioned in {ref}`sec:p_value_misunderstood`, even professionals misunderstand p-values on a regular basis.
```

> Suppose that a researcher is testing whether one variable influences another or is comparing two treatments or effect sizes. Suppose also that the researcher is primarily interested in whether there is an effect (or difference) and, if so, the direction of the effect. Finally, suppose that the researcher wants to set alpha at .05, which is to say, have a 5% probability of rejecting the null hypothesis of no effect, if it is true.

> Using the fixed-sample stopping rule, the researcher would determine the number of subjects to be tested prior to performing the study. However, there is another type of stopping rule, called sequential stopping rules, which was first proposed by Wald in 1947. In a sequential stopping rule, the outcome ofthe statistical test could lead to testing more subjects. Thus, the number of subjects to be tested is not fixed in advance.{cite}`frick_better_1998`

> According to Wainer (2000) an adaptive test can be considered complete after a predetermined number of items have been administered, when a predetermined level of measurement precision has been reached, or when a predetermined length of time has elapsed. The two most commonly used methods for determining when a computerized adaptive test is complete are the fixed length and variable length stopping rules.

> Under a fixed length stopping rule, an adaptive test is terminated when a predetermined number of items have been administered. Accordingly, all examinees are administered the same number of items, regardless of the degree of measurement precision achieved upon termination of the test. \[...\]

> In contrast, variable length stopping rules typically seek to achieve a certain degree of measurement precision for all examinees, even when doing so means that some examinees are given more items than others. Two types of variable length stopping rules have been used (Dodd, Koch, & De Ayala, 1993). These are the standard error (SE) stopping rule and the minimum information stopping rule. Of these, the most commonly used has been the SE stopping rule, which terminates an adaptive test when a predetermined standard error has been reached for the most recent examinee trait estimate (Boyd, Dodd, & Choi, 2010).{cite}`choi_new_2010`

> One criticism of rules like O'Brien and Fleming is their rigidity in requiring a fixed maximum number of preplanned interim analyses. Greater flexibility is possible with the Peto-Haybittle rule, which simply specifies a fixed p value (often $p<0-001$) for stopping early. For example, the European myocardial infarction amiodarone trial (EMIAT) is an ongoing study of 1500 patients at high risk after myocardial infarction comparing amiodarone (an antiarrhythmic drug) with placebo. Two year mortality is the primary end point, and the stopping guideline for efficacy is $p < 0.001$ in favour of amiodarone.{cite}`pocock_when_1992`

A clear stopping rule is necessary when the number of datapoints you could look at is practically infinite; we could survey every single person in the United States to determine their political views, but it is more feasible to pick a large enough sample of them to achieve a certain statistical accuracy. Alternatively, we could flip between data gathering and analysis until our target accuracy or statistical measure is reached, but this risks coming to a premature stop due to statistical fluctuations; had we just analyzed X more datapoints, our test statistic would switch from "statistically significant" to "not statistically significant" and our declaration of significance would be premature.

Dream has not completed a practically infinite number of random-seed any-percent Minecraft 1.16 runs, however. If our hypothesis is that Dream boosted his drop/barter rate since returning to that speedrun category, then the entire dataset consists of thirty-three runs where Blazes were killed for Blaze rods, and twenty-two runs where Ender pearls were bartered for, spread across six streaming sessions. There is no more data to be collected, and the data that is present is nowhere near large enough to pose an analytic challenge. If those datapoints were insufficient to establish the hypothesis, then a well-designed statistical test metric will conclude the evidence is inconclusive. If the fluctuations could be due to chance, then a well-designed metric will take that into account. The data cannot be cherry-picked to artificially boost the metric, as the MST report examines every applicable cherry.

The imposition of a binary decision threshold on continuous test statistics, and the resulting necessity of stopping rules, has led some researchers to call for the abandonment of statistical significance entirely.{cite}`doi:10.1080/00031305.2018.1527253` Rather than have the researcher or publisher check if p-values or Bayes factors cross a certain threshold, they propose researchers and publishers take a holistic approach that also factors in "related prior evidence, plausibility of mechanism, study design and data quality, real world costs and benefits," and "novelty of finding" among other things.

As an outsider to the Minecraft speedrunning community, I do not have full knowledge of prior evidence. I do not have a good understanding of the costs or benefits of removing Dream's speed-running records, and should I make the wrong decision I will not pay the consequences. The best thing I can do is to instead lay out my full reasoning as clearly I can. If the community accepts the premises behind my arguements and can find few flaws in how I link them together, they are in a much better position to translate the continuous Bayes factor into a binary decision.
