from twitmining.models import RelevantTweet


class Scorer:
    """
    This class will perform the scoring of tweet to identify the most relevant tweets
    """

    def __init__(self, keyword, df):
        self.tweets = df
        self.keyword = keyword
        self.relevant = list()

    def score_retweets(self):
        for index, tweet in self.tweets.iterrows():
            if tweet["is_retweeted"]:
                self.tweets.at[index, "score"] = int(tweet['score'] - 500)
    
    def score_occurrences(self):
        for index, tweet in self.tweets.iterrows():
            self.tweets.at[index, "score"] = int(tweet['score'] + tweet["keyword_occurrence"]*100)
            self.tweets.at[index, "score"] = int(tweet['score'] + tweet["hashtag_occurrence"]*100)

    def score_user(self):
        for index, tweet in self.tweets.iterrows():
            if 0 <= tweet["user_followers"] <= 1000:
                followers_score = 0
            elif 1000 <= tweet["user_followers"] <= 10000:
                followers_score = 200
            elif 100000 <= tweet["user_followers"] <= 100000:
                followers_score = 500
            else:
                followers_score = 1000
            self.tweets.at[index, "score"] = int(tweet['score'] + followers_score)
            if tweet["verified"]:
                self.tweets.at[index, "score"] = int(tweet['score'] + 200)
    
    def score_place(self):
        for index, tweet in self.tweets.iterrows():
            if tweet["location"]:
                self.tweets.at[index, "score"] = int(tweet['score'] + 500)

    def score_sharing(self):
        for index, tweet in self.tweets.iterrows():
            self.tweets.at[index, "score"] = int(tweet['score'] + tweet["favorite_count"])
            self.tweets.at[index, "score"] = int(tweet['score'] + tweet["retweet_count"])

    def score_tweets(self):
        """
        Score tweets and return the relevant list containing the most relevant tweets
        """

        self.score_occurrences()
        self.score_retweets()
        self.score_sharing()
        self.score_user()
        self.score_place()

        relevant = self.tweets.nlargest(10, "score")
        relevant_links = list()

        for index, tweet in relevant.iterrows():
            relevant_links.append(self.tweets.at[index, 'link'])
            RelevantTweet.objects.create(link=self.tweets.at[index, 'link'], text=self.tweets.at[index, 'text'])

        return relevant_links
