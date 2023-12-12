import random

class Sorter:
    def sort(self,data):
        raise NotImplementedError
    
class BubbleSort(Sorter):
    def sort(self, data):
        length = len(data)
        for i in range(length):
            for j in range(length - i - 1):
                if  data[j ] > data[j+1]:
                    data[j], data[j+1] = data[j + 1],data[j]

class PrintingSort:
    def PrintSort(self, data):
        print(data)

class Alogrithm:
    def __init__(self, sorter, printer):
        self.sorter = sorter
        self.printer = printer

    def run(self, data):
        self.sorter.sort(data)
        self.printer.PrintSort(data)

if __name__ == '__main__':
    random.seed()
    data_sort = [random.randint(0,100) for _ in range(10)]
    print(data_sort)
    sorter = BubbleSort()
    printer = PrintingSort()
    alogrithm_object = Alogrithm(sorter=sorter, printer=printer)
    alogrithm_object.run(data_sort)