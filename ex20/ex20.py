#-*-coding:cp949
from sys import argv # �ý������κ��� �Ű������� �����´�

script, input_file = argv # �Ű������� input_file(test.txt)�̴�.


def print_all(f): # �Լ� print���忭, f�� ����
    print(f.read()) # �� ������ ��� ������ �о��


def rewind(f): # �Լ� rewind, f�� ����
    f.seek(0) # ���� ��ġ�� ���ư�.
              # seek(): �ڱ� ������ ���� ���ϴ� ������ �����ϱ� ����.
              # seek(n): ������ġ�κ��� n byte ��ġ�� �ڷḦ �б�/���� �غ��϶�� �ǹ�

def print_a_line(line_count,f):
    print("%d %s" % (line_count, f.readline())) # read_line �� ������ �� �྿ ������� �ǹ�

current_file = open(input_file)

print ("First let's print the whole file:�n")

print_all(current_file) # print_all ȣ��

print ("Now let's rewind, kind of like a tape.")

rewind(current_file) # rewind ȣ��

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line +1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)