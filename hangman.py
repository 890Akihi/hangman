#ハングドマンを作ろう！

import random as rd
"""
words = ["cat","dog","rat"]

def hangman(word):
    wrong = 0
    stages = ["",
              "_____     ",
              "|         ",
              "|    |    ",
              "|    O    ",
              "|   /|\\   ",
              "|   / \\   ",
              "|__....   "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ...！")

    while wrong < len(stages) -1:
        print("\n")
        msg = "1文字予想してみてね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print("残りは..."+ "".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You Winer!")
            print(" ".join(board) + "!!")
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose...正解は{}".format(word))

def word():
    n = rd.randint(0,3)
    w = words[n]
    hangman(w)

word()
"""

class Hangman_state:
    words = ["dog","cat","rat"]

    def __init__(self):
        self.word = self.words[rd.randint(0,2)]
        w = self.word
        game = Hungman_game(w)
        game.game()

class Hungman_game():
    stages = ["",
              "_____      ",
              "|          ",
              "|    |     ",
              "|    O     ",
              "|   /|\\    ",
              "|   / \\    ",
              "|__....    "
              ]
    def __init__(self,w):
        self.wrong = 0
        self.word = w
        self.board = ["_"] * len(w)
        self.rletters = list(w)
        self.win = False
    
    def game(self):
        print("ハングマンで勝負だ！")
        print(" ".join(self.board))
        while self.wrong < len(self.stages) -1:
            print("\n")
            msg = "一文字予想してね"
            char = input(msg)
            if char in self.rletters:
                cind = self.rletters.index(char)
                self.board[cind] = char
                self.rletters[cind] = "$"
            else:
                self.wrong += 1
            print("残りは：" + " ".join(self.board))
            e = self.wrong + 1
            print("\n".join(self.stages[:e]))
            if "_" not in self.board:
                print("You Win!!")
                print("正解は..." + "".join(self.board))
                self.win = True
                break
        if not self.win:
            print("You Lose...")
            print("正解は " + "".join(self.word) + "だったよ")

game_state = Hangman_state()