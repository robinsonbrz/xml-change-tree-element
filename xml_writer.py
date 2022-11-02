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


# sobrescrevendo host com a string ""
root.find('.//Parameter[@name="host"]').text = "localhost"
root.find('.//Parameter[@name="port"]').text = "25432"

print(root.find('.//Parameter[@name="host"]').text)
print()


datasource_parameter_type_value = root.find('.//Parameter[@name="host"]')


tree.write("novo_area_do_projeto.xml")


# # lista todos valores internos ao datasource
# dss = tree.find("Layer/Datasource")
# for ds in dss:
#     print(ds.text)

