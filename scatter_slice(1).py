#select the scatter points 
def deleteAllOutputs(node):
	while len(node.outputs())> 0 :
	    for child in node.outputs(): child.destroy()

def slice_cam(selected_node, cam_path, slice_num, referframe):
	node = selected_node
	deleteAllOutputs(node)

	#input a integer for group num
	'''
	parmSliceNum = hou.IntParmTemplate('slice_num','Slice Amount',1,(3,),min=2, max=10,min_is_strict=True, max_is_strict=True,)
	#node.removeSpareParmTuple(parmSliceNum)
	if  hou.parmTuple("slice_num")==None :
		node.addSpareParmTuple(parmSliceNum)

	else:
		node.removeSpareParmTuple(parmSliceNum)
		node.addSpareParmTuple(parmSliceNum)


	slice_num =  node.evalParm("slice_num")
	#slice_num = 3
	#get the excuted(selected) node name 


	#select the cam node, then create objmerge node (parameter 1.cam path ; 2.into this obj) 
	path = '/obj/cam1/camOrigin'
	parmCam = hou.StringParmTemplate('cam_path', 'Reference Camera',1,(path,),string_type=hou.stringParmType.NodeReference)

	if hou.parmTuple("cam_path")==None :
		node.addSpareParmTuple(parmCam)
	else:
		node.removeSpareParmTuple(parmCam)
		node.addSpareParmTuple(parmCam)

	cam_path = node.evalParm("cam_path")

	#cam_path = 'cam_path'

	'''
	'''
	resetScript = ''
	resetButton = hou.ButtonParmTemplate('reset','Reset',script_callback=resetScript, script_callback_language=hou.scriptLanguage.Python)
	node.addSpareParmTuple(resetButton)
	'''
	subnet = node.createOutputNode("subnet","slice_net")

	slice_num = int(slice_num)
	cam_path = str(cam_path)+'/camOrigin'
	referframe = int(referframe)
	posx = node.position()[0]
	posy = node.position()[1]

	cammerge = subnet.createNode("object_merge","cam_merge")
	   
	cammerge.setParms({"objpath1":cam_path, "xformtype":1})
	cammerge.setPosition([posx+2, posy-1])

	timeshift = cammerge.createOutputNode("timeshift")
	timeshift.parm('frame').deleteAllKeyframes()
	timeshift.parm('frame').set(referframe)
	timeshift.setPosition([posx+2, posy-2])

	#creat wrangle node with input1 and intput2 
	'''#####################################################################
	vector cam_P = point(1,'P',0);\n
	vector center =  getbbox_center(0);\n
	vector normal = cam_P - center; \n

	float dist =  planepointdistance(@P, normal, cam_P,center);\n
	f@dist = dist;\n
	'''#####################################################################

	dist = subnet.createNode('attribwrangle','compute_dist')
	dist.setInput(1,timeshift,0)
	inputs = subnet.indirectInputs()
	dist.setInput(0,inputs[0],0)
	dist.setPosition([posx+1, posy-3])
	dist_str = "vector cam_P = point(1,'P',0);\nvector center =  getbbox_center(0);\nvector normal = cam_P - center; \nfloat dist =  planepointdistance(@P, normal, cam_P,center);\nf@dist = dist;\n"
	dist.parm("snippet").set(dist_str)

	#create attribute promote  to compute the parameter 'max_dist'  
	#parameter original name  'dist'
	#original class 'point'
	#new class 'Detail'
	#promotion method 'Maximum'
	#change new name 'true'
	#new name 'max_dist'
	max_dist = dist.createOutputNode('attribpromote','max_dist')
	max_dist.setParms({"inname":"dist",
	        "inclass":2,
	        "outclass":0,
	        "method":0,
	        "useoutname":1,
	        "outname":"max_dist",
	        "deletein":0,
	})

	#create attribute promote  to compute the parameter 'min_dist' 
	#parameter original name  'dist'
	#original class 'point'
	#new class 'Detail'
	#promotion method 'Minimum'
	#change new name 'true'
	#new name 'min_dist'
	min_dist = max_dist.createOutputNode('attribpromote','min_dist')
	min_dist.setParms({"inname":"dist",
	        "inclass":2,
	        "outclass":0,
	        "method":1,
	        "useoutname":1,
	        "outname":"min_dist",
	        "deletein":0,
	})

	#creat wrangle node with input1
	#get the 'group num' and for loop the groups select


	'''#####################################################################
	float slice_num  = ch('slice_num');
	float min_dist = detail(0,'min_dist');
	float max_dist = detail(0,'max_dist');

	float dist_slice1 = min_dist + (max_dist-min_dist) / slice_num * 1;
	float dist_slice2 = min_dist + (max_dist-min_dist) / slice_num * 2;
	float dist_slice3 = min_dist + (max_dist-min_dist) / slice_num * 3;
	float dist_slice4 = min_dist + (max_dist-min_dist) / slice_num * 4;
	float dist_slice5 = min_dist + (max_dist-min_dist) / slice_num * 5;

	if (@dist >= min_dist && @dist <= dist_slice1)    i@group_slice1 = 1;
	else if(@dist > dist_slice1 && @dist <= dist_slice2)   i@group_slice2 = 1;
	else if(@dist > dist_slice2 && @dist <= dist_slice3)   i@group_slice3 = 1;
	else if(@dist > dist_slice3 && @dist <=max_dist)   i@group_slice4 = 1;


	'''#####################################################################
	'''
	node_name = "scatter"
	obj = hou.node("/obj")
	scatter = obj.createNode("geo","DISPLAY_"+node_name)
	for child in scatter.children():
	    child.destroy()
	wrangle = scatter.createNode("pointwrangle",node_name)
	'''
	slice = min_dist.createOutputNode('attribwrangle','generate_slice')
	slice_string = ""
	sni = "float min_dist = detail(0,'min_dist');\nfloat max_dist = detail(0,'max_dist');\n"
	for x in range(slice_num+1):    
	    slice_string = "float dist_slice" + str(x) +" = min_dist + (max_dist-min_dist) * " + str((x)/float(slice_num)) + ";\n";  
	    sni += slice_string

	sni += "\nif    (@dist >= dist_slice0 && @dist <= dist_slice1)   i@group_slice1 = 1;\n"

	for x in range(2,slice_num+1): 
	        sni += "else if(@dist > dist_slice"+str(x-1)+" && @dist <= dist_slice" + str(x)+ ")   i@group_slice" + str(x) + " = 1;\n"

	slice.parm("snippet").set(sni)


	#creat a null node and rename it 'OUT'

	posx = slice.position()[0]
	posy = slice.position()[1]
	disPosx = node.parent().position()[0]
	disPosy = node.parent().position()[1]
	obj = hou.node("/obj")
	for x in range(slice_num): 
		    group_slice = 'slice'+ str(x+1)
		    out_name = node.parent().name().upper() +'_'+group_slice.upper()
		    blast = slice.createOutputNode('blast',group_slice)
		    blast.setParms({'negate':1, 'group':group_slice, 'grouptype': 3 })
		    null = blast.createOutputNode('null','OUT_'+ out_name )
		    blast.setPosition([posx+x*2-1, posy-2])
		    null.setPosition([posx+x*2-1, posy-3])
		    if obj.node(str("DISPLAY_"+out_name)) != None: obj.node(str("DISPLAY_"+out_name)).destroy()
		    instance = obj.createNode("geo","DISPLAY_" + out_name )
		    instance.setPosition([disPosx,disPosy-x-2])
			instance.setDisplayFlag(False)
			instance.setColor(hou.Color((0.475,0.812,0.204)))
			for child in instance.children():   child.destroy()

			objmerge = instance.createNode("object_merge",out_name)
			objmerge.parm("objpath1").set(null.path())
			objmerge.parm("xformtype").set(1)



import toolutils
if len(hou.selectedNodes())==1:
	selected_node = hou.selectedNodes()[0]

	camP = hou.ui.selectNode(initial_node=hou.node("/obj/cam1"),node_type_filter=hou.nodeTypeFilter.ObjCamera)
	param = hou.ui.readMultiInput(
	    message='Please set up your slice parameter, \nthen press OK',
	    input_labels = ('Slice Amount','Reference Frame',),
	    buttons=('OK', 'Cancel'),
	    default_choice=0,
	    close_choice=1,
	    title = 'slice parameter',
	    initial_contents=('3','1'))

	    
	if param[0]==0:
	    slice_cam(selected_node, camP,param[1][0],param[1][1])


elif len(hou.selectedNodes())==0:
	hou.ui.displayMessage('please select a node', buttons=('OK',))

elif len(hou.selectedNodes())>1:
	hou.ui.displayMessage('you've selected too much nodes', buttons=('OK',))