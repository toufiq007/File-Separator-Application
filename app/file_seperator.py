import os,shutil

# file extensions --> you can write every single extensions inside the tuple

folders = {
    'audios' : ['.mp3','.mp4','.wav','.flac'],
    'videos' : ['.mp4','.mkv','.MKV','.flv','.mpeg'],
    'images' : ['.jpg','.jepg','png'],
    'documents' : ['.pdf','.doc','.txt','.xlsx','.rar','.zip','.xls','pptx'],

}

# for folder_name in folders:
#     print(folder_name,folders[folder_name])
    

# directory = input('Enter your locations: ')

def create_move(extension,file_name):
    fname = False
    for folder_name in folders:
        if '.'+extension in folders[folder_name]:
            # print('.'+extension,folder_name)
            if folder_name not in os.listdir(directory):
                os.mkdir(os.path.join(directory,folder_name))
            
            shutil.move(os.path.join(directory,file_name),os.path.join(directory,folder_name))
            fname=True
            break
    if fname !=True:
        if other_name not in os.listdir(directory):
            os.mkdir(os.path.join(directory,other_name))
        
        shutil.move(os.path.join(directory,file_name),os.path.join(directory,other_name))





directory = "F:\\myfile"
other_name = input('Enter other name: ')
all_files = os.listdir(directory)
# print(all_files)


for i in all_files:
    if os.path.isfile(os.path.join(directory,i))== True:
        create_move(i.split('.')[-1],i)





















