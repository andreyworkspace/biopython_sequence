from Bio.SeqIO import parse
import os.path


def get_extension(name):
    if name[0][0] == 'f':
        return 'fasta'
    return name


def seq_parser(file_name, out):
    temp_counter = 0  # счетчик для файла
    out('{}:\n\n'.format(file_name))
    parse_result = parse(file_name, get_extension(os.path.splitext(file_name)[1][1:]))  # обходим все записи. splitext - получаем разширение файла, без точки
    try:
        for record in parse_result:
            temp_counter += 1  # инкремент счетчика
            out('{0} {1}\n'.format(temp_counter, record.name))  # записываем в файл. 0 = порядковый номер, 1 = название
    except Exception as e:
        out(str(e))
    out('\nкол-во последовательностей в {0}: {1}\n\n'.format(file_name, temp_counter))  # записываем в файл кол-во последовательностей в файле
    return temp_counter  # возвращаем общий счётчик
