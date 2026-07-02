class BattleManager:
    def __init__(self):
        pass

    def is_monster_dead(self, monster):
        """
        몬스터의 HP가 0 이하인지 확인합니다.
        :param monster: 몬스터 객체
        :return: 죽었으면 True, 살아있으면 False
        """
        return monster.hp <= 0

    def player_attack(self, player, monster):
        """
        플레이어가 몬스터를 공격하고 상태를 출력합니다.
        :param player: 플레이어 객체
        :param monster: 몬스터 객체
        """
        # 플레이어가 몬스터를 공격 (내부적으로 데미지 차감 및 처치 시 경험치 획득 처리 수행됨)
        player.attack(monster)

        # 공격 후 상태에 따른 메시지 출력
        if self.is_monster_dead(monster):
            print(f"🎉 시스템: {monster.name}을(를) 완벽히 처치하였습니다!")
        else:
            print(f"👾 시스템: {monster.name}의 남은 HP는 {monster.hp}/{monster.max_hp}입니다.")