# Intelligent Duelling

from random import seed
from random import gauss

# Map the Attack to all moves that block it
attackBlocksDict = {
   "Swing Right": ["Shield Right", "Swing Right"],
   "Swing Left": ["Shield Left", "Swing Left"],
   "Swing Down": ["Shield Up", "Swing Up"],
   "Swing Up": ["Shield Down", "Swing Down"]
   "Jab": ["Shield Forward", "Swing Right", "Swing Down"] 
}

class Sword:
   """A class representing the sword"""
   def __init__(self):
      self.type = "Sword"
      self.damage = 3 # How much damage it can inflict
      self.moves = ["Swing Right", "Swing Left", "Swing Up", "Swing Down", "Jab", "Nothing"]

class WoodenShield:
   """A class representing a wooden shield. This is a weak shield."""
   def __init__(self):
      self.type = "Wooden Shield"
      self.maxIntegrity = 25 # How much damage it can withstand before breaking
      self.currentIntegrity = 25
      self.moves = ["Block Right", "Block Left", "Block Up", "Block Down", "Block Forward", "Nothing"]

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

   def displayCharacterStats(self):
      print("Player {}: {}".format(self.playerNum, self.name))
      print("\tHitpoings: {}".format(self.hitpoints))
      print("\tEnergy: {}/{}".format(self.energy, self.endurance))
      print("\tWeapon: {}".format(self.weapon.type))
      print("\tShield: {}".format(self.shield.type))   
      print("\tShield Integrity: {}/{}".format(self.shield.maxIntegrity, self.shield.currentIntegrity))

   # Maybe this doesn't belong to a character. Does it belong to the game?
   def calculateAttack(self, move):
      # Where should I handle a defensive move? In here?
      # Maybe I could differentiate between an offensive move and a defensive
      # If it's defensive, return 0 attack and empty list?

      global attackBlocksDict

      # Obtain a list of moves that can block the chosen move
      blockingMoves = attackBlocksDict[move]

      # Higher strength = larger attack. Higher speed = weaker attack.
      maxAttack = (self.strength / self.speed) * self.weapon.damage

      # This is the attack value with the highest probability
      meanAttack = (self.energy / self.endurance) * maxAttack

      # Select the attack amount with a gaussian distribution of probabilities
      # The meanAttack has the highest probability of being selected
      standardDeviation = 1.5
      attack = gauss(meanAttack, 1.5)

      if attack > maxAttack:
         attack = maxAttack
      elif attack < 0:
         attack = 0

      # Returning to the same position takes time. This would decrease the effectiveness of the blow
      # Decrease the attack amount if the current move is the same as the last move
      if move == self.lastMove:
         attack = attack / 2

      return attack, blockingMoves
      

def performInteraction():
   # Take the moves of each player
   # Calculate the attack of them
   # Compare the speeds. Grant higher probability of hit to player with greater speed.
   # Decrease attack dealt with respect to the attackee's armor
   # Lower the hitpoints of the attacked
   # Decrease/increase the integrity of the shield used for blocking
   # Decrease/increase the energy

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