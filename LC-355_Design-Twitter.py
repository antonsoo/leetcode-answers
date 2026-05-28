# Problem: 355. Design Twitter
# Solution: https://leetcode.com/problems/design-twitter/solutions/7882236/python3-detailed-optimal-max-heap-approa-y8bo/

import heapq

class Twitter:
    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.timer += 1
        self.tweets[userId].append((tweetId, self.timer))


    def getNewsFeed(self, userId: int) -> list[int]:
        sources = list(self.followers.get(userId, set())) + [userId]
        heap = []
        res = []
        for follower in sources:
            if follower in self.tweets:
                tweet_id, time_stamp  = self.tweets[follower][-1]
                heapq.heappush(heap, (-time_stamp, tweet_id, follower, len(self.tweets[follower]) - 1))

        while heap and len(res) < 10:
            time, tweet_id, user_id, index = heapq.heappop(heap)
            res.append(tweet_id)
            index -= 1
            if index >= 0:
                new_tweet_id, new_time_stamp = self.tweets[user_id][index]
                heapq.heappush(heap, (-new_time_stamp, new_tweet_id, user_id, index))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            return
        self.followers[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
