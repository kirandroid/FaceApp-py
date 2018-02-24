from tkinter import *
import io
from PIL import Image, ImageTk
from faceapp.faceapp import FaceApp

Fa = FaceApp()
filters = ['smile', 'smile_2', 'hot', 'old', 'young', 'female', 'male']

window = Tk()
window.geometry("418x300")

def ok():
    global saved_img
    selected_filter_str = selected_filter.get()
    code = Fa.get_code('./img/paveldurov.jpg')

    b = Fa.make_img(code, selected_filter_str)
    image = Image.open(io.BytesIO(b))
    image.save('./img/' + str(selected_filter_str) + '.png')

    image = Image.open('./img/'+ str(selected_filter_str) + '.png')
    photo = ImageTk.PhotoImage(image)

    label = Label(window, image=photo)
    label.image = photo 
    label.pack()


selected_filter = StringVar(window)
selected_filter.set(filters[0])

dropdown = OptionMenu(window, selected_filter, *filters)
dropdown.pack()

button = Button(window, text="OK", command=ok)
button.pack()


window.mainloop()

