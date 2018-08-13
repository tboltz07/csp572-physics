Steps to start from scratch.
1. Execute the inplist.py file (requires python 3.3 or hight)
  a. In this file you need to make sure you specify which element on the periodic table you want to get the atoms.inp files 
  b. Once you specify what base element you want, you need to ensure you specify the path you want the file to go
  
2.Next, execute the FEFF.py file (requires python 3.3 or higher)
  a. You need to make sure you have the atoms.inp files in a directory that was created by the inplist.py file
  b. Once you do that you just need to run  this file.
  c. This file will create 11 versions of the specified molecule with 11 angstrom lengths for each molecule

3.Next, run looper.sh to run the jfeff over all the feff.inp files in your directory, you need to make sure you do the following:

  a. Makes sure you change the "Cu" in the looper.sh to whatever element name you have created already in the pervious files
  b. Ensure that paths are changed to match what you have on the computer you have decided to run the calcs
  c. Ensure you have a folder on the desktop named "Completed" and inside that folder, you need to make a new folder and name it whatever      base element you have decided right now it is "Cu" because that is what we started with.  If the base element you choose from the          archive is "H", then you need to make sure the folder inside the "Completed" folder is named "H", and all the references to "Cu" in the    "looper.sh" is changed to "H" (use a copy and replace in word).
  d. Ensure that the "JFEFF" folder that is in the JFEFF package is on the desktop. This the folder that has the feff command file in it. Ask Dr. Jeff Terry for the folder, it is where the executable is 
  The location of the feff executable is: /Applications/jfeff.app/Contents/Resources/JFEFF
  e. Ensure that you have a folder with all the feff.inp files on the desktop.

NOTES:
Please email me if you have any issues at tboltz@hawk.iit.edu .  It is best to text me at 502-640-1645.
