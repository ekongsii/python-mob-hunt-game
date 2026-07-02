from player import Player
from monster import Slime
from battle import Battle

class Game:
    def __init__(self):
        player_name = input("플레이어 이름을 입력하세요: ")
        if not player_name.strip():
            player_name = "플레이어"
        self.player = Player(player_name, hp=100, attack_power=20, defense=5)
        self.mob = Slime("초록 슬라임", hp=80, attack_power=10, defense=3)
        self.battle_manager = Battle(self.player, self.mob)

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
                # 플레이어가 몬스터를 공격
                self.player.attack(self.mob)
                
                # 몬스터 체력이 0 이하가 되면 게임 종료
                if self.mob.hp <= 0:
                    print("\n★ 축하합니다! 몬스터를 처치하여 승리했습니다! ★")
                    break
                
                # 몬스터 반격
                print("\n[몬스터의 반격!]")
                self.mob.attack(self.player)
                
                # 플레이어 사망 시 게임 종료
                if self.player.hp <= 0:
                    print("\n★ 플레이어가 쓰러졌습니다. 게임 오버! ★")
                    break
            elif choice == "2":
                self.player.info()
            elif choice == "3":
                self.mob.info()
            elif choice == "4":
                print("게임을 종료합니다.")
                break
            else:
                print("올바른 번호를 입력해주세요 (1~4)")