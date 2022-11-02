import xml.etree.ElementTree as ET

tree = ET.parse('novo_area_do_projeto.xml')
root = tree.getroot()

''' extract of xml file
    <Layer name="layer" srs="+proj=aea +lat_1=-2 +lat_2=-22 +lat_0=-12 +lon_0=-54 +x_0=0 +y_0=0 +ellps=aust_SA +units=m +no_defs ">
        <StyleName>layer_style</StyleName>
        <Datasource>
			<Parameter name="type">postgis</Parameter>
			<Parameter name="host">localhost</Parameter>
			<Parameter name="port">25432</Parameter>
'''


# Lendo os textos com 
host_par = root.find('.//Parameter[@name="host"]').text
host_port = root.find('.//Parameter[@name="port"]').text

print(root.find('.//Parameter[@name="host"]').text)
print(host_par)
print(host_port)


# # lista todos valores internos ao datasource
# dss = tree.find("Layer/Datasource")
# for ds in dss:
#     print(ds.text)

