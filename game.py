print()
print('*****************************')
print('*          Привет!          *')
print('*     Это игра в ГОРОДА     *')
print('*****************************')
print()
print('Для выхода из игры нажми "5" в свой ход')
print('Итак, начинаем!!!')
print()

history = []
priority = ('Твой ход:  ', 'Ход друга: ')
quetion = ('Добавлять очков:  ', 'Убавлять очков:   ')
i = 0
scores = [0, 0]
plus_points= int(input(quetion[0]))
minus_points = int(input(quetion[1]))
while True:
   
   city = input(priority[i]).lower()

   if city == '5':
      break
   if len(history) != 0 and city[0] != last_letter:
      print(f'... город должен начинаться на букву "{last_letter}"')
      scores[i] = scores[i] - minus_points
      continue
   if city in history:
      print('... это название уже было')
      scores[i] = scores[i] - minus_points
      continue

   history.append(city)

   last_letter = city[-1]
   if city[-1] in ['ь', 'ъ', 'й', 'ы']:
      last_letter = city[-2]

   scores[i] = scores[i] + plus_points
   i = (i + 1) % 2

print()
print('Правильно названо городов:', len(history))
print(f'Твои баллы:  {scores[0]}')
print(f'Баллы друга: {scores[1]}')
print()
print('*********** Пока! ***********')
