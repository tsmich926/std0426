import heapq


# heappush

heap = []
heapq.heappush(heap, 50)
print(heap)
# 결과:[50]

heapq.heappush(heap, 10)
print(heap)
# 결과:[10,50] 

heapq.heappush(heap, 5)
print(heap)
# 결과:[5,50,10]


# heapify
# 생성해둔 리스트가 있으면 heapify를 이용해 힙자료형으로 변환

heap2 = [50 ,10, 20]
heapq.heapify(heap2)

print(heap2)
# 결과: [10,50,20]


# heappop
# 가장 작은 원소를 힙에서 제거 
result = heapq.heappop(heap2)
print(result)
# 결과: 10
print(heap2)
# 결과: [20,50]