# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

#using map to reduce the access to O(1)
class Tweet:
        def __init__(self,id,time):
            self.id = id
            self.time = time
            
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = {}
        self.followers = {}
        self.id = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.followers:
            self.followers[userId] = {}
            self.followers[userId][userId] = True
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append(Tweet(tweetId,self.id))
        self.id += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.followers:
            self.followers[followerId] = {}
            self.followers[followerId][followerId] = True
        self.followers[followerId][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.followers:
            return;
        if followeeId not in self.followers[followerId]:
            return;
        del self.followers[followerId][followeeId]


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)