import matplotlib.pyplot as plt


x = []
y = []

time = 0
bacterias = 1

for i in range(100000000000):
    if (time % 10) == 0 :
        bacterias = bacterias * 2

    time = time + 1
    x.append(time)
    y.append(bacterias)
    print (f'This is time:{time} and this is the amount of bacteria : {bacterias}')


print(f'x:{x}')
print(f'y:{y}')

plt.plot(x, y, marker='o')
plt.show()
'''

x = [0, 1, 2, 3, 4, 5, 6]
y = [1, 2, 4, 8, 16, 32, 64]

plt.plot(x, y, marker='*')

plt.show()
'''

