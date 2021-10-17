import os
import time
import shutil

def main():
    deletedFolderCount = 0
    deletedFilesCount = 0
    path = input('Enter the path of the directory: ')
    days = 2
    seconds = time.time()-(days*24*60*60)

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds>=getFileOrFolderAge(root_folder):
                removefolder(root_folder)
                deletedFolderCount+=1
                break
            else:
                for folder in folders:
                    folderPath = os.path.join(root_folder,folder)
                    if seconds>=getFileOrFolderAge(folderPath):
                        removefolder(folderPath)
                        deletedFolderCount+=1
                for file in files:
                    filePath = os.path.join(root_folder,file)
                    if seconds>=getFileOrFolderAge(filePath):
                        removeFile(filePath)
                        deletedFilesCount+=1
    
    else:
        print('Path is not found')
    print('total folders deleted: ',deletedFolderCount,'total files deleted: ',deletedFilesCount)

def removefolder(path):
    if not shutil.rmtree(path):
        print('removed', path)
    else:
        print('unable to remove',path)

def removefile(path):
    if not os.remove(path):
        print('removed', path)
    else:
        print('unable to remove',path)

def getFileOrFolderAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()