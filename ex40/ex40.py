# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex40.html

mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])         # mystuff['apple'] 은 get apple from dict

import mystuff

mystuff.apple()                   # mystuff.apple() 은 get apple from the module
print(mystuff.tangerine)         # mystuff.tangerine 은 same thing, it's just a vatiable

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thounsand years between"

    def apple(self):
        print("I AN CLASSY APPLES!")
# end class MyStuff

thing = MyStuff()
thing.apple()
print(thing.tangerine)


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
