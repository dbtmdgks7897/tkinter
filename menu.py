import time
import random

menuDB = ["짜장면", "짬뽕", "탕슉"]

li = [i for i in range(1, 46)]
print(random.sample(li, 6))

print("메뉴 골라줘")
print("AI가 추천해주는 메뉴는?")

for i in range(5, 0, -1):
    print(f'{i}...')
    time.sleep(1)

print("분석 후 추천")
menu = random.choice(menuDB)
print(f'{menu}먹으셈')