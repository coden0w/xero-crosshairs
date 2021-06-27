
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
import json

xero_dir = os.getcwd()
print(xero_dir)
weapons = {
    "Plasma Sword":"2000001",
    "Counter Sword":"2000002",
    "Storm Bat":"2000003",
    "Spy Dagger":"2000006",
    "Twin Blades":"2000010",
    "Breaker":"2000013",
    "Sigma Blade":"2000017",
    "Katana":"2000018",
    "Exo Scythe":"2000029",
    "Iron Boots":"2000030",
    "Metallic Fist":"2000036",
    "Vital Shock":"2000063",
    "Submachine Gun":"2010000",
    "Revolver":"2010002",
    "Semi Rifle":"2010004",
    "Heavy Machine Gun":"2020001",
    "Rail Gun":"2030001",
    "Cannonade":"2030002",
    "Sentry Gun":"2040001",
    "Mine Gun":"2050001",
    "Mind Energy":"2060001",
    "Mind Shock":"2060002",
    "Gauss Rifle":"2020002",
    "Senti Nell":"2040003",
    "Smash Rifle":"2010006",
    "Handgun":"2010007",
    "Burst Shotgun":"2010008",
    "Air Gun":"2010016",
    "Shockwave Gun":"2010019",
    "Lightmachine Gun":"2020007",
    "Spark Rifle":"2010018",
    "Assault Rifle":"2010024",
    "Rescue Gun":"2050004",
    "Sharpshooter":"2030006",
    "Dual Magnum":"2010028",
    "Turret":"2020005"
}

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

primary = IntVar()
secondary = IntVar()

check_primary = ttk.Checkbutton(root, text='Primary (Normal)', variable=primary, onvalue=1, offvalue=0)
check_primary['state'] = 'disabled'
check_secondary = ttk.Checkbutton(root, text='Secondary (Zoom)', variable=secondary, onvalue=1, offvalue=0)
check_secondary['state'] = 'disabled'

btn_set_crosshair = ttk.Button(root, text='Set CrossHair', width=18)
btn_own_corsshair = ttk.Button(root, text='Add Own CrossHair', width=18)
btn_refresh = ttk.Button(root, text='Refresh', width=18)

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

def listWeapons():
    weaps = ['Select a weapon ...']
    weaps.extend([*weapons])
    return weaps

def refreshCrossHairs():
    combo_punteros['values'] = listCrossHairs()
    combo_punteros.current(0)
    combo_armas['values'] = listWeapons()
    combo_armas.current(0)

def enableCheckButtons(event):
    xmldoc = minidom.parse('xml/crosshairs.xml')
    crosshairs = xmldoc.getElementsByTagName('crosshair')
    weapon_selected = combo_armas.get()
    for cross in crosshairs:
        if(cross.getAttribute('id') == weapons[weapon_selected]):
            if(cross.childNodes):
                check_primary['state'] = 'enable'
                check_secondary['state'] = 'enable'
            else:
                check_primary['state'] = 'disable'
                check_secondary['state'] = 'disable'



def setCrossHair():
    xmldoc = minidom.parse('xml/crosshairs.xml')
    crosshairs = xmldoc.getElementsByTagName('crosshair')
    weapon_selected = combo_armas.get()
    crosshair_selected = combo_punteros.get()
    for cross in crosshairs:
        if(cross.getAttribute('id') == weapons[weapon_selected]):
            if(cross.childNodes):
                if(primary.get()):
                    cross.childNodes.item(3).setAttribute('path', crosshair_selected)
                if(secondary.get()):
                    cross.childNodes.item(5).setAttribute('path', crosshair_selected)
            else:
                cross.setAttribute('path', crosshair_selected)

    with open('xml/crosshairs.xml', 'w') as fich:
        xmldoc.writexml(fich)




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
    combo_armas['values'] = listWeapons()
    combo_armas['state'] = 'readonly'
    combo_armas.current(0)
    combo_armas.place(x=15, y=20)
    combo_armas.bind('<<ComboboxSelected>>', enableCheckButtons)
    
    combo_punteros['values'] = listCrossHairs()
    combo_punteros['state'] = 'readonly'
    combo_punteros.current(0)
    combo_punteros.place(x=280, y=20)


    check_primary.place(x=15, y=230)
    check_secondary.place(x=15, y=255)

    btn_refresh.place(x=405, y=305)
    btn_refresh.bind('<Button-1>', lambda event: refreshCrossHairs())

    btn_set_crosshair.place(x=405, y=275)
    btn_set_crosshair.bind('<Button-1>', lambda event: setCrossHair())

    btn_own_corsshair.place(x=405, y=245)
    btn_own_corsshair.bind('<Button-1>', lambda event: addOwnCrossHair())


root.mainloop()

