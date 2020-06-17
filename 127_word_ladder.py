class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS
        # Tricky: how to know there is only one bit difference
        # Approach1: Naive BFS 
        # TLE
        '''
        from collections import deque
        queue = deque()
        queue.append(beginWord)
        seen = set()
        seen.add(beginWord)
        dic = {}
        for word in wordList:
            if word not in dic:
                dic[word] = True
        count = 0
        while queue:
            count += 1
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                for i in range(len(wordList)):
                    for letter in "abcdefghijklmnopqrstuvwxyz":
                        if cur == endWord:
                            return count
                        if cur[:i] + letter + cur[i + 1:] in dic and cur[:i] + letter + cur[i + 1:] not in seen:
                            seen.add(cur[:i] + letter + cur[i + 1:])
                            queue.append(cur[:i] + letter + cur[i + 1:])
        return 0
        '''
