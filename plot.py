#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Konstantin (k0nze) Lübeck"
__copyright__   = "Copyright 2021"

__license__     = "BSD 3-Clause License"
__version__     = "0.1"
__contact__     = {
                    "Twitch": "https://twitch.tv/k0nze",
                    "Youtube": "https://youtube.com/k0nze",
                    "Patreon": "https://patreon/k0nze",
                    "Twitter": "https://twitter.com/k0nze_gg",
                    "Instagram": "https://instagram.com/k0nze.gg",
                    "Discord": "https://discord.k0nze.gg",
                }


import matplotlib.pyplot as plt
import numpy as np

# enter prices for bits and subs
bit_emotes_1_cost = 13.31
bit_emotes_2_cost = 67.51
bit_emotes_3_cost = 132.08

tier_1_cost = 4.99
tier_2_cost = 9.99
tier_3_cost = 24.99

# enter max months to plot (has to start with 1)
months = np.arange(1, 24)

bit_emotes_1_costs = np.full(months.shape, 13.31)
bit_emotes_2_costs = np.full(months.shape, 67.51)
bit_emotes_3_costs = np.full(months.shape, 132.08)

tier_1_costs = np.zeros(months.shape)
tier_2_costs = np.zeros(months.shape)
tier_3_costs = np.zeros(months.shape)

for month in months:
    tier_1_costs[month-1] = tier_1_cost*month
    tier_2_costs[month-1] = tier_2_cost*month
    tier_3_costs[month-1] = tier_3_cost*month

# plot
plt.plot(months, bit_emotes_1_costs)
plt.plot(months, bit_emotes_2_costs)
plt.plot(months, bit_emotes_3_costs)

plt.plot(months, tier_1_costs)
plt.plot(months, tier_2_costs)
plt.plot(months, tier_3_costs)

plt.ylabel('Accumulated Cost [€]')
plt.xlabel('Months')

plt.legend(("1K bits emote", "5K bits emote", "10K bits emote", "Tier 1 sub emotes", "Tier 2 sub emotes", "Tier 3 sub emotes"))

plt.show()
