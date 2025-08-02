import random
from time import sleep

liste=[
    "   0      1       1         01         0            0           1         1                  0                1        0 1           011                 01",
    "     1     0   1           0          1        0    1           0           0            0          1          0                 1            0        1          0 ",
    "0        1       0            11 1           0          1         0        1         0 1            0        1           0      1        0       1 ",
    "1     1          10        0               1         0           1           0               10                 1            0          0"

]

while True:
    x=random.choice(liste)
    print(x)
    sleep(0.12)