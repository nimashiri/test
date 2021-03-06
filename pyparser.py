from xml.dom import minidom 
import parso
import sys

doc = minidom.Document()
positions = [0]

def main(file):
  parsoAst = parso.parse(readFile(file))
  gumtreeAst = toGumtreeNode(parsoAst)
  doc.appendChild(gumtreeAst)
  processNode(parsoAst, gumtreeAst)
  xml = doc.toprettyxml()
  print(xml)

def processNode(parsoNode, gumtreeNode):
  if parsoNode.type == 'error_node':
    sys.exit(parsoNode)

  for parsoChild in parsoNode.children:
    gumtreeChild = toGumtreeNode(parsoChild)
    if gumtreeChild != None:
      gumtreeNode.appendChild(gumtreeChild)
      if hasattr(parsoChild, 'children'):
        processNode(parsoChild, gumtreeChild)

def toGumtreeNode(parsoNode):
  if parsoNode.type in ['keyword', 'newline', 'endmarker']:
    return
  if parsoNode.type == 'operator' and parsoNode.value in ['.', '(', ')', '[', ']', ':', ';']:
    return
  gumtreeNode = doc.createElement('tree')
  gumtreeNode.setAttribute("type", parsoNode.type)
  startPos = positions[parsoNode.start_pos[0] - 1] + parsoNode.start_pos[1]
  endPos = positions[parsoNode.end_pos[0] - 1] + parsoNode.end_pos[1]
  length = endPos - startPos
  gumtreeNode.setAttribute("pos", str(startPos))
  gumtreeNode.setAttribute("length", str(length))
  if (not hasattr(parsoNode, 'children')) or len(parsoNode.children) == 0:
    gumtreeNode.setAttribute("label", parsoNode.value)
  return gumtreeNode

def readFile(file):
  with open(file, 'r') as file:
    data = file.read()
  index = 0
  for chr in data:
    index += 1
    if chr == '\n':
      positions.append(index)
  return data