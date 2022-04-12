# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.
year = int(input('Vvedite god:'))
century = year//100
if century >= 0:
    century += 1
    print(century,'й -век',sep='')
else:
    print('input no correct')

'''
if 1901 <= year <= 2000:
    print('20 век')
elif 1801 <= year <= 1900:
    print('19 век')
elif 1701 <= year <= 1800:
    print('18 век')
else:
    print('drevnij vek')
'''