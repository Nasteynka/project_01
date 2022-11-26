# Задача 4
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайныThree_songе значения, используйсте модуль random

import random


my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
# print('Три случайных песни - ' random.sample(my_favorite_songs[0], 3))
Three_song = random.choices(my_favorite_songs, k=3)
print('Три случайных песни звучат - ', )

# task = (random.choices(my_favorite_songs), k=3)
#Three_song_cort = Three_song.items()
time=float(Three_song[0][1])+float(Three_song[1][1])+float(Three_song[2][1])
    
print(time)



