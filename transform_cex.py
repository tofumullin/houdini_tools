for sel in hou.selectedNodes():
    sel.parm("px").setExpression("$CEX")    
    sel.parm("py").setExpression("$CEY")
    sel.parm("pz").setExpression("$CEZ")