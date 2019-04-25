

class Character:
   """A class representing a character"""
   def __init__(self, name, playerNum):
      self.name = name
      self.playerNum = playerNum
      self.hitpoints = 10

   def displayCharacterStats():
      print("Player " + playerNum + ": " + name)
      print("\tHitpoings: " + hitpoints)
      

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

   playing = True

   firstMoveP1 = 0
   secondMoveP1 = 0

   firstMoveP2 = 0
   secondMoveP2 = 0

   while playing:
      # Player 1 selects two moves.
      firstMoveP1, secondMoveP2 = getMoves(player1)

      # Player 1's first move (attack) is applied to Player 2's second move (Nothing for the very first time, defend for the second).
      
      
      # Player 2 selects two moves. (Like attack and defend)
      
      # Player 2's first move (Attack) is applied to Player 1's second move. (Defend)



   



if __name__ == "__main__":
   main() 