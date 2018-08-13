import re
import fileinput
from robobrowser import RoboBrowser
import os
import requests
from bs4 import BeautifulSoup

br = RoboBrowser()
#This is where you enter what element from the periodic table you want
#from the Archive, you can use any element
base_Element_Name="Cu"
url='http://cars9.uchicago.edu/cgi-bin/atoms/Atoms-Search.cgi'
#Selects the element in the periodic table
post_data={'pt_elem':base_Element_Name}
#Post request that selects the element
req=requests.post(url,data=post_data)
status=req.status_code
#Gets the text
html=req.text
#Parses the html
soup=BeautifulSoup(html,'html.parser')
#Gets the list of vales to enter
p_soup=soup.find('p')
#gets all the text
d_soup=p_soup.findAll(text=True)
#Splits so we get the file name
e_soup=str(d_soup).split(':')
#create empty list for .inp files
atomsInp_list=[""]

#Loop to pull the 'atoms.inp' filenames on the page.
#This generates a list of .inp filenames for the post request
for elem in e_soup:
    count=0
    #splits on comma so we can get the 2nd element
    temp=(elem.split(','))
    #gets 2nd element
    nu=temp[1]
    nu_length=len(nu)
    inp_ext=len(nu)-5
    nu_beg=2
    #print(nu[2:len(nu)-5])
    #length used to determine end of the string
    nu_length=len(nu)-1
    if count==0 and nu[(nu_length-4):nu_length]=='.inp':
        atomsInp_list.insert(0,nu[nu_beg:inp_ext])
        count+=1
    elif nu[(nu_length-4):nu_length]=='.inp':
        atomsInp_list.append(nu[nu_beg:inp_ext])


#This does a post request to get the 'atoms.inp' from the filelist atomSInp_list
for inp in atomsInp_list:
    inpExt=str(inp)+'.inp'
    print(inpExt)
    post_data={'chosen_file':inpExt}
    req=requests.post(url,data=post_data)
    status=req.status_code
    html=req.text
    soup=BeautifulSoup(html,'html.parser')
    path = "C:\\Users\\boltz\\PycharmProjects\\untitled\\venv\\" + base_Element_Name + "\\"+inp

    #creates the directory if it does not already exist
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)

    # creates and writes file object new atom.inp file
    if inp!='':
        file = open(inpExt, "w")
        file.write(str(soup))
        file.close()
#changes path to base element name
path="C:\\Users\\boltz\\PycharmProjects\\untitled\\venv\\" + base_Element_Name
os.chdir(path)


