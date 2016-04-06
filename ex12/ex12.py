#-*-coding:cp949

age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weight?")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)


# ex11과의 차이점 :: ex12는 raw_input의 가로안에 문장이 들어가 있어서 ex11보다 입력해야할 글이 적다.
