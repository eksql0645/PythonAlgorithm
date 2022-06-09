arr = [5, 3, 7, 9, 2, 5, 2, 6]

# 무한대를 사용한 방법
arrMin = float('inf')     # 파이썬에서 가장 큰 무한대 값(infinity)으로 초기화한다.
for i in range(len(arr)): # i는 0부터 7까지 8번 반복한다.(인덱스번호라고 생각하기)
    print(arr[i])         # print하고 자동 줄바꿈이 된다.
    if arr[i] < arrMin:   # arr[i]가 arrMin보다 작으면
        arrMin = arr[i]   # arrMin에 arr[i]를 할당한다.
print(arrMin)

# 무한값을 초기화하고 for문 다르게 하는 경우: x는 arr의 0번값부터 적용된다.
for x in arr: 
    if x < arrMin:   
        arrMin = x

# 첫번째 값으로 초기화
arrMin = arr[0]
for i in range(1,len(arr)) # 인덱스 번호 1부터 for문 돌게 함
    if arr[i] < arrMin:   
        arrMin = arr[i]
print(arrMin)
