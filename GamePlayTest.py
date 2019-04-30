
class Sword:
   """A class representing the sword"""
   def __init__(self):
      self.type = "Sword"
      self.damage = 3 # How much damage it can inflict
      self.moves = ["Swing Right", "Swing Left", "Swing Up", "Swing Down", "Jab"]

class WoodenShield:
   """A class representing a wooden shield. This is a weak shield."""
   def __init__(self):
      self.type = "Wooden Shield"
      self.maxIntegrity = 25 # How much damage it can withstand before breaking
      self.currentIntegrity = 25
      self.moves = ["Block Right", "Block Left", "Block Up", "Block Down", "Block Forward"]

class Character:
   """A class representing the attributes of a character"""
   def __init__(self, name, playerNum):
      self.name = name
      self.playerNum = playerNum

      self.hitpoints = 20   # The remaining life
      self.endurance = 5    # The max energy
      self.energy = 5       # energy/endurance * max attack = highest probably attack amount

      self.weapon = Sword() # This has the damage amount and the moves.
      self.shield = WoodenShield() # Different shields can withstand more damage.
      self.strength = 5     # Affects max attack
      self.speed = 5        # Affects the probability of a block or a hit
      self.armor = 5        # Dampens the effect of an opponent's attack

      self.specialAbility = "" # An ability specific to this character      
      self.lastMove = ""    # The move most recently executed. The same move executed twice will decrease the damage or speed

   def displayCharacterStats():
      print("Player " + playerNum + ": " + name)
      print("\tHitpoings: " + hitpoints)
      print("\tEnergy: " + hitpoints + " of " + endurance)
      print("\tWeapon: " + weapon.type())
      print("\tShield Integrity: " + shield.maxIntegrity + " of " + shield.currentIntegrity)
 

def getContestants():
   # Get player 1's name
   print("-------------------")
   nameP1 = input("Player 1, enter a name for your character: ")
   player1 = Character(nameP1, 1)

   print("Welcome, " + nameP1 + "! Prepare for your duel!")

   # Get player 2's name
   print("-------------------")
   nameP2 = input("Player 2, enter a name for your character: ")
   player2 = Character(nameP2, 2)
   
   print("Welcome, " + nameP2 + "! Prepare for your duel!")

   return player1, player2

def getMoves(player):
   player.displayCharacterStats()
   print("Player " + player.playerNum + ", Select two moves:")
   print("\t0: Nothing")
   print("\t1: Attack")
   print("\t2: Defend")
   firstMove = int(input("1st Move: "))
   secondMove = int(input("2nd Move: "))

   return firstMove, secondMove

def getAttackResult():
   pass


def main():
   print("Intelligent Duelling")

   player1, player2 = getContestants()

   player1.displayCharacterStats()
   player2.displayCharacterStats()

   playing = True

   firstMoveP1 = 0
   secondMoveP1 = 0

   firstMoveP2 = 0
   secondMoveP2 = 0

   #while playing:
      # Player 1 selects two moves.
    #  firstMoveP1, secondMoveP2 = getMoves(player1)

      # Player 1's first move (attack) is applied to Player 2's second move (Nothing for the very first time, defend for the second).
      
      
      # Player 2 selects two moves. (Like attack and defend)
      
      # Player 2's first move (Attack) is applied to Player 1's second move. (Defend)



   



if __name__ == "__main__":
   main() 