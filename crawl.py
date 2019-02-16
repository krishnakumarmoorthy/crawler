import requests
from bs4 import BeautifulSoup
#f=open("crawled.txt",'w')
j=0
def web(page,WebUrl,j):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        jo="crawled"+str(j)+".txt"
        f=open(jo,"w")
        #for link in s.findAll('a', {'class':'s-access-detail-page'}):
        for link in s.find_all('a'):
            tet = link.get('title')
            #print(tet)
            tet_2 = link.get('href')
            #print(tet_2)
            string=str(tet)+str(tet_2)
            f.write(string+"\n")
sites=["http://www.enjen.in/products.html","http://www.enjen.in/index.html","https://www.amazon.in/Vivo-NEX-Black-128GB-Storage/dp/B07F6CQRKG/ref=gbph_img_s-3_c373_1c45a699?smid=A14CZOWI0VEHLG&pf_rd_p=b15a4fc3-8019-435d-8c60-da8457dec373&pf_rd_s=slot-3&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=GD22J6DAXB66RFTHSEPF"]
for i in sites:
        web(1,i,j)
        j=j+1
