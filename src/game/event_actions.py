import time

from typing import List

from spawn import *


def attacking(attacker: Pawn, targets: List[Enemy], effects):
    if attacker.last_attack + 1 / attacker.attack_speed > time.time():
        return

    # Place effects
    effects.extend([])
    for n in range(attacker.attack_range + 1):
        effect_pos = (-1)**int(attacker.left_facing) * n + attacker.pos
        if n > 0:
            effects.append(
                Effect(
                    pos=effect_pos, 
                    render=attacker.attack_render, 
                    lifetime=0.15
            ))

        for target in targets:
            if target.pos == effect_pos:
                attacker.damage(target)
    attacker.last_attack = time.time()