import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
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



#medidas ventana aplicacion
app_ancho = 530
app_alto = 350

root = Tk()
root.config(bg='white')
root.resizable(False, False)
root.title('Xero - Crosshairs Changer GUI')

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

zoom_weapons_lb = Label(root, text='Zoom Weapons:', bg='white')

primary = IntVar()
secondary = IntVar()


check_primary = ttk.Checkbutton(root, text='Primary (Normal)', variable=primary, onvalue=1, offvalue=0)
check_primary['state'] = 'disabled'
check_secondary = ttk.Checkbutton(root, text='Secondary (Zoom)', variable=secondary, onvalue=1, offvalue=0)
check_secondary['state'] = 'disabled'

btn_set_crosshair = ttk.Button(root, text='Set CrossHair', width=18)
btn_own_corsshair = ttk.Button(root, text='Add Own CrossHair', width=18)
btn_refresh = ttk.Button(root, text='Restore Default', width=18)

xero_lb = Label(root, text='@Wanheda', bg='white', fg='blue', cursor='hand2')

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
    status_lb.configure(text="Status: The App is on Xero folder, Great!", fg='green')

def enableCheckButtons(event):
    xmldoc = minidom.parse('xml/crosshairs.xml')
    crosshairs = xmldoc.getElementsByTagName('crosshair')
    weapon_selected = combo_armas.get()
    for cross in crosshairs:
        if(weapon_selected != 'Select a weapon ...'):
            if(cross.getAttribute('id') == weapons[weapon_selected]):
                if(cross.childNodes):
                    check_primary['state'] = 'enable'
                    check_secondary['state'] = 'enable'
                else:
                    check_primary['state'] = 'disable'
                    check_secondary['state'] = 'disable'
        else:
            pass
        
def restoreCrossHairs():
    restore = """\
<?xml version="1.0" encoding="utf-8"?>\n
<crosshairs>
	<crosshair id="2000001" path="melee.dds" /> <!-- Plasma Sword -->
	<crosshair id="2000002" path="melee.dds" /> <!-- Counter Sword -->
	<crosshair id="2000003" path="melee.dds" /> <!-- Storm Bat -->
	<crosshair id="2000006" path="melee.dds" /> <!-- Spy Dagger -->
	<crosshair id="2000010" path="melee.dds" /> <!-- Twin Blades -->
	<crosshair id="2000013" path="melee.dds" /> <!-- Breaker -->
	<crosshair id="2000017" path="melee.dds" /> <!-- Sigma Blade -->
	<crosshair id="2000018" path="melee.dds" /> <!-- Katana -->
	<crosshair id="2000029" path="melee.dds" /> <!-- Exo Scythe -->
	<crosshair id="2000030" path="melee.dds" /> <!-- Iron Boots -->
	<crosshair id="2000036" path="melee.dds" /> <!-- Metallic Fist -->
	<crosshair id="2000063" path="melee.dds" /> <!-- Vital Shock -->
	<crosshair id="2010000" path="cross.dds" /> <!-- Submachine Gun -->
	<crosshair id="2010002" path="cross.dds" /> <!-- Revolver -->
	<crosshair id="2010004"> <!-- Semi Rifle -->
		<primary path="cross.dds" />
		<secondary path="zoom.dds" />
	</crosshair>
	<crosshair id="2020001" path="cross.dds" /> <!-- Heavy Machine Gun -->
	<crosshair id="2030001"> <!-- Rail Gun -->
		<primary path="circle2.dds" />
		<secondary path="zoom.dds" />
	</crosshair>
	<crosshair id="2030002"> <!-- Cannonade -->
		<primary path="circle3.dds" />
		<secondary path="zoom1.dds" />
	</crosshair>
	<crosshair id="2040001" path="stationary.dds" /> <!-- Sentry Gun -->
	<crosshair id="2050001" path="projectile.dds" /> <!-- Mine Gun -->
	<crosshair id="2060001" path="circle.dds" /> <!-- Mind Energy -->
	<crosshair id="2060002" path="circle.dds" /> <!-- Mind Shock -->
	<crosshair id="2020002" path="cross.dds" /> <!-- Gauss Rifle -->
	<crosshair id="2040003" path="stationary.dds" /> <!-- Senti Nell -->
	<crosshair id="2010006" path="cross.dds" /> <!-- Smash Rifle -->
	<crosshair id="2010007" path="cross.dds" /> <!-- Handgun -->
	<crosshair id="2010008" path="cross.dds" /> <!-- Shotgun -->
	<crosshair id="2010016" path="circle.dds" /> <!-- Air Gun -->
	<crosshair id="2010015" path="circle1.dds" /> <!-- Homing Rifle -->
	<crosshair id="2051337" path="circle.dds" /> <!-- Air Gun -->
	<crosshair id="2010019" path="circle1.dds" /> <!-- Shockwave Gun -->
	<crosshair id="2020007" path="circle1.dds" /> <!-- Lightmachine Gun -->
	<crosshair id="2010018" path="circle1.dds" /> <!-- Spark Rifle -->
	<crosshair id="2010024" path="cross.dds" /> <!-- Assault Rifle -->
	<crosshair id="2050004" path="projectile.dds" /> <!-- Rescue Gun -->
	<crosshair id="2030006"> <!-- Sharpshooter -->
		<primary path="cross.dds" />
		<secondary path="zoom.dds" />
	</crosshair>
	<crosshair id="2010028" path="cross.dds" /> <!-- Dual Magnum -->
	<crosshair id="2020005" path="cross.dds" /> <!-- Turret -->
</crosshairs>
"""
    dom = minidom.parseString(restore)
    with open('xml/crosshairs.xml', 'w') as fich:
        dom.writexml(fich)
    refreshCrossHairs()
    status_lb.configure(text="Status: Crosshairs have been restored by default!", fg='blue')


