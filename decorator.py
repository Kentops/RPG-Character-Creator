import character
import abc #Is this really needed?

class Decorator(character.Character, abc.ABC):
  '''
  The wrapper class for a character
  _char: the Character instance under the wrapper
  '''

  def __init__(self, char):
    super().__init__(char.name)
    self._char = char

  def abilities(self):
    '''Increments abilities'''
    return self._char.abilities()

  def constitution(self):
    '''Modifies the constitution stat'''
    return self._char.constitution()

  def strength(self):
    '''Modifies the strength stat'''
    return self._char.strength()

  def wisdom(self):
    '''Modifies the wisdom stat'''
    return self._char.wisdom()

  #Because decorator extends character, the string method is already carried over
  