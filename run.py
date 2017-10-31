from Bio.SeqIO import parse
import argparse
import sys
import os.path

def parseFile(fileName, out, counter):
    temp_counter = 0  # счетчик для файла
    out.write('{}:\n\n'.format(fileName))
    for record in parse(fileName, os.path.splitext(fileName)[1][1:]):  # обходим все записи. splitext - получаем разширение файла, без точки
        counter += 1  # инкремент счетчика
        temp_counter += 1  # инкремент счетчика
        out.write('{0} {1}\n'.format(temp_counter, record.name))  # записываем в файл. 0 = порядковый номер, 1 = название
    out.write('\nкол-во последовательностей в {0}: {1}\n\n'.format(fileName, temp_counter))  # записываем в файл кол-во последовательностей в файле
    return counter #возвращаем общий счётчик

parser = argparse.ArgumentParser(prog='bio_counter', description="Подсчёт последовательностей")
parser.add_argument("-o", "--out", help="результирующий файл", default='out.txt')
parser.add_argument("-f", "--files", help="входные данные", nargs='+')
args = parser.parse_args()

# проверка на обзятельный параметр
if not args.files:
    print('Ошибка, укажите файл с входными данными\n')
    print(parser.print_help())
    sys.exit()

counter = 0  # общий счетчик
outFile = open(args.out, 'w') #открыли файл на запись

for fileName in args.files:
    if not os.path.isfile(fileName): # проверка существования файла
        outFile.write('файла {} не существует\n\n'.format(fileName))
    else:
        counter = parseFile(fileName, outFile, counter)

outFile.write('\n\nобщее кол-во последовательностей: {}'.format(counter)) #записываем в файл общее кол-во последовательностей
outFile.close() #закрыли файл