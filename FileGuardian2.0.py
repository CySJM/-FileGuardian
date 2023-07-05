from tkinter import *
from tkinter import filedialog
import os
from cryptography.fernet import Fernet
import fnmatch


########################################################################
#Master Screen
global Master
Master = Tk()
Master.title("File Guardian Ver1.0")
Master.resizable(width=False,height=False)
icon = PhotoImage(file='C:\\Users\\Jon\\Desktop\\Python Workshop\\lockerimg80x80.png')
Master.iconphoto(True,icon)
app_height = 680
app_width = 530
screen_width = Master.winfo_screenwidth()
screen_height = Master.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
Master.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


#Sub Screens
def Main_Screen():
    Master.config(background='black')
    Tool_Name_Label.place(x=65, y=0, height=60, width=400)
    Tool_Desc_Label.place(x=60, y=65, height=50, width=400)
    Tool_Photo_Label.place(x=5, y=110, height=520, width=520)
    Entry_Button.place(x=60, y=630, height=50, width=400)


def Warning_Screen():
    Tool_Name_Label.destroy()
    Tool_Desc_Label.destroy()
    Tool_Photo_Label.destroy()
    Entry_Button.destroy()
    Master.config(background='red')
    Create_Warning_Img_1_Img2_Label_Variables()
    Warning_Img_1.place(x=50, y=0, width=100, height=100)
    Warning_Label.place(x=150, y=0, width=230, height=100)
    Warning_Img_2.place(x=380, y=0, width=100, height=100)
    Warning_Text1.place(x=0, y=100, width=530, height=440)
    Create_Warning_Exit_Button()
    Proceed_Button1.place(x=115, y=560, width=300, height=50)
    Dont_Proceed_Button.place(x=115, y=620, width=300, height=50)

    
def Drive_Selection_Screen():
    Warning_Img_1.destroy()
    Warning_Label.destroy()
    Warning_Img_2.destroy()
    Warning_Text1.destroy()
    Proceed_Button1.destroy()
    Dont_Proceed_Button.destroy()
    Master.config(background='blue')
    Select_Directory_To_Encrypt_Button.place(x=115, y=10, width=300, height=50)
    Select_Directory_To_Decrypt_Button.place(x=115, y=70, width=300, height=50)
    Drive_Selection_Screen_Exit_Button.place(x=115, y=130, width=300, height=50)
    Encrypt_Decrypt_Label.place(x=115, y=190, width=300, height=25)
    Directory_Listbox_Frame.place(x=65, y=225, width=400, height=370)
    Directory_Listbox.config(bg='#a8bce3',
                             fg='black',
                             font=('Dubai',15))
    Directory_Listbox.pack(fill=BOTH)

def Generate_Key_Screen():
    Select_Directory_To_Encrypt_Button.destroy()
    Select_Directory_To_Decrypt_Button.destroy()
    Drive_Selection_Screen_Exit_Button.destroy()
    Encrypt_Decrypt_Label.destroy()
    Directory_Listbox_Frame.destroy()
    Generate_Encryption_Key_Button.destroy()
    Generate_Key_Button.place(x=115, y=10, width=300, height=50)
    Generate_Key_Screen_Exit_Button.place(x=115, y=70, width=300, height=50)
    Generated_Key_Label.place(x=115, y=190, width=300, height=25)
    Key_Listbox_Frame.place(x=65, y=225, width=400, height=370)
    Key_Listbox.config(bg='#a8bce3',
                       fg='black',
                       font=('Dubai',15))
    Key_Listbox.pack(fill=BOTH)

