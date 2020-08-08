from tkinter import *
import os, shutil
from tkinter import messagebox, ttk, PhotoImage, filedialog
import time

class main_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Clear The Clutter")
        self.root.geometry("800x600+100+100")
        self.root.config(bg="#F9DDA4")
        self.root.resizable(False, False)

        self.extentions = {
                    "audio" : (".mp3",".wv",".3gp", '.oog', '.flac', '.mp4a', '.wma', '.wv', '.webm', '.m4p'),
                    "video" : (".mp4",".mkv",".avi", '.flv', '.ogv', '.gif', '.mov', '.qt', '.wmv', '.rm', '.rmvb', '.m4v', '.svi'),
                    "image" : (".jpg", ".png", '.webp', '.tiff','.psd','.raw','.bmp','.jpeg','.svg','.ai','.esp'),
                    "documents" : (".py",".txt",".pdf",'.7z','.rar','.zip','.deb','.pkg','.rpm','.tar','.z','.iso','.bin','.dmg','.csv','.sql','.htm','.html','.js','.apk','.msi','.exe','.xhtml','.jar')
                    }

        # variables

        self.folderpathvar = StringVar()

        heading = Label(root, text="Clear the Clutter", font=("Monospace", 25, "bold"), bd=10, relief=GROOVE, bg="cyan", fg="crimson").place(x=0, y=0, relwidth="1")

        self.folderpathlbl = Label(root, text="Choose Folder : ", bg="#F9DDA4",font=("monospace", 18, 'bold')).place(x=50, y=90)
        self.folderpathtxt = Entry(root, width="35", textvariable=self.folderpathvar,font=("monospace", 13), bd=7, relief=RIDGE).place(x=270, y=90)
        self.folderpathbtn = Button(root, text="Browse",bg="#758AA2", font=("monospace", 15, "bold"), bd=7, relief=RIDGE, command=self.browse).place(x=650, y=85)

        extent_frame = LabelFrame(root, text="Various Extention Supports",font=("monospace", 15, 'bold'),bg="#53E0BC", bd=8, relief=GROOVE,).place(x=30, y=160, width=750, height=100)

        self.image_comb = ttk.Combobox(extent_frame, width=10,state='readonly', font=("monospace", 15, 'bold'))
        for key, value in self.extentions.items():
            if key == 'image':
                image_ext = value
                image_ext = ('images',) + image_ext
        self.image_comb['values'] = image_ext
        self.image_comb.current(0)
        self.image_comb.place(x=60, y=200)

        self.video_comb = ttk.Combobox(extent_frame, width=10,state='readonly', font=("monospace", 15, 'bold'))
        for key, value in self.extentions.items():
            if key == 'video':
                video_ext = value
                video_ext = ('videos',) + video_ext
        self.video_comb['values'] = video_ext
        self.video_comb.current(0)
        self.video_comb.place(x=400, y=200)

        self.audio_comb = ttk.Combobox(extent_frame, width=10,state='readonly', font=("monospace", 15, 'bold'))
        for key, value in self.extentions.items():
            if key == 'audio':
                audio_ext = value
                audio_ext = ('audio',) + audio_ext
        self.audio_comb['values'] = audio_ext
        self.audio_comb.current(0)
        self.audio_comb.place(x=220, y=200)

        self.documents_comb = ttk.Combobox(extent_frame, width=10,state='readonly', font=("monospace", 15, 'bold'))
        for key, value in self.extentions.items():
            if key == 'documents':
                doc_ext = value
                doc_ext = ('documents',) + doc_ext
        self.documents_comb['values'] = doc_ext
        self.documents_comb.current(0)
        self.documents_comb.place(x=580, y=200)

        self.main_frame = Frame(root, bd=7,relief=RIDGE, bg="#7CEC9F").place(x=30, y=270, width=745, height=270)

        total_lbl = Label(self.main_frame, bg="#7CEC9F",text="Total : ", font=("monospace", 18, 'bold')).place(x=50, y=290)

        self.image_img = PhotoImage(file='photo.png')
        self.audio_img = PhotoImage(file='audio.png')
        self.video_img = PhotoImage(file='video.png')
        self.doc_img = PhotoImage(file='documents.png')

        self.image_lbl = Label(self.main_frame, image=self.image_img, bd=5, relief=RAISED).place(x=80, y=340)
        self.audio_lbl = Label(self.main_frame, image=self.audio_img, bd=5, relief=RAISED).place(x=240, y=340)
        self.video_lbl = Label(self.main_frame, image=self.video_img, bd=5, relief=RAISED).place(x=400, y=340)
        self.doc_lbl = Label(self.main_frame, image=self.doc_img, bd=5, relief=RAISED).place(x=570, y=340)

        status = Label(root, text="STATUS :", bg="#F9DDA4",font=("times new roman", 20, 'bold')).place(x=45, y=560)
        self.totalbl = Label(root, text="Total :", bg="#F9DDA4",font=("times new roman", 17, 'bold')).place(x=180, y=560)
        self.movedlbl = Label(root, text="Moved :", bg="#F9DDA4",font=("times new roman", 17, 'bold')).place(x=310, y=560)
        self.leftlbl = Label(root, text="Left :", bg="#F9DDA4",font=("times new roman", 17, 'bold')).place(x=460, y=560)


        self.clear_btn = Button(root, text="Clear", bg="#758AA2",font=("Times new roman",16, 'bold'), bd=5, relief=RIDGE).place(x=570, y=550)
        self.start_btn = Button(root, text="Start",bg="#758AA2", font=("Times new roman",16, 'bold'), bd=5, relief=RIDGE, command=self.start).place(x=660, y=550)

    def browse(self):
        self.folderpath = filedialog.askdirectory(title="Select the folder")
        self.folderpathvar.set(self.folderpath)
        self.total_files = len(os.listdir(self.folderpath))
        self.total_num = Label(self.main_frame, bg="#7CEC9F",text=self.total_files, font=("monospace", 20, "bold")).place(x=180, y=290)

        self.image_file = 0
        self.audio_file = 0
        self.video_file = 0
        self.doc_file = 0

        for doc in os.listdir(self.folderpath):
            for key, value in self.extentions.items():
                if doc.endswith(value):
                    if key == 'image':
                        self.image_file += 1
                    if key == 'audio':
                        self.audio_file += 1
                    if key == 'video':
                        self.video_file += 1
                    if key == 'documents':
                        self.doc_file += 1


        self.image_num = Label(self.main_frame,text=self.image_file, bg="#7CEC9F",font=("times new roman", 20, 'bold')).place(x=120, y=480)
        self.audio_num = Label(self.main_frame,text=self.audio_file, bg="#7CEC9F",font=("times new roman", 20, 'bold')).place(x=275, y=480)
        self.video_num = Label(self.main_frame,text=self.video_file, bg="#7CEC9F",font=("times new roman", 20, 'bold')).place(x=450, y=480)
        self.doc_num = Label(self.main_frame,text=self.doc_file, bg="#7CEC9F",font=("times new roman", 20, 'bold')).place(x=620, y=480)
        self.totalnum = Label(root, text=self.total_files, bg="#F9DDA4",font=("times new roman", 17, 'bold')).place(x=250, y=560)

    def file_finder(self,folderpath, file_extentions):
        files = []
        for item in os.listdir(folderpath):
            for extention in file_extentions:
                if item.endswith(extention):
                    files.append(item)
        return files


    def start(self):
        for file_type, type_extention in self.extentions.items():
            for doc in self.file_finder(self.folderpath, type_extention):
                try:
                    self.folder_path = os.path.join(self.folderpath, file_type)
                    os.mkdir(self.folder_path)
                except FileExistsError:
                    pass
                except:
                    pass
                doc_path = os.path.join(self.folderpath, doc)
                doc_new_path = os.path.join(self.folder_path, doc)
                shutil.move(doc_path, doc_new_path)
        
        self.left_num = 0
        self.moved_num = self.total_files
        self.movednum = Label(root, text=self.moved_num, bg="#F9DDA4",font=("times new roman", 17, 'bold')).place(x=400, y=560)
        self.leftnum = Label(root, text=self.left_num, bg="#F9DDA4",font=("times new roman", 17, 'bold')).place(x=520, y=560)
        messagebox.showinfo("Sucess", "Successfully creaded the clutter!!!")


root=Tk()
obj = main_app(root)
root.mainloop()