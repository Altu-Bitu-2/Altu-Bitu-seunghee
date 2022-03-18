#백준 2108번

import sys #sys를 임포트한다.
from collections import Counter #collections 모듈의 Counter 클래스를 임포트한다. 
n = int(sys.stdin.readline()) #입력받을 수의 개수를 정한다.
li = [] #수를 저장할 리스트를 만든다.
for _ in range(n): #n번동안 for문을 돌린다.
    li.append(int(sys.stdin.readline())) #n번동안 숫자를 입력 받은 것을 리스트에 저장한다.
 
# 산술평균 - 다 더해서 / n
print(round(sum(li)/n)) #sum함수와 round함수를 이용해서 산술평균 구하기
 
# 중앙값 - 오름차순 -> 중간값
li.sort() #리스트를 오름차순 정렬한다.
print(li[n//2]) #n을 2로 나눈후 중앙값을 프린트한다.
 
# 최빈값 - 빈출
cnt_li = Counter(li).most_common() 
#Counter 사용하여 요소의 개수를 센다. most_common()은 빈도가 높은 순으로 리스트 안의 튜플형태로 반환해준다.
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]: #최빈값 2개 이상인 경우 
    print(cnt_li[1][0]) #두번째 키값을 출력
else:
    print(cnt_li[0][0]) #그렇지 않은 경우 첫번째 키값 출력
 
# 범위 - 최댓값-최솟값
print(max(li)-min(li)) #최댓값 함수와 최솟값 함수 이용한다.

