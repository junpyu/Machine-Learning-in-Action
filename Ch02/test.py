import KNN
import importlib
importlib.reload(KNN)
datingDataMat, datingLabels = KNN.file2matrix('datingTestSet2.txt')
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
fig = plt.figure()
ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
# plt.show()
font = FontProperties(fname=r"c:\windows\fonts\DengXian.ttf", size=15)
labelsShowSizeColor = [x*20 for x in datingLabels]
# datingDataMat矩阵的第二、第三列数据
# ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], labelsShowSizeColor, labelsShowSizeColor)
# plt.title("datingDataMat矩阵的第二、第三列数据", fontproperties=font)
# plt.xlabel('玩视频游戏所耗时间百分比', fontproperties=font)
# plt.ylabel('每周消费的冰淇淋公升数', fontproperties=font)
# datingDataMat矩阵的第一、第二列数据
ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], labelsShowSizeColor, labelsShowSizeColor)
plt.title("datingDataMat矩阵的第二、第三列数据", fontproperties=font)
plt.xlabel('每年获取的飞行常客里程数', fontproperties=font)
plt.ylabel('玩视频游戏所耗时间百分比', fontproperties=font)
# import matplotlib.patches as mpatches
# red_patch = mpatches.Patch(color='#FDE725', joinstyle='round', label='The red data')
# blue_patch = mpatches.Patch(color='blue', label='The blue data')
# plt.legend(handles=[red_patch, blue_patch])
colors = ["#440154", "#21918C", '#FDE725'] 
texts = ["didntLike", "smallDoses", "largeDoses"]
ms = [5, 7, 9]
patches = [ plt.plot([],[], marker="o", ms=ms[i], ls="", mec=None, color=colors[i], 
      label="{:s}".format(texts[i]))[0] for i in range(len(texts)) ] 
plt.legend(handles=patches,loc='upper left', ncol=1, facecolor="plum", numpoints=1) 
plt.show()