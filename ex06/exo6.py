#-*-coding:cp949

x = "There are %d types of people." % 10 # 10인 사람들이 있다.
binary = "binary" # 2진법
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # 2진법을 아는 사람들과 2진법을 알지 못하는 사람들

print x
print y

print "I said: %r." % x # 나는 말했다. "10인 사람들이 있다."
print "I also said: '%s'." % y # 나는 또한  말했다. "2진법을 알거나 모르는 사람."  

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # 이것은 농담이 아님니다. 웃겨요?

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
