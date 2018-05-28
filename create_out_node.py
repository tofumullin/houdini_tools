ctrl_bool = kwargs["ctrlclick"]

nodes = list(hou.selectedNodes())

for node in nodes:
    posx = node.position()[0]
    posy = node.position()[1]

    if not ctrl_bool:
        node_name = node.name().upper()
    else:
        node_name = node.parent().name().upper()

    out_node = node.createOutputNode('null')
    out_node.setName('OUT_' + node_name)
    out_node.setPosition([posx, posy-1])
    out_node.setColor(hou.Color((0.475,0.812,0.204)))
    out_node.setDisplayFlag(1)
    