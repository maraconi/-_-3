import os
import glob
from pprint import pprint

def get_file_size():
        document_size = {}
        for name in glob.glob('*.txt'):
                with open(f'{name}', encoding='utf-8') as f:
                        lines = f.readlines()
                document_size[name] = len(lines)
        document_sorted = {}
        document_sorted_keys = sorted(document_size, key=document_size.get)
        for i in document_sorted_keys:
                document_sorted[i] = document_size[i]
        return document_sorted

def get_new_file():
        with open('4.txt', 'w+', encoding='utf-8') as f:
                f.write('')

def get_write_new_file():
        files = get_file_size()
        text_name = []
        text_str_number = []
        for key, value in files.items():
                text_name.append(key)
                text_str_number.append(value)
        for i in range(len(text_name)-1):
                with open(f'{text_name[0]}', 'a', encoding='utf-8') as f2, open(f'{text_name[i+1]}',
                encoding='utf-8') as f1:
                        text = f1.read()
                        f2.write(f'{text_name[i+1]}\n')
                        f2.write(f'{text_str_number[i+1]}\n')
                        f2.write(f'{text}\n')
                        f2.write('\n')

def get_service_iformation():
        with open('4.txt', encoding='utf-8') as f:
                for line in f:
                        text_name = line.lower().strip()
                        counter = f.readline().strip()
                        text_list = []
                        for i in range(int(counter)):
                                line = f.readline().strip()
                                text_list.append(line)
                        f.readline()
                        print(text_name)
                        print(counter)
                        for i, text_list in enumerate(text_list):
                                print('Строка номер',i+1, 'файла номер', text_name)

get_file_size()
get_new_file()
get_write_new_file()
get_service_iformation()
