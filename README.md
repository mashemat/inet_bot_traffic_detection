[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<p align="center">
<img src="./image/vul.png" width="250" height="180">
<p>

# In network bot traffic analysis

We conducted an analysis on several pre-existing datasets such as Twibot-20 [1], bot-net [2], Wikimedia API [3], Amazon [3], and Alibaba benchmark generator [4]. However, these datasets did not meet our criteria due to either lacking sufficient annotations or lacking essential query and user information. As a result, we conducted a thorough review, which encompassed an analysis
of the characteristics of the web requests [5], web traffic [6], workload [7], bot traffic [8], and network caches [9]. Then,
we formulated a set of guiding principles for the precise generation of a bot traffic dataset. The following are the key
principles we adhered to during the dataset creation process:

1- Search queries made by bots are often long search queries and tend to search for not so popular items in the e-commerce search engine [10]. 

2- User requests follow a Zipfian distribution [11]. This observation signifies that specific segments of the data experience
a higher volume of requests, a pattern that evolves over time.

3- The average time interval between consecutive requests made by bots is five times shorter than normal users [12].


