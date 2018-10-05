import KNN
import importlib
importlib.reload(KNN)
# datingDataMat, datingLabels = KNN.file2matrix('datingTestSet2.txt')
# normMat, ranges, minVals = KNN.autoNorm(datingDataMat)
KNN.classifyPerson()


