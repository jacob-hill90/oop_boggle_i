import random

class BoggleBoard:
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  length = 4

  def __init__(self, custom_length = None, random_seed = None):
    #allow user to input custom length
    if custom_length is not None:
      self.length = custom_length
    if random_seed is not None:
      random.seed(random_seed)
    # initialize board with underscores
    self.board = ['_' for _ in range(self.length ** 2)]
    self.print_board()
  
  def print_board(self):
    for i, x in enumerate(self.board):
      print(x, end = '')
      # make sure we add a new line every row
      if (i + 1) % self.length == 0:
        print('\n', end = '')
      
    print('\n', end = '')

  def shake(self):
    #loop through board and assign random letter
    for i, _ in enumerate(self.board):
      self.board[i] = random.choice(self.alphabet)
    self.print_board()
    return self.board
