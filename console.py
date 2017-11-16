import argparse
import sys
import os.path
from seqParser import seq_parser

parser = argparse.ArgumentParser(prog='bio_counter', description="Подсчёт последовательностей")
parser.add_argument("-o", "--out", help="результирующий файл", default='out.txt')
parser.add_argument("-f", "--files", help="входные данные", nargs='+')
args = parser.parse_args()

# проверка на обязательный параметр
if not args.files:
    print('Ошибка, укажите файл с входными данными\n')
    print(parser.print_help())
    sys.exit()

counter = 0  # общий счетчик
outFile = open(args.out, 'w')  # открыли файл на запись

for fileName in args.files:
    if not os.path.isfile(fileName):  # проверка существования файла
        outFile.write('файла {} не существует\n\n'.format(fileName))
    else:
        counter += seq_parser(fileName, outFile.write)

outFile.write('\n\nобщее кол-во последовательностей: {}'.format(counter))  # записываем в файл общее кол-во последовательностей
outFile.close()  # закрыли файл
