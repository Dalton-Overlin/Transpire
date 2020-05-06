"""
##############################
    Transpire Version: 2.0
##############################
    Coded by, Dalton Overlin
##########################################################
    Last Code Revision Date: April. 5, 2020
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
def sync(From,To,z):
    z+=1
    print('z : Depth : ',z)
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
            sync(t[0],t[1],z)
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
                aloe()
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
        exit()
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
    dearWorld="""MIT License
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
        destroyer(root)
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
                naxx("Welcome to Transpire")
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
                    aloe()
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
print('Transpire')
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
def aboutMe():
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
    root.title('Transpire by: Dalton Overlin.')
    scroll = Scrollbar(root)
    scroll.pack(side=RIGHT, fill=Y)
    eula = Text(root, wrap=WORD, yscrollcommand=scroll.set)
    dearWorld="""Welcome to Transpire V.1.
Coded by: Dalton Overlin.
Date of Last Revision to Code: March. 25, 2020
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
    c = tkinter.Button(root, text ="Close", anchor='c',command=root.destroy,bg='green4',fg=ex.fg,font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    c.pack()
    c.place(bordermode=OUTSIDE, height=25, width=45,relx=0.0, rely=1.0, anchor=SW)

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
            sync(source, target,"sync",z)
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
    btn2=tkinter.Button(root, text ="Select Folder", anchor='c',command=foldera,bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    btn2.config(bg='darkgreen')
    btn2.place(bordermode=OUTSIDE, height=30, width=310,relx=0.5, rely=0.9, anchor=S)
    btn=tkinter.Button(root, text ="Next", anchor='c',command=nextua,bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    btn.config(bg='darkgreen')
    btn.place(bordermode=OUTSIDE, height=30, width=310,relx=0.5, rely=1.0, anchor=S)
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
    root.mainloop()
def killer(root):
    try:
        root.destroy()
    except:
        pass
    print('Transpire has been croaked. Bye :)')
    exit()
class image:
    imageA="""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""".encode('ascii')
def mainCat(indo):
    root = tkinter.Tk()
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
    background_image=tkinter.PhotoImage(data = image.imageA)
    background_label = tkinter.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    def smo():
        clearScreen()
        updateDrives()
        synchronizeDrives(b,root)
    def smo2():
        clearScreen()
        root.destroy()
        initNewDevice()
    a = tkinter.Button(background_label, text ="Synchronize\nAll Devices",command=smo, anchor='c',bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    a.pack()
    a.place(bordermode=OUTSIDE, height=100, width=100,relx=0.5, rely=0.5, anchor=CENTER)
    b = tkinter.Button(background_label, text =indo, command=aboutMe,anchor='c',bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    b.pack()
    b.place(bordermode=OUTSIDE, height=100, width=100,relx=0.5, rely=0.0, anchor=N)
    def venom():
        killer(root)
    def setNew():
        clearScreen()
        root.destroy()
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
        selectDriveToRe()
    e = tkinter.Button(background_label, text ="Re-Initialize\nDevice",command=nedra, anchor='c',bg="darkgreen",fg='white',font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    e.pack()
    e.place(bordermode=OUTSIDE, height=100, width=100,relx=1.0, rely=0.5, anchor=E)
    root.mainloop()
mainCat('Transpire\nVersion: 2\n\nClick for\nInstructions.')
