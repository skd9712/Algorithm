from collections import deque

# 큐 구현을 위해 deque 사용
queue = deque()
# 5삽입 - 2삽입 - 3삽입 - 7삽입 - 삭제 - 1삽입 - 4삽입 - 삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # queue출력
queue.reverse() # 역순으로
print(queue) 
