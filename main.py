import os
import scipy.stats as stats
import numpy as np

def inputFile():
    while True:   
        filename = input('Введите имя файла: ').replace('.txt', '') + '.txt'
                
        if os.path.isfile(filename):
            f = open(filename, 'r')

            fileString = ''
            for s in f:        
                fileString += s.strip() 
            fileString = fileString.replace(',', '.').replace('\t', ' ').replace('\n', ' ')
            
            f.close()
            
            return fileString
        else:
            print('Ошибка: файла не существует.')

def inputCountSplit(count):
    while True:
        num = input('Введите количество серий, на которое стоит разделить выборку: ')
        if num.isdigit():
            num = int(num)
            if num > 1 and num < count:
                return num
            else:
                print(f'Ошибка: Число должно быть в больше 1 и меньше {count - 1}.')
        else:    
            print('Ошибка: Не удалось преобразовать ввод в число.')
    
def inputSignificanceLevel():
    while True:
        num = input('Введите уровень значимости: ').replace(',', '.')

        if num.replace('.', '',1).isdigit():
            num = float(num)
            if num > 0 and num < 1:
                return num
            else:
                print('Ошибка: Число должно быть больше 0 и меньше 1.')
        else:
            print('Ошибка: Не удалось преобразовать ввод в число.')
    
def main():    
    fileString = inputFile()
    
    arr = list(map(float,fileString.split(' ')))

    print(f'Количество элементов выборки: {len(arr)}')
    print(f'Среднее арифметическое значение: {np.mean(arr)}')
    print(f'Оценка среднего квадратического отклонения: {stats.tstd(arr)}')

    countSplit = inputCountSplit(len(arr))
    significanceLevel = inputSignificanceLevel()


    arr = np.array_split(arr, countSplit)    

    oneway = stats.f_oneway(*arr)
    pvalue = oneway[1]

    print(f'pvalue: {pvalue}')
    if pvalue <= significanceLevel:
        print('Фактор влияет на погрешность.')        
    else:        
        print('Фактор не влияет на погрешность.')

main()
