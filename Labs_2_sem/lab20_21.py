n = int(input('Введите количество n: '))
count_a = 0
count_b = 0
count_c = 0
for i in range(1, n+1):
    a = i ** 5
    count_a += a
for j in range(1, n+1):
    b = j**7
    count_b += b
for l in range(1,n+1):
    count_c += l
    c = 2 * count_c**4
if c == count_b + count_a:
   print('Что и требовалось доказать ', c,'=', count_b, '+', count_a)

