class Mob:
    def __init__(self, name, hp, attack_power, defense):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
    def attack(self, skill):
        print(f'{self.name}이 {skill}으로 공격했습니다.')
        # obj.hp -= self.attack_power-obj.defense

    def info(self):
        print("-"*20)
        print(f"이름: {self.name}")
        print(f"체력: {self.hp}")
        print(f"공격력: {self.attack_power}")
        print(f"방어력: {self.defense}")

class Mushroom(Mob):
    def __init__(self, name, hp, attack_power, defense):
        super().__init__(name, hp, attack_power, defense)
    def run(self):
        super().attack("달리기")
    def jump(self):
        super().attack("점프")
    def info(self):
        super().info()
        print("-"*20)


class Slime(Mob):
    def __init__(self, name, hp, attack_power, defense):
        super().__init__(name, hp, attack_power, defense)
        self.count = 1
    def split(self):
        self.count *= 2
        print(f"{self.name}이 {self.count}마리가 되었습니다.")
    def info(self):
        super().info()
        print(f"개수: {self.count}")
        print("-"*20)
