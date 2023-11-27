# 웹 문서 읽기 : XML
import xml.etree.ElementTree as etree
'''
xmlf = open("../testdata/my.xml", mode="r", encoding="utf-8").read()
print(xmlf, type(xmlf))  # <class 'str'>
root = etree.fromstring(xmlf)
print(root, type(root))  # 파싱이 되었다 <class 'xml.etree.ElementTree.Element'>
print(root.tag, ' ', len(root))
print()
'''


# 더 간단한 방법
xmlfile = etree.parse("../testdata/my.xml")
print(xmlfile, type(xmlfile))
root = xmlfile.getroot()
print(root.tag)
print(root[0].tag)
print(root[0][0].tag)
print(root[0][1].tag)
print(root[0][0].attrib)
print(root[0][0].attrib.keys())
print(root[0][0].attrib.values())
print()

myname = root.find('item').find('name').text
print(myname)
print()

for child in root:
    #print(child.tag)
    for child2 in child:
        print(child2.tag, child2.attrib)

print()
children = root.findall('item')
print(children)

for it in children:
    re_id = it.find('name').get('id')
    re_name = it.find('name').text
    re_tel = it.find('tel').text
    print(re_id, re_name, re_tel)

