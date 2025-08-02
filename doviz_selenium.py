from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
prices={}




service = Service(ChromeDriverManager().install())






opts = Options()
opts.add_argument("--start-maximized")
opts.add_argument("--incognito")
opts.add_argument("--disable-gpu")
opts.add_argument("--headless")
opts.add_experimental_option("prefs",{"download.default_dricetory":"C:\\Downloads"})



def donusturucu(price):
    
    c_price=price.replace(".","")
    c_price=c_price.replace(",",".")
    c_price=c_price.replace("$","")
    return float(c_price)

def para_bozma(birim,miktar):
    alinacak_para=float(miktar)*prices[birim]
    print("Hesaplanıyor...")
    sleep(3)
    x=f"Miktar: {alinacak_para}"
    return x



def guncel_kur():
    
    driver = webdriver.Chrome(service=service, options=opts)


    url = "https://www.doviz.com/"
    driver.get(url)
    sleep(3)
    
    birimler=driver.find_elements(By.CSS_SELECTOR,"div.item")
    
    
    
    for i,veri in enumerate(birimler[:6],start=1):
        
        try:
            name=veri.find_element(By.CSS_SELECTOR,"span.name")
            r_name=name.text.strip()       
        except NoSuchElementException:
            continue
        
        try:
            price=veri.find_element(By.CSS_SELECTOR,"span.value")
            r_price=price.text.strip()
            r_price=donusturucu(r_price)       
        except NoSuchElementException:
            continue

        try:
            rate=veri.find_element(By.CSS_SELECTOR,"div.change-rate.status down")
            r_rate=rate.text.strip()
        
        except NoSuchElementException:
            r_rate="-"
            pass
        
        print(f"\n{i}-{r_name}  {r_price}  Değişim:{r_rate}\n")


        prices[r_name]=r_price
    print()
    sleep(5)
def guncel_haberler():    
    driver = webdriver.Chrome(service=service, options=opts)


    url = "https://www.doviz.com/"
    driver.get(url)
    sleep(3)
    news=driver.find_elements(By.CSS_SELECTOR,"a[data-ga-event='homepage_news_section_click']")
    
    
    
    for i,haber in enumerate(news[1:8],start=1):

        
        

        try:
            news_name=haber.find_element(By.CSS_SELECTOR,"h2.headline--default")
            haber_name=news_name.text.strip()
        except NoSuchElementException:
            continue

        try:
            news_time=haber.find_element(By.CSS_SELECTOR,"div.timestamp")
            haber_time=news_time.text.strip()
        except NoSuchElementException:
            pass

        print(f"\n{i}-{haber_name}\n{haber_time}\n")
    sleep(7)



#ANAMENÜ



print()
print()
while True:
    print("1-Para birimleri ve Güncel döviz kuru\n" \
    "2-Para dönüştürücü\n" \
    "3-Ekonomi ile ilgili son haberler\n" \
    "4-Uygulmadan çık ")
    sleep(1)
    karar=input("Seçiniz (1,2,3,4): ")

    if karar=="1":
        guncel_kur()
        sleep(5)

    
    elif karar=="2":
        if not prices:
            guncel_kur()
        else:
            pass
        
        while True:
            bozulan_para=input("TL'ye çevirmek istediğiniz para birimini giriniz.(ör:DOLAR,EURO) :").upper()
            try:
                tutar=input("Bozulacak para miktarını giriniz: ")
                sayi=float(tutar)
            except ValueError:
                print("Lütfen sayı giriniz.")
                sleep(2)
                continue
            if bozulan_para in prices:
                para=para_bozma(bozulan_para,sayi)
                print(para)
                break
            else:
                print("Geçersiz giriş.")
                sleep(3)
    
    
    elif karar=="3":
        guncel_haberler()
        sleep(5)

   
    elif karar=="4":
        print("Sistemdem çıkılyor...")
        sleep(3)
        break
    
    
    
    else:
        print("Geçersiz giriş.Lütfen belirtilen elemanları giriniz.")
        sleep(5)
















