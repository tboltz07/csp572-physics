import re
import fileinput
from robobrowser import RoboBrowser
import os
import requests
from bs4 import BeautifulSoup
#choose base element folder you want to input into webatoms
base_Element_Name = 'Cu'
#changes path to that folder
path="C:\\Users\\boltz\\PycharmProjects\\untitled\\venv\\" + base_Element_Name
os.chdir(path)
#Creates a list of the atoms.inp files to send to Webatoms
inpList = os.listdir(path)
count=0
flag=0
#LocalVariables
for inp in inpList:
    # Open url get status code
    inpExt = str(inp.rstrip()) + '.inp'
    url = 'http://cars9.uchicago.edu/webatoms?url=http://cars9.uchicago.edu/atomsdb/' + inpExt
    req = requests.get(url)
    status = req.status_code
    # Open url get status code
    if status != 500: #defensive coding in the case of database erro
        #if flag <= 2:
            #Variables
            i_path = "C:\\Users\\boltz\\PycharmProjects\\untitled\\venv\\" + base_Element_Name+"\\"+inp.rstrip()
            i_pathExt = i_path+".inp"
            inpExt = str(inp.rstrip()) + '.inp'
            angstrom = -0.1
            a = str(" PRINT     5      0     0     5     1      5\n")
            feff8_string = ' * This feff8 '

            #end Variables
            #Change directory for Web atoms to get the file
            os.chdir(i_path)
            #End Change
            #Open browswer object with parser = 'html.parser'
            br=RoboBrowser(parser='html.parser')
            #End open
            #Assign url get statment where the path is equal to os.dirche you did earlier
            url = 'http://cars9.uchicago.edu/webatoms/?file=' + inpExt
            #Open url
            br.open(url)
            #get main form
            form1=br.get_form(id='main')
        #Angstrom lengths, this formats the numbers to 5 decimals
            a_ang=float("{0:.5f}".format(float(form1['a'].value)))
            b_ang=float("{0:.5f}".format(float(form1['b'].value)))
            c_ang=float("{0:.5f}".format(float(form1['c'].value)))
            #starts from the ceiling of -0.1 from inital angstrom length
            a_nu=a_ang+angstrom
            b_nu=b_ang+angstrom
            c_nu=c_ang+angstrom
            print("old->"+str(a_ang)+" new->"+str(a_nu))
            print("old->"+str(b_ang)+" new->"+str(b_nu))
            print("old->"+str(c_ang)+" new->"+str(c_nu))

            # gets the text output of the feff, and copies the top part
            src = str(br.parsed(id="atomsoutput"))
            src_End = len(src)
            src_1 = (src[64:(src_End - 12)])
            src_top=(feff8_string+src_1[14:430])

            for count in range(0,11):
                #Enters the input into web atoms

                form = br.get_form(id='main')
                form['st'].value = '8elements'
                form['rc'].value = 10
                form['rm'].value = 10
                form['rs'].value = 10
                a_ang=a_nu
                b_ang=b_nu
                c_ang=c_nu
                form['a'].value=a_ang
                form['b'].value=b_ang
                form['c'].value=c_ang
                #submits the form
                br.submit_form(form)
                final_feff_name = inp.rstrip() + "_" + str(float("{0:.5f}".format(a_nu)))
                i_path_nu = "C:\\Users\\boltz\\PycharmProjects\\untitled\\venv\\" + base_Element_Name+"\\"+inp.rstrip()+"\\"+final_feff_name
                if not os.path.exists(i_path_nu):
                    os.makedirs(i_path_nu)
                os.chdir(i_path_nu)

                #Parses feff ouput
                src_nu = str(br.parsed(id="atomsoutput"))
                src_End_nu= len(src_nu)
                src_1_nu = (src_nu[254:(src_End_nu - 12)])
                print(final_feff_name)
                #adds the title part(that doesnt change) and adds the new bottom part for each differe angstrom length
                total_src=src_top+src_1_nu
                # creates and writes file object new feff.inp file
                file = open("feff.inp", "w")
                file.write(total_src)
                file.close()


                # reads new file object
                with open('feff.inp', "r") as f:
                    lines = f.readlines()
                # writes in the line
                with open('feff.inp', "w") as f:
                    for line in lines:
                        if line[0:6] == " PRINT":  # searching for the specific line to replace with a
                            line = a
                        f.write(line)
               #adds 0.02 to the angstorm length
                a_nu+=0.02
                b_nu+=0.02
                c_nu+=0.02

                count+=1
    else:
        print("Error 500!!! "+inpExt+" !!!ERROR500")
    #flag += 1
