import threading
from telnetlib import EC

import requests as request
import re

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.util import wait


class Parser_v2():
    yandex_url=[]
    google_url=[]
    chrome_options = webdriver.ChromeOptions()
    def __init__(self):
        self.yandex_url=["https://yandex.ru/maps/org/tomskaya_oblastnaya_klinicheskaya_bolnitsa/1012195348/reviews/?ll=85.064881%2C56.522236&mode=search&sctx=ZAAAAAgBEAAaKAoSCZYEqKllE0NAEflM9s%2FTaktAEhIJAAAAAKCe%2Bz8RAIni31sT4z8oCjgAQAFIAFXNzMw%2BWABqAnJ1cACdAc3MTD2gAQCoAQC9AYuxn%2B7CARaUwNPiA9ih8pQIutKAuLgG%2BcrxlvMG6gEA8gEA%2BAEAggJJ0KLQvtC80YHQutCw0Y8g0L7QsdC70LDRgdGC0L3QsNGPINC60LvQuNC90LjRh9C10YHQutCw0Y8g0LHQvtC70YzQvdC40YbQsIoCAA%3D%3D&sll=85.064881%2C56.522236&source=wizgeo&sspn=0.049150%2C0.016382&tab=reviews&text=%D0%A2%D0%BE%D0%BC%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%BD%D0%B0%D1%8F%20%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D1%8F%20%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D1%86%D0%B0&utm_medium=maps-desktop&utm_source=serp&z=15.14",
                             "https://yandex.ru/maps/org/tomskaya_klinicheskaya_psikhiatricheskaya_bolnitsa/1062962099/reviews/?display-text=%D1%82%D0%BE%D0%BC%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BF%D1%81%D0%B8%D1%85%D0%B8%D0%B0%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D0%BA%D0%B0&ll=85.064881%2C56.522236&mode=search&sll=85.064881%2C56.522236&source=wizgeo&sspn=0.049150%2C0.016382&tab=reviews&text=%D1%82%D0%BE%D0%BC%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BF%D1%81%D0%B8%D1%85%D0%B8%D0%B0%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D0%BA%D0%B0&utm_medium=maps-desktop&utm_source=serp&z=13.14",
                             "https://yandex.ru/maps/org/ogauz_bolnitsa_skoroy_meditsinskoy_pomoshchi/1000103122/reviews/?display-text=%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D1%86%D0%B0%20%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D0%B9%20%D0%BC%D0%B5%D0%B4%D0%B8%D1%86%D0%B8%D0%BD%D1%81%D0%BA%D0%BE%D0%B9%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D0%B8%20%D1%82%D0%BE%D0%BC%D1%81%D0%BA%D0%BE%D0%B9&ll=85.002768%2C56.504788&mode=search&sll=85.064881%2C56.522236&source=wizgeo&sspn=0.196602%2C0.065530&tab=reviews&text=%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D1%86%D0%B0%20%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D0%B9%20%D0%BC%D0%B5%D0%B4%D0%B8%D1%86%D0%B8%D0%BD%D1%81%D0%BA%D0%BE%D0%B9%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D0%B8%20%D1%82%D0%BE%D0%BC%D1%81%D0%BA%D0%BE%D0%B9&utm_medium=maps-desktop&utm_source=serp&z=16.14",
                             "https://yandex.ru/maps/org/ogauz_bolnitsa_2/1121658534/reviews/?ll=84.990645%2C56.488768&mode=search&sll=85.002768%2C56.504788&source=wizgeo&sspn=0.024575%2C0.008195&tab=reviews&text=%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BD%D0%BE%D0%BC%D0%BD%D0%BE%D0%B5%20%D1%83%D1%87%D1%80%D0%B5%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B7%D0%B4%D1%80%D0%B0%D0%B2%D0%BE%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20%C2%AB%D0%91%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D1%86%D0%B0%20%E2%84%962%C2%BB&utm_medium=maps-desktop&utm_source=serp&z=13.14",
                             "https://yandex.ru/maps/org/gorodskaya_klincheskaya_bolnitsa_3_im_b_i_alperovicha/1057686962/reviews/?ll=84.975815%2C56.459626&mode=search&sll=84.990645%2C56.488768&source=wizgeo&sspn=0.196602%2C0.065588&tab=reviews&text=%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BD%D0%BE%D0%BC%D0%BD%D0%BE%D0%B5%20%D1%83%D1%87%D1%80%D0%B5%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B7%D0%B4%D1%80%D0%B0%D0%B2%D0%BE%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20%C2%AB%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D1%86%D0%B0%20%E2%84%963%20%D0%B8%D0%BC.%20%D0%91.%D0%98.%E2%80%89%D0%90%D0%BB%D1%8C%D0%BF%D0%B5%D1%80%D0%BE%D0%B2%D0%B8%D1%87%D0%B0%C2%BB&utm_medium=maps-desktop&utm_source=serp&z=14.14"]
        self.google_url=["https://www.google.com/maps/place/%D0%A2%D0%BE%D0%BC%D1%81%D0%BA%D0%B0%D1%8F+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%BD%D0%B0%D1%8F+%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F+%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D1%86%D0%B0/@56.523369,85.0569732,17z/data=!4m7!3m6!1s0x432693741c785ab9:0x6f630b210640de50!8m2!3d56.5233661!4d85.0591619!9m1!1b1?hl=ru-KG",
                         "https://www.google.com/maps/place/%D0%A2%D0%BE%D0%BC%D1%81%D0%BA%D0%B0%D1%8F+%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F+%D0%BF%D1%81%D0%B8%D1%85%D0%B8%D0%B0%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F+%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D1%86%D0%B0/@56.543568,84.9475471,13z/data=!4m10!1m2!2m1!1z0KLQvtC80YHQutCw0Y8g0LrQu9C40L3QuNGH0LXRgdC60LDRjyDQv9GB0LjRhdC40LDRgtGA0LjRh9C10YHQutCw0Y8g0LHQvtC70YzQvdC40YbQsA!3m6!1s0x432693741c785ab9:0x2d21dfb1b2301b86!8m2!3d56.543568!4d84.982566!9m1!1b1?hl=ru-KG",
                         "https://www.google.com/maps/place/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F+%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D1%86%D0%B0+%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D0%B9+%D0%BC%D0%B5%D0%B4%D0%B8%D1%86%D0%B8%D0%BD%D1%81%D0%BA%D0%BE%D0%B9+%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D0%B8/@56.4678273,84.9207959,13z/data=!4m10!1m2!2m1!1z0J7Qk9CQ0KPQlyDQsdC-0LvRjNC90LjRhtCwINGB0LrQvtGA0L7QuSDQvNC10LTQuNGG0LjQvdGB0LrQvtC5INC_0L7QvNC-0YnQuA!3m6!1s0x432693741c785ab9:0x426f1062480e5ff6!8m2!3d56.5049256!4d85.0030472!9m1!1b1?hl=ru-KG",
                         "https://www.google.com/maps/place/%D0%91%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D1%86%D0%B0+%E2%84%96+2/@56.4677775,84.9503,15.67z/data=!4m7!3m6!1s0x4326934fa002f94f:0xad9afb1eba6f3f04!8m2!3d56.4695403!4d84.9681483!9m1!1b1?hl=ru-KG",
                         "https://www.google.com/maps/place/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F+%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F+%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D1%86%D0%B0+%E2%84%96+3+%D0%B8%D0%BC.+%D0%91.%D0%98.%D0%90%D0%BB%D1%8C%D0%BF%D0%B5%D1%80%D0%BE%D0%B2%D0%B8%D1%87%D0%B0/@56.4537646,84.9646113,16z/data=!4m10!1m2!2m1!1z0J7QsdC70LDRgdGC0L3QvtC1INCz0L7RgdGD0LTQsNGA0YHRgtCy0LXQvdC90L7QtSDQsNCy0YLQvtC90L7QvNC90L7QtSDRg9GH0YDQtdC20LTQtdC90LjQtSDQt9C00YDQsNCy0L7QvtGF0YDQsNC90LXQvdC40Y8gwqvQk9C-0YDQvtC00YHQutCw0Y8g0LrQu9C40L3QuNGH0LXRgdC60LDRjyDQsdC-0LvRjNC90LjRhtCwIOKEljMg0LjQvC4g0JEu0Jgu4oCJ0JDQu9GM0L_QtdGA0L7QstC40YfQsMK7!3m6!1s0x4326ecac18d04051:0x6b99ce306a51a86c!8m2!3d56.4547943!4d84.9605088!9m1!1b1?hl=ru-KG"
                         ]
    def yandex_parse(self,index):
        result=""
        url=self.yandex_url[index]
        req = request.get(url)
        soup = BeautifulSoup(req.text)
        data_html=soup.find_all("div", {"class": "business-review-view__body-text _collapsed"})
        for info in data_html:
            result+=info.text+"***"
        check = result.split("***")
        #print(len(check))
        return result
    def google_parse(self,index):
        driver = webdriver.Chrome()
        driver.get(self.google_url[index])
        delay = 3  # seconds
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                (By.CLASS_NAME, "section-layout.section-scrollbox.scrollable-y.scrollable-show")))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        element = driver.find_element_by_class_name("section-layout.section-scrollbox.scrollable-y.scrollable-show")
        print(element)
        last_height =new_height=869
        result=""
        while (True):
            new_height += 869
            driver.execute_script("""arguments[0].scrollTo(arguments[2],arguments[1]);""", element, new_height,
                                  last_height)
            WebDriverWait(driver, 2)
            time.sleep(2)
            if new_height > driver.execute_script("return arguments[0].scrollHeight;", element):
                elements = driver.find_elements_by_class_name("section-review-text")
                break
            last_height = new_height
        for elem in elements:
            if elem.text != "":
                result+=elem.text + "***"

        check=result.split("***")
        #print(len(check))
        return result

    #Томская городская клиническая больница
    def pars_okb_Tomsk_txt(self):
        print("Томская городская клиническая больница")
        f1 = open("data_google_okb_tomsk_ru.txt", 'w', encoding="utf-8")
        all_info=self.yandex_parse(0)+self.google_parse(0)
        f1.write(all_info)
        f1.close()
        self.Check(all_info)
    #Томская кличическия психиатрическая больница
    def pars_okpb_Tomsk_txt(self):
        print("омская кличическия психиатрическая больница")
        f1 = open("data_okpb_Tomsk.txt", 'w', encoding="utf-8")
        all_info=self.yandex_parse(1)+self.google_parse(1)
        f1.write(all_info)
        f1.close()
        self.Check(all_info)
    #Больница скорой медицинской помощи
    def pars_Ambulance_Tomsk_txt(self):
        print("Больница скорой медицинской помощи")
        f1 = open("data_Ambulance_Tomsk.txt", 'w', encoding="utf-8")
        all_info = self.yandex_parse(2) + self.google_parse(2)
        f1.write(all_info)
        f1.close()
        self.Check(all_info)
    #ОГАУЗ Больница № 2
    def pars_OGAYZ_Hospital_2_txt(self):
        print("ОГАУЗ Больница № 2")
        f1 = open("data_OGAYZ_Hospital_2.txt", 'w', encoding="utf-8")
        all_info = self.yandex_parse(3) + self.google_parse(3)
        f1.write(all_info)
        f1.close()
        self.Check(all_info)
    #Городская клинческая больница №3 им. Б.И. Альперовича
    def pars_klinikal_Hospital_3_txt(self):
        print("Городская клинческая больница №3 им. Б.И. Альперовича")
        f1 = open("data_klinikal_Hospital_3.txt", 'w', encoding="utf-8")
        all_info = self.yandex_parse(4) + self.google_parse(4)
        f1.write(all_info)
        f1.close()
        self.Check(all_info)









    def pars_okb_Tomsk_json(self):
        # ФИГНЯ
        count = 0;
        data = name = comment = ""
        for i in range(5):
            j = 0
            if i != 0:
                # задаем url, так как на сайте несколько страниц c комментариями
                # проходимся по ним всем добавля str(i) к концу url
                url = "https://okb.tomsk.ru/thanks.php?page=" + str(i)
            else:
                url = "https://okb.tomsk.ru/thanks.php"
            # формируем запрос к странице
            req = request.post(url)
            # ЭТО И ЕСТЬ НАШ ПАРСЕР
            soup = BeautifulSoup(req.text)
            print(soup)
            # задаем класс поиска(то есть те теги где лежит инфа)
            table = soup.find("div", {"class": "mainfield"}).find_all("div")[1].find("table")
            # упращаем до строк таблицы(в нашем случаи инфа лежит в табличках)
            trs = table.find_all('tr')

            # проходимся по всем строком где лежит нужна инфармоция в данном случаи
            # ЭТО КАЖДАЯ ТРЕТЬЯ СТРОКА
            while (j < len(trs)):
                if count == 2:
                    count = 0
                count += 1
                if len(trs[j].find_all("td")) == 2:
                    data = trs[j].find_all("td")[1].text
                    name = trs[j].find_all("td")[0].text
                else:
                    info = trs[j].find("td").text
                    # все Было ОЧЕНЬ ПРОСТО.....
                    info = re.sub(r"\b\s{2,10}\b", " ", info)
                    info = re.sub(r"\s{2,5}", "", info)
                    comment = info
                    to_json = {
                        "data": data[6:],
                        "name": name[7:],
                        "comment": comment}
                    with open('pars_okb_Tomsk_json.json', 'a', encoding='utf-8') as f:
                        f.write(json.dumps(to_json, ensure_ascii=False))
                j += count
                # Добавляем encoding для представления текста в utf-8
                # ensure_ascii для того чтобы буквы не представлялись в юникоде


    def parsing(self):
        th1_okb = threading.Thread(target=self.pars_okb_Tomsk_txt)
        th2_okb = threading.Thread(target=self.pars_okpb_Tomsk_txt)
        th3_okb = threading.Thread(target=self.pars_Ambulance_Tomsk_txt)
        th4_okb = threading.Thread(target=self.pars_OGAYZ_Hospital_2_txt)
        th5_okb = threading.Thread(target=self.pars_klinikal_Hospital_3_txt)
        self.file_clear()
        th1_okb.start()
        th2_okb.start()
        th3_okb.start()
        th4_okb.start()
        th5_okb.start()
        th1_okb.join()
        th2_okb.join()
        th3_okb.join()
        th4_okb.join()
        th5_okb.join()
    def Check(self,info):
        mas_info=info.split("***")
        print(len(mas_info))

    def file_clear(self):
        f = open("data_google_okb_tomsk_ru.txt", 'w+')
        f.seek(0)
        f.close()

par=Parser_v2()
par.parsing()
