# https://www.runoob.com/matplotlib/matplotlib-pyplot.html
import matplotlib.pyplot as plt
import numpy as np
import time
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False


def demo1():
    bar1 = [4, 5, 6, 8, 7]
    bar2 = [7, 6, 2, 5, 4]
    labels = ['小明', '小张', '小洪', '小红', '小铭']
    bar_width = 0.35

    plt.bar(np.arange(5)-0.5*bar_width, bar1, label='第一次',
            width=bar_width, color='#58C9B9')
    plt.bar(np.arange(5)+0.5*bar_width, bar2, label='第二次',
            width=bar_width, color='#519D9E')
    plt.xlabel('人名', fontsize=15)
    plt.ylabel('数量', fontsize=15)
    plt.title('数量统计', fontsize=18)
    plt.ylim([0, 10])
    plt.legend()
    plt.xticks(np.arange(5), labels, fontsize=13)
    plt.box(False)
    plt.grid(color='0.4', axis='y', linestyle='solid', alpha=0.1)

    for i, j in enumerate(bar1):
        plt.text(i-0.5*bar_width-0.05, j+0.1, str(j))

    for i, j in enumerate(bar2):
        plt.text(i+0.5*bar_width-0.05, j+0.1, str(j))
    plt.savefig('fig.pdf', bbox_inches='tight')


def scatter_plot():
    # 打开交互模式
    plt.ion()
    for index in range(50):
        # plt.cla()

        plt.title("动态散点图")
        plt.grid(True)
        point_count = 5
        x_index = np.random.random(point_count)
        y_index = np.random.random(point_count)

        color_list = np.random.random(point_count)
        scale_list = np.random.random(point_count) * 100

        plt.scatter(x_index, y_index, s=scale_list, c=color_list, marker="^")

        plt.pause(0.001)

    plt.ioff()

    plt.show()

# 动态图像：https://juejin.cn/post/7033368966081085470


def demo2():
    plt.ion()
    t0 = time.time()
    while True:
        plt.clf()
        # plt.subplot(1, 2, 1)
        plt.title('曲线图')
        plt.xlabel('时间(x)')
        plt.ylabel('数值')
        plt.ylim(-2, 2)
        t = time.time()-t0
        x = np.arange(t, t+8, 0.1)
        y1 = np.sin(x)
        y2 = np.sin(x*3)/3
        y3 = np.sin(x*5)/5
        y4 = np.sin(x*7)/7

        plt.plot(x, y1, color='r', linestyle=':', label='y=sin(t)/1')
        plt.plot(x, y2, color='g', linestyle=':', label='y=sin(3t)/3')
        plt.plot(x, y3, color='b', linestyle=':', label='y=sin(5t)/5')
        plt.plot(x, y4, color='#0ff', linestyle=':', label='y=sin(7t)/7')

        plt.legend(loc='upper right')
        plt.pause(0.05)


def demo3():
    v0 = 0.1
    h0 = 1000
    g = 9.8
    plt.ion()
    t0 = time.time()
    while True:
        plt.ylim(0, 1000)
        plt.xlim(0, 1.5)
        plt.xlim()
        t = time.time()-t0
        t_array = np.arange(t, t+1, 0.01)
        x = v0*t_array
        y = h0-0.5*g*(t_array**2)
        plt.plot(x, y, color='r', linestyle=':')
        plt.pause(0.01)
demo3()