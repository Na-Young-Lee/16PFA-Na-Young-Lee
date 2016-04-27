# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/book/ex21.html
def add(a,b): # 매개변수 목록
    print ("ADDING %d + %d" % (a,b)) # 출력할 값
    return a + b  # return 의 기능 : 계산 결과를 다른 함수로 받아 쓸 수 있음. , 반환

def subtract(a,b):
    print ("SUBTRACTING %d - %d" % (a,b))
    return a - b

def multiply(a,b):
    print ("MULTIFLYING %d * %d" % (a,b))
    return a * b

def divide(a,b):
    print ("DIVIDING %d / %d" % (a,b))
    return a / b


print ("Let's do some math with just fuction!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print ("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))


# A puzzle for the extra credit, type it in anyway.
print ("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2)))) # 안쪽에 있는 값부터 계산이 됨.

print ("That becomes: ", what, "Can you do it by hand?")