def Encrypt_Warning_Screen():
    Generate_Key_Button.destroy()
    Generate_Key_Screen_Exit_Button.destroy()
    Generated_Key_Label.destroy()
    Key_Listbox_Frame.destroy()
    Encrypt_Files_Button.destroy()
    Master.config(background='red')
    Create_Warning_Img_1_Img2_Label_Variables()
    Warning_Img_1.place(x=50, y=0, width=100, height=100)
    Warning_Label.place(x=150, y=0, width=230, height=100)
    Warning_Img_2.place(x=380, y=0, width=100, height=100)
    Warning_Text2.place(x=0, y=100, width=530, height=440)
    Create_Warning_Exit_Button()
    Proceed_Button2.place(x=115, y=560, width=300, height=50)
    Dont_Proceed_Button.place(x=115, y=620, width=300, height=50)
    

def Decryption_Key_Screen():
    Select_Directory_To_Encrypt_Button.destroy()
    Select_Directory_To_Decrypt_Button.destroy()
    Drive_Selection_Screen_Exit_Button.destroy()
    Encrypt_Decrypt_Label.destroy()
    Directory_Listbox_Frame.destroy()
    Get_Decryption_Key_Screen_Button.destroy()
    Get_Decryption_Key_Button.place(x=115, y=10, width=300, height=50)
    Get_Decryption_Key_Screen_Exit_Button.place(x=115, y=70, width=300, height=50)
    Decryption_Key_Listbox_Label.place(x=115, y=190, width=300, height=25)
    Decryption_Key_Listbox_Frame.place(x=65, y=225, width=400, height=370)
    Decryption_Key_Listbox.config(bg='#a8bce3',
                                  fg='black',
                                  font=('Dubai',15))
    Decryption_Key_Listbox.pack(fill=BOTH)
    

def Encrypt_Files_Post_Operation_Screen():
    Warning_Img_1.destroy()
    Warning_Label.destroy()
    Warning_Img_2.destroy()
    Warning_Text2.destroy()
    Proceed_Button2.destroy()
    Dont_Proceed_Button.destroy()
    Master.config(background='blue')
    Status_Label.place(x=115, y=30, width=300, height=25)
    Final_Operation_Listbox_Frame.place(x=65, y=65, width=400, height=370)
    Final_Operation_Listbox.config(bg='#a8bce3',
                                   fg='black',
                                   font=('Dubai',15))
    Final_Operation_Listbox.pack(fill=BOTH)
    Display_Status()
    Combined_Post_Operation_Screen_Exit_Button.place(x=115, y=620, width=300, height=50)


def Decrypt_Files_Post_Operation_Screen():
    Get_Decryption_Key_Button.destroy()
    Get_Decryption_Key_Screen_Exit_Button.destroy()
    Decryption_Key_Listbox_Label.destroy()
    Decryption_Key_Listbox_Frame.destroy()
    Decrypt_Files_Button.destroy()
    Master.config(background='blue')
    Status_Label.place(x=115, y=30, width=300, height=25)
    Final_Operation_Listbox_Frame.place(x=65, y=65, width=400, height=370)
    Final_Operation_Listbox.config(bg='#a8bce3',
                                   fg='black',
                                   font=('Dubai',15))
    Final_Operation_Listbox.pack(fill=BOTH)
    Display_Status()
    Combined_Post_Operation_Screen_Exit_Button.place(x=115, y=620, width=300, height=50)


########################################################################
#background code
def Combined_Encrypt_Command():
    Clear_Directory_Listbox()
    Get_Files_To_Encrypt()  
    
    
def Combined_Decrypt_Command():
    Clear_Directory_Listbox()
    Get_Files_To_Decrypt()


def Clear_Directory_Listbox():
    Directory_Listbox.delete(0,END)
    try:
        Generate_Encryption_Key_Button.destroy()
    except:
        pass
    try:
        Get_Decryption_Key_Screen_Button.destroy()
    except:
        pass
    

def No_Directory_Selected_Error():
    Directory_Listbox.insert(END,"Error:" + "\n\n")
    Directory_Listbox.insert(END,"Either:" + "\n")
    Directory_Listbox.insert(END,"No directory was selected" + "\n")
    Directory_Listbox.insert(END,"Or:" + "\n")
    Directory_Listbox.insert(END,"You did not select a root directory" + "\n")
    Directory_Listbox.insert(END,"To proceed: select a root directory")
    Directory_Listbox.insert(END,"Select the removable drive root directory" + "\n")
    

