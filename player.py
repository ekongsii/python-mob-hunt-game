import time

class Player:
    def __init__(self, name, hp=100, attack_power=20, defense=5, max_xp=100):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.xp = 0
        self.max_xp = max_xp
        self.last_skill_time = 0.0
        self.skill_cooldown = 5.0  # Cooldown in seconds (set to 5 for easy testing)

    def attack(self, target):
        if self.hp <= 0:
            print("Game Over: 사망하여 공격할 수 없습니다.")
            return
        
        damage = max(1, self.attack_power - target.defense)
        target.hp -= damage
        print(f"{self.name}이(가) {target.name}을(를) 공격하여 {damage}의 피해를 입혔습니다.")
        
        if target.hp <= 0:
            target.hp = 0
            print(f"{target.name}을(를) 처치했습니다!")
            xp_reward = getattr(target, 'xp_reward', 50)
            self.gain_xp(xp_reward)

    def skill_attack(self, target):
        if self.hp <= 0:
            print("Game Over: 사망하여 스킬을 사용할 수 없습니다.")
            return

        current_time = time.time()
        elapsed = current_time - self.last_skill_time
        if elapsed < self.skill_cooldown:
            remaining = self.skill_cooldown - elapsed
            print(f"스킬 재사용 대기 시간 중입니다. ({remaining:.1f}초 남음)")
            return False

        self.last_skill_time = current_time
        damage = max(1, (self.attack_power * 2) - target.defense)
        target.hp -= damage
        print(f"{self.name}이(가) 강력한 스킬 공격으로 {target.name}에게 {damage}의 피해를 입혔습니다!")
        
        if target.hp <= 0:
            target.hp = 0
            print(f"{target.name}을(를) 처치했습니다!")
            xp_reward = getattr(target, 'xp_reward', 50)
            self.gain_xp(xp_reward)
        return True

    def gain_xp(self, amount):
        if self.hp <= 0:
            return
        self.xp += amount
        print(f"{amount} XP를 획득했습니다. (현재 XP: {self.xp}/{self.max_xp})")
        if self.xp >= self.max_xp:
            self.level_up()

    def level_up(self):
        self.xp = 0
        self.max_hp += 10
        self.hp = self.max_hp
        self.attack_power += 5
        self.defense += 2
        print(f"\n★ 레벨 업! ★")
        print(f"HP가 모두 회복되었습니다. (HP: {self.hp}/{self.max_hp})")
        print(f"공격력이 {self.attack_power}로, 방어력이 {self.defense}로 상승했습니다!\n")

    def take_damage(self, damage):
        if self.hp <= 0:
            return
        actual_damage = max(1, damage - self.defense)
        self.hp -= actual_damage
        print(f"{self.name}이(가) {actual_damage}의 피해를 입었습니다. (남은 HP: {self.hp}/{self.max_hp})")
        if self.hp <= 0:
            self.hp = 0
            print("Game Over")

    def info(self):
        print("-" * 20)
        print(f"플레이어 이름: {self.name}")
        print(f"체력: {self.hp}/{self.max_hp}")
        print(f"공격력: {self.attack_power}")
        print(f"방어력: {self.defense}")
        print(f"경험치: {self.xp}/{self.max_xp}")
        print("-" * 20)
