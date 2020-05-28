version="2.1"
"""
##############################
    Transpire.
##############################
    Coded by, Dalton Overlin
##########################################################
    Last Code Revision Date: May. 23, 2020
##########################################################
    This is a program for syncing a home directory
    to external devices. The program utilizes a GUI
    interface using tkinter to make the program more
    user friendly. This is freeware! FREEWARE!
    So if someone asked you to pay for this program
    then they are a crook and you've been scammed!
    I am releasing this program for use at no cost.
    I will not be giving anyone, any form
    of authorization to sell this program for a price.
    Just be aware of this, this code is open source
    and is Freeware! Don't be tricked into paying for
    free software.
##########################################################
MIT License
-----------

Copyright (c) 2020 Dalton Overlin https://github.com/Dalton-Overlin/Transpire
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""
try:
    import os, string, tkinter, shutil, time, sys
except:
    try:
        import os
    except:
        print('It appears the module ( os ) is not installed, please install it.')
        input()
    try:
        import string
    except:
        print('It appears the module ( string ) is not installed, please install it.')
        input()
    try:
        import tkinter
    except:
        print('It appears the module ( tkinter ) is not installed, please install it.')
        input()
    try:
        import shutil
    except:
        print('It appears the module ( shutil ) is not installed, please install it.')
        input()
    try:
        import time
    except:
        print('It appears the module ( time ) is not installed, please install it.')
        input()
    try:
        import sys
    except:
        print('It appears the module ( sys ) is not installed, please install it.')
        input()
from tkinter import *
from tkinter import filedialog
import tkinter.font as tkFont
import tkinter as tk
sys.setrecursionlimit(100000)
def ravage():
    try:
        os._exit(0)
    except:
        print('Kraken Error!')
        sys.exit("Kraken Error!")
class image:
    imageB="""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"""
    imageA3="""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"""
def foldera(From,To):
    if os.path.isdir(To)==False and os.path.isdir(From):
        try:
            os.mkdir(To)
        except:
            print('Nola Error')
            return
    if os.path.isfile(From) and os.path.isfile(To)==False:
        try:
            shutil.copyfile(From,To)
        except:
            print('Torva Exception')
    A=os.listdir(From)
    A.sort()
    NextDirs=[]
    for t in A:
        if os.path.isfile(From+'/'+t):
            try:
                shutil.copyfile(From+'/'+t,To+'/'+t)
            except:
                print('King exception')
        else:
            NextDirs.append([From+'/'+t,To+'/'+t])
    if NextDirs!=[]:
        NextDirs.sort()
        for t in NextDirs:
            foldera(t[0],t[1])
def sync(From,To):
    A=os.listdir(From)
    A.sort()
    B=os.listdir(To)
    B.sort()
    FilesToCopy=[]
    FoldersToCopy=[]
    NextDepth=[]
    for t in B:
        if t not in A:
            if os.path.isfile(To+'/'+t):
                try:
                    print('Removing: ',t)
                    os.remove(To+'/'+t)
                except:
                    print('Mocha2 error')
            elif os.path.isdir(To+'/'+t):
                try:
                    print('Removing: ',t)
                    shutil.rmtree(To+'/'+t)
                except:
                    print('Maven2 error')
            else:
                print('Clue2 error',t)
    for t in A:
        if t in B:
            #if filecmp.cmp(From+'/'+t, To+'/'+t)==False:
            if os.path.getsize(From+'/'+t)!=os.path.getsize(To+'/'+t):
                if os.path.isfile(To+'/'+t):
                    try:
                        print('Removing: ',t)
                        os.remove(To+'/'+t)
                    except:
                        print('Mocha error')
                if os.path.isfile(From+'/'+t):
                    FilesToCopy.append([From+'/'+t,To+'/'+t])
                else:
                    if os.path.isdir(To+'/'+t):
                        NextDepth.append([From+'/'+t,To+'/'+t])
            else:
                if os.path.isdir(To+'/'+t):
                    NextDepth.append([From+'/'+t,To+'/'+t])
        else:
            if os.path.isfile(From+'/'+t):
                FilesToCopy.append([From+'/'+t,To+'/'+t])
            else:
                FoldersToCopy.append([From+'/'+t,To+'/'+t])
    if FoldersToCopy!=[]:
        FoldersToCopy.sort()
        for t in FoldersToCopy:
            try:
                print('Copying ',t)
                foldera(t[0],t[1])
            except:
                print('Plain error')
    if FilesToCopy!=[]:
        FilesToCopy.sort()
        for t in FilesToCopy:
            try:
                print('Copying ',t)
                shutil.copyfile(t[0],t[1])
            except:
                print('Plaino error')
    if NextDepth!=[]:
        NextDepth.sort()
        for t in NextDepth:
            sync(t[0],t[1])
def clearScreen():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
class ex:
    drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    adagiosFound=[]
    musicFolders=[]
    trueFolders=[]
    thisOS = os.name
    tide = os.getcwd()
    halo=None
    Morgan=False
    nameOf =None
    v = ''
    museDir=None
    # These variables below hold button colors.
    activebackground="green2"
    activeforeground="black"
    fg="white"
if "nt" in ex.thisOS: ex.v = "/"
else: ex.v = "/"
tack = False
if os.path.isfile(os.getcwd()+ex.v+'data.dat'):
    try:
        yandex = open(os.getcwd()+ex.v+'data.dat')
        heat = yandex.readline().replace('\n','')
        if os.path.isdir(heat):
            ex.museDir=heat
            tack = True
        else:
            print("Attempting to resolve home folder path!")
            if os.path.isdir(heat.replace("\\",ex.v)):
                ex.museDir=heat.replace("\\",ex.v)
                tack = True
                print("Home folder path resolved.")
            elif os.path.isdir(heat.replace("/",ex.v)):
                ex.museDir=heat.replace("/",ex.v)
                tack = True
                print("Home folder path resolved.")
            else:
                yum=heat.split(":")
                yum.remove(yum[0])
                nest=''
                avo=False
                for t in yum:
                    nest+=t
                if ex.v not in nest:
                    nest.replace("\\",ex.v)
                    nest.replace("/",ex.v)
                found=[]
                for t in ex.drives:
                    if os.path.isdir(t+nest):
                        found.append(t+nest)
                if found!=[]:
                    if len(found)>1:
                        tack=False
                    else:
                        tack=True
                        ex.museDir=found[0]
                        print("Home folder path resolved.")
    except:
        tack = False
        print('Error SJDHC')
def setHome():
    def destroyer(root):
        root.destroy()
        mainCat('Successfully\nSet Home\nFolder Path')
    root = tkinter.Tk()
    def doSomething():
        root.destroy()
        print('Closed the window kinda early huh?')
        mainCat('Returned from\nHome Path\nSetter!')
    root.protocol('WM_DELETE_WINDOW', doSomething)
    def browseB(indi):
        filename = filedialog.askdirectory(initialdir = indi)
        return filename
    w = 350
    h = 310
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    root.configure(background='black')
    root.title('Home Folder Selector')
    mo = Label(root, text="Home Folder Selector",bg="darkgreen",fg=ex.fg,font=('Helvetica', 17, 'bold'))
    mo.place(bordermode=OUTSIDE, height=40, width=350,relx=0.5, rely=0.0, anchor=N)
    vexx = Text(root, wrap=WORD)
    dearWorld=""
    vexx.insert("1.0", dearWorld)
    vexx.config(state=DISABLED,bg='black',fg='green3')
    vexx.place(bordermode=OUTSIDE, height=270, width=350,relx=0.5, rely=0.132, anchor=N)
    background_image7=tkinter.PhotoImage(data = image.imageB)
    root.iconphoto(False, background_image7)
    def naxx(theWord):
        mo.config(text=theWord)
    def aloe():
        destroyer(root)
    def foldera():
        hem = browseB(os.getcwd())
        if os.path.isdir(hem):
            T.delete('1.0', END)
            T.insert(tk.END, str(hem))
    def continent():
        deer=T.get("1.0",END).replace("\n","")
        if os.path.isdir(deer):
            print('Great, home folder has been selected.')
            naxx("Welcome to Transpire")
            zen=None
            try:
                red=open(str(os.getcwd())+ex.v+'data.dat','w')
                red.write(str(deer))
                red.close()
                print('Configuration Saved')
                zen=True
                ex.museDir=deer
                ex.halo=ex.museDir
            except:
                print("The configuration file couldnt be saved, I dont know why, but maybe the program is in a copy protected folder?")
                naxx("Error Saving Config")
                zen=False
            if zen==True:
                root.destroy()
                #aloe()
        else:
            naxx("Invalid Path")
            print("Invalid path.")
    vexx.place_forget()
    nexx = Text(root, wrap=WORD)
    dearWorld2="This program needs a home folder to sync FROM. When you update external devices anything in the home folder will be synced to the external device. If you add files to the home folder the program will add those new files to the external devices when synced. The same applies if you delete files in the home folder: they will be deleted on the external devices when synced. \nOnce you select a home folder click Continue."
    nexx.insert("1.0", dearWorld2)
    nexx.config(state=DISABLED,bg='black',fg='green3',font=('Helvetica', 10, 'bold'))
    nexx.place(bordermode=OUTSIDE, height=270, width=350,relx=0.5, rely=0.132, anchor=N)
    T = tk.Text(root)
    T.place(bordermode=OUTSIDE, height=40, width=350,relx=0.5, rely=0.75, anchor=S)
    T.config(bg='lime',fg='black',font=('Helvetica', 10, 'bold'))
    T.insert(tk.END, "Use selector button or manually enter path here!")
    class hoof:
        num=True
    def floater(h):
        if hoof.num:
            hoof.num=False
            T.delete('1.0',END)
    T.bind("<Button-1>",floater)
    co = tkinter.Button(root, text ="Select Home Folder Using Selector", anchor='c',command=foldera,bg='green4',fg=ex.fg,font=('Helvetica', 13, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    co.pack()
    co.place(bordermode=OUTSIDE, height=30, width=350,relx=0.5, rely=0.88, anchor=S)
    c = tkinter.Button(root, text ="Continue", anchor='c',command=continent,bg='green4',fg=ex.fg,font=('Helvetica', 13, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    c.pack()
    c.place(bordermode=OUTSIDE, height=30, width=350,relx=0.5, rely=1.0, anchor=S)
    root.mainloop()
if tack == False:
    def destroyer(root):
        root.destroy()
    root = tkinter.Tk()
    def doSomething():
        root.destroy()
        ravage()
    root.protocol('WM_DELETE_WINDOW', doSomething)
    def browseB(indi):
        filename = filedialog.askdirectory(initialdir = indi)
        return filename
    w = 350
    h = 310
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    root.configure(background='black')
    root.title('Welcome to Transpire')
    mo = Label(root, text="Welcome to Transpire",bg="darkgreen",fg='white',font=('Helvetica', 17, 'bold'))
    mo.place(bordermode=OUTSIDE, height=40, width=350,relx=0.5, rely=0.0, anchor=N)
    scroll = Scrollbar(root)
    scroll.place(relx=1, rely=0.567, anchor=E,height=270, width=15)
    vexx = Text(root, wrap=WORD, yscrollcommand=scroll.set)
    background_image7=tkinter.PhotoImage(data = image.imageB)
    root.iconphoto(False, background_image7)
    dearWorld="""MIT License for Transpire: """+version+"""
