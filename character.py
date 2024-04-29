import abc

class Character(abc.ABC):
  '''
  Name: The character's name
  <Abstract> Abilities: The levels of skill the character has
  <Abstract> Constitution, Strength, Wisdom: character stats
  '''

  def __init__(self, name):
    self._name = name

  def __str__(self):
    the_string = self._name + "\n" + "-Abilities-" + "\n"
    numbs = self.abilities()
    classes = ["Archery", "Fighting", "Fire Magic", "Healing"]
    for i in range(0,4):
      if(numbs[i] >= 1):
        the_string += classes[i] + f": Level {numbs[i]}\n"
    #That loop is done
    the_string += "-Stats-\n"
    the_string += f"Con: {self.constitution()} \nStr: {self.strength()} \nWis: {self.wisdom()}"
    return the_string
    

  @abc.abstractmethod
  def abilities(self)-> list[int]:
    '''Returns a list of ints representing Archery, Fighting, Fire, and Healing levels'''

  @abc.abstractmethod
  def constitution(self)-> int:
    '''The constitution stat'''

  @abc.abstractmethod
  def strength(self)-> int:
    '''The strength stat'''

  @abc.abstractmethod
  def wisdom(self)-> int:
    '''The wisdom stat'''
  
  #Accessor
  @property
  def name(self):
    '''Accessor method for the name variable'''
    return self._name

  