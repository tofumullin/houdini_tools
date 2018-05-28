ctrl_bool = kwargs["ctrlclick"]

nodes = list(hou.selectedNodes())

for node in nodes:
    posx = node.position()[0]
    posy = node.position()[1]

    node_name = node.parent().name().upper()

    out_node = node.createOutputNode('null')
    out_node.setName('RENDER_' + node_name)
    out_node.setPosition([posx, posy-1])
    out_node.setColor(hou.Color((0.565,0.494,0.863)))
    out_node.setRenderFlag(1)