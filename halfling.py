import character

class Halfling(character.Character):
  '''The Halfling class
  Name: The character's name
  <Abstract> Abilities: The levels of skill the character has
  <Abstract> Constitution, Strength, Wisdom: character stats'''

  def __init__(self, name):
    super().__init__(name + " the halfling")

  def abilities(self):
    return [0,0,0,1]

  def constitution(self):
    return 15

  def strength(self):
    return 10

  def wisdom(self):
    return 13