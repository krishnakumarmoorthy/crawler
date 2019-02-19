import requests
from bs4 import BeautifulSoup
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
i=4
j=5
sites=["g","s","s","a","http://www.enjen.in/products.html","http://www.enjen.in/index.html"]
def web(page,WebUrl,k):
    if(page>0):
        print("sello")
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
	jo="crawled"+str(k)+".txt"
        f=open(jo,"w")
        for link in s.find_all('a'):
            tet = link.get('title')
            tet_2 = link.get('href')
            string=str(tet)+str(tet_2)
            f.write(string+"\n")
def window():
   app = QApplication(sys.argv)
   win = QDialog()
   b1 = QPushButton(win)
   b1.setText("b1 clicked")
   b1.move(50,20)
   b1.clicked.connect(b1_clicked)
   b2 = QPushButton(win)
   b2.setText("b2 clicked")
   b2.move(50,50)
   QObject.connect(b2,SIGNAL("clicked()"),b2_clicked)

   win.setGeometry(100,100,200,100)
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())
def b1_clicked():
	web(1,sites[i],i)
def b2_clicked():
	web(i,sites[j],j)
if __name__=="__main__":
	window()
