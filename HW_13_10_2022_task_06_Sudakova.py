# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

import random
my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
my_favorite_songs2=my_favorite_songs.items()
#print(my_favorite_songs2)
songstime = []
for song, time in my_favorite_songs2:
    songstime.append(time)
print(songstime) 
m = 0
k=3
while k !=0:
    k -=1
    #print(random.choice(songstime))
    m += float(random.choice(songstime))
print('Три песни звучат ',m)

