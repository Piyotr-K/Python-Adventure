class Adventure():

    def __init__(self):
        pass

    def combatLoop(self) -> None:
        self.e_hp = 100
        self.p_hp = 100
    
    def eval_btn(self, _id : int) -> None:
        if _id == 0:
            print("Attack")
    
    def game_update(self) -> None:
        self.eval_btn()