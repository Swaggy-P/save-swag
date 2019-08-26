from class_for_cnc import CNC_1,CNC_2,CNC_3,CNC_4,CNC_5,CNC_6,CNC_7,CNC_8

from random import randint
import random
from copy import deepcopy
class CNC():
    # cnz的各项参数


    def __init__(self):
        self.work_time_1=580    # CNC的工作参数：加工一道工序的物料需要580秒
        self.move_time_1=20     # RGV的加工参数：移动一个单位需要20秒
        self.move_time_2=35     # RGV的加工参数：移动两个单位需要35秒
        self.move_time_3=50     # RGV的加工参数：移动三个单位需要50秒
        self.cnc_1 = CNC_1()      # 初始化cnc数据
        self.cnc_2 = CNC_2()
        self.cnc_3 = CNC_3()
        self.cnc_4 = CNC_4()
        self.cnc_5 = CNC_5()
        self.cnc_6 = CNC_6()
        self.cnc_7 = CNC_7()
        self.cnc_8 = CNC_8()

    def is_useful(self,the_machine):
        if the_machine.condition==True:
            print(str(the_machine)+" is useful")
            return True
        else:
            print(str(the_machine)+" is not useful")
            return False


    def change_condition(self,the_machine):
        if the_machine.condition == True:
            the_machine.condition=False
        elif the_machine.condition==False:
            the_machine.condition=True



    def start_work(self,the_machine):       # 执行该函数，代表cnc开始工作，开始计时，其状态变为false
        the_machine.condition=False
        print(the_machine.time_for_machine_1)

    def time_for_move(self,step):
        if step==1:
            time=20
        if step==2:
            time=33
        if step==3:
            time=46
        return time
'''

next functions is out 

'''
sys=CNC()

# 定义一个限定函数，筛选出第二次和第三次选择里面的0——8之间的数

def limit(codes):
    codes1=deepcopy(codes)
    for code in codes:
        if code not in range(1,9):
            codes1.remove(code)

    return(codes1)


def is_useful(the_machine):
    if the_machine.condition==True:
        print(str(the_machine)+" is useful")
        return True
    else:
        print(str(the_machine)+" is not useful")
        return False

# 定义一个外部函数，为下一步做出选择
def first_choice(the_machine_code):
    if the_machine_code%2==0:
        next_machine_code=the_machine_code-1
    elif the_machine_code%2==1:
        next_machine_code=the_machine_code+1
    return (next_machine_code)

def second_choice(the_machine_code):             # 注意：此处需要考虑方向：往前或者往后
    the_machine_list=[sys.cnc_1,sys.cnc_2,sys.cnc_3,sys.cnc_4,
                      sys.cnc_5,sys.cnc_6,sys.cnc_7,sys.cnc_8]
    if the_machine_code%2==0:
        next_machine_list=limit([the_machine_code-3,the_machine_code-2,
                                 the_machine_code+1,the_machine_code+2])
        for next_machine_code in next_machine_list:
            if is_useful(the_machine_list[next_machine_code-1]):
                return next_machine_code
                break
    if the_machine_code%2==1:
        next_machine_list=limit([the_machine_code-1,the_machine_code-2,
                                 the_machine_code+1,the_machine_code+3])
        for next_machine_code in next_machine_list:
            if is_useful(the_machine_list[next_machine_code-1]):
                return next_machine_code
                break

# def third_choice(the_machine):



# 测试代码块


# sys.start_work(sys.cnc_1)
# sys.start_work(sys.cnc_2)
# sys.start_work(sys.cnc_5)
# sys.start_work(sys.cnc_6)
# print(second_choice(4))

#初始化数据
total_time=0

the_machine_list = [sys.cnc_1, sys.cnc_2, sys.cnc_3, sys.cnc_4,
                    sys.cnc_5, sys.cnc_6, sys.cnc_7, sys.cnc_8]
# 运行代码块
first_machine_code=input("输入你想第一台开始的机器的编号：")
sys.start_work(the_machine_list[int(first_machine_code)-1])           # 后期修改插眼
total_time+=28                      # 对第一台cnc进行上下料用时
# 现在cnc开始工作了，开始while循环
while True:
    #下面判断第一个选择是否可用
    next_machine1_code=first_choice(int(first_machine_code)) # 后期修改插眼
    next_machine1=the_machine_list[next_machine1_code-1]
    if is_useful(next_machine1):
        print(first_machine_code+"号机器优先启动")
        print("下一个机器是第"+str(next_machine1_code)+"号")
        total_time+=31              # 对第二台机器进行上下料
    if not is_useful(next_machine1):#第一个选择没用，启用第二个选择

        next_machine2=second_choice(int(first_machine_code))


        print("\n")