import os,shutil

dict_folders = {
    'audios' : ['.mp3','.mp4','.wav','.flac'],
    'videos' : ['.mp4','.mkv','.MKV','.flv','.mpeg'],
    'images' : ['.jpg','.jepg','png','.gif'],
    'documents' : ['.doc','.txt','.pptx'],
    'excel_sheets' : ['.xls','.xlsx'],
    'pdf_files' : ['.pdf'],
    'application' : ['.exe'],
    'zip_files' : ['.zip','.rar',]

}


def rename_folder():
    for folder in os.listdir(directory):
        if os.path.isdir(os.path.join(directory,folder)) ==True:
            os.rename(os.path.join(directory,folder),os.path.join(directory,folder.lower()))


def create_move(extensions,file_name):
    find = False
    for folder_name in dict_folders:
        if '.'+extensions in dict_folders[folder_name]:
            if folder_name not in os.listdir(directory):
                os.mkdir(os.path.join(directory,folder_name))
            shutil.move(os.path.join(directory,file_name),os.path.join(directory,folder_name))
            find = True
            break
    if find != True:
        if others_file not in os.listdir(directory):
            os.mkdir(os.path.join(directory,others_file))
        shutil.move(os.path.join(directory,file_name),os.path.join(directory,others_file))
    



directory = input('Enter your folder or directory path: ')
all_files = os.listdir(directory)
rename_folder()
others_file = input('Enter folder name for others file: ')
length = len(all_files)
count=1

for file in all_files:
    if os.path.isfile(os.path.join(directory,file)) == True:
        create_move(file.split('.')[-1],file)
    print(f' Total files: {length} || Done: {count} || Left: {length-count} ')
    count+=1