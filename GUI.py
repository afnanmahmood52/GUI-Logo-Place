import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from algorithm import algorithm_call

width = 600
height = 500

mainFrame = tk.Tk() 
mainFrame.title('Water Marking Application') 

mainFrame.geometry("600x520")
mainFrame.resizable(False,False)

def printDestination():
    print("Source Folder:\n" + source_textField.get())
    print("WaterMark:\n" + waterMark_textField.get())
    print("Output Folder:\n" + output_textField.get())
    print("Filetype:\n" + filetype.get())
    print("Water Mark Position:\n" + str(watermark_pos.get()))

# To get source directory
def getSource_directory():
   source_folder = askdirectory()
   source_textField.delete(0,END)
   source_textField.insert(0,source_folder)

# To get WaterMark file
def getWaterMark_directory(): 
    watermark_directory = filedialog.askopenfilename(initialdir = "/",title = "Select Water Mark file",filetypes = (("JPEG(*.jpg;*.JPG)","*.jpg;*.JPG"),("PNG(.png;*.PNG)","*.png;*.PNG")))
    waterMark_textField.delete(0,END)
    waterMark_textField.insert(0,watermark_directory)

# To get Output folder
def getOutput_directory():
   output_folder = askdirectory()
   output_textField.delete(0,END)
   output_textField.insert(0,output_folder)

def waterMark_Algorithm():
    error = False
    print("Source Folder:\n" + source_textField.get())
    print("WaterMark:\n" + waterMark_textField.get())
    print("Output Folder:\n" + output_textField.get())
    print("Filetype:\n" + filetype.get())
    print("Water Mark Position:\n" + str(watermark_pos.get()))

    if not source_textField.get():
        messagebox.showerror("Error", "Please Select the Source Folder!")
        error = True

    if not waterMark_textField.get():
        messagebox.showerror("Error", "Please Select the Water Mark File (Logo)!")
        error = True

    if not output_textField.get():
        messagebox.showerror("Error", "Please Select the Destination/Output Folder!")
        error = True

    if not watermark_pos.get():
        messagebox.showerror("Error", "Position of Water Mark not selected!")
        error = True

    # algorithm_call(source_folder, watermark, output_folder, fileType, position):
    if(error == False):
        algorithm_call(source_textField.get(), waterMark_textField.get(), output_textField.get(), filetype.get(), watermark_pos.get())    

# Loading Images (For the Browse folder icon)
browse_folder = PhotoImage(file = r"C:\Users\Afnan\Desktop\WaterMarking Application\browse.png")
browse_folder = browse_folder.subsample(30,30)

# ------------------------------------------
# This part is related to the intialization
# of GUI elements
# ------------------------------------------

# Label for Main Heading
label1 = tk.Label(mainFrame, text="Image Water Marking Program",font ="Helvetica 28 bold",fg='blue')

# -----------------------------------------
#              Source Folder
# -----------------------------------------
# source_label = text to select Source folder
# source_button = Browse button
# source_textField = Entry field
source_label = tk.Label(mainFrame, text="Source Folder (Images without Logos):",font ="Helvetica 10 bold",fg='black')
source_button = tk.Button(mainFrame, text='Browse', image = browse_folder, compound = LEFT ,bd ='3', font ='7',command = getSource_directory) 
source_textField = tk.Entry(mainFrame)

# -----------------------------------------
#              Water Mark Logo
# -----------------------------------------
# waterMark_label = text to select WaterMark
# waterMark_button = Browse button to logo file
# waterMark_textField = Entry field
waterMark_label = tk.Label(mainFrame, text="Select the Water Mark i-e Logo:",font ="Helvetica 10 bold",fg='black')
waterMark_browse = tk.Button(mainFrame, text='Browse', image = browse_folder, compound = LEFT ,bd ='3', font ='7',command = getWaterMark_directory) 
waterMark_textField = tk.Entry(mainFrame)

