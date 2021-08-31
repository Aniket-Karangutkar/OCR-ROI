from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from easyocrtest import implementOcr
# from testFile import test

def performOcr(filepath):
    global total
    # filepath = r'{}'.format(filepath[58:])
    
    amount, img2 = implementOcr(filepath)
    total += int(amount)
    img2 = Image.fromarray(img2)
    img2 = img2.resize((380, 200), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    imgArea2 = Label(root, image=img2)
    imgArea2.image = img2
    imgArea2.place(x=110, y=340)

    lblTotal = Label(root, text="TOTAL").place(x=280, y=600)
    lblAmount = Label(root, text="            ").place(x=285, y=620)
    lblAmount = Label(root, text=amount).place(x=285, y=620)
    

def getFile():
    filepath = filedialog.askopenfilename(title ='open')
    return filepath


def openFile():
    filepath = getFile()
    if(filepath == ''):
        print('[INFO]: Empty')
    else:
        img = Image.open(filepath)
        img = img.resize((380, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        imgArea = Label(root, image=img)
        imgArea.image = img
        imgArea.place(x=110, y=80)

        btnOcr = Button(root, text='Perform OCR', command= lambda: performOcr(filepath)).place(x=260, y=300)



root = Tk()
root.title("Currency Calculator")
root.geometry("600x800")
total = 0
myLabel = Label(root, text = "Currency Calculator")
myLabel.pack()
    
btnImg = Button(root, text='Select Note', command = openFile).place(x=265, y=40)

mainloop()

