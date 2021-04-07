import os,shutil

folders = {
    'audios' : ['.mp3','.mp4','.wav','.flac'],
    'videos' : ['.mp4','.mkv','.MKV','.flv','.mpeg'],
    'images' : ['.jpg','.jepg','png'],
    'documents' : ['.pdf','.doc','.txt','.xlsx','.rar','.zip','.xls','.pptx'],
}

def create_move(extension,file_name):
    found = False
    for folder_name in folders:
        if '.'+extension in folders[folder_name]:
            if folder_name not in os.listdir(directory):
                os.mkdir(os.path.join(directory,folder_name))
            shutil.move(os.path.join(directory,file_name),os.path.join(directory,folder_name))
            found = True
            break
    if found !=True:
        if other_name not in os.listdir(directory):
            os.mkdir(os.path.join(directory,other_name))
        
        shutil.move(os.path.join(directory,file_name),os.path.join(directory,other_name))




directory = "F:\\myfile"
all_files = os.listdir(directory)
other_name = input('Enter the others directory: ')

for i in all_files:
    if os.path.isfile(os.path.join(directory,i))==True:
        create_move(i.split('.')[-1],i)







