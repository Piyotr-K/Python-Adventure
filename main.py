import Controllers as C

def start():
    print("Game Start")
    game = C.GameController()
    game.start()
    # print(C.__doc__) Module level comment, multi-line comment at the top

if __name__ == "__main__":
    start()