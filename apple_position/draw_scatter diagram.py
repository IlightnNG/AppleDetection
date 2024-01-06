import matplotlib.pyplot as plt
import numpy as np


def main(file_name):
    with open(file_name, 'r') as file:
        line_content = file.readlines()
        x = [0] *len(line_content)
        y = [0] *len(line_content)
        i = 0
        for line in line_content:
            index1 = line.index('[')
            index2 = line.index(',')
            index3 = line.index(']')
            if index1 != -1 and index2 != -1 and index3 != -1:
                x[i] = float(line[index1+1:index2])
                y[i] = float(line[index2+1:index3])
            i+=1
                

        # 创建一个绘图窗口，大小为8x6英寸
        plt.figure(figsize=(8, 6))

        # 绘制散点图
        plt.scatter(x, y, s=50, alpha=0.5)

        # 添加标题和轴标签
        plt.title('the Scatter Diagram of the Position of Apple')
        plt.xlabel('x')
        plt.ylabel('y')
        # 显示图像
        plt.show()
     
file_path = "D:\SSD\deep-learning-for-image-processing-master\deep-learning-for-image-processing-master\pytorch_object_detection\ssd\\apple_position\\apple_position.txt"  

if __name__ == "__main__":
    main(file_path)

    