def Get_Files_To_Encrypt():
    root_directory = filedialog.askdirectory(title="Select Removable Drive To Encrypt",initialdir='D:\\')
    
    #check if selected directory is a root directory
    if root_directory and os.path.isdir(root_directory) and os.path.ismount(root_directory):
        global files_to_be_encrypted
        files_to_be_encrypted = []
        
        # Recursively iterate over directories and files using os.walk()
        for dirpath, dirnames, filenames in os.walk(root_directory):
            if dirpath != "D:/System Volume Information":
                # Iterate over files in the current directory
                for filename in filenames:
                    # Create the full path of the file
                    file_path = os.path.join(dirpath, filename)
                    # Add the file path to the list
                    files_to_be_encrypted.append(file_path)
        
        for file in files_to_be_encrypted:
            Directory_Listbox.insert(END,file + "\n")
        
        global Generate_Encryption_Key_Button
        Generate_Encryption_Key_Button = Button(Master,
                                 text="Generate Encryption Key",
                                 font=('Dubai',15),
                                 command=Generate_Key_Screen,
                                 activebackground='green',
                                 activeforeground='black')
        Generate_Encryption_Key_Button.place(x=115, y=620, width=300, height=50)

    else:
        No_Directory_Selected_Error()
        

def Get_Files_To_Decrypt():
    root_directory = filedialog.askdirectory(title="Select Removable Drive To Encrypt",initialdir='D:\\')
    
    #check if selected directory is a root directory
    if root_directory and os.path.isdir(root_directory) and os.path.ismount(root_directory):
        global files_to_be_decrypted
        files_to_be_decrypted = []
        
        # Recursively iterate over directories and files using os.walk()
        for dirpath, dirnames, filenames in os.walk(root_directory):
            if dirpath != "D:/System Volume Information":
                # Iterate over files in the current directory
                for filename in filenames:
                    # Create the full path of the file
                    file_path = os.path.join(dirpath, filename)
                    # Add the file path to the list
                    files_to_be_decrypted.append(file_path)
        
        for file in files_to_be_decrypted:
            Directory_Listbox.insert(END,file + "\n")
        
        global Get_Decryption_Key_Screen_Button
        Get_Decryption_Key_Screen_Button = Button(Master,
                                           text="Get Decryption Key",
                                           font=('Dubai',15),
                                           command=Decryption_Key_Screen,
                                           activebackground='green',
                                           activeforeground='black')
        Get_Decryption_Key_Screen_Button.place(x=115, y=620, width=300, height=50)
    
    else:
        No_Directory_Selected_Error()


def Combined_Generate_Key():
    Clear_Key_Listbox()
    Generate_Key()


def Clear_Key_Listbox():
    Key_Listbox.delete(0,END)


def Generate_Key():
    global Encryption_Key
    Encryption_Key = Fernet.generate_key()
    with open("C:\\Users\\Jon\\Desktop\\TheKey.key","wb") as thekey:
        thekey.write(Encryption_Key)
    Key_Listbox.insert(END, Encryption_Key)
    global Encrypt_Files_Button
    Encrypt_Files_Button = Button(Master,
                                  text="Begin Encryption",
                                  font=('Dubai',15),
                                  command=Encrypt_Warning_Screen,
                                  activebackground='green',
                                  activeforeground='black')
    Encrypt_Files_Button.place(x=115, y=620, width=300, height=50)
    

