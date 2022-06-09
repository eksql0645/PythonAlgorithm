# import sys
# sys.stdin = open("input.txt", "rt")

n = input()
arr = map(int,input().split())  # n개의 수학점수가 한줄로 들어오기 때문에 띄어쓰기를 구분자로 나눈 후 int화 하여 arr에 요소롤 넣는다.

# 평균 구하기
avg = sum(arr)/len(arr)

# 평균 소수점 첫째자리 반올림하기
# round 함수를 사용해서 소수점 첫째 반올림도 가능하지만 파이썬의 round는 round-half-even이기 때문에 round-half-up을 하기 위해 코드를 직접 짠다.
avg = avg + 0.5  # 소수점 0.5 이상이면 반올림이 된다.
avg = int(avg)   # 소수점 0.5 미만이면 정수화하면서 반올림이 되지 않는다.

repNum = float('inf')   # 대표값을 큰 값으로 설정한다.

# 평균과 수학점수의 차이를 통해서 평균과 가까운 값 구하기
for idx, num in enumerate(arr):        # enumerate를 쓰면 idx(학생번호), num(수학점수) 둘 다 구할 수 있다.
  res = abs(avg-num)                   # 음수가 나오지 않게 절댓값으로 구한다.
  if repNum > res:                     # repNum가 res보다 크기 때문에 resNum가 res로 바뀐다.
    repNum = res
    score = num
    stuNum = idx+1                     # 학생번호가 1부터 시작하기 때문에 +1
  elif repNum = res:                   # 현재 배열요소와 평균과의 차이가 기존 배열요소와 평균과의 차이와 같다면
    if score < num:                    # 둘의 점수를 비교해서 현재 배열요소의 점수가 더 크면  / 이 조건에서 같다가 없기 때문에 같은 점수일 경우 학생번호가 앞선게 답이 된다.
      score = num                      # score에 현재 배열요소 점수를 할당한다.
      stuNum = idx+1                   # 학생번호에도 현재 배열요소의 idx+1을 할당한다.
      
print(avg, stuNum)