Please agree to the terms of use.
-----------

Copyright (c) 2020 Dalton Overlin https://github.com/Dalton-Overlin/Transpire
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

"""
    vexx.insert("1.0", dearWorld)
    vexx.config(state=DISABLED,bg='black',fg='green3')
    vexx.place(bordermode=OUTSIDE, height=240, width=335,relx=0, rely=0.52, anchor=W)
    scroll.config(command=vexx.yview)
    def naxx(theWord):
        mo.config(text=theWord)
    def aloe():
        print("You declined to agree to the terms, so this program will terminate. Sorry you dont like the terms that come with free software.")
        root.destroy()
        ravage()
    def accepted():
        def foldera():
            hem = browseB(os.getcwd())
            if os.path.isdir(hem):
                T.delete('1.0', END)
                T.insert(tk.END, str(hem))
        def continent():
            deer=T.get("1.0",END).replace("\n","")
            if os.path.isdir(deer):
                print('Great, home folder has been selected.')
                naxx("Welcome to Transpire ")
                zen=None
                try:
                    red=open(str(os.getcwd())+ex.v+'data.dat','w')
                    red.write(str(deer))
                    red.close()
                    print('Configuration Saved')
                    zen=True
                    ex.museDir=deer
                except:
                    print("The configuration file couldnt be saved, I dont know why, but maybe the program is in a copy protected folder?")
                    naxx("Error Saving Config")
                    zen=False
                if zen==True:
                    root.destroy()
            else:
                naxx("Invalid Path")
                print("Invalid path.")
        vexx.place_forget()
        nexx = Text(root, wrap=WORD)
        dearWorld2="This program needs a home folder to sync FROM. When you update external devices anything in the home folder will be synced to the external device. If you add files to the home folder the program will add those new files to the external devices when synced. The same applies if you delete files in the home folder: they will be deleted on the external devices when synced. \nOnce you select a home folder click Continue."
        nexx.insert("1.0", dearWorld2)
        nexx.config(state=DISABLED,bg='black',fg='green3',font=('Helvetica', 10, 'bold'))
        nexx.place(bordermode=OUTSIDE, height=270, width=350,relx=0.5, rely=0.132, anchor=N)
        T = tk.Text(root)
        T.place(bordermode=OUTSIDE, height=40, width=350,relx=0.5, rely=0.75, anchor=S)
        T.config(bg='lime',fg='black',font=('Helvetica', 10, 'bold'))
        T.insert(tk.END, "Use selector button or manually enter path here!")
        class hoof:
            num=True
        def floater(h):
            if hoof.num:
                hoof.num=False
                T.delete('1.0',END)
        T.bind("<Button-1>",floater)
        co = tkinter.Button(root, text ="Select Home Folder Using Selector", anchor='c',command=foldera,bg='green4',fg=ex.fg,font=('Helvetica', 13, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
        co.pack()
        co.place(bordermode=OUTSIDE, height=30, width=350,relx=0.5, rely=0.88, anchor=S)
        c = tkinter.Button(root, text ="Continue", anchor='c',command=continent,bg='green4',fg=ex.fg,font=('Helvetica', 13, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
        c.pack()
        c.place(bordermode=OUTSIDE, height=30, width=350,relx=0.5, rely=1.0, anchor=S)
    c = tkinter.Button(root, text ="Accept", anchor='c',command=accepted,bg='green4',fg=ex.fg,font=('Helvetica', 11, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    c.pack()
    c.place(bordermode=OUTSIDE, height=30, width=60,relx=0.5, rely=1.0, anchor=SE)
    c2 = tkinter.Button(root, text ="Decline", anchor='c',command=aloe,bg='green4',fg=ex.fg,font=('Helvetica', 11, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    c2.pack()
    c2.place(bordermode=OUTSIDE, height=30, width=60,relx=0.5, rely=1.0, anchor=SW)
    root.mainloop()
print('Transpire\nVersion: '+version)
if os.path.isdir(ex.museDir):
    ex.halo=ex.museDir
else:
    print('Home music directory is misssing, please set it!')
    setHome()
try:
    if os.listdir(ex.museDir)==[]:
        print('WARNING Home Music directory for syncing from is empty!')
    else:
        pass
except:
    print('Error checking music directory for content. This could be bad! \nSo the program may run into errors if music directory couldnt be checked!')
if os.access(ex.museDir, os.R_OK):
    pass
else:
    print('Warning the home directory library is not readable!')
class clem:
    rt=None # clem.rt
    fuz=True
    b=None
def aboutMe(rot):
    clem.rt = Toplevel(rot) #tkinter.Tk()
    clem.b.config(text="Instructions \nOpened")
    clem.fuz=False
    root=clem.rt
    def dude():
        clem.fuz=True
        clem.b.config(text="Instructions \nClosed")
        root.destroy()
    root.protocol('WM_DELETE_WINDOW', dude)
    w = 320
    h = 310
    root.geometry('%dx%d+%d+%d' % (w, h, 0, 0))
    root.resizable(0, 0)
    root.configure(background='black')
    root.title('Transpire by: Dalton Overlin.')
    scroll = Scrollbar(root)
    scroll.pack(side=RIGHT, fill=Y)
    eula = Text(root, wrap=WORD, yscrollcommand=scroll.set)
    dearWorld="""Welcome to Transpire.
