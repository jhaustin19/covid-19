# Executive Summary

- This was a group object focused on analyzing trends between social media use and the spread of COVID-19
- We went into it without a great idea of what we were attempting to do, and instead were merely interested in "seeing what we could find"
- Without a clear focus, the project wasn't able to deliver much
- With that being said, we were able to procure a large amount of data
- The data was used to build a classifier capable of determining whether a document came from Reddit or Twitter with a high degree of accuracy

# Data Acquisition & Cleaning

As we needed social media data, the obvious first place to start was Reddit, since I could just use the series of function I designed for [this project](https://github.com/jhaustin19/reddit-nlp). Using these functions, I was able to grab every single post ever made (up to that point) from a collection of subreddits dedicated to discussing COVID-19. The data didn't need much cleaning, but there were a large amount of extraneous columns that needed to be removed.

Wishing to have something to compare the Reddit data with, we looked to Twitter. Getting Twitter data was as simple as using [this library](https://github.com/Mottl/GetOldTweets3). Here, the major issue with cleaning was that many of the tweets weren't in English and needed to be removed.

The New York Times maintains a GitHub repository with updated case/death counts for the whole United States as well as individual states ([here](https://github.com/nytimes/covid-19-data)). The data was remarkably clean, so not much needed to be done with it.

# Modeling

As mentioned, we went into this project without a great idea of what we were trying to accomplish. With a large amount of data in hand, however, we decided that as budding data scientists it was prudent to build a model. Three separate classifiers were built to determine if a document came from Reddit or Twitter. The classifiers performed incredibly well, but upon closer inspection, it turned out they were doing so for relatively trivial reasons. One of these is that a large amount of Tweets contained hyperlinks (with `http` or `https` in them) that were a dead giveaway to the origin of a document.

# Conclusions

- It's probably not good to go into a project without a clear idea of what you're attempting to do
- We built a classifier capable of making predictions with a high degree of accuracy, but it's very hard to think of a potential application for the model