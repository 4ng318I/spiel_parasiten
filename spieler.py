class Spieler:

    def __init__(self, name):
        self.name = name
        self.strasse = 1
        self.energie = 15

    def platz(self):
        return self.name, self.strasse, self.energie


    def bewegen(self, geschwindigkeit):
        if geschwindigkeit == "1":
            self.strasse +=1
        elif geschwindigkeit == "2":
            self.strasse +=2
        else:
            self.strasse +=3
        self.energie -= 1

