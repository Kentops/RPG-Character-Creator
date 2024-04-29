import decorator

class Healing(decorator.Decorator):
  '''A wrapper class for decorator. An instance of this wrapper will increase the healing level by one and change the character's stats'''

  def abilities(self):
    stats = super().abilities()
    stats[3] += 1
    return stats

  def constitution(self):
    return super().constitution() + 3

  def strength(self):
    return super().strength() - 4

  def wisdom(self):
    return super().wisdom() + 2