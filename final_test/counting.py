# Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека.
# Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
# Игра происходит до тех пор, пока не останется последний человек.
# Для данных N и К дать номер последнего оставшегося человека.

N = 18
K = 5

# all people
people = [x for x in range(1, N + 1)]

print(people)

while len(people) > K:
    # remove i-elem
    people.pop(K)

i = K % len(people)
while len(people) > 1:
    people.pop(i)
    i = K % len(people)

print(people)
