import random


class Parasiten:

    def __init__(self):
        self.strasse = random.randint(10, 20)
        self.richtung = random.choice(['links', 'rechts'])
        self.geschwindigkeit = random.randint(1, 3)


    def bewegen(self):
        if self.richtung == 'links':
            self.strasse -= self.geschwindigkeit
        else:
            self.strasse += self.geschwindigkeit

    def nicht_sichtbar(self):
        if self.strasse <0 or self.strasse > 35:
            return True
        else:
            return False