def Encrypt_Files():
    for file in files_to_be_encrypted:
        with open(file,"rb") as thefile:
            contents = thefile.read()
        contents_ecrypted = Fernet(Encryption_Key).encrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_ecrypted)
    
    global Encrypt_Success_Msg1
    global Encrypt_Success_Msg2
    global Encrypt_Success_Msg3
    global Encrypt_Success_Msg4
    global Encrypt_Success_Msg5
            
    Encrypt_Success_Msg1 = "All files processed."
    Encrypt_Success_Msg2 = "USB drive is now secured."
    Encrypt_Success_Msg3 = "To decrypt this drive, you will need:"
    Encrypt_Success_Msg4 = "1. FileGuardian.exe"
    Encrypt_Success_Msg5 = "2. The Decryption/Encryption Key"
    
    Encrypt_Files_Post_Operation_Screen()
    

def Combined_Get_Decryption_Key():
    Clear_Decryption_Key_Listbox()
    Get_Decryption_Key()


def Clear_Decryption_Key_Listbox():
    Decryption_Key_Listbox.delete(0,END)


def Get_Decryption_Key():
    file_path = filedialog.askopenfilename(title="Select Key File",initialdir="C:\\Users\\Jon\\Desktop", filetypes=(("key files","*.key"),("all files","*.*")))
    
    if file_path:
        filename = os.path.basename(file_path)
        if fnmatch.fnmatch(filename, "*.key"):
            #Key_Listbox.delete(0,END)
            Decryption_Key_Listbox.insert(END,"You selected the follow Key file:" + "\n")
            Decryption_Key_Listbox.insert(END,str(filename) + "\n" + "\n")
            Decryption_Key_Listbox.insert(END,"Containting key:" + "\n")
            with open(file_path, "r") as file:
                global Decryption_Key
                Decryption_Key = file.read()                
                
            Decryption_Key_Listbox.insert(END, Decryption_Key)
            
            global Decrypt_Files_Button
            Decrypt_Files_Button = Button(Master,
                                          text="Begin Decryption",
                                          font=('Dubai',15),
                                          command=Decrypt_Files,
                                          activebackground='green',
                                          activeforeground='black',
                                          width=25)
            Decrypt_Files_Button.place(x=115, y=620, width=300, height=50)
        else:
            Decryption_Key_Listbox.insert(END,"The file chosen is not a valid key file" + "\n" + "\n")
            Decryption_Key_Listbox.insert(END,"Try another file")
    else:
        Decryption_Key_Listbox.insert(END,"No key file selected" + "\n" + "\n")
        Decryption_Key_Listbox.insert(END,"Select a key file to continue")


