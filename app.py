import random

class Human:
  health = 30
  name = ""
  def __init__(self, name):
      self.name = name

  def eat(self):
      self.health+=5

myHuman = Human("Hassan")
myHuman.eat()
print(myHuman.health)

class Ninja(Human):
    health = 10
    def __init__(self, name):
        Human.__init__(self, name)

    def meditate(self):
        self.health+=5

    def backstab(self, obj):
        obj.health-=10

kevTheNinja = Ninja("Kevin")
kevTheNinja.eat()
print(kevTheNinja.health)
kevTheNinja.backstab(myHuman)
print(myHuman.health)

class Wizard(Human):
    health = 25
    magicPower = 0
    def __init__(self, name):
        Human.__init__(self, name)

    def study(self):
        self.health+=random.randint(1,3)

    def fireBall(self, obj):
        obj.health-=self.magicPower

xandoTheWizard = Wizard("Xando")
print(xandoTheWizard.health)
xandoTheWizard.study()
print(xandoTheWizard.health)
xandoTheWizard.fireBall(myHuman)
print(kevTheNinja.health)


class Warrior(Human):
    health = 40
    armor = 10
    def __init__(self, name):
        Human.__init__(self, name)

    def armorUp(self):
        self.armor+=5

    def shieldAlly(self, obj):
        if(self.armor > 4):
            obj.health+=5
            self.armor-=5
        else:
            print 'error'

preciousTheWarrior = Warrior("Precious")
print(preciousTheWarrior.armor)
preciousTheWarrior.shieldAlly(myHuman)
print(preciousTheWarrior.armor)