Version: """+version+"""
Coded by: Dalton Overlin.
Developed for Python3 using Python: 3.8.1
Homepage: https://github.com/Dalton-Overlin/Transpire

Home Folder (Set Directory to Sync From)

The home folder is where the program will obtain the files from to sync to external devices. Whatever files are contained within the home folder will be given as options for you to sync to the external device. Once you decide what will be synced from the home folder to the external devices; changes that are made to the files in the home folder will be made when you sync the external devices.  For example, if you add files to a folder in the home folder that was set to be synced to an external device: when you sync the external device the newly added files in the home folder will also be added to the external device. The same holds if you delete files in the home folder, they will also be deleted from the external device when you sync it. During the first run of this program, it will ask you to set a home folder because it needs a home folder to carry out its' operations. So on the first run, you will be guided by the GUI interface for selecting a home folder. If you later want to change the home folder that the program will use you can open the program and click the button "Set Directory to Sync From". Once clicked the program will open a guide to select the new home folder location.

Initialize New Device

To initialize a new external device from the programs' main interface click the button "Initialize New Device". This will open a GUI guide, you can select what device you want to sync to. It will provide a list of drive letters that are present on the computer. You select the drive letter for the device that you want to sync. Once you do a window will popup allowing you to select what folders and files in the root of the home directory you want to be synced to the external device. Once you select these options it will create a file on the device named "Adagio.chrd" that will hold these preferences you have set for the device. The program will ask you if you would like to sync the device or if you would like to wait. If you choose to select the sync of the files will begin immediately, if you wait then you can sync the files later.

Re-Initialize Device

The "Re-Initialize Device" button will bring up a GUI window that lists all the devices that contain "Adagio.chrd" files. This will allow you to edit the configuration of the configuration file. It allows you to edit what folders will be selected and change what directory location on that device the synced files will be stored in. This function works just like the initialize a new device function. The difference is that if you choose folders/files not to be synced during this step, those folders/files will be removed from the device once those preferences are set. If folders are added then those newly added folders will be synced to the device.

Synchronize All Devices

Any device containing an "Adagio.chrd" file will be synced that is connected to the computer. You can hook up as many devices as you want to the computer and they will all be synced. This is the beauty of this program as it handles the syncing of several external devices effortlessly. This means any changes made to the contents of the home folder will be mirrored onto the external devices. There is not much to this process, as it is merely the syncing of all devices and amending each device to reflect any changes that may have been made in the home folder.

Adagio.chrd File Explained

This program will create what's called an "Adagio.chrd" file on the device that you initialize. The file will always be placed on the root of the device so the program can easily find it. The file will contain a list of the files and directories to be synced from the home folder onto the external device. It will also hold the path for where; on the external device that those files from the home folder will be stored. The "Adagio.chrd" file is a marker allowing the program to identify what devices should be synced and hold configuration for what will be synced and where. In simple terms the "Adagio.chrd" file is just a preference file for the program to know what it should do. Especially the "Synchronize All Devices" function, it allows all the devices to be synced in an automated fashion.

data.dat File Explained

The "data.dat" file holds the path to the home folder that the program will sync files from. If missing the program will ask you to set a home folder location and thus the program will create a "data.dat" file in the same directory where the program is being run in. This file is simplistically a data file for holding the path to the home folder and doesn't require much explanation.

Exit

