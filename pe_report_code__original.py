#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
import matplotlib.pyplot as plt
from scipy.stats import binom
from matplotlib.lines import Line2D
import copy

# number of gold barters needed to get numneeded ender pearls
# assuming that after numneeded (10) ender pearls are obtained, trading stops
# uses an algorithm that includes a random number of ender pearls obtained per trade
# (though this does not matter for 10 ender pearls 
# since only 2 trades are needed for this goal

# to test the hypothesis that the probability of ender pearls was somehow boosted
# calculate the number of gold barters needed for a variety of ender pearl
# probabilities from the nominal 20/423 (probpearlboost=1) up to 100/423
# (probpearlboost=5), representing a uniform prior of 1-5 for this boost probability

# note, this simulation can take several minutes

prob_pearls=20.0/423.0
num_prob_pearl_boost=41
prob_pearl_boost_arr=numpy.linspace(1,5,num_prob_pearl_boost)
num_monte_carlo=1000000 # number of monte carlo simulations
num_pearls_needed=10

# stores the number of gold needed in each simulation for each boost
gold_needed_arr=numpy.zeros([num_monte_carlo,num_prob_pearl_boost])

# stores the number of successful pearl trades needed
trades_needed_arr=numpy.zeros([num_monte_carlo,num_prob_pearl_boost])

# loop over each boost and each simulation
for iboost in range(num_prob_pearl_boost):
    for imc in range(num_monte_carlo):
        # reset the simulation
        current_pearls=0
        current_gold=0
        current_trades=0
        # trade until the number of pearls obtained
        while current_pearls < num_pearls_needed:
            # do one gold barter
            current_gold=current_gold+41
            # check if this barter leads to an ender pearl trade
            # using boosted probability
            if numpy.random.uniform()<prob_pearls*prob_pearl_boost_arr[iboost]:
                current_trades=current_trades+1
                # give between 4-8 pearls
                # approximating the observed distribution
                current_pearls=current_pearls+numpy.round(4*numpy.random.uniform()+0.5) + 3
                gold_needed_arr[imc,iboost]=current_gold
                trades_needed_arr[imc,iboost]=current_trades

# now take the simulation results and turn them into a probability of
# getting 10 ender pearls given a specific number of gold bartered and
# a specific probability boost

max_gold=500 # maximum number of gold barters in the array
prob_this_gold_arr=numpy. zeros([max_gold,num_prob_pearl_boost])
for igrid in range(num_prob_pearl_boost):
    for this_gold in range(max_gold):
        prob_this_gold_arr[this_gold,igrid]=numpy.sum(gold_needed_arr[:,igrid]==this_gold)/num_monte_carlo
        
# data from Dream trades on 11 streams of interest

# see MST Report Appendix A and http://bombch.us/DPPU
dream_trades= [22,5,24,18,4,1,7,12,26 ,8,5,20,2,13,10,10 ,21,20,10,3,
18 ,3,27,4,13,5,35,70,11,7,24,34,7,15,10,1,40,50,5]
dream_successes =[3,2,2 ,2 ,0,1,2,5 ,38 ,2,2,2 ,0,1 ,2 ,2 ,2 ,2 ,2,1,
2 ,2, 2,0, 0,1, 1, 2, 0,1, 0, 0,0, 0, 0,0, 3, 2,0]
dream_goalof12= [1 ,0,0 ,1, 0,0,0,0 ,1, 1,0,0, 0,0, 1, 1, 1, 1, 1, 0,
1 ,0, 1,0, 0,0, 0, 0, 0,0, 0, 0,0, 0, 0,0, 1, 0,0]
dream_goalof10= [1, 1,1, 1, 0,0,1,1, 1, 1,1,1, 0,0, 1, 1, 1, 1, 1, 0,
1, 1, 1,0, 0,0, 0, 1, 0,0, 0, 0,0, 0, 0,0, 1, 1,0]

# data from Dream trades on 6 streams of interest
# see MST Report Appendix A and http://bombch.us/DPPU

#dream_trades= [22,5,24,18,4,1,7,12,26,8,5,20,2,138,10,10,21,20,10,8,18,3]
#dream_successes=[(3 ,2,2 ,2 ,0,1,2,5 ,8 ,2,2,2 ,0,1 ,2 ,2 ,2 ,2 ,2 ,1,2 ,2]
#dream_goalof12= [1 ,0,0 ,1, 0,0,0,0 ,1, 1,0,0, 0,0, 1, 1, 1, 1, 1, 0,1 ,0/]
#dream_goalof10= [1, 1,1, 1, 0,0,1,1, 1, 1,1,1, 0,0, 1, 1, 1, 1, 1, 0,1, 1[

# probability calculation for each individual trade
# “goalof10” trades use Barter Stopping Probability
# other trades use Binominal Probability

this_trade_prob=numpy.zeros([len(dream_trades),num_prob_pearl_boost])
                  
for iboost in range(num_prob_pearl_boost):
    for this_trade in range(len(dream_trades)):

        if dream_goalof12[this_trade] == 1:
            this_trade_prob[this_trade,iboost]=prob_this_gold_arr[dream_trades[this_trade],iboost]
        else:

            # probability when trades = successes is prob’successes
            if dream_trades [this_trade]==dream_successes[this_trade]:
                this_trade_prob[this_trade,iboost]=(prob_pearls*prob_pearl_boost_arr[iboost])**(dream_successes[this_trade])
            else:
                this_trade_prob[this_trade,iboost]=binom.pmf(dream_successes[this_trade],dream_trades[this_trade], prob_pearls*prob_pearl_boost_arr[iboost])
                  
# allow for ignoring the last barter to correct for optional stopping
ignore_last_barter = True
if ignore_last_barter:
    last_barter_correction=-1
else:
    last_barter_correction=0

total_prob=numpy.product(this_trade_prob[0:len(this_trade_prob)+last_barter_correction,:] ,axis=0)
print (total_prob/numpy.sum(total_prob))
                


# In[ ]:




