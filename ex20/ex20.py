#-*-coding:cp949
from sys import argv # 시스템으로부터 매개변수를 가져온다

script, input_file = argv # 매개변수는 input_file(test.txt)이다.


def print_all(f): # 함수 print문장열, f는 변수
    print(f.read()) # 이 파일의 모든 내용을 읽어라


def rewind(f): # 함수 rewind, f는 변수
    f.seek(0) # 시작 위치로 돌아감.
              # seek(): 자기 테이프 위에 원하는 위차를 지정하기 위함.
              # seek(n): 시작위치로부터 n byte 위치의 자료를 읽기/쓰기 준비하라는 의미

def print_a_line(line_count,f):
    print("%d %s" % (line_count, f.readline())) # read_line 은 파일을 한 행씩 읽으라는 의미

current_file = open(input_file)

print ("First let's print the whole file:굈")

print_all(current_file) # print_all 호출

print ("Now let's rewind, kind of like a tape.")

rewind(current_file) # rewind 호출

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line +1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)