#IQG

#import libraries
import tkinter as tk
from tkinter import ttk
import random
import csv


background = "#d9dbda"
textcolor = "black"


#creation of main window (Tk() object)-------------------------------------------------------------------------
master = tk.Tk()
master.title("Main")
#geometry of main root window (master)
master.geometry("680x500")
master.configure(bg=background)


#night and daymodes---------------------------------------------------------------------------

def night():
    global background
    global textcolor
    background = "black"
    textcolor = "white"
    master.configure(bg=background)
    label.configure(bg=background, fg=textcolor)
    addboxButton.configure(bg=background, fg=textcolor)
    ohje.configure(bg=background, fg=textcolor)
    frame_for_boxes.configure(bg=background)
    saveButton.configure(bg=background, fg=textcolor)
    qlab.configure(bg=background, fg=textcolor)
    quotebtn.configure(bg=background, fg=textcolor)
    btn2.configure(bg=background, fg=textcolor)
    daymode.configure(bg=background, fg=textcolor)
    nightmode.configure(bg=background, fg=textcolor)
    maara1.configure(bg=background, fg=textcolor)
    maara2.configure(bg=background, fg=textcolor)

def day():
    background = "#d9dbda"
    textcolor = "black"
    master.configure(bg=background)
    label.configure(bg=background, fg=textcolor)
    addboxButton.configure(bg=background, fg=textcolor)
    ohje.configure(bg=background, fg=textcolor)
    frame_for_boxes.configure(bg=background)
    saveButton.configure(bg=background, fg=textcolor)
    qlab.configure(bg=background, fg=textcolor)
    quotebtn.configure(bg=background, fg=textcolor)
    btn2.configure(bg=background, fg=textcolor)
    daymode.configure(bg=background, fg=textcolor)
    nightmode.configure(bg=background, fg=textcolor)
    maara1.configure(bg=background, fg=textcolor)
    maara2.configure(bg=background, fg=textcolor)


daymode = tk.Button(master, text="Daymode", command=day, bg=background, fg=textcolor)
daymode.pack(anchor="w", pady=5, padx=10)

nightmode = tk.Button(master, text="Nightmode", command=night, bg=background, fg=textcolor)
nightmode.pack(anchor="w", padx=10)


#----------------------------------------------------------------------------


#text top of main window
label = tk.Label(master, text="Incorrect Quote Generator", font="Georgia 9", bg=background, fg=textcolor)
label.pack(pady = 10)


#------------------------------------


#creation of submission boxes for character names

char_num = 0 #number of characters
next_column = 0

def addBox():
    global char_num
    if char_num < 4:

        # use len(all_entries) to get number of next free column
        next_column = len(all_entries)

        # add entry in second row
        ent = ttk.Entry(frame_for_boxes)
        ent.grid(row=1, column=next_column, pady=5)

        all_entries.append(ent)

        char_num = char_num + 1

    else:
        pass

#------------------------------------

def saveEntries():
    #if names have already been entered (they are in the list 'names'), empty them
    if len(names) > 0:
        names.clear()
    #add new names to the list 'names'
    for i in all_entries:
        if str(i.get()) == "":
            #don't add empty inputs
            pass
        else:
            names.append(str(i.get()))

#------------------------------------

all_entries = []
names = []

#add an input field for names with a button
addboxButton = tk.Button(master, text="Add name of character", command=addBox, bg=background, fg=textcolor)
addboxButton.pack(anchor=tk.CENTER)
#instructions
ohje = tk.Label(master, text="(Max 4 characters)", bg=background, fg=textcolor)
ohje.pack(anchor=tk.CENTER)

frame_for_boxes = tk.Frame(master, bg=background)
frame_for_boxes.pack(anchor=tk.CENTER)

#button for saving
saveButton = tk.Button(master, text='Submit', command=saveEntries, bg=background, fg=textcolor)
saveButton.pack(anchor=tk.CENTER)


#-------------------------------------------------------------

#read quotes from the file
def read_file(file_path, index):
    #file_path: name of the file, where the quotes are (or whole path, if not in the same folder)
    #index: how many quotes will be selected
    with open(file_path, 'r') as t:
        all_quotes = list(csv.reader(t, delimiter=';'))
        file_text = all_quotes[index][0]
    return file_text



