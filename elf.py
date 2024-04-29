import character

class Elf(character.Character):
  '''The Elf class
  Name: The character's name
  <Abstract> Abilities: The levels of skill the character has
  <Abstract> Constitution, Strength, Wisdom: character stats'''
  #I should find out how to grab the superclass's docustring

  def __init__(self, name):
    super().__init__(name + " the elf")

  def abilities(self):
    return [1,0,0,0]

  def constitution(self):
    return 13

  def strength(self):
    return 10

  def wisdom(self):
    return 15