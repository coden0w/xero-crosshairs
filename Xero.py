
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from PIL import ImageFile
import os
from xml.dom import minidom
import shutil

xero_dir = os.getcwd()
print(xero_dir)

ImageFile.LOAD_TRUNCATED_IMAGES = True

#medidas ventana aplicacion
app_ancho = 530
app_alto = 350

root = Tk()
root.config(bg='white')
root.iconbitmap('./crosshair.ico')
root.resizable(False, False)
root.title('Xero - Crosshairs Changes GUI')

#centrar aplicacion en el centro de la pantalla
monitor_ancho = root.winfo_screenwidth()
monitor_alto = root.winfo_screenheight()
centro_x = int(monitor_ancho/2 - app_ancho/2)
centro_y = int(monitor_alto/2 - app_alto/2)
root.geometry(f'{app_ancho}x{app_alto}+{centro_x}+{centro_y}')

#elementos
arma_seleccionada = tk.StringVar()
puntero_seleccionado = tk.StringVar()

combo_armas = ttk.Combobox(root, textvariable=arma_seleccionada, width=35)
combo_punteros = ttk.Combobox(root, textvariable=puntero_seleccionado, width=35)

btn_set_crosshair = ttk.Button(root, text='Set CrossHair', width=18)
btn_own_corsshair = ttk.Button(root, text='Add Own CrossHair', width=18)
btn_refresh = ttk.Button(root, text='Refresh CrossHair', width=18)

status_lb = Label(root, text="Status: ", bg='white')
status_lb.place(x=5, y=325)

#funciones
def checkXeroFolder():
    if(os.path.exists('crosshairs') and os.path.exists('xml')):
        status_lb.configure(text="Status: The App is on Xero folder, Great!")
        return True
    else:
        status_lb.configure(text="Status: The App isn't on Xero Folder, Try Again!", fg='red')
        return False

def listCrossHairs():
    crosshairs = ['Select a crosshair ...']
    crosshairs.extend(os.listdir('crosshairs/'))
    return crosshairs

def listWeaponsXML():
    xmldoc = minidom.parse('xml/crosshairs.xml')
    crosshairsXML = xmldoc.getElementsByTagName('crosshair')
    for crosshairXML in crosshairsXML:
        pass
    return 0

def refreshCrossHairs():
    combo_punteros['values'] = listCrossHairs()
    combo_punteros.current(0)
    combo_armas['values'] = listWeaponsXML()
    combo_armas.current(0)

def setCrossHair():
    print('Set CrossHair')

def addOwnCrossHair():
    filetype = (
        ('Image File *.png', '*.png'),
        ('DDS File *.dds', '*.dds'),
        ('All Types *.*', '*.*')
    )
    f = fd.askopenfile(filetypes=filetype)
    if(f != None):
        nombre_fich = f.name.split('/')
        print('Nom Fich: ', nombre_fich[len(nombre_fich)-1])
        os.chdir('crosshairs')
        xero_dir = os.getcwd()
        shutil.copy(f.name, xero_dir)
        os.chdir('../')
        xero_dir = os.getcwd()
        refreshCrossHairs()
        status_lb.configure(text='Status: Crosshair added!', fg='green')
    else:
        status_lb.configure(text='Status: No crosshair selected!', fg='red')


#Comprobaciones
status = checkXeroFolder()

if(status):    
    combo_armas['values'] = listWeaponsXML()
    combo_armas['state'] = 'readonly'
    combo_armas.current(0)
    combo_armas.place(x=15, y=20)
    
    combo_punteros['values'] = listCrossHairs()
    combo_punteros['state'] = 'readonly'
    combo_punteros.current(0)
    combo_punteros.place(x=280, y=20)

    btn_refresh.place(x=405, y=305)
    btn_refresh.bind('<Button-1>', lambda event: refreshCrossHairs())

    btn_set_crosshair.place(x=405, y=275)
    btn_set_crosshair.bind('<Button-1>', lambda event: setCrossHair())

    btn_own_corsshair.place(x=405, y=245)
    btn_own_corsshair.bind('<Button-1>', lambda event: addOwnCrossHair())


root.mainloop()

