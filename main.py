import scipy.stats as stats
import numpy as np

def inputFile():
    try:
        filename = input('Input filename: ').replace('.txt', '')
        #filename = 'F_v02c'
        f = open(filename + '.txt', 'r')

        fileString = ''
        for s in f:        
            fileString += s.strip() 
        fileString = fileString.replace(',', '.').replace('\t', ' ').replace('\n', ' ')
        
        f.close()
        
        return fileString
    
    except FileNotFoundError:
        print('Ошибка! Файл не найден.')
        return inputFile()

def inputCountSplit(count):
    try:
        num = int(input('Введите количество разделений выборки: '))
        if num > 1 and num < count:
            return num
        else:
            print(f'Ошибка! Число должно быть в больше 1 и меньше {count - 1}')
            return inputCountSplit(count)
    except ValueError:
        print('Не удалось преобразовать в число')
        return inputCountSplit(count)
    
def inputSignificanceLevel():
    try:
        num = float(input('Введите уровень значимости: ').replace(',', '.'))
        if num > 0 and num < 1:
            return num
        else:
            print('Ошибка! Число должно быть больше 0 и меньше 1')
            return inputSignificanceLevel()
    except ValueError:
        print('Не удалось преобразовать в число')
        return inputSignificanceLevel()

    
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
    if pvalue <= (1 - significanceLevel):
        print('Cистематических погрешностей не обнаружено.')          
    else:
        print('Систематические погрешности есть.')              

main()
