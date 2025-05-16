
'''
# Dictionary
# Key - Value 쌍으로 이루어진 자료.
# Associative array 또는 hash 라고도 한다.
# 이름표가 붙어있는 사물함 안에 요소들을 넣는 방식이라고 생각하면 된다.

#  이는 API에 자주 활용된다.    (API : Application Programming Interface)

# 아래는 dictionary 자료형의 예시이다.
# {'key' : 'value'}   <= 한 쌍의 Key와 Value
dic = {'name' : 'dongho', 'HP' : '010-1234-5678', 'birthday' : '19981108'}

print(dic)
print(type(dic))


# value에는 List와 같은 자료형도 추가할 수 있다.
a = {'a' : [1, 2, 3]}
print(a)

# 기 생성된 dictionary에 값을 추가할 수 있다.
dic1 = {1 : 'a'}
dic1[2] = 'b'
dic1['아무거나'] = '추가가능'
dic1['리스트도가능'] = [1, 2, 'a', 'b']
print(dic1)

# dictionary에서 삭제도 가능하다.
# 삭제할 value의 "Key" 값을 중괄호 안에 넣고 del 해준다.
# 여러개를 한 줄의 코드로 삭제하고 싶다면, 콤마로 구분하여 작성하면 된다.
dic = {'name' : 'dongho', 'HP' : '010-1234-5678', 'birthday' : '19981108'}
del dic['name'], dic['HP']
print(dic)
'''

'''
# key 값을 활용하여 value값 가져오기
# dictionary의 이름 뒤, Key 값을 중괄호로 감싼다.
# 입력한 key 값이 dictionary 내에 없을 경우, KeyError가 return된다.
dicScore = {'std1' : 99, 'std2' : 98, 'std3' : 90}
print(dicScore)
print(dicScore['std2'])


# dictionary에 중복된 key 값을 사용하면 안된다.
# 에러는 발생하지 않으나, 중복 key값 중 가장 마지막에 추가된 key:value 값만 남는다.
a = {1 : 'a', 1 : 'b'}
print(a)

# key는 변형되면 안되는 값이기에, immutable 자료형만 key로 활용할 수 있다.


# .keys() 라는 함수를 사용하면, 해당 dictionary의 key 값들을 가져올 수 있다.
# key값들을 dict_keys 라는 자료형으로 return한다.   <= list 보다 좀 더 적은 메모리를 차지하는 자료형...
dic = {'name' : 'dongho', 'HP' : '010-1234-5678', 'birthday' : '19981108'}
print(list(dic.keys()))
print(dic.keys())

# .values() 라는 함수로 해당 dictionary의 value 값들을 가져올 수 있다.
print(dic.values())

# .items() 함수를 사용하면 key:value 를 한 쌍으로 얻을 수 있다.
# 가장 바깥에 list가 생성되며, key와 value 한 쌍은 tuple 자료형으로 안에 들어간다.
print(dic.items())

# .clear() 함수로 dictionary 값 모두 날리기
a = {'name' : 'dongho', 'HP' : '010-1234-5678', 'birthday' : '19981108'}
a.clear()
print(a)

# value 값을 가져올 때 .get() 함수를 사용하여도 된다.
# 딕셔너리 내 key 값이 없을 때 다른 return값을 출력한다.
# a['name']     -> KeyError 발생
# a.get('name') -> None 출력
a = {'name' : 'dongho', 'HP' : '010-1234-5678', 'birthday' : '19981108'}
print(a['name'])
print(a.get('name'))
# 값이 없을 때, None 이외 다른 값을 return받고 싶다 하면 아래와 같이 코드를 작성하자.
print(a.get('NoData', "값이 없습니다."))
'''

# Dictionary 안에 특정 key 값이 있는지 확인하고 싶은 경우
# 'key' in 변수명   -> True / False 로 값이 return된다.
a = {'name' : 'dongho', 'HP' : '010-1234-5678', 'birthday' : '19981108'}
print('name' in a)

# dictionary에서 key 이름을 0, 1, 2... 로 지정하게 되면 개념상 list와 거의 유사하다고 할 수 있다
# 물론 사용할 수 있는 함수는 다름
list = [1, 2, 3]
dic = {0:1, 1:2, 2:3}
print(list[1])
print(dic[1])






