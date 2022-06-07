import os
import glob
mp3_files = glob.iglob('**/*.webm', recursive=True)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def listmp3(mp3_files):
    mp3_files = glob.iglob('**/*.webm', recursive=True)
    listmp3files = []
    count = 0
    for file in mp3_files:
        count += 1
        print(f"{bcolors.OKGREEN}{count}. {file}{bcolors.ENDC}")
        listmp3files.append(file)
    return listmp3files

def playmp3(choice):
    os.system(f"play-audio {choice}") 

def mainapp(mp3_files):
    
        print(f"""{bcolors.OKGREEN}Enter the choice number or press 'q' to quit: {bcolors.ENDC}""")
        listmp3files = listmp3(mp3_files=mp3_files)
        choice = input("> ")
        if choice == 'q':
            exit()
        try:
            playmp3(listmp3files[int(choice)-1])
        except: 
            print(f"{bcolors.FAIL}Invalid choice{bcolors.ENDC}")

while True:
    mainapp(mp3_files)
