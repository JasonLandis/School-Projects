import random

value = str(input("Enter:"))
total = []
count = 0
try:
    for x in value:
        if x != 'd':
            count += 1
        else:
            dice = int(value[:count])
            count2 = 0
            for x in value:
                if x != 'l':
                    count2 += 1
                else:
                    roll = int(value[count + 1:count2])
                    luck = int(value[count2 + 1:])
    if dice > 1000 or roll > 1000 or luck > roll:
        print("Overflow Error")

except:
    print("Format - 1d20l20")

for x in range(1, dice + 1):
    total.append(random.randrange(1, roll + 1))

final = sum(total)

for x in range(1, dice * (luck + 1)):
    rand = random.randrange(1, 3)
    if rand == 1:
        final += 1

if final > dice * roll:
    final = dice * roll

print(final)

total.clear()
