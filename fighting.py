import decorator

class Fighting(decorator.Decorator):
  '''A wrapper class for decorator. An instance of this wrapper will increase the fighting level by one and change the character's stats'''

  def abilities(self):
    stats = super().abilities()
    stats[1] += 1
    return stats

  def constitution(self):
    return super().constitution() + 2

  def strength(self):
    return super().strength() +2

  def wisdom(self):
    return super().wisdom() - 3