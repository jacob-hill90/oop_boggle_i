from boggle_board import BoggleBoard
import unittest
import random

class BoggleBoardTestCases(unittest.TestCase):
    
    def test_initial_board_size(self):
        bb = BoggleBoard()
        self.assertEqual(len(bb.board), 16)
    
    def test_random_board(self):
        random.seed(7)
        bb = BoggleBoard(random_seed = 7)
        expected_output = list('KEMUBCRDLSBQGBCN')
        self.assertEqual(bb.shake(), expected_output)


if __name__ == '__main__':
    unittest.main()