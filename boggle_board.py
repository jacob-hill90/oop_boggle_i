import random
import string

class BoggleBoard:
  
  def __init__(self, length, width,):
    self.length = length
    self.width = width
  
  def new(self):
    print("_" * self.length)
    print("_" * self.length)
    print("_" * self.length)
    print("_" * self.length)

  def shake(self):
    print(f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}")
    print(f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}")
    print(f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}")
    print(f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}")

board = BoggleBoard(4,4)
board.new()
board.shake()
