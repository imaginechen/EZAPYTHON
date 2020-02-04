# -*- coding: utf-8 -*-
"""
    @Author  : Eric Zhang
    @Time    : 2020/1/8
    @Comment : 
"""
from xml.dom.minidom import parse
def readXML(xmlFile):
	domTree = parse(xmlFile)
	# 文档根元素
	rootNode = domTree.documentElement
	print(rootNode.nodeName)

	# 所有顾客
	customers = rootNode.getElementsByTagName("customer")
	print("****所有顾客信息****")
	for customer in customers:
		if customer.hasAttribute("ID"):
			print("ID:", customer.getAttribute("ID"))
			# name 元素
			name = customer.getElementsByTagName("name")[0]
			print(name.nodeName, ":", name.childNodes[0].data)
			# phone 元素
			phone = customer.getElementsByTagName("phone")[0]
			print(phone.nodeName, ":", phone.childNodes[0].data)
			# comments 元素
			comments = customer.getElementsByTagName("comments")[0]
			print(comments.nodeName, ":", comments.childNodes[0].data)

def writeXML():
	domTree = parse("./test.xml")
	# 文档根元素
	rootNode = domTree.documentElement

	# 新建一个customer节点
	customer_node = domTree.createElement("customer")
	customer_node.setAttribute("ID", "C003")

	# 创建name节点,并设置textValue
	name_node = domTree.createElement("name")
	name_text_value = domTree.createTextNode("kavin")
	name_node.appendChild(name_text_value)  # 把文本节点挂到name_node节点
	customer_node.appendChild(name_node)

	# 创建phone节点,并设置textValue
	phone_node = domTree.createElement("phone")
	phone_text_value = domTree.createTextNode("32467")
	phone_node.appendChild(phone_text_value)  # 把文本节点挂到name_node节点
	customer_node.appendChild(phone_node)

	# 创建comments节点,这里是CDATA
	comments_node = domTree.createElement("comments")
	cdata_text_value = domTree.createCDATASection("A small but healthy company.")
	comments_node.appendChild(cdata_text_value)
	customer_node.appendChild(comments_node)

	rootNode.appendChild(customer_node)

	with open('test2.xml', 'w') as f:
		# 缩进 - 换行 - 编码
		domTree.writexml(f, addindent='  ', encoding='utf-8')

def updateXML():
	domTree = parse("./test.xml")
	# 文档根元素
	rootNode = domTree.documentElement

	names = rootNode.getElementsByTagName("name")
	for name in names:
		if name.childNodes[0].data == "Acme Inc.":
			# 获取到name节点的父节点
			pn = name.parentNode
			# 父节点的phone节点，其实也就是name的兄弟节点
			# 可能有sibNode方法，我没试过，大家可以google一下
			phone = pn.getElementsByTagName("phone")[0]
			# 更新phone的取值
			phone.childNodes[0].data = 99999

	with open('test3.xml', 'w') as f:
		# 缩进 - 换行 - 编码
		domTree.writexml(f, addindent='  ', encoding='utf-8')

if __name__ == '__main__':
    updateXML()
    writeXML()
    readXML("test3.xml")