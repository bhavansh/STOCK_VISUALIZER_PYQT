# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\test.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import  QAbstractTableModel, Qt

class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


class Ui_MainWindow(object):

    def __init__(self):
        self.START_URL = "https://www.moneycontrol.com/stocks/marketinfo/marketcap/bse/index.html"

        self.URL_HEAD_DICT = {
                    'Market Capitalisation':'https://www.moneycontrol.com/stocks/marketinfo/marketcap/',
                    'Net Sales':'https://www.moneycontrol.com/stocks/marketinfo/netsales/',
                    'Net Profit':'https://www.moneycontrol.com/stocks/marketinfo/netprofit/',
                    'Total Assets':'https://www.moneycontrol.com/stocks/marketinfo/totassets/',
                    'Other Income':'https://www.moneycontrol.com/stocks/marketinfo/othinc/',
                    'Interest':'https://www.moneycontrol.com/stocks/marketinfo/interest/',
                    'Tax':'https://www.moneycontrol.com/stocks/marketinfo/tax/',
                    'EPS':'https://www.moneycontrol.com/stocks/marketinfo/eps/',
                    'Sundry Debtors':'https://www.moneycontrol.com/stocks/marketinfo/sdrs/',
                    'Cash/Bank':'https://www.moneycontrol.com/stocks/marketinfo/cashbank/',
                    'Inventory':'https://www.moneycontrol.com/stocks/marketinfo/inventory/',
                    'Debt':'https://www.moneycontrol.com/stocks/marketinfo/debt/',
                    'Contingent Liabilities':'https://www.moneycontrol.com/stocks/marketinfo/contliab/'
        }

        self.MARKETS = {'NSE':'nse/','BSE':'bse/'}

        self.PLOTLIST = ['Pie Chart','Bar Plots']
        self.SELECTIONLIST = ['Top 10', 'All']
        self.fetch_links(self.START_URL)
        self.checkboxList = []
        self.model_list = []


    def setupUi(self, MainWindow):
        
        # MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Frame Setup

        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.TitleLabel = QtWidgets.QLabel(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)

        # Title Label

        self.TitleLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout_5.addWidget(self.TitleLabel)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # Grid Layout

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.SectorCombobox = QtWidgets.QComboBox(self.frame)
        self.SectorCombobox.setObjectName("SectorCombobox")
        self.gridLayout.addWidget(self.SectorCombobox, 1, 2, 1, 1)

        self.SectorLabel = QtWidgets.QLabel(self.frame)
        self.SectorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SectorLabel.setObjectName("SectorLabel")
        self.gridLayout.addWidget(self.SectorLabel, 0, 2, 1, 1)

        self.CriteriaLabel = QtWidgets.QLabel(self.frame)
        self.CriteriaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CriteriaLabel.setObjectName("CriteriaLabel")
        self.gridLayout.addWidget(self.CriteriaLabel, 0, 1, 1, 1)

        self.PlotsLabel = QtWidgets.QLabel(self.frame)
        self.PlotsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PlotsLabel.setObjectName("PlotsLabel")
        self.gridLayout.addWidget(self.PlotsLabel, 0, 3, 1, 1)

        self.CriteriaCombobox = QtWidgets.QComboBox(self.frame)
        self.CriteriaCombobox.setObjectName("CriteriaCombobox")
        self.gridLayout.addWidget(self.CriteriaCombobox, 1, 1, 1, 1)

        self.SelectionLabel = QtWidgets.QLabel(self.frame)
        self.SelectionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SelectionLabel.setObjectName("SelectionLabel")
        self.gridLayout.addWidget(self.SelectionLabel, 0, 4, 1, 1)
        self.SelectionCombobox = QtWidgets.QComboBox(self.frame)
        self.SelectionCombobox.setObjectName("SelectionCombobox")
        self.gridLayout.addWidget(self.SelectionCombobox, 1, 4, 1, 1)

        self.MarketLabel = QtWidgets.QLabel(self.frame)
        self.MarketLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MarketLabel.setObjectName("MarketLabel")
        self.gridLayout.addWidget(self.MarketLabel, 0, 0, 1, 1)
        
        self.PlotCombobox = QtWidgets.QComboBox(self.frame)
        self.PlotCombobox.setObjectName("PlotCombobox")
        self.gridLayout.addWidget(self.PlotCombobox, 1, 3, 1, 1)
        self.MarketRadioLayout = QtWidgets.QHBoxLayout()
        self.MarketRadioLayout.setObjectName("MarketRadioLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.MarketRadioLayout.addItem(spacerItem)
        self.bse_radio = QtWidgets.QRadioButton(self.frame)
        self.bse_radio.setObjectName("bse_radio")
        self.MarketRadioLayout.addWidget(self.bse_radio)
        self.nse_radio = QtWidgets.QRadioButton(self.frame)
        self.nse_radio.setObjectName("nse_radio")
        self.MarketRadioLayout.addWidget(self.nse_radio)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.MarketRadioLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.MarketRadioLayout, 1, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        # CheckBoxes

        self.CheckBoxLayout = QtWidgets.QHBoxLayout()
        self.CheckBoxLayout.setObjectName("CheckBoxLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.CheckBoxLayout.addItem(spacerItem2)

        
        self.verticalLayout_2.addLayout(self.CheckBoxLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.frame)

        # View Widget Tables and Plots

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.DataTab = QtWidgets.QWidget()
        self.DataTab.setObjectName("DataTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.DataTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableView = QtWidgets.QTableView(self.DataTab)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_4.addWidget(self.tableView)
        self.tabWidget.addTab(self.DataTab, "")

        self.PlotTab = QtWidgets.QWidget()
        self.PlotTab.setObjectName("PlotTab")

        self.figure = plt.figure() 
        self.canvas = FigureCanvas(self.figure) 
        self.toolbar = NavigationToolbar(self.canvas, self.PlotTab) 

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.PlotTab.setLayout(layout) 

        self.tabWidget.addTab(self.PlotTab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.verticalLayout_3)


        # Button Layouts

        self.ButtonLayout = QtWidgets.QHBoxLayout()
        self.ButtonLayout.setObjectName("ButtonLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.ButtonLayout.addItem(spacerItem3)
        self.ViewData = QtWidgets.QPushButton(self.centralwidget)
        self.ViewData.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ViewData.sizePolicy().hasHeightForWidth())
        self.ViewData.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ViewData.setFont(font)
        self.ViewData.setObjectName("ViewData")
        self.ButtonLayout.addWidget(self.ViewData)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.ButtonLayout.addItem(spacerItem4)
        self.ViewPlot = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ViewPlot.setFont(font)
        self.ViewPlot.setObjectName("ViewPlot")
        self.ButtonLayout.addWidget(self.ViewPlot)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.ButtonLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.ButtonLayout)

        self.URLLabel = QtWidgets.QLabel()
        self.URLLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.URLLabel.setFont(font)
        self.URLLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.URLLabel.setObjectName("URLLabel")
        self.URLLabel.linkActivated.connect(self.openUrl)
        self.verticalLayout.addWidget(self.URLLabel)

        MainWindow.setCentralWidget(self.centralwidget)

        # Menubar and statusBar

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Custom UI

        
        self.CriteriaCombobox.addItems((self.URL_HEAD_DICT.keys()))
        self.SectorCombobox.addItems(self.link_df.Sector)
        self.PlotCombobox.addItems(self.PLOTLIST)
        self.SelectionCombobox.addItems(self.SELECTIONLIST)

        self.bse_radio.setChecked(True)

        self.ViewPlot.clicked.connect(self.ViewPlotFigure) 
        self.ViewData.clicked.connect(self.ViewDataTable)
        self.FetchData()
        self.ViewDataTable()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))

        MainWindow.setWindowTitle(_translate("MainWindow", "STOCK VISUALIZER"))
        self.TitleLabel.setText(_translate("MainWindow", "STOCK VISUALIZER"))
        self.SectorLabel.setText(_translate("MainWindow", "SECTOR"))
        self.CriteriaLabel.setText(_translate("MainWindow", "CRITERIA"))
        self.PlotsLabel.setText(_translate("MainWindow", "PLOTS"))
        self.SelectionLabel.setText(_translate("MainWindow", "SELECTION"))
        self.MarketLabel.setText(_translate("MainWindow", "MARKETS"))
        self.bse_radio.setText(_translate("MainWindow", "BSE"))
        self.nse_radio.setText(_translate("MainWindow", "NSE"))
        self.ViewData.setText(_translate("MainWindow", "VIEW DATA"))
        self.ViewPlot.setText(_translate("MainWindow", "VIEW PLOT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DataTab), _translate("MainWindow", "VIEW DATA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PlotTab), _translate("MainWindow", "VIEW PLOT"))


    def show_popup_error(self,title,message,detail):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Ignore|QMessageBox.Close)
        msg.setDefaultButton(QMessageBox.Retry)
        msg.setInformativeText('Such Errors occours when no data is available')
        msg.setDetailedText(detail)

        x = msg.exec()
        return x

    def show_popup_warning(self,title,message,detail):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Close)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText('A Warning Message')
        msg.setDetailedText(detail)

        x = msg.exec()
        return x

    def checkboxChanged(self):
        if len(self.checkboxList)  == len(self.table_heading_cols):
            for i in range(self.table_heading_len):
                if self.checkboxList[i].text() == self.table_heading_cols[i]:
                    return False
                else:
                    return True
        return True

    def isChecked(self):
        plotselect = []
        for i in self.checkboxList:
            if i.isChecked():
                plotselect.append(i.text())
        return plotselect

    def addCheckbox(self):  
        if self.checkboxChanged() == True:
            self.removeCheckboxes()
            self.checkboxList = []
            for i in range(self.table_heading_len):
                self.checkBoxName = QtWidgets.QCheckBox(f"{self.table_heading_cols[i]}")
                self.checkBoxName.setObjectName(f"{self.table_heading_cols[i]}")
                self.CheckBoxLayout.addWidget(self.checkBoxName)
                self.checkBoxName.setText(f"{self.table_heading_cols[i]}")
                self.checkboxList.append(self.checkBoxName)

    def removeCheckboxes(self):
        for i in self.checkboxList:
            self.CheckBoxLayout.removeWidget(i)
            i.deleteLater()
            i = None

    def showdf(self):
        model = pandasModel(self.df_copy)
        self.tableView.setModel(model)
        self.tableView.horizontalHeader().setStretchLastSection(True) 
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) 
        self.model_list.append(self.tableView)
        self.tableView.show()

    def cleardf(self):
        if len(self.model_list) > 0:
            for i in self.model_list:
                i.hide()
            

    def openUrl(self):
        url = QtCore.QUrl(self.URL)
        if not QtGui.QDesktopServices.openUrl(url):
            QtGui.QMessageBox.warning(self, 'Open Url', 'Could not open url')


    def fetch_links(self,URL,URL_HEAD ='Market Capitalisation',MARKET = 'BSE'):
        page = requests.get(URL)
        soup = BeautifulSoup(page.text,"html.parser")
        URL_HEAD =self.URL_HEAD_DICT['Market Capitalisation']
        MARKET=self.MARKETS['BSE']
        links = soup.find("div",attrs={'class':'lftmenu'}).ul
        link = links.findChildren('a')
        Sector = []
        Link = []
        Field = []
        for a in link:
            Link.append(URL_HEAD+MARKET)
            # Link.append(website_link + a['href'])
            Field.append(a['href'].split('/')[-1])
            Sector.append(a.string)
        link_df = pd.DataFrame(columns=['Sector','Link'])
        link_df['Sector'] = Sector
        link_df['Link'] = Link
        link_df['Field'] = Field
        link_df.Field[0] = 'index.html'
        link_df['Link'] = link_df['Link'] + link_df['Field']
        
        self.link_df = link_df

    def fetch_tables(self,URL):
        page = requests.get(URL)
        soup = BeautifulSoup(page.text,"html.parser")
        table_heading = soup.find_all('th',attrs={'class':'brdrgtgry'})
        sr_index = -1
        comapny_index= -1
        try:
            table_rows = soup.find_all('td',attrs={'class':'brdrgtgry'})
            cols=[]
            cols_vals=[]
            for i in table_heading:
                cols.append(i.text)
                if (i.text == 'Company Name' or i.text == 'Company'):
                    comapny_index = table_heading.index(i)
                if (i.text == 'Sr'):
                    sr_index = table_heading.index(i)
                cols_vals.append([])

            table_heading_len = len(table_heading)
            table_rows_len = len(table_rows)

            for i in range(0,table_rows_len,table_heading_len):
                for j in range(0,table_heading_len):
                    if(j==comapny_index):
                        cols_vals[(i+j)%table_heading_len].append(table_rows[i+j].text.splitlines()[0])
                    else:
                        cols_vals[(i+j)%table_heading_len].append(table_rows[i+j].text)


            df = pd.DataFrame(columns=cols)
            for i in range(table_heading_len):
                df[cols[i]] = cols_vals[i]

            for i in range(table_heading_len):
                if i == comapny_index:
                    df[cols[i]]= df[cols[i]]
                else:
                    df[cols[i]]= df[cols[i]].str.replace(',', '').replace('',np.nan).astype('float')

            if sr_index == -1:
                pass
            else:
                df.drop(cols[sr_index], axis = 1,inplace=True) 
                cols.pop(sr_index)
                table_heading_len = table_heading_len -1

            self.table_heading_len = table_heading_len
            self.table_heading_cols = cols
            self.df = df


            df.index = np.arange(1, len(df)+1)
            df.reset_index(level=0, inplace=True)    

            self.df_copy = df
            self.cols = cols
        except:
            return -1


    def FetchData(self):

        self.tabWidget.setCurrentWidget(self.DataTab)
        self.criteria = self.CriteriaCombobox.currentText()
        self.sector = self.SectorCombobox.currentText()
        self.plots = self.PlotCombobox.currentText()

        if self.bse_radio.isChecked():
            market = 'BSE'
        else:
            market = 'NSE'

        criteria_index = self.link_df[self.link_df['Sector'] == self.sector].index[0]
        
        self.URL = self.URL_HEAD_DICT[self.criteria] + self.MARKETS[market] + self.link_df.Field[criteria_index]
        
        self.URLLabel.setText(f'URL : <a href="{self.URL}">MoneyControl</a>')

    def ViewDataTable(self):
        self.FetchData()
        try:
            self.fetch_tables(self.URL)
            self.showdf()
            self.addCheckbox()

        except:
            user_selection = self.show_popup_error('ERROR','No Data Found','No Data is available for the current selection\n Please try with some other selection')
            if user_selection == QMessageBox.Cancel:
                print('Cancel')
            if user_selection == QMessageBox.Ignore:
                print('Ignore')
            if user_selection == QMessageBox.Retry:
                print('Retry')

            try:
                self.cleardf()

            except:
                pass
    
    def ViewPlotFigure(self):
        # try:
        if self.bse_radio.isChecked():
            market = 'BSE'
        else:
            market = 'NSE'
        self.FetchData()
        self.fetch_tables(self.URL)
        self.addCheckbox()
        checklist = []

        if(self.PlotCombobox.currentText() == self.PLOTLIST[0]):
            if(self.SelectionCombobox.currentText() == self.SELECTIONLIST[0]):
                for i in range(0,len(self.checkboxList)):
                    if i == 0:
                        self.checkboxList[i].setChecked(True)
                        checklist.append(self.checkboxList[i].text())
                    elif i == len(self.checkboxList)-1:
                        self.checkboxList[i].setChecked(True)
                        checklist.append(self.checkboxList[i].text())
                    else:
                        if self.checkboxList[i].isChecked() == True:
                            self.show_popup_warning("Combination not Available",'Current Combination Unavailable',"")
                        self.checkboxList[i].setChecked(False)
                self.Plot_Pie(checklist,market)

            elif(self.SelectionCombobox.currentText() == self.SELECTIONLIST[1]):
                self.tabWidget.setCurrentWidget(self.PlotTab)
                self.show_popup_warning("Combination not Available",'Current Combination Unavailable',"All Values Pie Chart Can't Be Visualized Properly")

        elif(self.PlotCombobox.currentText() == self.PLOTLIST[1]):
            if(self.SelectionCombobox.currentText() == self.SELECTIONLIST[0]):
                for i in range(0,len(self.checkboxList)):
                    if i == 0:
                        self.checkboxList[i].setChecked(True)
                        checklist.append(self.checkboxList[i].text())
                    else:
                        if self.checkboxList[i].isChecked() == True:
                            checklist.append(self.checkboxList[i].text())

                if  len(checklist) < 2:
                    self.show_popup_warning("Minimum 2 Values needed",'Minimum 2 Values needed',"Minimum 2 Values needed")
                else:
                    self.Plot_Bar(checklist,market,True)

            elif(self.SelectionCombobox.currentText() == self.SELECTIONLIST[1]):
                for i in range(0,len(self.checkboxList)):
                    if i == 0:
                        self.checkboxList[i].setChecked(True)
                        checklist.append(self.checkboxList[i].text())
                    else:
                        if self.checkboxList[i].isChecked() == True:
                            checklist.append(self.checkboxList[i].text())

                if len(checklist) == 2:
                    self.Plot_Bar(checklist,market,False)
                elif len(checklist) > 2:
                    self.show_popup_warning("Combination not Available",'Current Combination Unavailable',"All Values Bar Chart Can't Be Visualized Properly")
                elif  len(checklist) < 2:
                    self.show_popup_warning("Minimum 2 Values needed",'Minimum 2 Values needed',"Minimum 2 Values needed")
        # except:
        #     self.show_popup_error("Error in Application",'Contact the Owner of the Application',"Create an Issue on GitHub")
        #     pass

    def Plot_Pie(self,checklist,market):
        self.FetchData()
        self.tabWidget.setCurrentWidget(self.PlotTab)
        top_10 = self.df.sort_values(checklist[1],ascending=False).head(10)
        labels = top_10[checklist[0]]
        values = top_10[checklist[1]]
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.axis('equal')
        ax.pie(values, labels = labels,autopct='%1.2f%%')
        ax.set_title(f'Market Capitalization of Top {self.df.shape[0]} in {market}')
        ax.legend(
            labels=['%s, %1.1f%%' % (
                l, (float(s) / values.sum()) * 100) for l, s in zip(labels, values)],
            prop={'size': 10},
            bbox_to_anchor=(0.2, 1),
        )
        self.figure.tight_layout()
        self.canvas.draw() 

    def Plot_Bar(self,checklist,market,top_10 = False):
        colors = ['b','g','r','c','m','y','k']
        self.FetchData()
        self.tabWidget.setCurrentWidget(self.PlotTab)
        if top_10:
            df= self.df.head(10)
            df.set_index(checklist[0])
        else:
            df = self.df
            df.set_index(checklist[0])

        labels = df[checklist[0]]
        w=0.25
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        company = checklist[0]
        checklist = checklist[1:]
        
        ax.set_xlabel(f'{company}')
        # ax.set_title(f'{company} vs {checklist[1]}')
        for i in range(len(checklist)):
            # ax.bar([i + (0.25*(i))for i,_ in enumerate(df[company])], df[checklist[i]], color = colors[i], width = w,bottom = 0.001)
            df[checklist[i]].plot(kind='bar', color=colors[i], ax=ax, width=w, position=i)
            
        ax.set_xticks([i for i,_ in enumerate(df[company])])
        ax.set_xticklabels(labels=labels,rotation=90)
        ax.legend(labels = [checklist[i] for i in range(0,len(checklist))]) 
        ax.axhline(y=0)
        self.figure.tight_layout()
        self.canvas.draw() 





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
