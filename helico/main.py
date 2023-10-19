# ⬛ 🌲 🌊 🏥 🏦 💭 ⚡ 🔥 🚁 💜 💧 💲

from map import Map
from time import sleep
from os import system, name

TICK_SLEEP = 0.1


tmp = Map(20, 10)
tmp.gen_forest(3, 10)
tmp.gen_river(10)
tmp.gen_water(10)
tmp.draw_map()


tick = 1

while True:
    system('cls' if name == 'nt' else 'clear')
    print('TICK', tick)
    tmp.draw_map()
    tick += 1
    sleep(TICK_SLEEP)