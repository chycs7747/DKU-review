import os

class matrix:
    def __init__(self,*args):
        self.matrix = []
        self.row_num = len(args)
        self.column_num = len(args[0])
        for i in args:
            if (len(args[0]) == len(i)):
                self.matrix.append(i)
            else:
                self.matrix = []
                self.row_num = 0
                self.column_num = 0
                print("ERROR")
                return

    def __add__(self,other):
        if (self.row_num==other.row_num) and (self.column_num==other.column_num):
            result = []
            for i in range(self.row_num):
                tmp = []
                for j in range(self.column_num):
                    tmp.append(self.matrix[i][j]+other.matrix[i][j])
                result.append(tmp)
            return matrix(*result)
        else:
            return 'ERROR'

    def __sub__(self,other):
        if (self.row_num==other.row_num) and (self.column_num==other.column_num):
            result = []
            for i in range(self.row_num):
                tmp = []
                for j in range(self.column_num):
                    tmp.append(self.matrix[i][j]-other.matrix[i][j])
                result.append(tmp)
            return matrix(*result)
        else:
            return 'ERROR'

    def __mul__(self,other):
        if (self.column_num==other.row_num):
            result = []
            for i in range(self.row_num):
                tmp = []
                for j in range(other.column_num):
                    num = 0
                    for v in range(self.column_num):
                        num += self.matrix[i][v] * other.matrix[v][j]
                    tmp.append(num)
                result.append(tmp)
            return matrix(*result)
        else:
            return 'ERROR'



    def __truediv__(self,other):
        pass
    def __getitem__(self,index):
        return self.matrix[index]
    def __str__(self):
        os.system('clear')
        result = "| {}x{} Matrix |\n".format(self.row_num,self.column_num)
        for i in range(self.row_num):
            result += '\n|'
            for j in range(self.column_num):
                result = result+"{:>3}".format(self.matrix[i][j])
            result = result+ '|'
        return result