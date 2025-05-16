'''
# a = 123
# a = -178
# a = 0
# a = 1.2
# a = 4.2e10
# a = 0o763
# a = 0xab

a = 7
b = 4

print(a // b)
+
-
*
/

** 제곱
// 몫
% 나머지

'''


# 문자열 : ' ', " ", ''' ''', """ """
# 문자열 중간에 \' 이런식으로 들어가면 String 끝내는 것으로 인식하지 않음.
a = "Life is too short, You Need PYTHON"
b = 'I\'m Hungry'

print(a)
print(type(a))
print(b)


# 줄바꿈 : \n   <== 이스케이프 코드
# 혹은 따옴표 3 개를 사용하여 강력하게 묶어주면, 엔터로 줄바꿈 하여도 문제가 없다. (엔터 줄바꿈 시 \n과 동일하게 작동한다.)
c = "Life is too short,\nYou Need PYTHON"
d = '''Life is Too short,
You Need PYTHON'''
# print(c)
print(d)

