import unittest
from src.hourGlass import lambda_handler

class TestHourglassLambda(unittest.TestCase):

    def test_positive_hourglass(self):
        event = {
            'arr': [
                [1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 2, 4, 4, 0],
                [0, 0, 0, 2, 0, 1],
                [0, 1, 1, 2, 4, 0]
            ]
        }
        self.assertEqual(lambda_handler(event, None), 19)

    def test_negative_hourglass(self):
        event = {
            'arr': [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1]
            ]
        }
        self.assertEqual(lambda_handler(event, None), -7)

    def test_mixed_values(self):
        event = {
            'arr': [
                [1, 2, 3, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 2, 3, 0, 0, 0],
                [0, 0, 1, 2, 3, 0],
                [0, 0, 0, 1, 0, 1],
                [0, 1, 2, 3, 4, 0]
            ]
        }
        self.assertEqual(lambda_handler(event, None), 19)

    def test_edge_case(self):
        event = {
            'arr': [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ]
        }
        self.assertEqual(lambda_handler(event, None), 7)

    def test_invalid_input(self):
        event = {'arr': [[1, 2], [3, 4]]}
        self.assertEqual(
            lambda_handler(event, None),
            "Invalid input: Array must be at least 3x3 in size."
        )

if __name__ == '__main__':
    unittest.main()