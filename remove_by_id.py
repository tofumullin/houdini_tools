
import toolutils
viewer = toolutils.sceneViewer()
selPts = viewer.selectGeometry()
node = selPts.nodes()[0]

pts = selPts.mergedSelectionString()
listPt = hou.selectedNodes()[0].geometry().globPoints(pts)

idList = []
for i in listPt:
    idList.append(i.attribValue("id"))
    
idList.sort()

stPattern = ""
for i in range(0,len(idList)):
        if i == len(idList) - 1:
            stPattern += str(idList[i]) + " "
        else:
            if (idList[i-1]+1)!=idList[i] and (idList[i+1]-1)!=idList[i]:
                stPattern += str(idList[i]) + " "
            if (idList[i-1]+1)!=idList[i] and (idList[i+1]-1)==idList[i]:
                stPattern += str(idList[i]) + "-"
            if (idList[i-1]+1)==idList[i] and (idList[i+1]-1)!=idList[i]:
                stPattern += str(idList[i]) + " "
                
delwrangle = node.parent().createNode("attribwrangle")
delwrangle.setPosition(node.position() + hou.Vector2(0,-1))
delwrangle.setInput(0,node,0)
delwrangle.parm("group").set('@id="'+ stPattern + '"')
delwrangle.parm("snippet").set("removepoint(0,@ptnum);")
delwrangle.setDisplayFlag(1)
delwrangle.setRenderFlag(1)