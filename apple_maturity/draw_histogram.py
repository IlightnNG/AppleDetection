import matplotlib.pyplot as plt
import numpy as np


def main(file_name):
    with open(file_name, 'r') as file:
        #16-mature 17-pmature 18-immature
        line_content = file.readlines()
        all_count =0
        for line in line_content:
            if line[0] !=' ':    #Avoiding read failures caused by automatic line breaks
                index = line.find('-')
                count = int(line[:index])
                all_count +=count
        maturity = [0] *all_count

        i = 0
        for line in line_content:
            index = line.find('-')
            if index != -1:
                count = int(line[:index])
                index1 = line.find('[')
                index2 = line.find(']')
                if index1 != -1 and index2 != -1 :  #[16....16]
                    for j in range(0,count):
                        maturity[i] = line[index1 + j*3 +2]
                        i+=1
                else:                               #[16..(24*16)...16
                    for j in range(0,24):
                        maturity[i] = line[index1 + j*3 +2]
                        i+=1
            else:
                for j in range(0,count-24):
                        maturity[i] = line[ j*3 +2]
                        i+=1

                



        # 绘制直方图
        fig, ax = plt.subplots()
        ax.hist(maturity, bins=10, density=False, alpha=0.5, color='blue')

        # 设置图表标题和坐标轴标签
        ax.set_title('the Histogram of the Maturity of Apples', fontsize=16)
        ax.set_xlabel('Maturity', fontsize=14)
        ax.set_ylabel('Frequency', fontsize=14)

        # 设置坐标轴刻度标签大小
        ax.tick_params(axis='both', which='major', labelsize=12)

        # 显示图表
        plt.show()
     
file_path = "D:\SSD\deep-learning-for-image-processing-master\deep-learning-for-image-processing-master\pytorch_object_detection\ssd\\apple_maturity\\apple_maturity.txt"  

if __name__ == "__main__":
    main(file_path)

    