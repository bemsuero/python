mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

def apple():
    print("I AM APPLES!")

tangerine = "Living reflection of a dream."

# all of these do similar things
# mystuff['apple']
# mystuff.apple()
# mystuff.tangerine

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don\'t want to get sued",
                    "So I\'ll stop right there"])

bulls_on_parade = Song(["They really around tha family",
                        "With pockets full of shells"])

marina = (["You\'ve been acting awful tough lately",
            "Smoking a lot of cigarettes lately",
            "But inside..."])

the_diamonds = Song(marina)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

the_diamonds.sing_me_a_song()
