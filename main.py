import sys
#from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication,QMainWindow,QSystemTrayIcon,QMenu #QWidget, QLineEdit, QLabel,QVBoxLayout
from PyQt6 import uic
from PyQt6.QtGui import QIcon
import os
# os.getcwd()
#path = os.path.abspath("main.py")
speed = 120

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #uic.loadUi("./UI.ui", self)
        ui_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "UI.ui")
        uic.loadUi(ui_file_path, self)
        
        self.speed_entry.textChanged.connect(self.calculate) #绑定计算函数
        self.pushButton_qingkong.clicked.connect(self.qingkong) #绑定清空函数
        self.horizontalScrollBar.valueChanged.connect(self.huakuai) # 绑定清空处理函数
        self.label_2.enterEvent = (self.label_hovered_1) # 绑定鼠标悬停事件处理函数
        self.label_3.enterEvent = self.label_hovered_2 # 绑定鼠标悬停事件处理函数
        self.label_2.leaveEvent = self.label_left
        self.label_3.leaveEvent = self.label_left
        self.speed_entry.setFocus() #聚焦于输入框
        # font = self.font() # 继承字体
        # self.label_2.setFont(font)
        # self.label_3.setFont(font) 
        
        

    # 将calculate方法中的参数加上self
    def calculate(self):  # 添加self参数
        
        #window = self
        try:
            speed_text = self.speed_entry.text()
            if not speed_text:
                speed_text = '0'
            # global speed
            speed = float(speed_text)

            if speed == 0:  # 如果速度为零，直接触发 ZeroDivisionError
                raise ZeroDivisionError("Speed cannot be zero!")
                # 如果速度不为零，则执行以下代码
            time_a = {}  
            time_b = {}  
            print(speed_text)
            for e in range(1, 16):
                time_a[e] = 0
                time_b[e] = 0

            time_a[1] = 60000 / speed * 32  
            time_b[1] = time_a[1] * 3 / 4

            for i in range(1, 16):  
                time_a[i+1] = time_a[i] / 2  
                time_b[i+1] = time_b[i] / 2

            result_text_a = ""
            result_text_b = ""
            for u in range(1, 16):
                # time_a_val = "  {:.2f}".format(time_a[u])  
                # time_b_val = "  {:.2f}".format(time_b[u])  
                time_a_val = int(time_a[u]) if time_a[u].is_integer() else "{:.2f}".format(time_a[u]).rstrip('0').rstrip('.') 
                time_b_val = int(time_b[u]) if time_b[u].is_integer() else "{:.2f}".format(time_b[u]).rstrip('0').rstrip('.') 
                result_text_a += f"  {time_a_val}\n"  
                result_text_b += f"  {time_b_val}\n"  

            self.label_2.setText(result_text_a)
            self.label_3.setText(result_text_b)
            
        except ValueError:
            
            Tishi = "请输入BPM数字！！"
            print(Tishi)
            
            self.label_2.setText(Tishi)
            self.label_3.setText("(*^_^*)🍃")
            
        except ZeroDivisionError:
            print("速度不能为零！请重新输入速度。")
            Tishi = ""
            print(Tishi)
            
            self.label_2.setText(Tishi)
            self.label_3.setText(Tishi)
        except Exception as e:
            print(f"发生了未知错误")


    def qingkong (self):
        self.speed_entry.clear()
        self.speed_entry.setFocus() #聚焦于输入框
    def huakuai(self):
                # 设置滑块的最小值和最大值
        Min = speed - 100
        Max = speed + 100
        self.horizontalScrollBar.setMinimum(int(Min))
        self.horizontalScrollBar.setMaximum(int(Max))
        new_value = str(self.horizontalScrollBar.value())
        self.speed_entry.setText(new_value)
        pass
    def label_hovered_1(self,event):
        self.label_PS.setText("对应拍子的正数拍")
        pass

    def label_hovered_2(self,event):
        self.label_PS.setText("对应拍子的附点拍")
        pass

    def label_left(self, event):
        self.label_PS.setText("")

class TrayIcon(QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        super().__init__(icon, parent)
        self.setToolTip("My Application")
        
        # 创建菜单项
        menu = QMenu()
        show_action = menu.addAction("Show Main Window")
        show_action.triggered.connect(self.show_main_window)
        
        # 设置菜单
        self.setContextMenu(menu)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
    

