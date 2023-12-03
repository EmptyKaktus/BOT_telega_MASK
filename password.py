import random

PASSWORD = []

ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alpha = list("abcdefghijklmnopqrstuvwxyz")
num = list("1234567890")
special_znak = list("_-=+!{}[]()")

# Всего 20 символов
# 10 Букв
# 5 Цифр
# 5 Символов

letter_ABC = random.randint(0, 5)
for i in range(letter_ABC):
    PASSWORD.append(random.choice(ALPHA))

letter_abc = 5 - letter_ABC
for i in range(letter_ABC):
    PASSWORD.append(random.choice(alpha))

for i in range(3):
    PASSWORD.append(random.choice(num))

for i in range(3):
    PASSWORD.append(random.choice(special_znak))

random.shuffle(PASSWORD)
print("".join(PASSWORD))


# sz[9Pd9+MA7! telega obloko