# -----------------------------------------
#              Output Folder
# -----------------------------------------
# waterMark_label = text to select WaterMark
# waterMark_button = Browse button to logo file
# waterMark_textField = Entry field
output_label = tk.Label(mainFrame, text="Select the Output Folder/Directory:",font ="Helvetica 10 bold",fg='black')
output_browse = tk.Button(mainFrame, text='Browse', image = browse_folder, compound = LEFT ,bd ='3', font ='7',command = getOutput_directory) 
output_textField = tk.Entry(mainFrame)

# -------------------------------------------
#          Selecting the Output file type
# --------------------------------------------
filetype = StringVar(mainFrame)
filetype.set("JPEG") #default file type JPEG

filetype_option = OptionMenu(mainFrame,filetype,'JPEG','PNG')
filetype_label = tk.Label(mainFrame, text="Output file type:",font ="Helvetica 10 bold",fg='black')

# -----------------------------------------------------------
#   Radio Buttons and Rectangle
# -----------------------------------------------------------

WaterMarkPos_label = tk.Label(mainFrame, text="Select Position of Water Mark:",font ="Helvetica 10 bold",fg='black')

watermark_pos = IntVar()

top_left = tk.Radiobutton(mainFrame, text = "Top Left", variable=watermark_pos, value = 1)
top_right = tk.Radiobutton(mainFrame, text = "Top Right", variable=watermark_pos, value = 2)
bottom_left = tk.Radiobutton(mainFrame, text = "Bottom Left", variable=watermark_pos, value = 3)
bottom_right = tk.Radiobutton(mainFrame, text = "Bottom Right", variable=watermark_pos, value = 4)

#-----------------------------------------------
# Start Button Intialization
#-----------------------------------------------
start = tk.Button(mainFrame, text='START', bd ='3', font ='17',command = waterMark_Algorithm) 


# ------------------------------------------
# This part is related to the placement
# of GUI elements
# ------------------------------------------

# Title Label "Water Mark Program"
label1.pack(pady=(20))

# -----------------------------------------------------------
#   Placement of Elements for browsing Source Images folder
# -----------------------------------------------------------
source_label.place(x=0.20* width, y= 0.17*height+17)
source_textField.place(x=0.20* width, y= 0.23*height+17,width='300',height='22')
source_button.place(x=0.75* width, y= 0.22*height+17,width='80',height='27')

# -----------------------------------------------------------
#   Placement of Elements for Water Mark portion
# -----------------------------------------------------------
waterMark_label.place(x=0.20* width, y= 0.35*height,width='200',height='27')
waterMark_textField.place(x=0.20* width, y= 0.42*height,width='300',height='22')
waterMark_browse.place(x=0.75* width, y= 0.408*height,width='80',height='27')

# -----------------------------------------------------------
#   Placement of Elements for Output/Destination portion
# -----------------------------------------------------------
output_label.place(x=0.20* width, y= 0.52*height,width='220',height='27')
output_textField.place(x=0.20* width, y= 0.59*height,width='300',height='22')
output_browse.place(x=0.75* width, y= 0.58*height,width='80',height='27')

# -----------------------------------------------------------
#   Placement of File type selection on the screen
# -----------------------------------------------------------
filetype_label.place(x=0.19* width, y= 0.67*height)
filetype_option.place(x=0.19* width, y= 0.72*height,width = '100')

# -----------------------------------------------------------
#   Radio Buttons Placement
# -----------------------------------------------------------
WaterMarkPos_label.place(x=0.50* width, y= 0.67*height)

top_left.place(x=0.50* width, y= 0.72*height)
top_right.place(x=0.65* width, y= 0.72*height)
bottom_left.place(x=0.50* width, y= 0.78*height)
bottom_right.place(x=0.65* width, y= 0.78*height)

# -----------------------------------------------------------
#   Placement of Start Button
# -----------------------------------------------------------
start.place(x=0.80* width, y= 0.90*height,width='100',height='40')


mainFrame.mainloop()