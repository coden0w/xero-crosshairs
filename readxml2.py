from xml.dom import minidom

xmldoc = minidom.parse('crosshairs.xml')

print('Nombre Nodo: ', xmldoc.firstChild.tagName)

crosshairs = xmldoc.getElementsByTagName('crosshair')

for c in crosshairs:
    print(f'ID: {c.getAttribute("id")}\nPATH: {c.getAttribute("path")}\n-----------')



primary = crosshairs[16].childNodes.item(3)
secondary = crosshairs[16].childNodes.item(5)
print(primary.getAttribute('path'))
print(secondary.getAttribute('path'))
primary.setAttribute('path', 'circle2.dds')
print(primary.getAttribute('path'))

with open('crosshairs.xml', 'w') as file:
    xmldoc.writexml(file)