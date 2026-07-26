from collections import deque
import heapq


class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets: dict[int, deque[tuple]] = dict()
        self.following: dict[int, set[int]] = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = deque(maxlen=10)

        self.tweets[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1          

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            self.following[userId] = set()
        self.following[userId].add(userId)

        last_tweets = []
        for author in self.following[userId]:
            if author not in self.tweets:
                continue

            tweet_num = len(self.tweets[author]) - 1
            timestamp, tweet_id = self.tweets[author][tweet_num]
            last_tweets.append((timestamp, tweet_id, author, tweet_num))

        heapq.heapify(last_tweets)
        result = []
        while last_tweets and len(result) < 10:
            timestamp, tweet_id, author, tweet_num = heapq.heappop(last_tweets)
            result.append(tweet_id)
            if tweet_num > 0:
                new_tweet_num = tweet_num - 1
                new_timestamp, new_tweet_id = self.tweets[author][new_tweet_num]

                heapq.heappush(last_tweets, (new_timestamp, new_tweet_id, author, new_tweet_num))

        return result
            
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
