
# 게시판 페이징하기

'''
아래 값들을 입력으로 받아야 한다.
1. 게시물의 총 개수
2. 한 페이지에 보여 줄 게시물의 수

아래 값을 출력으로 뱉어야 한다.
1. 총 페이지 수

- 함수 이름 : get_total_page
'''

# 페이지 수 계산 함수
def get_total_page(m, n):
    return m // n + 1   # m을 n으로 나눈 몫에 1을 더하여 return 한다.

print(get_total_page(5, 10))    # 1 페이지
print(get_total_page(15, 10))   # 2 페이지
print(get_total_page(25, 10))   # 3 페이지
print(get_total_page(30, 10))   # 4 페이지  --> 3페이지만으로 모든 게시물을 출력할 수 있으므로, 실패 케이스이다.

# 나머지 값이 0이 나올 경우를 생각하여 함수를 다시 작성하자.
def get_total_page(m, n):
    if m % n == 0:      # 나눈 뒤의 나머지가 0일 때
        return m // n
    else:
        return m // n + 1

print(get_total_page(5, 10))    # 1 페이지
print(get_total_page(15, 10))   # 2 페이지
print(get_total_page(25, 10))   # 3 페이지
print(get_total_page(30, 10))   # 3 페이지




