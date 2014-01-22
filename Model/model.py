# -*- coding:utf-8 -*-

"""
Задачи:
1.
2.
3.

"""

from csv import writer as csvwriter
from datetime import datetime


def saveCSV(inRow=[None]):
    suffix = datetime.now().strftime("%y%m%d_%H%M%S")
    fileName = '_'.join(['out', suffix]) + '.csv'
    with open(fileName, 'a') as csvfile:
        writer = csvwriter(csvfile, delimiter=';')
        writer.writerow(inRow)


def main():
    print ('Еще не готово :(')

if __name__ == '__main__':
    main()