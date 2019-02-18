class new_car:
    def __init__(self, marka, kuzov, god):
        self.marka = marka
        self.kuzov = kuzov
        self.god = god

c1 = new_car("Audi", "Universal", 1998)
c2 = new_car("VW", "Sedan", 2000)
#c3 = new_car("Skoda")

print(c1.marka, c1.kuzov, c1.god)
print(c2.marka, c2.kuzov, c2.god)
print(type(c1))


class song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_a_song(self):
        for i in self.lyrics:
            print(i)


happy_b = song(["Happy birthday to you, happy birthday to you..."])
i_hate = song(["I hate everythihg about you, die whore..."])

happy_b.sing_a_song()
i_hate.sing_a_song()


