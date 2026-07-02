from player import Player
from monster import Slime
from battle import BattleManager

class Game:
    def __init__(self):
        player_name = input("플레이어 이름을 입력하세요: ")
        if not player_name.strip():
            player_name = "플레이어"
        self.player = Player(player_name, hp=100, attack_power=20)
        self.mob = Slime("초록 슬라임", hp=80, attack_power=10, defense=3)
        self.mob.max_hp = 80 # 필수: BattleManager의 monster.max_hp 출력을 위함
        self.battle_manager = BattleManager()

    def show_menu(self):
        print("\n=== 메뉴 ===")
        print("1. 공격하기")
        print("2. 플레이어 정보 보기")
        print("3. 몬스터 정보 보기")
        print("4. 종료")
        choice = input("원하는 메뉴 번호를 입력하세요 (1~4): ")
        return choice

    def start(self):
        print("★ 몹 잡기 게임을 시작합니다! ★")
        while True:
            choice = self.show_menu()
            if choice == "1":
                # 플레이어가 몬스터를 공격 (BattleManager 활용)
                self.battle_manager.player_attack(self.player, self.mob)
                
                # 몬스터 체력 판별 (is_monster_dead 활용)
                if self.battle_manager.is_monster_dead(self.mob):
                    break
                
                # 몬스터 반격
                print("\n[몬스터의 반격!]")
                self.mob.attack("몸통 박치기")
            elif choice == "2":
                self.player.info()
            elif choice == "3":
                self.mob.info()
            elif choice == "4":
                print("게임을 종료합니다.")
                break
            else:
                print("올바른 번호를 입력해주세요 (1~4)")