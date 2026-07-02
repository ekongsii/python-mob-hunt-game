import time
import random

class Battle:
    def __init__(self, player, mob):
        self.player = player
        self.mob = mob

    def start(self):
        """
        플레이어와 몬스터의 전투 루프를 실행합니다.
        """
        print(f"\n⚔️ {self.player.name} vs {self.mob.name} 전투 시작! ⚔️")
        self.mob.info()

        turn = 1
        while self.player.hp > 0 and self.mob.hp > 0:
            print(f"\n--- [턴 {turn}] ---")
            print(f"[{self.player.name}] HP: {self.player.hp}/{self.player.max_hp}")
            print(f"[{self.mob.name}] HP: {self.mob.hp}/{self.mob.max_hp}")
            print("-" * 20)

            # 1. 플레이어 행동 선택
            print("행동을 선택하세요:")
            print("1: 일반 공격")
            print("2: 스킬 공격 (쿨타임 5초)")
            
            choice = input("선택 (1 또는 2): ").strip()
            
            if choice == "1":
                self.player.attack(self.mob)
            elif choice == "2":
                # 스킬 공격이 쿨타임 등의 이유로 실패하면 턴을 소모하지 않고 다시 선택하도록 함
                success = self.player.skill_attack(self.mob)
                if not success:
                    continue
            else:
                print("❌ 올바른 선택이 아닙니다. 1번 또는 2번을 눌러주세요.")
                continue

            # 몬스터 처치 여부 확인
            if self.mob.hp <= 0:
                break

            time.sleep(0.5)

            # 2. 몬스터의 반격
            print(f"\n👾 {self.mob.name}의 반격!")
            
            # 몬스터 종류에 따라 고유 스킬 공격을 시도할 수도 있도록 구현
            if hasattr(self.mob, 'jump') and random.random() < 0.3:
                # 버섯 몬스터이고 30% 확률인 경우 점프 공격 수행
                self.mob.jump(self.player)
            elif hasattr(self.mob, 'split') and random.random() < 0.2:
                # 슬라임 몬스터이고 20% 확률인 경우 분열 수행 후 일반 공격
                self.mob.split()
                self.mob.attack(self.player)
            else:
                # 그 외에는 기본 공격 수행
                self.mob.attack(self.player)

            # 플레이어 사망 여부 확인
            if self.player.hp <= 0:
                break

            turn += 1
            time.sleep(0.5)
            
        print("\n⚔️ 전투가 종료되었습니다. ⚔️")