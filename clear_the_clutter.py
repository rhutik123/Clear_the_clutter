import os, shutil

extentions = {
    "audio" : (".mp3",".MP3",".3GP",".WAV",".3gp"),
    "video" : (".MP4",".mp4", ".MKV",".mkv",".AVI",".avi"),
    "image" : (".jpg",".JPG", ".png", ".PNG"),
    "documents" : (".py",".txt",".pdf")
}


folderpath = input("Enter the folder path here : ")

def file_finder(folderpath, file_extentions):
    files = []
    for item in os.listdir(folderpath):
        for extention in file_extentions:
            if item.endswith(extention):
                files.append(item)
    return files

for file_type, type_extention in extentions.items():
    for doc in file_finder(folderpath, type_extention):
        try:
            folder_path = os.path.join(folderpath, file_type)
            os.mkdir(folder_path)
        except FileExistsError:
            pass
        except:
            pass
        doc_path = os.path.join(folderpath, doc)
        doc_new_path = os.path.join(folder_path, doc)
        shutil.move(doc_path, doc_new_path)
