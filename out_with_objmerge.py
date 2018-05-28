ctrl_bool = kwargs["ctrlclick"]
obj = hou.node("/obj")
        
nodes = list(hou.selectedNodes())

for node in nodes:
    posx = node.position()[0]
    posy = node.position()[1]

    if not ctrl_bool:
        node_name = node.name().upper()
    else:
        node_name = node.parent().name().upper()

    if node_name.find("OUT") >= 0:
        node_name = node_name.replace("OUT_",'')
        if obj.node(str("DISPLAY_"+node_name)) != None:
            obj.node(str("DISPLAY_"+node_name)).destroy()
        out_node = node
    
    else:    
        out_node = node.createOutputNode('null')
        out_node.setPosition([posx, posy-1])
    out_node.setName('OUT_' + node_name)
    
    out_node.setColor(hou.Color((0.475,0.812,0.204)))
    out_node.setDisplayFlag(1)
        
    node.parent().setDisplayFlag(False)
    
    
    geo = obj.createNode("geo","DISPLAY_"+node_name)
    geo.setDisplayFlag(True)
    geo.setColor(hou.Color((0.475,0.812,0.204)))
    for child in geo.children():
       child.destroy()
    objmerge = geo.createNode("object_merge",node_name)
   
    objmerge.parm("objpath1").set(out_node.path())
    objmerge.parm("xformtype").set(1)
    out_node.setDisplayFlag(1)
    out_node.setRenderFlag(1)
    
    