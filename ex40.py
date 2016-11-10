# You could use a module like this

# import mystuff
# mystuff.apple()
# print(mystuff.tangerine)

# Or you could use a class like this.
# Class is like a mini module

class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

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

bulls_on_parade = Song(["The rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

lyrics = ["test", "lyrics"]
test = Song(lyrics)
test.sing_me_a_song()