from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox

def accion():
    enlace = link.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download(output_path="Descargas")
    MessageBox.showinfo("Éxito", "Video descargado correctamente en la carpeta seleccionada.")

root = Tk()
root.config(bd=15)
root.title("YouDownloader - By Gero")

imagen = PhotoImage(file="img/logo.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

instrucciones = Label(root, text="Descarga videos de youtube solo con el link")
instrucciones.grid(row=0, column=1)

link = Entry(root)
link.grid(row=1, column=1)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1)

root.mainloop()