#todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
'''
Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
Цены хранятся в словаре:
'''
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}
product = []
coin = []
for key, values in prices.items():     #вытаскиваем товары и ценники в каждый отельный список
  product.append(key)
  coin.append(values)

def compute_bill(list):
  s = 0
  for i in list:                     #сумма всех ценников
    s = i + s
  return(s)


print('стоимость: ',compute_bill(coin),'\n','shopper: ', *product, sep=' ')




