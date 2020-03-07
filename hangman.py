def hangman(word):
    wrong = 0
    stages = ["|------      ",
              "|      |     ",
              "|      |     ",
              "|      |     ",
              "|      o     ",
              "|     /|\    ",
              "|      |     ",
              "|     / \    ",
              "|------------"
              ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages):
        print("\n")
        msg = "アルファベットを一文字入力してね:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print("[解答欄:{} ]".format(" ".join(board)),"\n","\n","[↓ハングマンの状態↓]")
        print("\n".join(stages[0:wrong]))
        if "_" not in board:
            print("\n","あなたの勝ち！")
            print(" ".join(board))
            win =True
            break
    if not win:
        print("\n","あなたの負け！正解は\"{}\"でした。".format(word))

hangman("fuck")