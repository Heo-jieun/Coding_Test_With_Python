# N, K 입력받기
N, K  = map(int, input().split())

# A, B 배열 입력 받기
A = []
A += list(map(int, input().split()))
B = []
B += list(map(int, input().split()))
    
# 퀵 정렬
def quick(array, start, end) :
    # 원소가 한개이면 종료
    if start >= end: 
        return 
    pivot = start
    left = start+1
    right = end

    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(right < left):   
            array[pivot], array[right] = array[right], array[pivot]
        else : 
            array[left], array[right] = array[right], array[left]
    quick(array, start, right-1 )
    quick(array, right+1, end )


quick(A, 0, len(A)-1)
quick(B, 0, len(B)-1)

A = A[K:] + B[-K:]
sum = 0
for i in range(N):
    sum += A[i]
print(sum)