### Basic Dijkstra algorithm

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # directed graph
        dic = collections.defaultdict(dict)
        # Initialize the second order dic to save the flights
        for a, b, p in flights:
            dic[a][b] = p
        pq = [(0, src, K + 1)]
        
        while pq:
            price, i, stop = heapq.heappop(pq)
            if i == dst:
                return price
            if stop > 0:
                for j in dic[i]:
                    heapq.heappush(pq, (price + dic[i][j], j, stop - 1))
        
        return -1
