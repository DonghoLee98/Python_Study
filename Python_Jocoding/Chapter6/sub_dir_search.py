'''
def search(dirname):
    print(dirname)

search("c:/")

# python .\sub_dir_search.py 로 실행한다.
'''

# 입력한 디렉터리 아래 .py 파일 검색
'''
import os

def search(dirname):
    filenames = os.listdir(dirname)     # os 라이브러리의 listdir 내장 함수를 활용한다.
    for filename in filenames:
        full_filename = os.path.join(dirname, filename) # os.path.join 활용, 절대경로로 만들어 준다.
        ext = os.path.splitext(full_filename)[-1]   # os.path.splitext 활용, 확장자를 분리하여 Tuple 자료형으로 return한다. 여기서 [-1]로 확장자를 선택한다.
        if ext == '.py':
            print(full_filename)
        
search("c:/python/")
'''

# 입력한 디렉터리 아래 모든 파일 및 폴더에 대하여 .py 파일 검색
'''
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):    # isdir : 디렉토리 인지 확인
                search(full_filename)   # 재귀 함수! search() 를 다시 호출한다.
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:     # 권한이 없는 디렉터리 접근 시 pass
        pass

search("C:/python")
'''

# 하위 디렉터리 검색을 쉽게 해주는 os.walk 함수
# 위의 재귀함수 사용 코드보다 훨씬 간단하게 처리가 가능하다.
import os

for (path, dir, files) in os.walk("C:/Python"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))