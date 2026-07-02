class Mob:
    def __init__(self, name, hp, attack_power, defense, xp_reward=50):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.xp_reward = xp_reward

    def attack(self, target, skill="기본 공격"):
        if self.hp <= 0:
            return
        print(f'{self.name}이(가) {skill}으로 {target.name}을(를) 공격했습니다.')
        target.take_damage(self.attack_power)

    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp -= actual_damage
        print(f"{self.name}이(가) {actual_damage}의 피해를 입었습니다. (남은 체력: {self.hp}/{self.max_hp})")
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name}이(가) 쓰러졌습니다!")

    def info(self):
        print("-"*20)
        print(f"이름: {self.name}")
        print(f"체력: {self.hp}/{self.max_hp}")
        print(f"공격력: {self.attack_power}")
        print(f"방어력: {self.defense}")

class Mushroom(Mob):
    def __init__(self, name, hp, attack_power, defense, xp_reward=40):
        super().__init__(name, hp, attack_power, defense, xp_reward)
    def run(self):
        print(f"{self.name}이 달리기 동작을 수행합니다.")
    def jump(self, target):
        super().attack(target, "점프")
    def info(self):
        super().info()
        print("-"*20)


class Slime(Mob):
    def __init__(self, name, hp, attack_power, defense, xp_reward=30):
        super().__init__(name, hp, attack_power, defense, xp_reward)
        self.count = 1
    def split(self):
        self.count *= 2
        print(f"{self.name}이 {self.count}마리가 되었습니다.")
    def info(self):
        super().info()
        print(f"개수: {self.count}")
        print("-"*20)
