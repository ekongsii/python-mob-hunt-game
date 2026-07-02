from game import Game
from monster import Mushroom

if __name__ == "__main__":
    # 1. Game 객체 생성
    game = Game()
    
    # 2. game.py를 수정하지 않고 Mushroom을 사용하도록 self.mob 오버라이딩
    game.mob = Mushroom("주황버섯", hp=70, attack_power=12, defense=2)
    game.mob.max_hp = 70
    
    # 3. 게임 시작
    game.start()
