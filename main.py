from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageGrab

FONT = 'Courier'

# Grab file from Canvas widget

def getter(widget, image_name):
    # refresh widget, inthis case Canvas widget
    widget.update()

    x = window.winfo_rootx() + widget.winfo_x() + 2
    y = window.winfo_rooty() + widget.winfo_y() + 2
    x1 = x + widget.winfo_width() - 6
    y1 = y + widget.winfo_height() - 6
    ImageGrab.grab().crop((x, y, x1, y1)).save(f"{image_name}_watermarked.png")


# Open file explorer window and display in canvas chosen file

def watermark_img():
    filename = filedialog.askopenfile(initialdir='/', title="Select image", filetypes=(("Image files", '*.png*'),
                                                                                       ("all files", "*.*")))

    # Configure a Label widget to display img path
    label_img_path.configure(text=f'Image path: {filename.name}')

    img = Image.open(filename.name)
    tkimg = ImageTk.PhotoImage(img)

    # Adjust canvas size according to size of img
    canvas.config(width=tkimg.width(), height=tkimg.height())
    canvas.create_image(tkimg.width()/2, tkimg.height()/2, image=tkimg)

    # Add watermark text to canvas
    canvas.create_text(tkimg.width()-len(entry_watermark_text.get()*15), tkimg.height()-50, text=f'{entry_watermark_text.get()}', fill="white",
                       font=(FONT, 25, 'bold'))

    # Reinitialize entry widget
    entry_watermark_text.delete(0, END)
    entry_watermark_text.insert(END, string="Watermark text")

    # Save a reference of the image to avoid garbage collection
    canvas.image = tkimg

    getter(canvas, filename.name)



window = Tk()
window.title("Image Watermarking Desktop App")
window.minsize(width=300, height=300)

label_img_path = Label(text="Image path: None", foreground='blue')
label_img_path.grid(row=0, column=1, columnspan=2)

canvas = Canvas()
canvas.grid(row=1, column=0, columnspan=4)


# STEP1
label_step1 = Label(text="STEP 1:")
label_step1.grid(row=2, column=0)

# Entry widget for watermark text
entry_watermark_text = Entry(width=20)
# Text to begin with Entry widget
entry_watermark_text.insert(END, string="Watermark text")
entry_watermark_text.grid(row=2, column=1, sticky='w')


# STEP2
label_step2 = Label(text="STEP 2:")
label_step2.grid(row=3, column=0)

btn_img_import = Button(text="Pick Image to Watermark", command=watermark_img)
btn_img_import.grid(row=3, column=1, sticky='w')

window.grid_rowconfigure(3, minsize=50)

# TO DO: Create radio buttons to choose extension of file, make radio buttons functional
# Uncomment below lines

# STEP3
# label_step3 = Label(text="STEP 3:")
# label_step3.grid(row=2, column=2)

# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="JPG", value=1, variable=radio_state)
# radiobutton2 = Radiobutton(text="PNG", value=2, variable=radio_state)
# radiobutton1.grid(row=2, column=3)
# radiobutton2.grid(row=3, column=3)



window.mainloop()