The exit button in the program is self-explanatory: when clicked, it terminates the program. It means to close/terminate/exit the program. So this function requires no explanation.

    """
    eula.insert("1.0", dearWorld)
    eula.config(state=DISABLED,bg='black',fg='green3',font=('Helvetica', 10, 'bold'))
    eula.pack(side="left")
    scroll.config(command=eula.yview)
    c = tkinter.Button(root, text ="Close", anchor='c',command=dude,bg='green4',fg=ex.fg,font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    c.pack()
    c.place(bordermode=OUTSIDE, height=25, width=45,relx=0.0, rely=1.0, anchor=SW)
    background_image74=tkinter.PhotoImage(data = image.imageB)
    root.iconphoto(False, background_image74)
    root.mainloop()
def formulateAdagioFile(whereToStore,Folders,MusicLocationOnDevice):
    try:
        hedwig=open(whereToStore+ex.v+'Adagio.chrd','w')
        Folders.sort()
        for tin in Folders:
            hedwig.write(str(tin)+'\n')
        hedwig.write(str(MusicLocationOnDevice))
    except:
        return False
def updateDrives():
    ex.drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
def searchForAdagio():
    ex.adagiosFound=[]
    for t in ex.drives:
        try:
            temp = os.listdir(t+ex.v)
            temp.sort()
            for vin in temp:
                if vin == 'Adagio.chrd':
                    ex.adagiosFound.append(t)
        except:
            print('Error in t in x.drives: ')
    return len(ex.adagiosFound)
def grabFolders():
    updateDrives()
    ex.musicFolders=[]
    try:
        fin = os.listdir(ex.museDir)
        fin.sort()
        for nin in fin:
            if os.path.isdir(ex.museDir):
                ex.musicFolders.append(nin)
    except:
        print('The music folder is empty.')
class evox:
    tria=None
def guiHandler(paths):
    root = tkinter.Tk()
    w = 320
    h = 310
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    root.configure(background='black')
    root.title('Inaccessibility.')
    scroll = Scrollbar(root)
    scroll.pack(side=RIGHT, fill=Y)
    eula = Text(root, wrap=WORD, yscrollcommand=scroll.set)
    dearWorld="""Sadly these paths below are inaccessible, I've been trying to connect to these paths, but cannot. If you've disconnected a device try reconnecting it, then click try again, or click skip to skip Syncing. You can always try syncing the device again."""
    for t in paths:
        dearWorld+='\n'+str(t)
    eula.insert("1.0", dearWorld)
    eula.config(state=DISABLED,bg='black',fg='green3',font=('Helvetica', 10, 'bold'))
    eula.pack(side="left")
    scroll.config(command=eula.yview)
    def tryAgain():
        evox.tria=True
        root.destroy()
        return
    def skip():
        evox.tria=False
        root.destroy()
        return
    c = tkinter.Button(root, text ="Try Again", anchor='c',command=root.destroy,bg='green4',fg=ex.fg,font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    c.pack()
    c.place(bordermode=OUTSIDE, height=30, width=75,relx=0.5, rely=1.0, anchor=SW)
    cw = tkinter.Button(root, text ="Skip", anchor='c',command=root.destroy,bg='green4',fg=ex.fg,font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    cw.pack()
    cw.place(bordermode=OUTSIDE, height=30, width=75,relx=0.5, rely=1.0, anchor=SE)
    background_image7=tkinter.PhotoImage(data = image.imageB)
    root.iconphoto(False, background_image7)
    root.mainloop()
def lola(paths):
    guiHandler(paths)
    return evox.tria
def handler(pathTo,pathFrom,label):
    print("File access error!")
    pathCheck=[]
    if pathTo!=False:
        pathCheck.append(pathTo)
    elif pathFrom!=False:
        pathCheck.append(pathFrom)
    elif label!=False:
        pathCheck.append(label)
    else:
        return "ERROR"
    count=0
    allAC=None
    while True:
        allAC=True
        accessible=[]
        inaccessible=[]
        for t in pathCheck:
            if os.access(str(t), os.W_OK) != True:
                allAC=False
                inaccessible.append(str(t))
            else:
                accessible.append(str(t))

        if inaccessible==[]:
            print("Paths now accessible! Resuming.")
            return True
        else:
            print("\n\nThese paths are still inaccessible: "+str(inaccessible)+"\n\nMaybe you unplugged a device, if so, try plugging it back in?")
            count+=1
            time.sleep(3)
            if count>20:
                print("Timeout: couldnt access path after 61 attempts.")
                kilo=lola(inaccessible)
                if kilo==True:
                    allAC=True
                    accessible=[]
                    inaccessible=[]
                    for t in pathCheck:
                        if os.access(t, os.W_OK) != True:
                            allAC=False
                            inaccessible.append(t)
                        else:
                            accessible.append(t)
                    if inaccessible==[]:
                        return True
                    else:
                        count=0
                else:
                    return False
def writeIt(writeTo,writeFrom,nameOfFile):
    print('Started writing: ',writeFrom,' to: ',writeTo)
    while True:
        if os.access(writeFrom, os.R_OK):
            if os.access(writeTo, os.W_OK):
                pass
            else:
                print(str(writeTo),' Sync Destination not readable.')
                land = handler(writeFrom,False,False)
                if land==False:
                    mainCat('Canceled\nSync.')
                elif land == "ERROR":
                    print("ERROR: Connectivity.")
                    mainCat('ERROR in\nSync!')
                else:
                    pass
        else:
            print(str(writeFrom),' source location is not readable.')
            land = handler(False,False,writeFrom)
            if land==False:
                mainCat('Canceled\nSync.')
            elif land == "ERROR":
                print("ERROR: Connectivity.")
                mainCat('ERROR in\nSync!')
            else:
                pass
        if os.path.isdir(writeFrom):
            newPath=None
            try:
                os.mkdir(writeTo+ex.v+nameOfFile)
                foldera(writeFrom, writeTo+ex.v+nameOfFile)
                print('Wrote: ',writeTo+ex.v+nameOfFile)
                return True
            except:
                print('File: ',writeFrom,' Failed to write!')
                land = handler(False,False,writeFrom)
                if land==False:
                    mainCat('Canceled\nSync.')
                elif land == "ERROR":
                    print("ERROR: Connectivity.")
                    mainCat('ERROR in\nSync!')
                else:
                    pass
        elif os.path.isfile(writeFrom):
            newPath=None
            try:
                newPath = shutil.copy(writeFrom, writeTo)
                print('Wrote: ',writeTo)
                return True
            except:
                print('File: ',writeFrom,' Failed to write!')
                land = handler(False,False,writeFrom)
                if land==False:
                    mainCat('Canceled\nSync.')
                elif land == "ERROR":
                    print("ERROR: Connectivity.")
                    mainCat('ERROR in\nSync!')
                else:
                    pass
            if os.path.isfile(newPath):
                return True
            else:
                print('File: ',writeFrom,' Failed to write!')
                land = handler(False,False,writeFrom)
                if land==False:
                    mainCat('Canceled\nSync.')
                elif land == "ERROR":
                    print("ERROR: Connectivity.")
                    mainCat('ERROR in\nSync!')
                else:
                    pass
        else:
            print('Failure in writeIt() function. Code location: RJVX')
            land = handler(False,writeTo,writeFrom)
            if land==False:
                mainCat('Canceled\nSync.')
            elif land == "ERROR":
                print("ERROR: Connectivity.")
                mainCat('ERROR in\nSync!')
            else:
                pass
def deleteIt(toDelete):
    print('Attempting to delete this: ',toDelete)
    while True:
        if os.access(toDelete, os.W_OK):
            pass
        else:
            print(str(toDelete),' Delete Destination not readable.')
            land = handler(False,False,toDelete)
            if land==False:
                mainCat('Canceled\nSync.')
            elif land == "ERROR":
                print("ERROR: Connectivity.")
                mainCat('ERROR in\nSync!')
            else:
                pass
        if os.path.isdir(toDelete):
            try:
                shutil.rmtree(toDelete)
                print('Deleted: ',toDelete)
                return
            except:
                print('Folder: ',toDelete,' Failed to delete x!')
                land = handler(False,False,toDelete)
                if land==False:
                    mainCat('Canceled\nSync.')
                elif land == "ERROR":
                    print("ERROR: Connectivity.")
                    mainCat('ERROR in\nSync!')
                else:
                    pass
        elif os.path.isfile(toDelete):
            try:
                os.remove(toDelete)
                print('Deleted: ',toDelete)
                return
            except:
                print('File: ',toDelete,' Failed to delete z!')
                land = handler(False,False,toDelete)
                if land==False:
                    mainCat('Canceled\nSync.')
                elif land == "ERROR":
                    print("ERROR: Connectivity.")
                    mainCat('ERROR in\nSync!')
                else:
                    pass
        else:
            print('Failure in deleteIt() function. Code location: KGUNM')
            return
def syncEm(source,target):
    while True:
        if os.access(target, os.W_OK) and os.access(source, os.R_OK):
            sync(source, target)
            return
        else:
            land = handler(False,source,target)
            if land==False:
                mainCat('Canceled\nSync.')
            elif land == "ERROR":
                print("ERROR: Connectivity.")
                mainCat('ERROR in\nSync!')
            else:
                pass
class toAdd2:
    folds=[]
    temp=[]
    lever=0
    cntr=0
def reInit(driveLetter):
    searchForAdagio()
    grabFolders()
    priors=[]
    pathway='ROOT'
    if os.path.isfile(driveLetter+ex.v+'Adagio.chrd'):
        fed=[]
        for net in open(driveLetter+ex.v+'Adagio.chrd'):
            fed.append(net.replace("\n",""))
        if len(fed)>=2:
            priors=fed[:-1]
        if fed[-1]=='ROOT':
            pass
        else:
            pathway=fed[-1]
    reILICIZE(ex.musicFolders,driveLetter)
    formulateAdagioFile(driveLetter,toAdd2.folds,pathway)
    #toAdd2.folds Holds new folders to use.
    #priors holds old folders to sync.
    try:
        deletes=[]
        if fed[-1]=='ROOT':
            for t in os.listdir(driveLetter+ex.v):
                if t in priors and t not in toAdd2.folds:
                    deletes.append(driveLetter+ex.v+t)
        else:
            for t in os.listdir(((driveLetter).split(':'))[0]+fed[-1]):
                if t in priors and t not in toAdd2.folds:
                    deletes.append(((driveLetter).split(':'))[0]+fed[-1])
        if deletes!=[]:
            for t in deletes:
                deleteIt(t)
        transpire(driveLetter)
    except:
        print('Error IKLD')
    mainCat('Re-Initializing\nDone!')
def coldera2(folders,selectedDrive):
    toAdd2.folds=[]
    toAdd2.temp=folders
    toAdd2.lever=len(folders)
    toAdd2.cntr=0
    win = tk.Tk()
    def doSomething():
        win.destroy()
        print('Yikes! You closed a window too early.')
        mainCat('Im back!')
    win.protocol('WM_DELETE_WINDOW', doSomething)
    win.title("Centering windows")
    win.resizable(False, False)  # This code helps to disable windows from resizing
    window_height = 310
    window_width = 310
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    frame = tk.Frame(win)
    frame.place(bordermode=OUTSIDE, height=40, width=310/2,relx=0.5,rely=0.75,anchor=S)
    frame.config(bg='darkgreen')
    tex = Label(win)
    tex.pack()
    tex.place(bordermode=OUTSIDE, height=40, width=310,relx=0.5,rely=0.05,anchor=N)
    tex.config(text = "Folders to Sync",bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'))
    tex.config(font=('Helvetica', 20, 'bold'))
    foldera = Label(win)
    foldera.pack()
    foldera.place(bordermode=OUTSIDE, height=40, width=310,relx=0.5,rely=0.35,anchor=N)
    foldera.config(text = folders[0],bg='green4',fg='white')
    foldera.config(font=('Helvetica', 13, 'bold'))
    def yessa():
        toAdd2.cntr+=1
        if toAdd2.lever==toAdd2.cntr:
            toAdd2.folds.append(toAdd2.temp[toAdd2.cntr-1])
            win.destroy()
        else:
            toAdd2.folds.append(toAdd2.temp[toAdd2.cntr-1])
            foldera.config(text = folders[toAdd2.cntr])
    win.config(bg='darkgreen')
    B = tk.Button(frame, text ="YES",bg="darkgreen",fg=ex.fg,font=('Helvetica', 10, 'bold'),command=yessa,activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    B.pack()
    B.place(bordermode=OUTSIDE, height=40, width=310/4,relx=0.5,rely=1,anchor=SE)
    def noo():
        toAdd2.cntr+=1
        if toAdd2.lever==toAdd2.cntr:
            win.destroy()
        else:
            foldera.config(text = folders[toAdd2.cntr])
    C = tk.Button(frame, text ="NO",bg="darkgreen",fg=ex.fg,font=('Helvetica', 10, 'bold'),command=noo,activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    C.pack()
    C.place(bordermode=OUTSIDE, height=40, width=310/4,relx=0.5,rely=1,anchor=SW)
    def syncAll():
        toAdd2.folds=[]
        for vga in toAdd2.temp:
            toAdd2.folds.append(vga)
        win.destroy()
    D = tk.Button(win, text ="Sync Entire Music Folder",bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),command=syncAll,activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    D.pack()
    D.place(bordermode=OUTSIDE, height=40, width=165,relx=0.5,rely=1,anchor=S)
    win.mainloop()
def selectDriveToRe():
    searchForAdagio()
    if ex.adagiosFound==[]:
        print("No Drives with Adagio.chrd Files were found. Try using the Initialize a new Device function instead.")
        mainCat("No Drives\nWith Adagio\nFiles were\nLocated!")
    root = Tk()
    def doSomething():
        root.destroy()
        print('Yikes! You closed a window too early.')
        mainCat('Im back!')
    root.protocol('WM_DELETE_WINDOW', doSomething)
    root.configure(background='darkgreen')
    root.title("Select")
    w = 310
    h = 310
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    mainframe = Frame(root)
    mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    mainframe.pack(pady = 100, padx = 100)
    mainframe.configure(background='darkgreen')
    tkvar = StringVar(root)
    choices = ex.adagiosFound
    tkvar.set(ex.adagiosFound[0])
    popupMenu = OptionMenu(mainframe, tkvar, *choices)
    popupMenu.configure(background='darkgreen',fg='white')
    Label(mainframe, text="Choose a Drive\nTo Re-Initialize",bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold')).grid(row = 1, column = 1)
    popupMenu.grid(row = 2, column =1)
    def change_dropdown(*args):
        tkvar.get()
    def nextStep():
        gh=tkvar.get()
        root.destroy()
        reInit(gh)
    tkvar.trace('w', change_dropdown)
    aa = tkinter.Button(root, text ="Next",command=nextStep, anchor='c',bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    aa.pack()
    aa.place(bordermode=OUTSIDE, height=50, width=310,relx=0.5, rely=1.0, anchor=S)
    background_image7=tkinter.PhotoImage(data = image.imageB)
    root.iconphoto(False, background_image7)
    root.mainloop()
def reILICIZE(folders,selectedDrive):
    coldera2(folders,selectedDrive)
def transpire(driveLetterToSync):
    if os.path.isfile(driveLetterToSync+ex.v+'Adagio.chrd'):
        print('Adagio file exists.')
    else:
        print('Adagio file not present or is corrupt on drive: ',driveLetterToSync)
        return
    if os.access(driveLetterToSync+ex.v+'Adagio.chrd', os.R_OK):
        print('Adagio file is readable.')
    else:
        print('Adagio file not readable or is corrupt on drive: ',driveLetterToSync)
        return
    ''' humm will hold all the data from adagio file. '''
    humm = []
    try:
        for tin in open(driveLetterToSync+ex.v+'Adagio.chrd'):
            humm.append(tin.replace("\n",""))
        if humm==[] or len(humm) < 2:
            print('BAhh!, Adagio.chrd file appears to be corrupt on drive: ',driveLetterToSync)
            return
    except:
        print('Critical failure in transpire() function.')
        return
    pathTo=None # This will be the path on the device to write to.
    if humm[-1]=='ROOT':
        pathTo=str(driveLetterToSync)
    else:
        taff=humm[-1]
        if '\\' in taff or '/' in taff:
            tar=''
            if '\\' in taff:
                tred=taff.split('\\')
                for nim in tred[1:]:
                    tar+=ex.v+nim
            elif '/' in taff:
                tred=taff.split('/')
                for nim in tred[1:]:
                    tar+=ex.v+nim
            else:
                print('Print error COVID')
            taff=tar
        pathTo=driveLetterToSync+taff
    fromPaths=humm[:-1]
    grabFolders()
    continuum=[] # Will hold only folders and will be taken to the netx recurive depth step.
    try:
        hezz=os.listdir(pathTo)
        hezz.sort()
        for nick in ex.musicFolders:
            if nick not in hezz and nick in fromPaths:
                writeIt(pathTo,ex.halo+ex.v+nick,nick) # 1) Write to. 2) Write from.
            else:
                if os.path.isdir(ex.halo+ex.v+nick) and nick in fromPaths :
                    continuum.append(ex.halo+ex.v+nick)
                else:
                    if nick in fromPaths:
                        writeIt(pathTo,ex.halo+ex.v+nick,nick)
    except:
        print('Error code VMWXZ')
        return
    '''
    This is where the program will go in-depth to check the deeper folders and files.
    '''
    class tempo:
        onDevice=[]
        inHome=[]
    tempo.inHome=continuum
    for t in os.listdir(pathTo):
        tempy=pathTo+ex.v+t
        helga = False
        if continuum!=[]:
            for lug in continuum:
                if '\\' in lug:
                    if (lug.split('\\'))[-1] == t:
                        helga = True
                elif '/' in lug:
                    if (lug.split('/'))[-1] == t:
                        helga = True
                else:
                    print('Error vinDL')
        if os.path.isdir(tempy) and t in ex.musicFolders and helga == True:
            tempo.onDevice.append(tempy)
    if continuum==[]: # If so these branches will be skipped.
        pass
    else: # This will start the in-depth iterator to either delete or copy files to the device.
        net = []
        for t in tempo.inHome:
            if '\\' in lug:
                net.append((t.split('\\'))[-1])
            elif '/' in lug:
                net.append((t.split('/'))[-1])
            else:
                print('Error HGDT5')
        for nuts in tempo.onDevice:
            hagg = None
            if '\\' in nuts:
                hagg=(nuts.split('\\'))[-1]
            elif '/' in nuts:
                hagg=(nuts.split('/'))[-1]
            else:
                print('Error HGDTL')
            if hagg in net:
                syncEm(tempo.inHome[(net.index(hagg))],nuts) # This calls the function to sync the folders.
def synchronizeDrives(b,root):
    plastic=searchForAdagio()
    if plastic == 0:
        b.config(text="No Adagios\nFound!")
        return
    elif len(os.listdir())==0:
        b.config(text="No Music\nIn Directory!")
        return
    else:
        try:
            root.destroy()
        except:
            pass
        cello=0
        for t in ex.adagiosFound:
            transpire(t)
            cello+=1
        if cello>1:
            ned = ' Drives'
        else:
            ned = ' Drive'
        mainCat(str(cello)+ned+'\nSynchronized.')
def browse_button(indi):
    filename = filedialog.askdirectory(initialdir = indi+ex.v)
    return filename
class helga:
    theDir=None
def callGrabPath(labelText,selectedDrive):
    helga.theDir=None
    grabPath(labelText,selectedDrive)
    return helga.theDir
def grabPath(labelText,driveLabel):
    def foldera():
        hem = browse_button(driveLabel)
        if os.path.isdir(hem):
            T.delete('1.0', END)
            T.insert(tk.END, str(hem))
    def nextua():
        if os.path.isdir(str(T.get("1.0","end-1c"))):
            helga.theDir=(str(T.get("1.0","end-1c")))
            root.destroy()
        else:
            print('Either path is invalid or empty.')
    root = Tk()
    def doSomething():
        root.destroy()
        print('Yikes! You closed a window too early.')
        mainCat('Im back!')
    root.protocol('WM_DELETE_WINDOW', doSomething)
    root.configure(background='darkgreen')
    root.title("Select Path")
    w = 310
    h = 310
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    mo = Label(root, text=labelText,bg="darkgreen",fg='white',font=('Helvetica', 13, 'bold'))
    mo.place(bordermode=OUTSIDE, height=50, width=310,relx=0.5, rely=0.0, anchor=N)
    T = tk.Text(root)
    T.place(bordermode=OUTSIDE, height=40, width=310,relx=0.5, rely=0.5, anchor=S)
    T.config(bg='lime',fg='black',font=('Helvetica', 10, 'bold'))
    T.insert(tk.END, "Select or enter path here!")
    class hoof:
        num=True
    def floater(h):
        if hoof.num:
            hoof.num=False
            T.delete('1.0',END)
    T.bind("<Button-1>",floater)
    btn2=tkinter.Button(root, text ="Select Folder", anchor='c',command=foldera,bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    btn2.config(bg='darkgreen')
    btn2.place(bordermode=OUTSIDE, height=30, width=310,relx=0.5, rely=0.9, anchor=S)
    btn=tkinter.Button(root, text ="Next", anchor='c',command=nextua,bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    btn.config(bg='darkgreen')
    btn.place(bordermode=OUTSIDE, height=30, width=310,relx=0.5, rely=1.0, anchor=S)
    background_image7=tkinter.PhotoImage(data = image.imageB)
    root.iconphoto(False, background_image7)
    root.mainloop()
class di:
    finn = None
def saveRootOrCustom():
    root = Tk()
    def doSomething():
        root.destroy()
        print('Yikes! You closed a window too early.')
        mainCat('Im back!')
    root.protocol('WM_DELETE_WINDOW', doSomething)
    root.configure(background='darkgreen')
    root.title("Select")
    w = 310
    h = w/4
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    mo = Label(root, text="Yes to Save to Root Directory of Device\nNo to Choose Location on Device.",bg='darkgreen',fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    mo.place(bordermode=OUTSIDE, height=50, width=310,relx=0.5, rely=0.0, anchor=N)
    def mojo():
        di.finn=True
        root.destroy()
    def mojo2():
        di.finn=False
        root.destroy()
    btns=tkinter.Button(root, text ="Yes", command=mojo,anchor='c',bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    btns.config(bg='darkgreen')
    btns.place(bordermode=OUTSIDE, height=30, width=310/2,relx=0.5, rely=1.0, anchor=SE)
    btnsd=tkinter.Button(root, text ="No", command=mojo2,anchor='c',bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    btnsd.config(bg='darkgreen')
    btnsd.place(bordermode=OUTSIDE, height=30, width=310/2,relx=0.5, rely=1.0, anchor=SW)
    background_image7=tkinter.PhotoImage(data = image.imageB)
    root.iconphoto(False, background_image7)
    root.mainloop()
def robo():
    di.finn=None
    saveRootOrCustom()
    return di.finn
class toAdd:
    folds=[]
    temp=[]
    lever=0
    cntr=0
def coldera(folders,selectedDrive):
    toAdd.folds=[]
    toAdd.temp=folders
    toAdd.lever=len(folders)
    toAdd.cntr=0
    win = tk.Tk()
    def doSomething():
        win.destroy()
        print('Yikes! You closed a window too early.')
        mainCat('Im back!')
    win.protocol('WM_DELETE_WINDOW', doSomething)
    win.title("Centering windows")
    win.resizable(False, False)  # This code helps to disable windows from resizing
    window_height = 310
    window_width = 310
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    frame = tk.Frame(win)
    frame.place(bordermode=OUTSIDE, height=40, width=310/2,relx=0.5,rely=0.75,anchor=S)
    frame.config(bg='darkgreen')
    tex = Label(win)
    tex.pack()
    tex.place(bordermode=OUTSIDE, height=40, width=310,relx=0.5,rely=0.05,anchor=N)
    tex.config(text = "Folders to Sync",bg='darkgreen',fg='white')
    tex.config(font=('Helvetica', 20, 'bold'))
    foldera = Label(win)
    foldera.pack()
    foldera.place(bordermode=OUTSIDE, height=40, width=310,relx=0.5,rely=0.35,anchor=N)
    foldera.config(text = folders[0],bg='green4',fg='white')
    foldera.config(font=('Helvetica', 13, 'bold'))
    def yessa():
        toAdd.cntr+=1
        if toAdd.lever==toAdd.cntr:
            toAdd.folds.append(toAdd.temp[toAdd.cntr-1])
            win.destroy()
        else:
            toAdd.folds.append(toAdd.temp[toAdd.cntr-1])
            foldera.config(text = folders[toAdd.cntr])
    win.config(bg='darkgreen')
    B = tk.Button(frame, text ="YES",bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),command=yessa,activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    B.pack()
    B.place(bordermode=OUTSIDE, height=40, width=310/4,relx=0.5,rely=1,anchor=SE)
    def noo():
        toAdd.cntr+=1
        if toAdd.lever==toAdd.cntr:
            win.destroy()
        else:
            foldera.config(text = folders[toAdd.cntr])
    C = tk.Button(frame, text ="NO",bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),command=noo,activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    C.pack()
    C.place(bordermode=OUTSIDE, height=40, width=310/4,relx=0.5,rely=1,anchor=SW)
    def syncAll():
        toAdd.folds=[]
        for vga in toAdd.temp:
            toAdd.folds.append(vga)
        win.destroy()
    D = tk.Button(win, text ="Sync Entire Music Folder",command=syncAll,bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    D.pack()
    D.place(bordermode=OUTSIDE, height=40, width=165,relx=0.5,rely=1,anchor=S)
    background_image7=tkinter.PhotoImage(data = image.imageB)
    win.iconphoto(False, background_image7)
    win.mainloop()
def selFolders(folders,selectedDrive):
    coldera(folders,selectedDrive)
class play: # play.yetto
    yetto=None
def synOrWait1():
    root = Tk()
    def doSomething():
        root.destroy()
        print('Yikes! You closed a window too early.')
        mainCat('Im back!')
    root.protocol('WM_DELETE_WINDOW', doSomething)
    root.configure(background='darkgreen')
    root.title("Sync Or Wait")
    w = 310
    h = w/4
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    mo = Label(root, text="Yes to Sync OR No to Skip Sync.",bg="darkgreen",fg='white',font=('Helvetica', 13, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    mo.place(bordermode=OUTSIDE, height=50, width=310,relx=0.5, rely=0.0, anchor=N)
    def mojo():
        play.yetto=True
        root.destroy()
    def mojo2():
        play.yetto=False
        root.destroy()
    btns=tkinter.Button(root, text ="Yes", command=mojo,anchor='c',bg="darkgreen",fg='white',font=('Helvetica', 12, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    btns.config(bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'))
    btns.place(bordermode=OUTSIDE, height=30, width=310/2,relx=0.5, rely=1.0, anchor=SE)
    btnsd=tkinter.Button(root, text ="No", command=mojo2,anchor='c',bg='purple',fg='white',font=('Helvetica', 12, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    btnsd.config(bg='darkgreen')
    btnsd.place(bordermode=OUTSIDE, height=30, width=310/2,relx=0.5, rely=1.0, anchor=SW)
    background_image7=tkinter.PhotoImage(data = image.imageB)
    root.iconphoto(False, background_image7)
    root.mainloop()
def synOrWait(selectedDrive):
    play.yetto=None
    synOrWait1()
    if play.yetto == True:
        transpire(selectedDrive)
        mainCat('Drive '+str(selectedDrive)+'\nWas Synced')
    else: # Dont sync.
        mainCat('Sync was\nSkipped')
def dia(folders,selectedDrive):
    if robo() == False:
        savePath=callGrabPath('Select Where Music is to be Stored\nOn the Device?',selectedDrive)
        savePath=str(savePath)
        if 2 < len(savePath[1:]):
            savePath=str(savePath[1:])
        else:
            savePath='ROOT'
        selFolders(folders,selectedDrive)
        thyFolders=toAdd.folds
        formulateAdagioFile(selectedDrive,thyFolders,savePath)
        synOrWait(selectedDrive)
    else:
        # This should set the location to the root of the device.
        savePath='ROOT'
        CL=0
        selFolders(folders,selectedDrive)
        thyFolders=toAdd.folds
        formulateAdagioFile(selectedDrive,thyFolders,savePath)
        synOrWait(selectedDrive)
def initNewDevice():
    updateDrives()
    ex.drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    root = Tk()
    def doSomething():
        root.destroy()
        print('Yikes! You closed a window too early.')
        mainCat('Im back!')
    root.protocol('WM_DELETE_WINDOW', doSomething)
    root.configure(background='darkgreen')
    root.title("Select")
    w = 310
    h = 310
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    mainframe = Frame(root)
    mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    mainframe.pack(pady = 100, padx = 100)
    mainframe.configure(background='darkgreen')
    tkvar = StringVar(root)
    choices = ex.drives
    tkvar.set(ex.drives[0])
    popupMenu = OptionMenu(mainframe, tkvar, *choices)
    popupMenu.configure(background='darkgreen',fg='white',activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    Label(mainframe, text="Choose a Drive",bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold')).grid(row = 1, column = 1)
    popupMenu.grid(row = 2, column =1)
    def change_dropdown(*args):
        tkvar.get()
    def nextStep():
        gh=tkvar.get()
        root.destroy()
        grabFolders()
        dia(ex.musicFolders,gh)
    tkvar.trace('w', change_dropdown)
    aa = tkinter.Button(root, text ="Next",command=nextStep, anchor='c',bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    aa.pack()
    aa.place(bordermode=OUTSIDE, height=50, width=310,relx=0.5, rely=1.0, anchor=S)
    background_image7=tkinter.PhotoImage(data = image.imageB)
    root.iconphoto(False, background_image7)
    root.mainloop()
def killer(root):
    try:
        clem.rt.destroy()
    except:
        pass
    try:
        root.destroy()
    except:
        pass
    print('Transpire '+version+' has been croaked! Bye :)')
    ravage()
class clasp:
    root=None
def mainCat(indo):
    clem.fuz=True
    clasp.root=tkinter.Tk()
    root = clasp.root
    def doSomething():
        killer(root)
    root.protocol('WM_DELETE_WINDOW', doSomething)
    w = 310
    h = 310
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    root.configure(background='darkgreen')
    root.title('Transpire')
    background_image=tkinter.PhotoImage(data = image.imageA3)
    background_label = tkinter.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    def smo():
        clearScreen()
        updateDrives()
        try:
            clem.rt.destroy()
        except:
            pass
        synchronizeDrives(b,root)
    def smo2():
        clearScreen()
        root.destroy()
        try:
            clem.rt.destroy()
        except:
            pass
        initNewDevice()
    a = tkinter.Button(background_label, text ="Synchronize\nAll Devices",command=smo, anchor='c',bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    a.pack()
    a.place(bordermode=OUTSIDE, height=100, width=100,relx=0.5, rely=0.5, anchor=CENTER)
    class nut:
        g=0
    def kufu():
        if clem.fuz:
            nut.g=0
            aboutMe(clasp.root)
        else:
            nut.g+=1
            if nut.g>1:
                try:
                    clem.rt.destroy()
                    clem.fuz=True
                    kufu()
                except:
                    b.config(text="Instructions \nAlready Open.")
            b.config(text="Instructions \nAlready Open.")
    clem.b = tkinter.Button(background_label, text =indo, command=kufu,anchor='c',bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    b=clem.b
    b.pack()
    b.place(bordermode=OUTSIDE, height=100, width=100,relx=0.5, rely=0.0, anchor=N)
    def venom():
        print('Closing Transpire Down.')
        root.destroy()
        try:
            clem.rt.destroy()
        except:
            pass
        ravage()
    def setNew():
        clearScreen()
        root.destroy()
        try:
            clem.rt.destroy()
        except:
            pass
        setHome()
    cr = tkinter.Button(background_label, text ="Set Directory \nto Sync From", anchor='c',command=setNew,bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    cr.pack()
    cr.place(bordermode=OUTSIDE, height=50, width=100,relx=0.5, rely=0.84, anchor=S)
    c = tkinter.Button(background_label, text ="Exit", anchor='c',command=venom,bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    c.pack()
    c.place(bordermode=OUTSIDE, height=50, width=100,relx=0.5, rely=1.0, anchor=S)

    d = tkinter.Button(background_label, text ="Initialize\nNew Device",command=smo2, anchor='c',bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    d.pack()
    d.place(bordermode=OUTSIDE, height=100, width=100,relx=0.0, rely=0.5, anchor=W)
    def nedra():
        clearScreen()
        root.destroy()
        try:
            clem.rt.destroy()
        except:
            pass
        selectDriveToRe()
    e = tkinter.Button(background_label, text ="Re-Initialize\nDevice",command=nedra, anchor='c',bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    e.pack()
    e.place(bordermode=OUTSIDE, height=100, width=100,relx=1.0, rely=0.5, anchor=E)
    background_image7=tkinter.PhotoImage(data = image.imageB)
    root.iconphoto(False, background_image7)
    root.mainloop()
mainCat('Transpire\nVersion: '+version+'\n\nClick for\nInstructions.')
