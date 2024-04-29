import character

class Dwarf(character.Character):
  '''The Dwarf Class
  Name: The character's name
  <Abstract> Abilities: The levels of skill the character has
  <Abstract> Constitution, Strength, Wisdom: character stats'''

  def __init__(self, name):
    super().__init__(name + " the dwarf")

  def abilities(self):
    return [0,1,0,0]

  def constitution(self):
    return 13

  def strength(self):
    return 15

  def wisdom(self):
    return 10