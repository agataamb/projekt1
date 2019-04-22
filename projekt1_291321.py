#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:41:27 2019

@author: admin
"""
from __future__ import unicode_literals
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
#from PyQt5.QtGui import QIcon
#from qt import * 
#from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit,\
# QGridLayout, QColorDialog, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
#from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QWidget, QMainWindow
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import math
from PyQt5.QtWidgets import QWidget,QDialog, QPushButton, QApplication, QLabel, QLineEdit, QGridLayout, QColorDialog, QMessageBox, QVBoxLayout
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		

		self.gridLayout = QtWidgets.QGridLayout(self)
		self.gridLayout.setObjectName("gridLayout")

        #punkt A
		self.label = QtWidgets.QLabel(self)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
         #XA
		self.lineEditXA = QtWidgets.QLineEdit(self)
		self.lineEditXA.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditXA.setObjectName("lineEditXA")
		self.gridLayout.addWidget(self.lineEditXA, 1, 0, 1, 1)
        #YA
		self.lineEditYA = QtWidgets.QLineEdit(self)
		self.lineEditYA.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditYA.setObjectName("lineEditYA")
		self.gridLayout.addWidget(self.lineEditYA, 2, 0, 1, 1)
        #punkt B
		self.label_2 = QtWidgets.QLabel(self)
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName("label_2")
		self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        #XB
		self.lineEditXB = QtWidgets.QLineEdit(self)
		self.lineEditXB.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditXB.setObjectName("lineEditXB")
		self.gridLayout.addWidget(self.lineEditXB, 4, 0, 1, 1)
        #YB
		self.lineEditYB = QtWidgets.QLineEdit(self)
		self.lineEditYB.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditYB.setObjectName("lineEditYB")
		self.gridLayout.addWidget(self.lineEditYB, 5, 0, 1, 1)
         #punkt C
		self.label_3 = QtWidgets.QLabel(self)
		self.label_3.setAlignment(QtCore.Qt.AlignCenter)
		self.label_3.setObjectName("label_3")
		self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        #XC
		self.lineEditXC = QtWidgets.QLineEdit(self)
		self.lineEditXC.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditXC.setObjectName("lineEditXC")
		self.gridLayout.addWidget(self.lineEditXC, 7, 0, 1, 1)
        #YC
		self.lineEditYC = QtWidgets.QLineEdit(self)
		self.lineEditYC.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditYC.setObjectName("lineEditYC")
		self.gridLayout.addWidget(self.lineEditYC, 8, 0, 1, 1)
         # punkt D
		self.label_4 = QtWidgets.QLabel(self)
		self.label_4.setAlignment(QtCore.Qt.AlignCenter)
		self.label_4.setObjectName("label_4")
		self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)
        #XD
		self.lineEditXD = QtWidgets.QLineEdit(self)
		self.lineEditXD.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditXD.setObjectName("lineEditXD")
		self.gridLayout.addWidget(self.lineEditXD, 10, 0, 1, 1)
        #YD
		self.lineEditYD = QtWidgets.QLineEdit(self)
		self.lineEditYD.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditYD.setObjectName("lineEditYD")
		self.gridLayout.addWidget(self.lineEditYD, 11, 0, 1, 1)
        #wspólrzedne punktu przeciecia
		self.label_5 = QtWidgets.QLabel(self)
		self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.label_5.setAlignment(QtCore.Qt.AlignCenter)
		self.label_5.setObjectName("label_5")
		self.gridLayout.addWidget(self.label_5, 12, 0, 1, 1)
        #XP
		self.lineEditXP = QtWidgets.QLineEdit(self)
		self.lineEditXP.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditXP.setObjectName("lineEditXP")
		self.gridLayout.addWidget(self.lineEditXP, 13, 0, 1, 1)
        #YP
		self.lineEditYP = QtWidgets.QLineEdit(self)
		self.lineEditYP.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditYP.setObjectName("lineEditYP")
		self.gridLayout.addWidget(self.lineEditYP, 14, 0, 1, 1)
        # komentarz 1
		self.textBrowserWsp = QtWidgets.QTextBrowser(self)
		#self.textBrowserWsp.setMaximumSize(QtCore.QSize(100, 100))
		self.textBrowserWsp.setObjectName("textBrowserWsp")
		self.gridLayout.addWidget(self.textBrowserWsp, 15, 0, 1, 1)
    # komentarz 2 
		self.textBrowserKom = QtWidgets.QTextBrowser(self)
		self.textBrowserKom.setMinimumSize(QtCore.QSize(200, 200))
		self.textBrowserKom.setObjectName("textBrowserKom")
		self.gridLayout.addWidget(self.textBrowserKom, 16, 0, 1, 1)
#resetuj push button
		self.pushButtonResetuj = QtWidgets.QPushButton(self)
		self.pushButtonResetuj.setObjectName("pushButtonResetuj")
		self.gridLayout.addWidget(self.pushButtonResetuj, 1, 1, 1, 1)
#oblicz push button 
		self.PushButtonLicz = QtWidgets.QPushButton(self)
		self.PushButtonLicz.setObjectName("PushButtonLicz")
		self.gridLayout.addWidget(self.PushButtonLicz, 2, 1, 1, 1)
        #rysuj push button
		self.pushButtonRysuj = QtWidgets.QPushButton(self)
		self.pushButtonRysuj.setObjectName("pushButtonRysuj")        
		self.gridLayout.addWidget(self.pushButtonRysuj,3,1,1,1)
# zamknij push button 
		self.pushButtonZamknij = QtWidgets.QPushButton(self)
		self.pushButtonZamknij.setObjectName("pushButtonZamknij")
		self.gridLayout.addWidget(self.pushButtonZamknij, 4, 1, 1, 1)
        
		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		self.gridLayout.addWidget(self.canvas, 2, 2, 12, -1) #wyznaczenie wymiaru wykresu w oknie aplikacji
        
        

		self.retranslateUi(Window)
		#QtCore.QMetaObject.connectSlotsByName(Window)
        
		self.pushButtonZamknij.clicked.connect(self.zamkniecie)
		self.pushButtonResetuj.clicked.connect(self.restart)   
		self.PushButtonLicz.clicked.connect(self.wykres) 
#		self.pushButtonKolor.clicked.connect(self.color)  
		self.pushButtonRysuj.clicked.connect(self.rysuj)        
        

	def retranslateUi(self,Window):
		_translate = QtCore.QCoreApplication.translate
		#Window.setWindowTitle(_translate("Window", "Window"))
		self.pushButtonResetuj.setText(_translate("Dialog", "Resetuj"))
		self.PushButtonLicz.setText(_translate("Dialog", "Licz"))
		self.lineEditXD.setPlaceholderText(_translate("Dialog", "X"))
		self.label.setText(_translate("Dialog", "Punkt A"))		
		self.lineEditYC.setPlaceholderText(_translate("Dialog", "Y"))
		self.lineEditYA.setPlaceholderText(_translate("Dialog", "Y"))
		self.lineEditYB.setPlaceholderText(_translate("Dialog", "Y"))
		self.lineEditYP.setPlaceholderText(_translate("Dialog", "Y"))
		self.lineEditXP.setPlaceholderText(_translate("Dialog", "X"))
		self.label_2.setText(_translate("Dialog", "Punkt B"))
		self.label_3.setText(_translate("Dialog", "Punkt C"))
		self.lineEditXB.setPlaceholderText(_translate("Dialog", "X"))
		self.lineEditYD.setPlaceholderText(_translate("Dialog", "Y"))
		self.lineEditXC.setPlaceholderText(_translate("Dialog", "X"))
		self.label_4.setText(_translate("Dialog", "Punkt D"))
		self.lineEditXA.setPlaceholderText(_translate("Dialog", "X"))
#		self.pushButtonKolor.setText(_translate("Dialog", "Wybierz kolor"))
		self.pushButtonZamknij.setText(_translate("Dialog", "Zamknij"))
		self.pushButtonRysuj.setText(_translate("Dialog","Rysuj wykres"))        
		self.label_5.setText(_translate("Dialog", "Współrzędne punktu przecięcia"))
        
	def wykres(self):#funkcja tworząca wykres oraz wyswietlajaca komunikaty

		XA=self.lineEditXA.text()
		YA=self.lineEditYA.text()
		XB=self.lineEditXB.text()
		YB=self.lineEditYB.text()
		XC=self.lineEditXC.text()
		YC=self.lineEditYC.text()
		XD=self.lineEditXD.text()
		YD=self.lineEditYD.text()
 
		xa=XA.lstrip('-').replace('.', '', 1).isdigit()
		ya=YA.lstrip('-').replace('.', '', 1).isdigit()
		xb=XB.lstrip('-').replace('.', '', 1).isdigit()
		yb=YB.lstrip('-').replace('.', '', 1).isdigit()
		xc=XC.lstrip('-').replace('.', '', 1).isdigit()
		yc=YC.lstrip('-').replace('.', '', 1).isdigit()
		xd=XD.lstrip('-').replace('.', '', 1).isdigit()
		yd=YD.lstrip('-').replace('.', '', 1).isdigit()
        
		if xa & ya & xb & yb & xc & yc & xd & yd == True:
				kom="Wspolrzedne są prawidłowe"
				Xa = float(XA)
				Ya = float(YA)                 
				Xb = float(XB)
				Yb = float(YB)
				Xc = float(XC)
				Yc = float(YC)
				Xd = float(XD)
				Yd = float(YD)
				m=((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc))
				if m==0:
						kom="Wprowadź prawidłowe wspolrzedne!"
				else:
						kom="współrzędne ok"
            
		self.textBrowserWsp.setText(str(kom))
                
		t1=((Xc-Xa)*(Yd-Yc)-(Yc-Ya)*(Xd-Xc))/((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc)) 
		t2=((Xc-Xa)*(Yb-Ya)-(Yc-Ya)*(Xb-Xa))/((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc))
		Xp=Xa+t1*(Xb-Xa)
		Yp=Ya+t1*(Yb-Ya)
		plik = open("wspolrzedne punkt P.txt", "a")
		plik.write('\n|{:^9}|{:^9}|'.format('Xp','Yp'))
		plik.write('\n|{:^9.3f}|{:^9.3f}|'.format(Xp,Yp))
		plik.close()
        
		if 0<= t1 <=1 and 0<= t2 <=1:
				info="Punkt znajduje sie na przecieciu odcinków."
		elif 0<= t1 <=1 or 0<= t2 <=1:
				info='Punkt znajduje się na przedłużeniu jednego z odcinków  '
		else:
				info = 'Punkt znajduje się na przedłużeniu dwóch odcinków '           

		self.textBrowserKom.setText(str(info))
		self.lineEditXP.setText(str('{:.3f}'.format(Xp)))  #współrzędne P z dokł 3 miejsc
		self.lineEditYP.setText(str('{:.3f}'.format(Yp)))

# gdzie znajduje się punkt C
		detC=Xa*Yb+Xb*Yc+Xc*Ya-Xc*Yb-Xa*Yc-Xb*Ya  # obliczenie wyznacznika
		if detC>0: # okreslenie na podstawie wartosci wyznacznika połozenia punktu 
				punktC="Punkt C leży po prawej stronie odcinka AB. "
		elif detC<0:
				punktC="Punkt C leży po lewej stronie odcinka AB."
		else:
				punktC="Punkt C jest współliniowy z odcinkiem AB." 
		self.textBrowserKom.append(str(punktC))


# gdzie znajduje się punkt D  
		detD=Xa*Yb+Xb*Yd+Xd*Ya-Xd*Yb-Xa*Yd-Xb*Ya
		if detD>0:
				punktD="Punkt D leży po prawej stronie odcinka AB. "
		elif detD<0:
				punktD="Punkt D leży po lewej stronie odcinka AB."
		else:
				punktD="Punkt D jest współliniowy z odcinkiem AB." 
	
		self.textBrowserKom.append(str(punktD))

        
		
# obliczenie azymutu i odległości miedzy punktami AB   
        
		dX=Xb-Xa                      # delta X
		dY=Yb-Ya                      # delta Y
		if dY>0 and dX>0:                      #ćwiartka
				az= math.atan(dY/dX)          # obliczenie azymutu 
				az_st = math.degrees(az)      # azymut w stopniach 
		elif dY>0 and dX<0:
				az= math.atan(dY/dX)+ math.pi
				az_st = math.degrees(az)
		elif dY<0 and dX<0:
				az= math.atan(dY/dX)+ math.pi
				az_st = math.degrees(az)
		elif dY<0 and dX>0:
				az= math.atan(dY/dX)+ 2*math.pi
				az_st = math.degrees(az)
		elif dY>0 and dX==0:
				az_st = 90
		elif dY==0 and dX<0:
				az_st = 180    
		elif dY<0 and dX==0:
				az_st = 270
		elif dY==0 and dX==0:
				az_st=0
		elif dY==0 and dX>0:
				az_st = 360

		self.textBrowserKom.append(str('{} {:.3f} {}'.format('Azymut odcinka AB = ',az_st,'\u00b0')))  


# obliczenie odległości punktu P od punktów A, B, C, D		
		if True:
				Xp=float(Xp) # zamiana współrzędnych punktu P na float
				Yp=float(Yp)
				odlA= float(math.sqrt((Xa-Xp)**2+(Ya-Yp)**2))  # obliczenie odległoci między punktami 
				odlB= float(math.sqrt((Xb-Xp)**2+(Yb-Yp)**2))
				odlC= float(math.sqrt((Xc-Xp)**2+(Yc-Yp)**2)) 
				odlD= float(math.sqrt((Xd-Xp)**2+(Yd-Yp)**2)) 

		else:
				odlA = ('nie można obliczyć odległości AP')
				odlB = ('nie można obliczyć odległości BP')
				odlC = ('nie można obliczyć odległości CP')
				odlD = ('nie można obliczyć odległości DP')
		self.textBrowserKom.append(str('{} {:.3f}'.format('Odległość AP : ', odlA)))
		self.textBrowserKom.append(str('{} {:.3f}'.format('Odległość BP : ', odlB)))                    
		self.textBrowserKom.append(str('{} {:.3f}'.format('Odległość CP : ', odlC)))
		self.textBrowserKom.append(str('{} {:.3f}'.format('Odległość DP : ', odlD)))		




         # rysowanie wykresu #    

	def rysuj(self):
        	color = QColorDialog.getColor() # wybór koloru lini przedłużanych
        	if color.isValid():
        	        	colory = color.name()

        	self.figure.clear()
        	XA=self.lineEditXA.text()
        	YA=self.lineEditYA.text()
        	XB=self.lineEditXB.text()
        	YB=self.lineEditYB.text()
        	XC=self.lineEditXC.text()
        	YC=self.lineEditYC.text()
        	XD=self.lineEditXD.text()
        	YD=self.lineEditYD.text()
 
        	xa=XA.lstrip('-').replace('.', '', 1).isdigit()
        	ya=YA.lstrip('-').replace('.', '', 1).isdigit()
        	xb=XB.lstrip('-').replace('.', '', 1).isdigit()
        	yb=YB.lstrip('-').replace('.', '', 1).isdigit()
        	xc=XC.lstrip('-').replace('.', '', 1).isdigit()
        	yc=YC.lstrip('-').replace('.', '', 1).isdigit()
        	xd=XD.lstrip('-').replace('.', '', 1).isdigit()
        	yd=YD.lstrip('-').replace('.', '', 1).isdigit()
        
        	if xa & ya & xb & yb & xc & yc & xd & yd == True:
                
        	        	Xa = float(XA)
        	        	Ya = float(YA)                 
        	        	Xb = float(XB)
        	        	Yb = float(YB)#
        	        	Xc = float(XC)
        	        	Yc = float(YC)
        	        	Xd = float(XD)
        	        	Yd = float(YD)
				
        	t1=((Xc-Xa)*(Yd-Yc)-(Yc-Ya)*(Xd-Xc))/((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc)) 
        	#t2=((Xc-Xa)*(Yb-Ya)-(Yc-Ya)*(Xb-Xa))/((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc))
        	Xp=Xa+t1*(Xb-Xa)
        	Yp=Ya+t1*(Yb-Ya)

        	XP=float(Xp) # zamiana współrzędnych punktu P na float
        	YP=float(Yp)
#        	self.figure = plt.figure()            
#        	self.canvas = FigureCanvas(self.figure) 
#        	self.toolbar = NavigationToolbar(self.canvas, self)                      
        	plt.scatter(Xa,Ya,marker = 'o', color='black')
        	plt.text(Xa+.03, Ya+.03, 'A: ({:.2f},{:.2f})'.format(Xa,Ya), fontsize = 10)
        	plt.scatter(Xb,Yb,marker = 'o', color='black')
        	plt.text(Xb+.03, Yb+.03, 'B: ({:.2f},{:.2f})'.format(Xb,Yb), fontsize = 10)
        	plt.scatter(Xc,Yc,marker = 'o', color='black')
        	plt.text(Xc+.03, Yc+.03, 'C: ({:.2f},{:.2f})'.format(Xc,Yc), fontsize = 10)
        	plt.scatter(Xd,Yd,marker = 'o', color='black')
        	plt.text(Xd+.03, Yd+.03, 'D: ({:.2f},{:.2f})'.format(Xd,Yd), fontsize = 10) 
        	plt.scatter(XP,YP,marker = 'o', color='black')
        	plt.text(XP+.03, YP+.03, 'P: ({:.2f},{:.2f})'.format(XP,YP), fontsize = 10)                             
        	plt.plot([Xa,XP], [Ya,YP], '--', color = colory) # linie - przedłużenia odcinka jeśli P na przedłużeniu
        	plt.plot([Xc,XP], [Yc,YP], '--', color = colory)
        	plt.plot([Xa,Xb], [Ya,Yb], color='red', label='odcinek AB') #odcinek AB
        	plt.plot([Xc,Xd], [Yc,Yd], color='blue', label= "odcinek CD")
        	plt.xlabel("X[m]") # nazwa osi z jednostką
        	plt.ylabel("Y[m]")
        	plt.title('Wizualizacja analizowanych punktów')            
        	plt.legend()
        
   
        	self.canvas.draw()

         
        
    
 # funkcja czyści wszystkie pola       
	def restart(self):
		liczba='0'
		self.figure.clear()        
		self.lineEditXA.setText(liczba)
		self.lineEditYA.setText(liczba)
		self.lineEditXB.setText(liczba)
		self.lineEditYB.setText(liczba)
		self.lineEditXC.setText(liczba)
		self.lineEditYC.setText(liczba)
		self.lineEditXD.setText(liczba)
		self.lineEditYD.setText(liczba)        
		self.lineEditXP.setText(liczba)
		self.lineEditYP.setText(liczba)
		self.textBrowserWsp.setText(str())
		self.textBrowserKom.setText(str())
        
	def zamkniecie(self,event):#funkcja wyswietlaj okienko do konczenia pracy programu
		odp = QMessageBox.question(self, 
                                   'Komunikat',  
                                   "Zamknąć program?", 
                                   QMessageBox.Yes | QMessageBox.No, 
                                   QMessageBox.No 
                                   )
		if odp == QMessageBox.Yes:
				sys.exit()


if __name__ == '__main__':
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    window = Window()
    window.show()
    app.exec_()
