import json
import os
from types import SimpleNamespace


def all_minion_card():
    card_data = list()
    dirpath = os.path.dirname(__file__)
    filepath = os.path.join(dirpath, "data.json")
    f = open(filepath, "r", encoding='utf-8')
    #data = json.loads(f.read())
    x = json.loads(f.read(), object_hook=lambda d: SimpleNamespace(**d))

    # for i in x:
    #     if i.name == "아기 멀록":
    #         print(i)
    #     if i.name == "방패병":
    #         print(i)

    card_battlecry = []
    card_devine_shield = []
    card_death_rattle = []
    card_poisonous = []
    card_netural = []
    for i in x:
        if i.type != "MINION": continue
        try:
            # if "BATTLECRY" in i.mechanics:
            #     card_battlecry.append(i)
            if 'DIVINE_SHIELD' in i.mechanics:
                card_devine_shield.append(i)
            if 'DEATHRATTLE' in i.mechanics:
                card_death_rattle.append(i)
            if 'POISONOUS' in i.mechanics:
                card_poisonous.append(i)
        except Exception as e:
            card_netural.append(i) #아무 효과가 없는카드

    #json의 set에 battleground용 태그 존재
    #여기서는 하스스톤 모든 카드중 하수인만을 선별하도록 하자..
    # 브란 브론즈비어드 같은 애는 현재 AURA로 되어있음

    # print(len(card_battlecry),len(card_death_rattle),len(card_devine_shield),len(card_poisonous))
    # print(len(card_netural))
    # for i in card_netural:
    #     print(i)

all_minion_card()

