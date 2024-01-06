import matplotlib.pyplot as plt
import numpy as np


def main(file_name):
    with open(file_name, 'r') as file:
        line_content = file.readlines()
        #name = [""] *len(line_content)
        count = [0] *len(line_content)
        i = 0
        for line in line_content:
            index1 = line.index('.')
            index2 = line.index('[')
            index3 = line.index(']')
            if index1 != -1 and index2 != -1 and index3 != -1:
                #name[i] = line[:index1]
                count[i] = int(line[index2+1:index3])
            i+=1
                

        # 绘制直方图
        fig, ax = plt.subplots()
        ax.hist(count, bins=10, density=False, alpha=0.5, color='blue')

        # 设置图表标题和坐标轴标签
        ax.set_title('the Histogram of the Number of Apples', fontsize=16)
        ax.set_xlabel('Count', fontsize=14)
        ax.set_ylabel('Frequency', fontsize=14)

        # 设置坐标轴刻度标签大小
        ax.tick_params(axis='both', which='major', labelsize=12)

        # 显示图表
        plt.show()
     
file_path = "D:\SSD\deep-learning-for-image-processing-master\deep-learning-for-image-processing-master\pytorch_object_detection\ssd\\apple_count\\apple_count.txt"  

if __name__ == "__main__":
    main(file_path)

    