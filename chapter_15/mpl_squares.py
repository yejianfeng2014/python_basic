import matplotlib.pyplot as plt
#折线图
squares = [1, 4, 9, 16, 25]
#设置标题和文字，线条粗细
plt.plot(squares,linewidth =1)
plt.xlabel('value',fontsize =15)
plt.title('first pic')
plt.ylabel('ylabel',fontsize =12)


plt.grid()
plt.show()