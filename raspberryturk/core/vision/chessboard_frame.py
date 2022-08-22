import numpy as np
from raspberryturk.core.vision.square import Square
from raspberryturk.core.vision.constants import SQUARE_SIZE, BOARD_SIZE

class ChessboardFrame():
    def __init__(self, img):
        self.img = img

    def square_at(self, i):
        y = BOARD_SIZE - ((i // 8) % 8) * SQUARE_SIZE - SQUARE_SIZE
        x = (i % 8) * SQUARE_SIZE
        return Square(i, self.img[y:y+SQUARE_SIZE, x:x+SQUARE_SIZE, :])
