"""
Actors.py

Classes and helper classes related to
Actors and characters in the game
such as, player, enemy and whatever else

Date-Created: 2022 OCT 10
Date-Last-Modified: 2022 OCT 12
Author: Piyotr Kao
"""
import Settings as S

class Actor():

    actor_count : int = 0

    def __init__(self, _name : str, _maxHp : int) -> None:
        self.id : int = Actor.actor_count
        self.name : str = _name
        self.maxHp : int = _maxHp
        self.currHp : int = self.maxHp
        Actor.actor_count += 1
    
    def __repr__(self) -> str:
        return f"Actor: {self.id}\nName: {self.name}\nMax Hp: {self.maxHp}\nCurrent Hp: {self.currHp}"
    
    def damage(self, _amt : int) -> None:
        self.currHp -= _amt
    
    def create(self):
        # TO-DO
        pass

    def delete(self):
        # TO-DO
        pass

class Player(Actor):
    """
    Player

    An actor representing the player, will probably create
    another class later that represents actors that can/cannot
    take damage
    """

    def __init__(self, _name : str, _maxHp : int) -> None:
        super().__init__(_name, _maxHp)
        self.items : S.type.List[str] = []
    
    def attack(self, _target : Actor) -> None:
        _target.damage(S.rand.randint(7,20))
    
    def defend(self, _dmg : int) -> None:
        """
        Damage gets multiplied by inverse of defence percentage
        """
        defence = 0.2
        self.damage(_dmg * (1 - defence))
    
    def bag(self) -> None:
        pass
