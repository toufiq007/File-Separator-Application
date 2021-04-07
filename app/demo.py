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
            found=True
            break
    
    if found!= True:
        if others_name not in os.listdir(directory):
            os.mkdir(os.path.join(directory,others_name))
        shutil.move(os.path.join(directory,file_name),os.path.join(directory,others_name))
    


directory = "Enter your file or folder path: "
all_files = os.listdir(directory)
others_name = 'Enter the others folder locations: '

for file in all_files:
    if os.path.isfile(os.path.join(directory,file)) == True:
        create_move(file.split('.')[-1],file)

