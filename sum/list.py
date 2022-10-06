import openpyxl
import os


workbook = openpyxl.load_workbook('data.xlsx')
worksheet = workbook['Sheet1']
sheet=workbook.active
ori = r"C:\Users\19484\Documents\LDA\sum\new"
os.chdir(ori)
fileList = os.listdir(ori)
for i in range(1,len(fileList)+1):
    with open(str(i)+".txt", "r",encoding='utf-8') as f:  # 打开文件
        data = f.read()  # 读取文件
        sheet['A'+str(i+1)]=data
    print(i)

#sheet['A1']='hi,wwu'
workbook.save('data.xlsx')
