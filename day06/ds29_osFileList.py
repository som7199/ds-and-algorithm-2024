# file : ds29_osFileList.py
# desc : 윈도우 파일 리스트

import os
# import sys

# print(sys.executable)
fnameAry = []
folderName = 'C:/Sources/ds-and-algorithm-2024/day06'

for dirName, subDirList, fnames in os.walk(folderName):
    for fname in fnames:
        fnameAry.append(fname)
    
print(len(fnameAry))
print(fnameAry)