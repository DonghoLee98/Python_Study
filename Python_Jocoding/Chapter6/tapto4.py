import sys

# python tapto4.py a.txt b.txt
# src --> a.txt
# dst --> b.txt
src = sys.argv[1]
dst = sys.argv[2]

# 파일 읽어와 변환하기 (\t --> '    ')
f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " " * 4)

# 변환한 파일로 b.txt 생성하기
f = open(dst, 'w')
f.write(space_content)
f.close()