#combining quotes to a possible name and creating linebreakes
def concatenate(user_input, file_text):
    #user_input: names, input by the user, in a list
    #file_text: quote selected from the file before modifications

    #find the correct part of the text (name)
    names = user_input
    break_words = ["nimi1", "nimi2", "nimi3", "nimi4"] #place holders for names in the file
    combined_text = file_text
    for j in range(len(names)): #go through all names the user has input
        break_word = break_words[j]
        break_index = combined_text.find(break_word)
        while break_index != -1: #find all parts in the text, where the current place holder is featured
            #add user's input to text and delete break_word by jumping over it
            combined_text = combined_text[:break_index] + names[j] + combined_text[break_index + len(break_word):]
            break_index = combined_text.find(break_word) #returns -1, when a place holder is no longer found (all have been replaced)


    #check if linebreaks are needed
    enter = "rivinvaihto" #placeholder word for indicating a linebreak
    enter_index = combined_text.find(enter)
    if enter_index == -1:
        final_text = [combined_text]
    else:
        final_text = []
        while enter_index != -1:
            between = combined_text[:enter_index]
            final_text.append(between)
            rest = combined_text[enter_index + len(enter) + 1:]
            enter_index = rest.find(enter)
            combined_text = rest
        final_text.append(combined_text)

    return final_text

#---------------------------------------------------------


#diplay quotes in the main window
def display():
    lukum = len(names)
    if lukum == 0:
        pass
    else:
        if lukum == 1:
            n1 = names
            with open("Quotes/onechar.csv", 'r') as t:
                all_quotes = list(csv.reader(t, delimiter=';'))
                pituus = len(all_quotes)
            luku = random.randint(0, pituus-1)
            quote_original = read_file("Quotes/onechar.csv", luku)
            quote = concatenate(n1, quote_original)
        elif lukum == 2:
            n2 = names
            with open("Quotes/twochar.csv", 'r') as t:
                all_quotes = list(csv.reader(t, delimiter=';'))
                pituus = len(all_quotes)
            luku = random.randint(0, pituus-1)
            quote_original = read_file("Quotes/twochar.csv", luku)
            quote = concatenate(n2, quote_original)
        elif lukum == 3:
            n3 = names
            with open("Quotes/threechar.csv", 'r') as t:
                all_quotes = list(csv.reader(t, delimiter=';'))
                pituus = len(all_quotes)
            luku = random.randint(0, pituus-1)
            quote_original = read_file("Quotes/threechar.csv", luku)
            quote = concatenate(n3, quote_original)
        else:
            n4 = names
            with open("Quotes/fourchar.csv", 'r') as t:
                all_quotes = list(csv.reader(t, delimiter=';'))
                pituus = len(all_quotes)
            luku = random.randint(0, pituus-1)
            quote_original = read_file("Quotes/fourchar.csv", luku)
            quote = concatenate(n4, quote_original)

        qlab.config(text="\n".join(quote))

qlab = tk.Label(master, text="", bg=background, fg=textcolor)
quotebtn = tk.Button(master, text="Give a random quote", command=display, bg=background, fg=textcolor)
quotebtn.pack(pady=20)
qlab.pack()

#button for closing the window
btn2 = tk.Button(master, text="Close", font="Georgia 9", command=master.destroy, bg=background, fg=textcolor)
btn2.pack(side=tk.BOTTOM, pady=17)

#number of quotes
with open("Quotes/onechar.csv", 'r') as t:
    all_quotes_1 = list(csv.reader(t, delimiter=';'))
    pituus1 = len(all_quotes_1)
with open("Quotes/twochar.csv", 'r') as t:
    all_quotes_2 = list(csv.reader(t, delimiter=';'))
    pituus2 = len(all_quotes_2)
with open("Quotes/threechar.csv", 'r') as t:
    all_quotes_3 = list(csv.reader(t, delimiter=';'))
    pituus3 = len(all_quotes_3)
with open("Quotes/fourchar.csv", 'r') as t:
    all_quotes_4 = list(csv.reader(t, delimiter=';'))
    pituus4 = len(all_quotes_4)
teksti = f"1 character: {pituus1}, 2 characters: {pituus2}, 3 characters: {pituus3}, 4 characters: {pituus4}"
maara2 = tk.Label(master, text=teksti, bg=background, fg=textcolor)
maara2.pack(pady=3, side=tk.BOTTOM)
maara1 = tk.Label(master, text="Number of quotes:", bg=background, fg=textcolor)
maara1.pack(side=tk.BOTTOM)


#mainloop, run indefinitely
tk.mainloop()
