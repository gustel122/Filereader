#-------------------------------------------------------------------#
# This is a Filereader written in Python 3.10
# Author: J.Matthias
# Description:
# You can write or reading or what appending in a File
#-------------------------------------------------------------------#

def Path_Contoller():
    is_path = False
    for i in path:
        if i == ':' or i == '"\"':
            is_path = True
    return is_path

#------------------------------------------------------------------#
# User Input
# What does the user want to do with this file?
#------------------------------------------------------------------#

# Where is the File (Path to the File)?
path = input("Bitte gib dein Pfade zu deiner Datei an!\n")

# Is it a Path ?
if Path_Contoller():
    action = input("Was möchtest du mit dieser Datei an stellen? Gib den jeweiligen Buchstaben an! Lesen: r; Schreiben: w oder Hinzufügen: a \n")

# if not a path --> ignore this lines of Code
try:
    if action == 'w' or action == 'a':
        file_write = input("Was soll in die Datei geschrieben werden?\n")
except NameError:
    pass

#---------------------------------------------------------------------------#
# Logic
# Description:
# if the choose of the User r, the Reader will read the file
# if the choose of the User w, the Reader will writes the file
# if the choose of the User a, the Reader will what appending in this file
# NOTICE: when the user chooses w to write the file and the user does not write
#         and press Enter the file content is deleted !!!!! 
#----------------------------------------------------------------------------#

try:
    if Path_Contoller():
        if action == 'r':
            with open(path,action) as file:
                for i in file:
                    print(f"Ausgabe: {i}")
        elif action == 'w':
            if file_write != "":
                with open(path,action) as file:
                        file.writelines(file_write)
                print("Datei wurde beschrieben!")
            else:
                print("Bitte geben Sie ein Inhalt an!")
        elif action == 'a':
            with open(path,action) as file:
                file.write(file_write)
            print("Datei wurde beschrieben!")
        else:
            print("Bitte gib eine der drei Auswahl möglichkeiten an! (r; w; a)")
    else:
        print("Bitte gib einen Pfad an!")
except OSError or PermissionError:
    print("ERROR: Der Pfad ist nicht gültig oder Sie haben nicht ausreichende Rechte um darauf zu zugreifen")
# END
