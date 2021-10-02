"""
1. Keep all your downloaded course files in a separate folder.
2. Copy the location of the folder.
3. Run the program.
4. Paste the location.
5. You have the required sub-folders in that folder now.
6. You may delete the old files.
"""

from os import listdir, chdir, mkdir, getcwd
from os.path import isdir, join, isfile
from datetime import datetime
from shutil import copy2


def folderizer(filename, path):
    fileNameList = filename.split(sep='_')
    # print(fileNameList)
    if isdir(fileNameList[0]):
        chdir(fileNameList[0])
    else:
        mkdir(fileNameList[0])
        chdir(fileNameList[0])

    if isdir(fileNameList[1]):
        chdir(fileNameList[1])
    else:
        mkdir(fileNameList[1])
        chdir(fileNameList[1])
    #
    try:
        date = datetime.strptime(fileNameList[7], '%d-%b-%Y')
    except ValueError:
        try:
            date = datetime.strptime(fileNameList[7], '%d-%m-%Y')
        except ValueError:
            print('Not a Valid Date')
    date = date.strftime('%Y-%m-%d')
    coreName = ' '.join(fileNameList[8:])
    newFileName = date + ' ' + fileNameList[6] + ' ' + coreName
    print(newFileName)
    copy2(path + '\\' + filename, newFileName)
    chdir(path)


if __name__ == '__main__':
    path = input("Enter the path of the file: ")
    chdir(path)
    files = (file for file in listdir(path)
             if isfile(join(path, file)))
    for f in files:
        folderizer(f, path)
