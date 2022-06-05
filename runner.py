from boggle_board import BoggleBoard

bb = BoggleBoard(4, 7)

i = 2
while i > 0:
    bb.shake()
    i -= 1