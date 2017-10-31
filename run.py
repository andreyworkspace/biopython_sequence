from Bio.SeqIO import parse #импортируем метот из либы

counter = 0 #общий счетчик

file = open('log.txt', 'w') #открыли файл на чтение

file.write('sequence.fasta:\n')
file.write('\n')
temp_counter = 0 #счетчик для файла
for record in parse("sequence.fasta", "fasta"): #обходим все записи
    counter += 1 #инкремент счетчика
    temp_counter += 1 #инкремент счетчика
    file.write('{0} {1}\n'.format(temp_counter, record.name)) #записываем в файл. 0 = порядковый номер, 1 = название
file.write('\n')
file.write('кол-во записей в sequence.fasta: {}\n'.format(temp_counter)) #записываем в файл кол-во записей в файле

file.write('\n')
file.write('\n')
file.write('sequence.gb:\n')
file.write('\n')
temp_counter = 0
for record in parse("sequence.gb", "genbank"):
    counter += 1
    temp_counter += 1
    file.write('{0} {1}\n'.format(temp_counter, record.name))
file.write('\n')
file.write('кол-во записей в sequence.gb: {}\n'.format(temp_counter))

file.write('\n')
file.write('\n')
file.write('общее кол-во записей: {}'.format(counter)) #записываем в файл общее кол-во записей

file.close() #закрыли файл