from heapq import heappush, heappop

class Twitter:

    def __init__(self):
        self.ut = {}
        self.length = 0
        self.fol = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not self.ut.get(userId):
            self.ut[userId] = [(self.length, tweetId)]
        else:
            self.ut[userId].append((self.length, tweetId))
        self.length += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        10 most recent tweets from followed onces
        """
        follows = [userId] + list(self.fol.get(userId, []))
        heap = []
        for f in follows:
            for t in self.ut.get(f, []):
                if len(heap) < 10:
                    heappush(heap, t)
                elif t[0] > heap[0][0]:
                    heappop(heap)
                    heappush(heap, t)
        res = []
        while heap:
            res.append(heappop(heap)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        followerId ----follow---> followeeId
        """
        if self.fol.get(followerId):
            self.fol[followerId].add(followeeId)
        else:
            self.fol[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        followerId ----unfollow---> followeeId
        """
        if self.fol.get(followerId):
            self.fol[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)