def Decrypt_Files():
    for file in files_to_be_decrypted:
        with open(file,"rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(Decryption_Key).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_decrypted)
    
    global Decrypt_Success_Msg1
    global Decrypt_Success_Msg2
         
    Decrypt_Success_Msg1 = "All files processed."
    Decrypt_Success_Msg2 = "USB drive returned to normal state."

    Decrypt_Files_Post_Operation_Screen()


def Display_Status():
    try:
        Final_Operation_Listbox.insert(END, Decrypt_Success_Msg1 + "\n\n")
        Final_Operation_Listbox.insert(END, Decrypt_Success_Msg2)
    
    except:
        pass    
        
    try:
        Final_Operation_Listbox.insert(END, Encrypt_Success_Msg1 + "\n\n")
        Final_Operation_Listbox.insert(END, Encrypt_Success_Msg2 + "\n\n")
        Final_Operation_Listbox.insert(END, Encrypt_Success_Msg3 + "\n\n")
        Final_Operation_Listbox.insert(END, Encrypt_Success_Msg4 + "\n")
        Final_Operation_Listbox.insert(END, Encrypt_Success_Msg5)
                
    except:
        pass


########################################################################
#Variables
Tool_Name_Label = Label(Master,
                  text="File Guardian V-1.0",
                  font=('Dubai',30,'bold'),
                  fg='#b929d6',
                  bg='black')
    
Tool_Desc_Label = Label(Master,
                  text="File Encyption Tool",
                  font=('Dubai',12,'bold'),
                  fg='#b929d6',
                  bg='black',
                  height=50,
                  width=400)

Tool_Photo = PhotoImage(file='C:\\Users\\Jon\\Desktop\\Python Workshop\\lockerimg520x520.png')

Tool_Photo_Label = Label(Master, image=Tool_Photo, bg='black')

Entry_Button = Button(Master,
                      text="Enter The Crypt !!",
                      command=Warning_Screen,
                      font=('Dubai',13,'bold'),
                      fg='#b929d6',
                      bg='black',
                      padx=75,
                      activebackground='green',
                      activeforeground='black')

Warning_Photo = PhotoImage(file='C:\\Users\\Jon\\Desktop\\Python Workshop\\WarningImg.png')

def Create_Warning_Img_1_Img2_Label_Variables():
    
    global Warning_Img_1
    Warning_Img_1 = Label(Master, image=Warning_Photo, bg='red')

    global Warning_Img_2
    Warning_Img_2 = Label(Master, image=Warning_Photo, bg='red')

    global Warning_Label
    Warning_Label = Label(Master,
                          text="WARNING !!",
                          font=('Dubai',30,'bold'),
                          fg='yellow',
                          bg='red')

def Create_Warning_Exit_Button():
    
    global Dont_Proceed_Button
    Dont_Proceed_Button = Button(Master,
                             text="Quit",
                             command=quit,
                             font=('Dubai',20,'bold'),
                             fg='yellow',
                             bg='red',activebackground='yellow',
                             activeforeground='black')
    
Proceed_Button1 = Button(Master,
                        text="Proceed",
                        command=Drive_Selection_Screen,
                        font=('Dubai',20,'bold'),
                        fg='yellow',
                        bg='red',
                        activebackground='yellow',
                        activeforeground='black')

Proceed_Button2 = Button(Master,
                        text="Encrypt Now",
                        command=Encrypt_Files,
                        font=('Dubai',20,'bold'),
                        fg='yellow',
                        bg='red',
                        activebackground='yellow',
                        activeforeground='black')

Warning_Text1 = Label(Master,
                     text="STOP!, before proceeding, this tool can cause catastophic damage to this computer if used on a drive other than the removabvle drive it was intended to be used on.  Do not select a drive other than the removable drive you are attempting to encrypt",
                     font=('Dubai',20,'bold'),
                     fg='yellow',
                     bg='red',
                     wraplength=500)

Warning_Text2 = Label(Master,
                      text="STOP!, This is your absolute last chance to avoid CATASTROPHIC damage to your computer.  Are you SURE, you have the right drive selected???\n\nIf so, go ahead and hit the \"Encrypt Now\" button below, otherwise, exit NOW before you destroy your computer!!!!",
                      font=('Dubai',20,'bold'),
                      fg='yellow',
                      bg='red',
                      wraplength=500)

Select_Directory_To_Encrypt_Button = Button(Master,
                                         text="Select Directory To Encrypt",
                                         font=('Dubai',15),
                                         command=Combined_Encrypt_Command,
                                         activebackground='green',
                                         activeforeground='black')

Select_Directory_To_Decrypt_Button = Button(Master,
                                         text="Select Directory To Decrypt",
                                         font=('Dubai',15),
                                         command=Combined_Decrypt_Command,
                                         activebackground='green',
                                         activeforeground='black')

Drive_Selection_Screen_Exit_Button = Button(Master,
                                            text="Exit",
                                            font=('Dubai',15),
                                            command=quit,
                                            activebackground='red',
                                            activeforeground='black')

Encrypt_Decrypt_Label = Label(Master,
                               text="Encryption/Decryption List:",
                               fg='yellow',
                               bg='blue',
                               font=('Dubai',15,'bold'))

Directory_Listbox_Frame = Frame()

Y_Scrollbar = Scrollbar(Directory_Listbox_Frame, orient=VERTICAL)
X_Scrollbar = Scrollbar(Directory_Listbox_Frame, orient=HORIZONTAL)

global Directory_Listbox
Directory_Listbox = Listbox(Directory_Listbox_Frame,
                            yscrollcommand=Y_Scrollbar.set, xscrollcommand=X_Scrollbar.set)

Y_Scrollbar.config(command=Directory_Listbox.yview)
X_Scrollbar.config(command=Directory_Listbox.xview)
Y_Scrollbar.pack(side=RIGHT, fill=Y)
X_Scrollbar.pack(side=BOTTOM, fill=X)

Generate_Key_Button = Button(Master,
                             text="Generate Key",
                             font=('Dubai',15),
                             command=Combined_Generate_Key,
                             activebackground='green',
                             activeforeground='black')

Generate_Key_Screen_Exit_Button = Button(Master,
                                         text="Exit",
                                         font=('Dubai',15),
                                         command=quit,
                                         activebackground='red',
                                         activeforeground='black')

Generated_Key_Label = Label(Master,
                            text="Key Generated:",
                            fg='yellow',
                            bg='blue',
                            font=('Dubai',15,'bold'))

Key_Listbox_Frame = Frame()

Y_Scrollbar = Scrollbar(Key_Listbox_Frame, orient=VERTICAL)
X_Scrollbar = Scrollbar(Key_Listbox_Frame, orient=HORIZONTAL)

global Key_Listbox
Key_Listbox = Listbox(Key_Listbox_Frame,
                      yscrollcommand=Y_Scrollbar.set, xscrollcommand=X_Scrollbar.set)

Y_Scrollbar.config(command=Key_Listbox.yview)
X_Scrollbar.config(command=Key_Listbox.xview)
Y_Scrollbar.pack(side=RIGHT, fill=Y)
X_Scrollbar.pack(side=BOTTOM, fill=X)

Get_Decryption_Key_Button = Button(Master,
                                   text="Get Decryption Key",
                                   font=('Dubai',15),
                                   command=Combined_Get_Decryption_Key,
                                   activebackground='green',
                                   activeforeground='black')

Get_Decryption_Key_Screen_Exit_Button = Button(Master,
                                               text="Exit",
                                               font=('Dubai',15),
                                               command=quit,
                                               activebackground='red',
                                               activeforeground='black')

Decryption_Key_Listbox_Label = Label(Master,
                             text="Decryption Key Selected:",
                             fg='yellow',
                             bg='blue',
                             font=('Dubai',15,'bold'))

Decryption_Key_Listbox_Frame = Frame()

Y_Scrollbar = Scrollbar(Decryption_Key_Listbox_Frame, orient=VERTICAL)
X_Scrollbar = Scrollbar(Decryption_Key_Listbox_Frame, orient=HORIZONTAL)

global Decryption_Key_Listbox
Decryption_Key_Listbox = Listbox(Decryption_Key_Listbox_Frame,
                                 yscrollcommand=Y_Scrollbar.set, xscrollcommand=X_Scrollbar.set)

Y_Scrollbar.config(command=Decryption_Key_Listbox.yview)
X_Scrollbar.config(command=Decryption_Key_Listbox.xview)
Y_Scrollbar.pack(side=RIGHT, fill=Y)
X_Scrollbar.pack(side=BOTTOM, fill=X)

Final_Operation_Listbox_Frame = Frame()

global Final_Operation_Listbox  
Final_Operation_Listbox = Listbox(Final_Operation_Listbox_Frame)

Status_Label = Label(Master,
                     text="Results of Encryption/Decryption:",
                     fg='yellow',
                     bg='blue',
                     font=('Dubai',15,'bold'))

Combined_Post_Operation_Screen_Exit_Button = Button(Master,
                                                    text="Exit",
                                                    font=('Dubai',15),
                                                    command=quit,
                                                    activebackground='red',
                                                    activeforeground='black',)


########################################################################
#Flow
Main_Screen()

Master.mainloop()