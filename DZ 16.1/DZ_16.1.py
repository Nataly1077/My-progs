class Kassa:
    def __init__(self, money=0):
        self.money = money
    
    def top_up(self, x):
        self.money += x
    
    def count_1000(self):
        return self.money // 1000
    
    def take_away(self, x):
        if x > self.money:
            print('не достаточно денег')
        self.money -= x

k = Kassa()
k.top_up(5000) # добавляем 5000 рублей в кассу
print(k.count_1000()) # выводим количество целых тысяч в кассе

k.take_away(3000) # забираем 3000 рублей из кассы
print(k.money) # выводим текущее количество денег в кассе

k.take_away(3000) # забираем еще 3000 рублей из кассы