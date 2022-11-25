import numpy as np
a:np.ndarray= np.arange(1,100,1)
# print(np.eye(4))
a = np.array([1,2,3])
b=np.array([[1],[2],[3]])
print (a.dot(b))
# 使用标量类型
dt = np.dtype(np.int32)
print(dt)

np.arange(2,3,1)
a = np.arange(24)
print (a.ndim)  
print(a);           # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2,4,3)  # b 现在拥有三个维度
print(b)
print (b.ndim)
x = np.empty([3,2], dtype = float) 
print (x)
np.linspace(1,1,10)



# 高级索引
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print ('我们的数组是：' )
print (x)
print ('\n')
rows = np.array([[0,0],[3,3]]) 
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols]  
print  ('这个数组的四个角元素是：')
print (y)



from matplotlib import pyplot as plot 
 
x = np.arange(1,11) 
y =  2  * x +  5 
plot.title("Matplotlib demo") 
plot.xlabel("x axis caption") 
plot.ylabel("y axis caption") 
plot.plot(x,y) 
plot.show()

# 计算正弦曲线上点的 x 和 y 坐标
x = np.arange(0,  3  * np.pi,  0.1) 
y = np.sin(x)
plot.title("sine wave form")  
# 使用 matplotlib 来绘制点
plot.plot(x, y) 
plot.show()


class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)
 
   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp1.displayCount()
emp1.displayEmployee()
