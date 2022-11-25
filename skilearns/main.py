import numpy as np
from sklearn import datasets
digits = datasets.load_digits()
# 输出数据集的样本数与特征数
print (digits.data.shape)
# 输出所有目标类别
print (np.unique(digits.target))
# 输出数据集
print (digits.data)

import matplotlib.pyplot as plt
# 导入字体管理器，用于提供中文支持
import matplotlib.font_manager as fm
font_set= fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc', size=14)

# 将图像和目标标签合并到一个列表中
images_and_labels = list(zip(digits.images, digits.target))

# 打印数据集的前8个图像
plt.figure(figsize=(8, 6))
for index, (image, label) in enumerate(images_and_labels[:8]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r,interpolation='nearest')
    plt.title(u'训练样本：' + str(label), fontproperties=font_set)

plt.show()
