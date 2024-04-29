import decorator

class Archery(decorator.Decorator):
  '''A wrapper class for decorator. An instance of this wrapper will increase the archery level by one and change the character's stats'''

  def abilities(self):
    '''Increments the archery ability'''
    stats = super().abilities()
    stats[0] += 1
    return stats

  def constitution(self):
    return super().constitution() -2

  def strength(self):
    return super().strength() + 5

  def wisdom(self):
    return super().wisdom() - 2