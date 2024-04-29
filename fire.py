import decorator

class Fire(decorator.Decorator):
  '''A wrapper class for decorator. An instance of this wrapper will increase the fire level by one and change the character's stats'''

  def abilities(self):
    stats = super().abilities()
    stats[2] += 1
    return stats

  def constitution(self):
    return super().constitution() - 3

  def strength(self):
    return super().strength() - 3

  def wisdom(self):
    return super().wisdom() + 5