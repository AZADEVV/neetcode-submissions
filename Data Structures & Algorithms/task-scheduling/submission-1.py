class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_count = {}

        for i in range(len(tasks)):
            task_count[tasks[i]] = task_count.get(tasks[i], 0) + 1

        maxHeap = [-cnt for cnt in task_count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, n + time])
                    
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

            

        print(maxHeap)