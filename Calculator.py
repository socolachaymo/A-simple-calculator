import PyQt5.QtWidgets as qtw 

class Window(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []
        self.answer = '0'
        self.show()
    
    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        #Add buttons
        self.result = qtw.QLineEdit()
        self.result.setText('0')
        result_button = qtw.QPushButton('=', clicked = self.final_result)
        clear_all = qtw.QPushButton('CA', clicked = self.clear_all)
        clear = qtw.QPushButton('C', clicked = self.clear)
        b9 = qtw.QPushButton('9', clicked = lambda: self.num_press('9'))
        b8 = qtw.QPushButton('8', clicked = lambda: self.num_press('8'))
        b7 = qtw.QPushButton('7', clicked = lambda: self.num_press('7'))
        b6 = qtw.QPushButton('6', clicked = lambda: self.num_press('6'))
        b5 = qtw.QPushButton('5', clicked = lambda: self.num_press('5'))
        b4 = qtw.QPushButton('4', clicked = lambda: self.num_press('4'))
        b3 = qtw.QPushButton('3', clicked = lambda: self.num_press('3'))
        b2 = qtw.QPushButton('2', clicked = lambda: self.num_press('2'))
        b1 = qtw.QPushButton('1', clicked = lambda: self.num_press('1'))
        b0 = qtw.QPushButton('0', clicked = lambda: self.num_press('0'))
        b_dot = qtw.QPushButton('.', clicked = lambda: self.num_press('.'))
        b_open = qtw.QPushButton('(', clicked = lambda: self.num_press('('))
        b_close = qtw.QPushButton(')', clicked = lambda: self.num_press(')'))
        b_plus = qtw.QPushButton('+', clicked = lambda: self.operation('+'))
        b_minus = qtw.QPushButton('-', clicked = lambda: self.operation('-'))
        b_mul = qtw.QPushButton('*', clicked = lambda: self.operation('*'))
        #Get Num-lock on
        #Press and hold Alt button and type 246
        b_div = qtw.QPushButton('÷', clicked = lambda: self.operation('/'))

        #Add the buttons to the Layout
        container.layout().addWidget(self.result,0,0,1,4)
        container.layout().addWidget(b_open,1,0)
        container.layout().addWidget(b_close,1,1)
        container.layout().addWidget(clear,1,2)
        container.layout().addWidget(clear_all,1,3)
        container.layout().addWidget(b9,2,0)
        container.layout().addWidget(b8,2,1)
        container.layout().addWidget(b7,2,2)
        container.layout().addWidget(b_plus,2,3)
        container.layout().addWidget(b6,3,0)
        container.layout().addWidget(b5,3,1)
        container.layout().addWidget(b4,3,2)
        container.layout().addWidget(b_minus,3,3)
        container.layout().addWidget(b3,4,0)
        container.layout().addWidget(b2,4,1)
        container.layout().addWidget(b1,4,2)
        container.layout().addWidget(b_mul,4,3)
        container.layout().addWidget(b0,5,0)
        container.layout().addWidget(b_dot,5,1)
        container.layout().addWidget(result_button,5,2)
        container.layout().addWidget(b_div,5,3)
        self.layout().addWidget(container)

    def num_press(self, number):
        self.temp_nums.append(number)
        if self.fin_nums:
            self.result.setText(''.join(self.fin_nums) + ''.join(self.temp_nums))
        else:
            self.result.setText(''.join(self.temp_nums))
        print(self.temp_nums)
    
    def operation(self, operator):
        if not self.fin_nums:
            if not self.temp_nums:
                self.fin_nums.append(self.answer)
            else:
                self.fin_nums += self.temp_nums
        else:
            if not self.temp_nums:
                self.fin_nums = self.fin_nums[:-1]
            else:
                self.fin_nums += self.temp_nums
        self.fin_nums.append(operator) 
        self.temp_nums = []
        self.result.setText(''.join(self.fin_nums))

    def final_result(self):
        string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        try:
            self.answer = str(eval(string))
            self.result.setText(string + '=' + self.answer)
            self.temp_nums = []
            self.fin_nums = []
        except:
            self.result.setText(string)
    
    def clear(self):
        if self.temp_nums:
            self.temp_nums.pop()
            string = self.fin_nums + self.temp_nums
            self.result.setText(''.join(string))
        else:
            self.fin_nums = self.fin_nums[:-1]
            self.result.setText(''.join(self.fin_nums))

    def clear_all(self):
        self.result.clear()
        self.answer = '0'
        self.result.setText('0')
        self.operated = False
        self.temp_nums = []
        self.fin_nums = []

app = qtw.QApplication([])
win = Window()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()