def setCrossHair():
    xmldoc = minidom.parse('xml/crosshairs.xml')
    crosshairs = xmldoc.getElementsByTagName('crosshair')
    weapon_selected = combo_armas.get()
    crosshair_selected = combo_punteros.get()
    for cross in crosshairs:
        if(crosshair_selected != 'Select a crosshair ...' and weapon_selected != 'Select a weapon ...'):
            if(cross.getAttribute('id') == weapons[weapon_selected]):
                if(cross.childNodes):
                    if(primary.get()):
                        cross.childNodes.item(3).setAttribute('path', crosshair_selected)
                        status_lb.configure(text='Status: The crosshair has been changed!', fg='green')
                    if(secondary.get()):
                        cross.childNodes.item(5).setAttribute('path', crosshair_selected)
                        status_lb.configure(text='Status: The crosshair has been changed!', fg='green')
                else:
                    cross.setAttribute('path', crosshair_selected)
                    status_lb.configure(text='Status: The crosshair has been changed!', fg='green')
            else:
                status_lb.configure(text='Status: The crosshair has been changed!', fg='green')
        else:
            status_lb.configure(text='Status: Check that you have selected weapon and crosshair!', fg='orange')

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

def xero_profile(event):
    os.system('start https://xero.gg/player/Wanheda/')

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

    xero_lb.place(x=430, y=325)
    xero_lb.bind('<Button-1>', xero_profile)

    zoom_weapons_lb.place(x=13, y=210)
    

    check_primary.place(x=15, y=230)
    check_secondary.place(x=15, y=255)

    btn_refresh.place(x=405, y=295)
    btn_refresh.bind('<Button-1>', lambda event: restoreCrossHairs())

    btn_set_crosshair.place(x=405, y=265)
    btn_set_crosshair.bind('<Button-1>', lambda event: setCrossHair())

    btn_own_corsshair.place(x=405, y=235)
    btn_own_corsshair.bind('<Button-1>', lambda event: addOwnCrossHair())


root.mainloop()

