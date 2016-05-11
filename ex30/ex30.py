# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex30.html

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:                         # elif는 갯수제한 없이 만들 수 있다.
     print("we should not take the cars.")
else:                                       # else는 1개 밖에 쓰지 못한다.if도 아니고 else도 아닐 때
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
