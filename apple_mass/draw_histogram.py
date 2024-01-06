import matplotlib.pyplot as plt
import numpy as np


def main(file_name):
    with open(file_name, 'r') as file:
        line_content = file.readlines()
        per_mass = [0] *len(line_content)
        i = 0
        flag = True
        for line in line_content:
            index1 = line.index('.')
            imagename = line[:index1]
            if flag:
                fimagename = imagename
                flag = False                
            index2 = line.index('[')
            index3 = line.index(']')
            if index1 != -1 and index2 != -1 and index3 != -1:
                mass = float(line[index2+1:index3])
                if imagename ==fimagename:
                    per_mass[i] += mass
                else:
                    i+=1
                    per_mass[i] += mass

                

        # 绘制直方图
        fig, ax = plt.subplots()
        ax.hist(per_mass, bins=10, density=False, alpha=0.5, color='blue')

        # 设置图表标题和坐标轴标签
        ax.set_title('the Histogram of the Masses of Apples', fontsize=16)
        ax.set_xlabel('Mass', fontsize=14)
        ax.set_ylabel('Frequency', fontsize=14)

        # 设置坐标轴刻度标签大小
        ax.tick_params(axis='both', which='major', labelsize=12)

        # 显示图表
        plt.show()
     
file_path = "D:\SSD\deep-learning-for-image-processing-master\deep-learning-for-image-processing-master\pytorch_object_detection\ssd\\apple_mass\\apple_mass.txt"  

if __name__ == "__main__":
    main(file_path)

    