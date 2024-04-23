import os

#defining main
def main():
    #os.mkdir("MyFiles") #creates the initial directory NOTE: when creating subfolders, comment out the initial directory so it doesn't make a new directory each time
    os.mkdir("MyFiles/Docs") #creates a subfolder for Docs
    os.mkdir("MyFiles/Images") #creates a subfolder for Images
    os.mkdir("MyFiles/Videos") #creates a subfolder for Videos

main()