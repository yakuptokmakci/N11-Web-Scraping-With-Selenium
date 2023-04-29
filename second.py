from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
##options.add_experimental_option("detach",True)     tarayıcı kapama
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
link="https://www.n11.com/urun/qcy-t13-bluetooth-51-enc-kulak-ici-kulaklik-2142899?magaza=n11#unf-sell"
sart=9.5


def nonbir(adress,degree):
    score = []
    price = []
    store = []

    driver.get(adress)
    driver.maximize_window()

    links = driver.find_elements("xpath", "//div[contains(@class,'unf-cmp-body-cvr')]//span[contains(@class,'b-p-new')]")
    points = driver.find_elements("xpath", "//div[contains(@class,'b-n-cvr')]//span[text()[contains(.,'.')]]")
    names = driver.find_elements("xpath", "//div[contains(@class,'b-n-cvr')]//a[contains(@class,'b-n-title')]")

    for link in links:
        price.append(link.get_attribute("innerHTML"))

    for point in points:
        qq = point.get_attribute("innerHTML")
        score.append(float(qq))

    for name in names:
        store.append(name.get_attribute("innerHTML"))

    for x in range(len(score)):

        if score[x] > degree:
            print(store[x], score[x], price[x])

nonbir(link,sart)