import character
import dwarf
import elf
import halfling
import decorator
import archery
import fire
import fighting
import healing
import check_input

'''
Character Crearor 4/22/2024
A DND-esque character creator.
'''

def main():
  print("Character Maker!")
  print("Choose your character:")
  print("1. Dwarf")
  print("2. Elf")
  print("3. Halfling")
  
  char = check_input.get_int_range("Enter your choice: ", 1,3)
  print()
  character_name = input("What is your character's name? ")
  
  if char == 1:
    character = dwarf.Dwarf(character_name)
  elif char == 2:
    character = elf.Elf(character_name)
  else:
    character = halfling.Halfling(character_name)
  
  print()
  print(character)
  print()
  print("You have 5 points to spend:")

  points = 5
  
  while points > 0:
    print("Add an ability:")
    print("1. Archery")
    print("2. Fighting")
    print("3. Fire Magic")
    print("4. Healing")
    ability = check_input.get_int_range("Enter ability: ", 1,4)

    if ability == 1:
      character = archery.Archery(character)
    elif ability == 2:
      character = fighting.Fighting(character)
    elif ability == 3:
      character = fire.Fire(character)
    elif ability == 4:
      character = healing.Healing(character)
    
    points -= 1
    print()
    print(character)

  stats = [character.constitution(), character.strength(), character.wisdom()]
  
  failed = False
  for value in stats:
    if value <= 0:
        failed = True
        break

  if failed:
    print("Your character has failed.")
  else:
    print("Congratulations! You have created your character.")

  
main()