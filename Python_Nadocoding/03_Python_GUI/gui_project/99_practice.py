# 결합
kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

print(list(zip(kor, eng)))

# 분리
mixed = [("사과", "apple"), ("바나나", "banana"), ("오랜지", "orange")]
print(list(zip(*mixed)))

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)