#-*-coding:cp949

x = "There are %d types of people." % 10 # 10�� ������� �ִ�.
binary = "binary" # 2����
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # 2������ �ƴ� ������ 2������ ���� ���ϴ� �����

print x
print y

print "I said: %r." % x # ���� ���ߴ�. "10�� ������� �ִ�."
print "I also said: '%s'." % y # ���� ����  ���ߴ�. "2������ �˰ų� �𸣴� ���."  

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # �̰��� ����� �ƴԴϴ�. ���ܿ�?

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
