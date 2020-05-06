
![Image](https://user-images.githubusercontent.com/30564402/77599033-10596f80-6ec9-11ea-87ca-3d15fa4684d2.jpg)

## **Whats New with Transpire**

Guess what, its here, Transpire V.2 that no longer needs any third party modules to run. I removed the need for dirsync and colorama. The program uses only modules that come with Python by default so no extra installations are needed. The removal of the printing of the large word Transpire has also been removed, it was too bulky and slowed the program down. So it's toast, so is the need for the missing module installer code. I've tested the program on large swaths of files and all works well so far. But as always should you come accros a bug please raise an issue with a description of the issue and I will try and fix it ASAP!

## **Getting Started with Transpire**

- This program requires Python 3. 

- You need these modules installed: **( os, string, tkinter, shutil, dirsync, time, colorama, importlib )**. 

- By default Python 3 comes with these packages: **( os, string, shutil, time, ~~importlib~~, tkinter )**.

- ~~So you probably only need to install these modules: **( dirsync, colorama )**.~~

~~When you first run this script it will check if those modules are installed. If they are not, then the script will try to automatically install them. However, sometimes the automated module installer doesnt work 100% of the time. Thats why I have included a **requirements.txt** file that you can use to install all modules in a few simple commands.~~ 

## **Manually Installing Requirements**

~~Open a terminal, and cd to the directory where the requirements.txt file is located. Then enter this command:  **pip install -r requirements.txt**~~

- ~~**Here below is a stricter guide for manually installing the dependencies.**~~
- ~~To install needed modules CD to the directory where the file requirements.txt is stored.~~
- ~~For command-line example: cd "C:\Users\Example\Desktop"~~
- ~~Next, run this command below.~~
- ~~pip install -r requirements.txt~~
- ~~If the above command fails try this one below.~~
- ~~python -m pip install -r requirements.txt~~
- ~~If you don't want to cd to the directory where the file is stored then use the full path to the requirements.txt file, here are some examples below of how to use the full path.~~
- ~~pip install -r "C:\Users\Your-Username\Desktop\requirements.txt"~~
- ~~python -m pip install -r "C:\Users\Your-Username\Desktop\requirements.txt"~~

~~Thats it, then just run the Transpire.py script. If you have Python 3 installed you can normally just click the script file and it will run. However, sometimes you have to run the script by calling it from the command line on systems like Linux. So, if your unfamiliar with this process heres a nice guide I found on how to run a Python script: https://www.datacamp.com/community/tutorials/running-a-python-script~~

~~Theoretically, this program works with all versions of these modules ( dirsync, colorama ). But, it is possible future versions of those modules could cause the program to break. So, if they do break then uninstall the newer version of those modules and use the requirements.txt file and it will install specific versions of those modules which have been tested to work with this program. Or run these commands below to manually install the tested versions of these modules using pip.~~

~~- **python -m pip install colorama == 0.4.3**~~
- ~~**python -m pip install dirsync == 2.2.4**~~

~~If pip fails to install those then try upgrading pip to the latest or try installing this specific pip version using the below command.~~ 

- ~~**python -m pip install pip == 20.0.2**~~

~~Note: the instructions above make it look extremely difficult to use this program. However, it is really simple. By default when you run the Transpire.py script it will try to install all requirements for you. I just included these instructions so that even beginners can get this program up and running if they run into unexpected issues. Even advanced users might find these instructions useful so that why they're here.~~ 

## Downloads

**[`Download Transpire`](https://github.com/Dalton-Overlin/Transpire/blob/master/Transpire.py "`Python Transpire Python script.`")**

**[`Download Requirements.txt`](https://github.com/Dalton-Overlin/Transpire/blob/master/requirements.txt "`The requirements.txt file for installing the required modules.`")**

**[`Download License.txt`](https://github.com/Dalton-Overlin/Transpire/blob/master/License.txt "`The License.txt file.`")**

**[`Download Transpire-Wallpaper.png`](https://github.com/Dalton-Overlin/Transpire/blob/master/Transpire-Wallpaper.png "`Transpire-Wallpaper.png Photo.`")**

## **What is Transpire**
![Program GUI Display](https://user-images.githubusercontent.com/30564402/77599083-3f6fe100-6ec9-11ea-8a02-33b31339e060.jpg)

Transpire is a program designed to sync music from a home folder to external devices. This program uses a home folder (home folder meaning where the content will come from) and synchronizes the data from the home folder to the external devices you're synchronizing. The program allows you to customize what folders and files from the home folder will be synced to each device. This program creates an Adagio.chrd file on the external device you want to sink to. 

These Adagio.chrd files hold information as to where on the device the synchronization will take place. This means you can not only have the music or folders synced to the root of the device, but you can also specify a subfolder on the device for the music or other files to be synced to. The Adagio.chrd file also holds information as to what folders are being synchronized to the external device. 

This means if you have, for example, 5 folders in your home directory, you could decide to have only 1, 2, 3, 4, or all folders synchronized to the device. This allows you to customize what is synced and what is not. Whenever you make an update to your home folder, if those folders are being synchronized to the device this program will reflect those changes on the device. 

For example, if you add new music in a folder in the home folder that is being synchronized to a device, then those changes to the home folder will be made to your external devices when you synchronize them. This works both ways, if you add content the content will be added to the devices you're synchronizing, if you remove content then the content will be removed from the devices you are synchronizing. 

Any changes you make to your home folder will be reflected on the devices you synchronize. I want to emphasize that this program both deletes files and copies them. So be aware that any changes you make to your home folder will also be made to the external devices when you synchronize them. This program works just like any media player that synchronizes musical content to external devices. 

However, this program is a little different than most media player synchronizing programs. This program keeps the structure of your folders the same when it places them on the external device. For example, I like to place all of my music in different folders with the name of the genre. Sadly, many media players that synchronize music change the folder structuring. 

That's why I developed this program, to keep the folder structure the same on my devices as it is in the home directory. This program is written in Python 3. The program utilizes Tkinter to provide the user with a graphical user interface. This makes the program much easier to use. Also, take note that I developed this program on a Windows operating system, therefore, the GUI may look a little unusual on Linux devices. 

This program has an option to synchronize all of the devices that contain the Adagio.chrd files. In short, those files are used as identifiers for devices you want to synchronize. This program not only works for music, but it also works for any other kind of files you want to synchronize. This is why I did not explicitly label the program for synchronizing music. 

Primarily because it can be used to synchronize anything. Also, when you first run this program a window will pop up making you aware that this program comes with no warranty. It will emphasize that this program is capable of deleting files and therefore could delete files you don't want to be deleted. During the first run, this program also asks you to define the home folder. 

Again, the home folder is where this program will obtain the content from. So that when you synchronize devices, the content from the home folder will be placed on those devices to be synchronized. Please see the instructions below for more information.

## **Attention**

This program copies and deletes files. By using this program you are aware that it could potentially delete files you don't want to be deleted. You agree that you are using this at your own risk with no warranty or guarantee as to the program's functionality. I have been using this program for a long time without any issues. However, there is a chance that bugs still exist within the program and on different operating systems the program may behave unexpectedly. 

I developed this program on Windows 10 64-bit Enterprise Edition. So if you run this on a Linux operating system it may respond unexpectedly. I designed the program to be able to run across different platforms, but I have not tested it on all platforms. I will continue to develop this program further to make it more stable. It is currently stable on my Windows operating system, I am unsure, however, how it acts on another operating system that I have not yet tested it on. 

Also, be aware that if you have set this program to synchronize a specific folder and you manually add music to that folder on the device and synchronize with the program it could delete the manually added content you place on the device. You should only do this if the content you added to the device manually is also in the home directory. This program is designed to synchronize your devices for you. 

Its designed to allow you to specify what folders will be synchronized, where they will be synchronized on the device, and allow you to synchronize all devices at the same time. This means if you have seven or eight devices attached to the computer you can synchronize all of them at the same time. This program is designed to make the synchronization process fast and easy. I just wanted to forewarn you that this program will likely contain bugs and does delete and create files. 

This way you are aware when synchronizing content to devices it may unwantedly delete content on your devices if that content is not in your home directory. However, this only applies to the folders you're synchronizing, but there is also a possibility that bugs could be present. Therefore if bugs are present especially when used on different operating systems the program may accidentally delete folders you didn't want to be deleted so be forewarned. 

My recommendation is to test this program out, by synchronizing a device that doesn't contain content you want to be deleted. This way you can learn how the program works, and make sure it works well on your operating system. This way you dont accidentally delete content you want to keep.

## **License**

**MIT License**

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

## **Home Folder (Set Directory to Sync From)**

The home folder is where the program will obtain the files from to sync to external devices. Whatever files are contained within the home folder will be given as options for you to sync to the external device. Once you decide what will be synced from the home folder to the external devices; changes that are made to the files in the home folder will be made when you sync the external devices.  

For example, if you add files to a folder in the home folder that was set to be synced to an external device: when you sync the external device the newly added files in the home folder will also be added to the external device. The same holds if you delete files in the home folder, they will also be deleted from the external device when you sync it. 

During the first run of this program, it will ask you to set a home folder because it needs a home folder to carry out its' operations. So on the first run, you will be guided by the GUI interface for selecting a home folder. If you later want to change the home folder that the program will use you can open the program and click the button "Set Directory to Sync From". Once clicked the program will open a guide to select the new location. 

## **Initialize New Device**

To initialize a new external device open the program, set the home folder and from the programs' main interface click the button "Initialize New Device". This will open a GUI guide, you can select what device you want to sync to. It will provide a list of the drive letters that are present on the computer. You select the drive letter for the device that you want to sync. Once you do a window will popup allowing you to select what folders and files in the root of the home directory you want to be synced to the external device. 

Once you select these options it will create a file on the device named "Adagio.chrd" that will hold these preferences you have set for the device. The program will ask you if you would like to sync the device or if you would like to wait. If you choose to select the sync of the files will begin immediately, if you wait then you can sync the files later. 

## **Re-Initialize Device**

The "Re-Initialize Device" button will bring up a GUI window that lists all the devices that contain "Adagio.chrd" files. This will allow you to edit the configuration of the configuration file. It allows you to edit what folders will be selected and change what directory location on that device the synced files will be stored in. 

This function works just like the initialize a new device function. The difference is that if you choose folders/files not to be synced during this step, those folders/files will be removed from the device once those preferences are set. If folders are added then those newly added folders will be synced to the device. 

## **Click for Instructions**

There is a button in this program that contains this text: "Click for Instructions" in the program. When clicked it brings up a GUI window containing a simplified version of these instructions here on this page along with the info about the build of the program and such. It acts like a portable version of these instructions that's always present within the program. 

## Synchronize All Devices

Any device containing an "Adagio.chrd" file will be synced that is connected to the computer. You can hook up as many devices as you want to the computer and they will all be synced. This is the beauty of this program as it handles the syncing of several external devices effortlessly. This means any changes made to the contents of the home folder will be mirrored onto the external devices. There is not much to this process, as it is merely the syncing of all devices and amending each device to reflect any changes that may have been made in the home folder. 

## **Adagio.chrd File Explained**

This program will create what's called an "Adagio.chrd" file on the device that you initialize. The file will always be placed on the root of the device so the program can easily find it. The file will contain a list of the files and directories to be synced from the home folder onto the external device. It will also hold the path for where; on the external device that those files from the home folder will be stored. The "Adagio.chrd" file is a marker allowing the program to identify what devices should be synced and hold configuration for what will be synced and where. In simple terms the "Adagio.chrd" file is just a preference file for the program to know what it should do. Especially the "Synchronize All Devices" function, it allows all the devices to be synced in an automated fashion. 

## **data.dat File Explained**

The "data.dat" file holds the path to the home folder that the program will sync files from. If missing the program will ask you to set a home folder location and thus the program will create a "data.dat" file in the same directory where the program is being run in. This file is simplistically a data file for holding the path to the home folder and doesn't require much explanation. 

## **Exit**

The exit button in the program is self-explanatory: when clicked, it terminates the program. It means to close/terminate/exit the program. So this function requires no explanation. 

###  **Note **
Do you like the Transpire graphics? I included the logo named Transpire-Wallpaper.png in the github repository if you would like to use it. Just incase :)
