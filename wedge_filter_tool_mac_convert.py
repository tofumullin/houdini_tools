# coding=utf-8
import platform, os, os.path
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
  
def convertFiles(filelist, imageFormat='jpg' ):
        files = []
        for i in range(len(filelist)):
            print i
            print filelist[i]
            getFileInfo = QFileInfo(filelist[i])
            outputFile = getFileInfo.absolutePath() + '/' + getFileInfo.completeBaseName() + '.' + imageFormat
            
            if QFileInfo(outputFile).exists():
                files.append(outputFile)
                
            elif getFileInfo.suffix() in ['jpg','exr','pic','png','rat']:
                command = 'iconvert '+ filelist[i] +' '+ outputFile
                os.system(command)
                files.append(outputFile)
            else :pass
        
        return files

class Ui_MainWindow(QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

    def setupUi(self,MainWindow=None):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_gridView = QPushButton(self.centralwidget)
        self.btn_gridView.setMinimumSize(QSize(50, 50))
        self.btn_gridView.setMaximumSize(QSize(80, 50))
        self.btn_gridView.setObjectName("btn_gridView")
        self.horizontalLayout.addWidget(self.btn_gridView)
        self.btn_listView = QPushButton(self.centralwidget)
        self.btn_listView.setMinimumSize(QSize(50, 50))
        self.btn_listView.setMaximumSize(QSize(80, 50))
        self.btn_listView.setObjectName("btn_listView")
        self.horizontalLayout.addWidget(self.btn_listView)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
 
        self.sortlabel = QLabel(self.centralwidget)
        self.sortlabel.setObjectName("sortlabel")
        self.horizontalLayout_2.addWidget(self.sortlabel)

        self.comboBox_sort = QComboBox(self.centralwidget)
        self.comboBox_sort.setEditable(False)
        self.comboBox_sort.setObjectName("comboBox_sort")
        self.horizontalLayout_2.addWidget(self.comboBox_sort)
        self.slider_view = QSlider(self.centralwidget)
        self.slider_view.setOrientation(Qt.Horizontal)
        self.slider_view.setObjectName("slider_view")
        self.horizontalLayout_2.addWidget(self.slider_view)
        self.btn_language = QPushButton(self.centralwidget)
        self.btn_language.setObjectName("btn_language")
        self.btn_language.setFlat(True)
        self.btn_language.setMinimumSize(QSize(30, 30))
        self.btn_language.setMaximumSize(QSize(30, 30))
        self.horizontalLayout_2.addWidget(self.btn_language)
        
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 3, 1, 2)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = TableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 5)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_addPic = QPushButton(self.centralwidget)
        self.btn_addPic.setObjectName("btn_addPic")
        self.horizontalLayout_5.addWidget(self.btn_addPic)
        self.btn_appPic = QPushButton(self.centralwidget)
        self.btn_appPic.setObjectName("btn_appPic")
        self.horizontalLayout_5.addWidget(self.btn_appPic)
        self.btn_convertHelp = QPushButton(self.centralwidget)
        self.btn_convertHelp.setObjectName("btn_convertHelp")
        self.horizontalLayout_5.addWidget(self.btn_convertHelp)
 
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 2)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_6.addWidget(self.btn_back)
        self.btn_next = QPushButton(self.centralwidget)
        self.btn_next.setObjectName("btn_next")
        self.horizontalLayout_6.addWidget(self.btn_next)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 4, 1, 1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.edit_node = QLineEdit(self.centralwidget)
        self.edit_node.setObjectName("edit_node")
        self.horizontalLayout_3.addWidget(self.edit_node)
        self.btn_node = QToolButton(self.centralwidget)
        self.btn_node.setObjectName("btn_node")
        self.horizontalLayout_3.addWidget(self.btn_node)
        self.btn_exNode = QPushButton(self.centralwidget)
        self.btn_exNode.setObjectName("btn_exNode")
        self.horizontalLayout_3.addWidget(self.btn_exNode)
        self.btn_exTxt = QPushButton(self.centralwidget)
        self.btn_exTxt.setObjectName("btn_exTxt")
        self.horizontalLayout_3.addWidget(self.btn_exTxt)

        # self.btn_quit = QPushButton(self.centralwidget)
        # self.btn_quit.setObjectName("btn_quit")
        # self.horizontalLayout_3.addWidget(self.btn_quit)

        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 5)
        self.line = QFrame(self.centralwidget)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_addPic, self.btn_appPic)
        MainWindow.setTabOrder(self.btn_appPic, self.btn_next)
        MainWindow.setTabOrder(self.btn_next, self.edit_node)
        MainWindow.setTabOrder(self.edit_node, self.btn_node)
        MainWindow.setTabOrder(self.btn_node, self.btn_exNode)
        # MainWindow.setTabOrder(self.btn_exNode, self.btn_quit)

    #display UI in English
   

        # initial widgets
        self.btn_language.toggle()
        self.btn_language.setCheckable(True)
        self.slider_view.setMaximum(800)
        self.slider_view.setMinimum(20)
        
        self.tableWidget.initUI('')
      
        self.comboBox_sort.addItems(['$HIPNAME.$OS.$WEDGE.$F.exr','$HIPNAME.$OS.$WEDGE.exr'])
        self.edit_node.setText('/out/wedge1')
        self.statusbar.showMessage('Ready')

        # connect the functions
        self.btn_listView.clicked.connect(self.clickListView)
        self.btn_gridView.clicked.connect(self.clickGridView)
        
        self.comboBox_sort.currentIndexChanged.connect(self.templateChange)

        # self.btn_node.clicked.connect(lambda:self.clickAddPicture(self.btn_addPic))
        self.btn_node.clicked.connect(self.selectWedgeNode)
        self.btn_exNode.clicked.connect(self.msgwarning)
        self.slider_view.sliderMoved.connect(self.sliderval)
        self.btn_language.clicked.connect(self.changeLanguage)
        self.btn_addPic.clicked.connect(self.getfiles)
        self.btn_appPic.clicked.connect(self.appendfiles)
        self.btn_convertHelp.clicked.connect(self.convertHelp)

        self.btn_exTxt.clicked.connect(self.savetxt)
        
        self.btn_back.clicked.connect(self.backfilter)
        self.btn_next.clicked.connect(self.nextfilter)
        # QObject.connect(self.btn_quit, SIGNAL("clicked()"), app, SLOT("quit()"))
        self.btn_back.setEnabled(0)
        
        self.btn_exNode.setEnabled(1)
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QApplication.translate("MainWindow", "WEDGE FILTER", None, -1))
        self.btn_gridView.setText(QApplication.translate("MainWindow", "Grid", None, -1))
        self.btn_listView.setText(QApplication.translate("MainWindow", "List", None, -1))
        self.btn_language.setText(QApplication.translate("MainWindow", "EN", None, -1))
        self.sortlabel.setText(QApplication.translate("MainWindow", "filename template", None, -1))
        self.btn_addPic.setText(QApplication.translate("MainWindow", "Add Picture", None, -1))
        self.btn_appPic.setText(QApplication.translate("MainWindow", "Append Picture", None, -1))
        self.btn_back.setText(QApplication.translate("MainWindow", "Back", None, -1))
        self.btn_next.setText(QApplication.translate("MainWindow", "Next Filter", None, -1))
        self.label.setText(QApplication.translate("MainWindow", "wedge node", None, -1))
        self.btn_node.setText(QApplication.translate("MainWindow", "...", None, -1))
        self.btn_exNode.setText(QApplication.translate("MainWindow", "Export to Nodes", None, -1))
        self.btn_exTxt.setText(QApplication.translate("MainWindow", "Export to TXT", None, -1))
        self.btn_convertHelp.setText(QApplication.translate("MainWindow", "Convert Help", None, -1))
        # self.btn_quit.setText(QApplication.translate("MainWindow", "QUIT", None, -1))

    #DISPLAY UI IN CHINESE
    def retranslateUiCN(self, MainWindow):
        MainWindow.setWindowTitle(QApplication.translate("MainWindow", "WEDGE窗口", None, -1))
        self.btn_gridView.setText(QApplication.translate("MainWindow", "网格显示", None, -1))
        self.btn_listView.setText(QApplication.translate("MainWindow", "列表显示", None, -1))
        self.btn_language.setText(QApplication.translate("MainWindow", "CN", None, -1))
        self.sortlabel.setText(QApplication.translate("MainWindow", "文件名格式", None, -1))
        self.btn_addPic.setText(QApplication.translate("MainWindow", "添加图片", None, -1))
        self.btn_appPic.setText(QApplication.translate("MainWindow", "追加图片", None, -1))
        self.btn_back.setText(QApplication.translate("MainWindow", "返回上一步", None, -1))
        self.btn_next.setText(QApplication.translate("MainWindow", "进一步筛选", None, -1))
        self.label.setText(QApplication.translate("MainWindow", "wedge节点", None, -1))
        self.btn_node.setText(QApplication.translate("MainWindow", "...", None, -1))
        self.btn_exNode.setText(QApplication.translate("MainWindow", "导出到节点", None, -1))
        self.btn_exTxt.setText(QApplication.translate("MainWindow", "导出TXT", None, -1))
        self.btn_convertHelp.setText(QApplication.translate("MainWindow", "格式转换命令", None, -1))
        # self.btn_quit.setText(QApplication.translate("MainWindow", "退出", None, -1))




    #DEFINE BUTTONS' FUNCTIONS
    def changeLanguage(self):
        if self.btn_language.isChecked():
            self.retranslateUiCN(MainWindow)
        else:
            self.retranslateUi(MainWindow)

    def clickAddPicture(self,btn):
        print(btn.text())
        # self.tableWidget.listview()

    def sliderval(self):
        self.tableWidget.cellresize(self.slider_view.value())
        if self.tableWidget.isGridView:
            self.tableWidget.gridview()
        else:   
            self.tableWidget.listview()
        
    def clickGridView(self):
        self.slider_view.setValue(200)
        self.tableWidget.cellresize(200)
        self.tableWidget.gridview()
        

    def clickListView(self):
        self.slider_view.setValue(30)
        self.tableWidget.cellresize(30)
        self.tableWidget.listview()
        

    def templateChange(self):
        files = self.tableWidget.nextFilterItem()[0]
        if files != []:
            self.tableWidget.clear()
            self.tableWidget.initUI(files,self.comboBox_sort.currentIndex())
            if self.tableWidget.isGridView : self.tableWidget.gridview()
            else : self.tableWidget.listview()

        
    def backfilter(self):
        files = self.oldfiles
        if files != []:
            self.tableWidget.clear()
            self.tableWidget.initUI(files,self.comboBox_sort.currentIndex())
            if self.tableWidget.isGridView : self.tableWidget.gridview()
            else : self.tableWidget.listview()

    def nextfilter(self):
        self.btn_back.setEnabled(1)
        self.oldfiles = self.tableWidget.nextFilterItem()[0]
        files = self.tableWidget.nextFilterItem()[1]

        if files != []:
            self.tableWidget.clear()
            self.tableWidget.initUI(files,self.comboBox_sort.currentIndex())
            if self.tableWidget.isGridView : self.tableWidget.gridview()
            else : self.tableWidget.listview()

    def getfiles(self):
        files, _ = QFileDialog.getOpenFileNames(self.btn_addPic ,
                                    "Select one or more files to open",
                                    "/home",
                                    "Images (*.png *.xpm *.jpg *.jpeg *.exr *.pic *.rat)")

        if files:
            files = convertFiles(files) 
            self.tableWidget.clear()
            self.tableWidget.initUI(files,self.comboBox_sort.currentIndex())
            self.tableWidget.listview()

    def appendfiles(self):
        self.oldfiles = self.tableWidget.nextFilterItem()[0]
        self.tableWidget.isGridView = self.tableWidget.nextFilterItem()[2]
        files, _ = QFileDialog.getOpenFileNames(self.btn_appPic ,
                                    "Select one or more files to open",
                                    "/home",
                                    "Images (*.png *.xpm *.jpg *.jpeg *.exr *.pic *.rat)")
        
        if files:
            newfiles = self.oldfiles
            files = convertFiles(files) 
            for file in files:
                if file not in self.oldfiles:
                    newfiles.append(file)
            self.tableWidget.clear()
            self.tableWidget.initUI(newfiles)
            if self.tableWidget.isGridView : self.tableWidget.gridview()
            else : self.tableWidget.listview()

    
           
    def msgwarning(self):
        msgBox = QMessageBox(self.btn_exNode)
        msgBox.setIcon(QMessageBox.Warning)
        # QMessageBox.Warning,,QMessageBox.Critical,,QMessageBox.Question
        msgBox.setText("Do you want to clean the takes named wedges and add new takes.")
        msgBox.setInformativeText("yes for cleaning  the exist wedge takes, \nno  for just adding takes but no cleaning?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Yes)
        ret = msgBox.exec_()
        if ret == QMessageBox.Yes:
            self.destroyTakes()
            self.exportTakes()
        elif ret == QMessageBox.No:
            self.exportTakes()
        else: pass

    def savetxt(self):
        txtfile, _ = QFileDialog.getSaveFileName()
        if txtfile:
            text_file = open(txtfile, "w")
            text_file.write(self.tableWidget.printList())
            text_file.close()
        

    def convertHelp(self):
        msgBox = QMessageBox(self.btn_convertHelp) 
        msgBox.setIcon(QMessageBox.Question)
        # QMessageBox.Warning,,QMessageBox.Critical,,QMessageBox.Question
        msgBox.setText("iconvert in commandLine (exr -> jpg)")
        msgBox.setInformativeText(
    '''
    Mac OS:
    for f in *.exr; do iconvert $f $f.jpg; done 
    for f in *.jpg; do mv $f ${f/.exr.jpg/.jpg}; done 

    Windows: 
    rename *.exr *. 
    for /r %i in (*) do iconvert %i %i.jpg&&iconvert %i %i.exr 
    '''
        )
        msgBox.setStandardButtons(QMessageBox.Ok )
        msgBox.setDefaultButton(QMessageBox.Ok)
        ret = msgBox.exec_()

    def selectWedgeNode(self):
        wedgeNode = hou.ui.selectNode(initial_node=hou.node("/out/wedge1"),node_type_filter=hou.nodeTypeFilter.Rop)
        self.edit_node.setText(wedgeNode)

    def destroyTakes(self):
        for take  in (hou.takes.findTake('Main').children()):
            if 'wedge' in take.name():take.destroy()

    def exportTakes(self):
        node_path = self.edit_node.text() 
        wedge_node = hou.node(node_path)
        wedge = list(self.tableWidget.pictures.wedgeList())
        print list(wedge)
        
        for i in range(len(self.tableWidget.pictures)):
            takeName = 'wedge' + str(i+1)

            curTake = hou.takes.findTake('Main')
            takeName = curTake.addChildTake(takeName)
            hou.takes.setCurrentTake(takeName)

            for j in range(self.tableWidget.pictures.wedgeAmount()):
                name = 'name' + str(j+1)
                parm = wedge_node.parm(name).eval()
                print parm
                for n in range(len(wedge)):
                    if wedge[n] == parm: 
                        chan = 'chan' + str(j+1)
                        path = wedge_node.parm(chan).eval()
                        modifiedParm = hou.parm(path)
                        takeName.addParmTuple(modifiedParm.tuple())
                        val = self.tableWidget.pictures.wedgeVal(i,j)
                        
                        if modifiedParm.parmTemplate().type() == hou.parmTemplateType.Float:
                            val = float(val)
                        elif modifiedParm.parmTemplate().type() == hou.parmTemplateType.Int:
                            val = int(float(val))
                        elif modifiedParm.parmTemplate().type() == hou.parmTemplateType.String:
                            val = str(val)
                        else: pass
                        modifiedParm.set(val)
                        
            hou.takes.setCurrentTake(hou.takes.findTake('Main'))            
    


#TABLE VIEWER DEFINE
class TableWidget(QTableWidget):
    def __init__(self, parent=None):
        super(TableWidget, self).__init__(parent)
        self.setAcceptDrops(True)
        self.isGridView = 0
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [(u.toLocalFile()) for u in event.mimeData().urls()]
        files = convertFiles(files)
        if files:
            self.initUI(files)
            self.listview()

    def initUI(self, files, template=0):
        self.setgrid(1, 1)
        self.setShowGrid(False)
        self.setEditTriggers(0)
        self.itemClicked.connect(self.getItem)

        self.setContextMenuPolicy(Qt.CustomContextMenu)######允许右键产生子菜单
        self.customContextMenuRequested.connect(self.generateMenu)   ####右键菜单
        
        self.pictures=FileNameToWedge(files,template)

    def getHeader(self):
        return self.header
    
    def nextFilterItem(self):
        newfiles = []
        oldfiles = []
        indexes = []
        for i in range(len(self.pictures)):
            oldfiles.append(self.pictures[i])
            if self.pictures.isSelected(i):
                newfiles.append(self.pictures[i])
                indexes.append(i)
        return oldfiles, newfiles, indexes
   
    def getItem(self, item):
        if self.isGridView :
            i = item.row() * self.columnCount()+ item.column()
            # print self.indexFromItem(item)

        elif not self.isGridView:
            i = item.row() 
        
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
            self.pictures.setSelction(i,False)
        else:
            item.setCheckState(Qt.Checked)

            self.pictures.setSelction(i,True)
        
    def cellresize(self,size):
        self.setIconSize(QSize(size,size))
        self.resizeColumnsToContents()
        for i in range(self.rowCount()):  
            self.setRowHeight(i ,size)  

    def autoResize(self):
        self.setColumnCount(self.width() / self.rowHeight(0))
        self.setRowCount(len(self.pictures)/self.columnCount()+1)
        self.resizeRowsToContents()
        self.resizeColumnsToContents()

    def setgrid(self, columenum,rownum):
        self.setColumnCount(columenum)
        self.setRowCount(rownum)

    def printList(self):
        return self.pictures.printList()

    def gridview(self):
        self.isGridView = 1
        self.selectIndexes = self.nextFilterItem()[2]
        self.clear()
        self.setColumnCount(self.width() / self.rowHeight(0))
        self.setRowCount(len(self.pictures)/self.columnCount()+1)
        
        self.setSelectionBehavior(QAbstractItemView.SelectItems)
        
        for k in range(len(self.pictures)):
            i = k / (self.columnCount())
            j = k % (self.columnCount())
            item = QTableWidgetItem() 
            icon = self.pictures.scaleimage(k, self.rowHeight(0))
            item.setIcon(icon)
            self.setItem(i,j,item)

        if self.columnCount() > len(self.pictures):
            self.setColumnCount(len(self.pictures))
        self.resizeRowsToContents()
        self.resizeColumnsToContents()
        self.setSortingEnabled(False)

        for k in self.selectIndexes:
            i = k / (self.columnCount())
            j = k % (self.columnCount())
            self.item(i, j).setCheckState(Qt.Checked)

    def listview(self):
        self.isGridView = 0
        self.selectIndexes = self.nextFilterItem()[2]
        self.columenum = self.pictures.wedgeAmount()+1
        self.rownum    = len(self.pictures)
        self.setgrid(self.columenum, self.rownum)
        
        for i in range(len(self.pictures)):
            for j in range(self.pictures.wedgeAmount()):
                item = QTableWidgetItem()
                # item.setFlags(Qt.ItemIsEnabled)
                item.setText(self.pictures.wedgeVal(i,j))
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                self.setItem(i,j+1,item) 

        self.header = ( self.pictures.wedgeList())
        self.setHorizontalHeaderLabels([u'pictures'] + self.header)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        for i in range(len(self.pictures)):
                item = QTableWidgetItem() 
                icon = self.pictures.scaleimage(i,self.rowHeight(0))
                item.setIcon(icon)
                self.setItem(i,0,item)
        # self.resizeRowsToContents()
        self.resizeColumnsToContents()
        self.setSortingEnabled(True)
        for k in self.selectIndexes:
            self.item(k, 0).setCheckState(Qt.Checked)

        
    def generateMenu(self,pos):
        select = self.selectionModel().selection().indexes()
        
        menu = QMenu()
        Select = menu.addAction(u"Select")
        Deselect = menu.addAction(u"Deselect")
        SelectAll = menu.addAction(u"Select All")
        DeselectAll = menu.addAction(u"Deselect All")
        Preview = menu.addAction(u"Preview")
        # Detail = menu.addAction(u"Detail" )

        action = menu.exec_(self.mapToGlobal(pos))
        if action == Select:
            for i in select:
                item = self.item(i.row(),i.column())
                if item:
                    if item.checkState() == Qt.Unchecked: self.getItem(item)
                
        elif action == Deselect:
            for i in select:
                item = self.item(i.row(),i.column())
                if item:
                    if item.checkState() == Qt.Checked: self.getItem(item)

        elif action == SelectAll:
            for i in range(self.rowCount()):
                for j in range(self.columnCount()):
                    item = self.item(i,j)
                    if item: 
                        if item.checkState() == Qt.Unchecked: self.getItem(item)
                
        elif action == DeselectAll:
            for i in range(self.rowCount()):
                for j in range(self.columnCount()):
                    item = self.item(i,j)
                    if item: 
                        if item.checkState() == Qt.Checked: self.getItem(item)
        
        elif action == Preview:
            for i in select:
                if self.isGridView:
                    item = self.item(i.row(),i.column())
                elif i.column()==0 : item = self.item(i.row(), 0)
                else :item = 0
                if item:
                    viewer = ImageView(self)
                    viewer.initUI(item.icon().pixmap(4000))

        else:
            pass

class FileNameToWedge():
    def __init__(self,filelist,template=0):
        # template: 0 = $HIPNAME.$OS.$WEDGE.$F.exr
        # template: 1 = $HIPNAME.$OS.$WEDGE.exr
        self.wedges = []
        self.template = template
        self.len  = len(filelist)
        self.image = filelist
        self.selection = []
        for i in range(self.len):
            self.selection.append(False)

            self.filename = QFileInfo(filelist[i]).fileName().split('_wedge_')[-1]
            if self.template == 0:
                self.wedges.append(('.'.join(self.filename.split('.')[:-2])).split('_'))
            elif self.template == 1:
                self.wedges.append(('.'.join(self.filename.split('.')[:-1])).split('_'))

    def __getitem__(self, key):
        return self.image[key]

    def __len__(self):
        return self.len

    def setSelction(self, i, selected):
        self.selection[i] = selected

    def isSelected(self,i):
        return self.selection[i]

    def scaleimage(self, i, height):
        pixmap = QPixmap(self.image[i])
        return pixmap.scaledToHeight(height)

    def fileAmount(self):
        return self.len 

    def wedgeAmount(self):
        return len(self.wedges[0][::2])

    def wedgeName(self, wedgenum):
        if wedgenum > self.wedgeAmount() or wedgenum < 0:
            return None
        else:
            return self.wedges[0][::2][wedgenum]

    def wedgeVal(self, filenum, wedgenum):
        if wedgenum > self.wedgeAmount() or wedgenum < 0 or filenum < 0 or filenum > self.fileAmount():
            return None
        else:
            return self.wedges[filenum][1::2][wedgenum]     

    def wedgeList(self):
        return self.wedges[0][::2]

    def printList(self):
        self.table = []
        for j in range(self.wedgeAmount()):
            self.table.append(self.wedgeList()[j])
            self.table.append('\t')
        self.table.append('\n')
        
        for i in range(self.fileAmount()):
            for j in range(self.wedgeAmount()):
                self.table.append(self.wedgeVal(i,j))
                self.table.append('\t')
            self.table.append('\n')
        return ''.join(self.table)

class ImageView(QMainWindow):
    
    def __init__(self, parent=None):
        super(ImageView, self).__init__(parent)
        self.setWindowTitle('Image Viewer')

    def initUI(self,pixmap):
        
        self.label = QLabel(self)
      
        self.label.setPixmap(pixmap)
        
        self.label.resize(pixmap.width(), pixmap.height())
        self.resize(pixmap.width(), pixmap.height())
        # self.label.adjustSize()
        self.show()

'''
if __name__ == "__main__":
    import sys
    app = QApplication.instance()
    if app is None:
        app = QApplication(['houdini'])
    cursor_pos = QCursor().pos()
    parent = app.topLevelAt(cursor_pos)
        
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setWindowFlags(Qt.Window)
    MainWindow.show()
    sys.exit(app.exec_())

# Inside Houdini 

'''
import sys
app = QApplication.instance()
if app is None:
    app = QApplication(['houdini'])

parent =hou.qt.createWindow()
MainWindow = QMainWindow()
ui = Ui_MainWindow(parent)
ui.setupUi(MainWindow)

MainWindow.show()

