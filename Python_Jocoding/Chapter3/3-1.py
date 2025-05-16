
# 조건문, 문법은 아래와 같다.
# if 조건문:
# else:
# if 조건문 또는 else 이후에 콜론(:)을 잊지 말고 붙이자.
'''
# money = True
money = False

if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# If문에서 Tab으로 들여쓰기가 제대로 되지 않는다면, 해당 코드는 if가 끝난 뒤의 일반 코드라고 인식한다. -> Indentation Error 가 Return


# 비교연산자는 아래와 같다.
# <, >, ==, !=, >=, <=
'''

'''
# 조건문을 실제 상황에 적용해 보자.
# money = 2000
# if money >= 3000:
#     print("택시 타셔도 됩니다")
# else:
#     print("걸어가세요")

# and / or / not
money = 2000
card = True
# if money >= 3000 and card:
if not card:
    # not card: <- card가 거짓이면 True이다.
    print("택시 타도 됩니다")
else:
    print("돈도 없는게 어디서 택시를 타려구")


# in / not in
# List, Tuple, String 자료형에 적용 가능
li = [1, 2, 3]
print(1 in li)
print(1 not in li)

tu = ('a', 'b', 'c')
print(1 in tu)
print(1 not in tu)

st = 'python'
print('j' in st)

# 실생활 적용
# 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라
whatsinmypocket = ['cellphone', 'recipt', 'money']
if 'money' in whatsinmypocket:
    print("택시 타도 됩니다")
else:
    print("어딜 택시를 타려고")


# if문 통과할 때 아무 동작도 하고싶지 않을 경우, 'pass' 를 적어준다
a = 3
if a == 3:
    pass
else:
    print("나올 수 없는 경우")
'''


# elif의 활용
# 주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.
pocket = ['recipt', 'cellphone']
card = True

if 'money' in pocket:
    print("택시!!")
# elif card == True:
elif card:
    print("택시!!")
else:
    print("걸으셈")


# if문 한 줄로 작성하기
# 가능은 하나,, 가독성이 많이 떨어지는 것 같음
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드 꺼내십쇼..")


# 조건부 표현식
score = 100

if score >= 60:
    message = "success"
else:
    message = "failure"
# 위의 네 줄 표현은 아래 한 줄로 바꿀 수 있다.

message = "success" if score >= 60 else "failure"
# 우항의 코드 : 참일 때의 결과 if 조건식 else 거짓일 때의 결과

print(message)
