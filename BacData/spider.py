import scrapy
import time
from scrapy import FormRequest
from selenium import webdriver

from BacData.BacItem import BacItem
from bs4 import BeautifulSoup

class BacData(scrapy.Spider):
    name = 'bd'
    start_urls = ['http://bacalaureat.edu.ro/Pages/TaraRezultAlfa.aspx']
    headers = [""]
    crtPage = 1
    totalPages = 13552
    errors = 0


    def start_requests(self):
        print("DOING SOMETHING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return [FormRequest("http://bacalaureat.edu.ro/Pages/TaraRezultAlfa.aspx",
                            formdata={'ctl00$ContentPlaceHolderBody$DropDownList2': '1',
                                      'ctl00$ContentPlaceHolderBody$ImageButtonDR1.x': '13',
                                      'ctl00$ContentPlaceHolderBody$ImageButtonDR1.y': '13'},
                            callback=self.parse)]


    def parse(self, response):
        print("## Beginning to parse ", self.crtPage, " page")

        crtTr = 0
        item = BacItem()
        self.errors = 0



        for tr in response.xpath('(//table[@class="mainTable"]/tr/td[@class="tdBac"])'):
            if crtTr == None:
                continue

            if crtTr % 31 == 0:
                item['nr'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 1:
                item['nume'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 2:
                item['posIerarhieJudet'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 3:
                item['posIerarhieTara'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 4:
                item['unitInvatamant'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 5:
                item['judet'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 6:
                item['promotieAnterioara'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 7:
                item['formaEducatie'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 8:
                item['specializare'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 9:
                item['examenOralRomana'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 10:
                item['notaScrisaRomana'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 11:
                item['notaContestatieRomana'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 12:
                item['notaFinalaRomana'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 13:
                item['limbaMaterna'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 14:
                item['limbaModerna'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 15:
                item['notaLimbaModerna'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 16:
                item['disciplinaObligatorie'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 17:
                item['disciplinaAlegere'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 18:
                item['competenteDigitale'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 19:
                item['medie'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 20:
                item['rezultatFinal'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 21:
                item['competenteMaterna'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 22:
                item['notaScrisaMaterna'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 23:
                item['notaContestatieMaterna'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 24:
                item['notaFinalaMaterna'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 25:
                item['notaDisciplinaObligatorie'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 26:
                item['notaContestatieDisciplinaObligatorie'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 27:
                item['notaFinalaDisciplinaObligatorie'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 28:
                item['notaDisciplinaAlegere'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 29:
                item['notaContestatieDisciplinaAlegere'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()

            if crtTr % 31 == 30:
                item['notaFinalaDisciplinaAlegere'] = BeautifulSoup(tr.extract().encode("utf-8")).get_text()




            if crtTr % 31 == 0 and crtTr != 0:
                yield  item

            crtTr += 1


        print("## Parsing page ", self.crtPage, " ended")

        #Go to the next page
        self.crtPage += 1

        if(self.crtPage <= self.totalPages):
            while True:
                print("## Trying to jump to next page: ", self.crtPage)


                try:
                    if response.css('input#__VIEWSTATE::attr(value)').extract_first() != None and response.css('input#__VIEWSTATEGENERATOR::attr(value)').extract_first() != None and  response.css('input#__EVENTVALIDATION::attr(value)').extract_first() != None:
                        self._viewState = response.css('input#__VIEWSTATE::attr(value)').extract_first()
                        self._viewGenerator = response.css('input#__VIEWSTATEGENERATOR::attr(value)').extract_first()
                        self._eventValidation = response.css('input#__EVENTVALIDATION::attr(value)').extract_first()

                    yield scrapy.FormRequest(
                        'http://bacalaureat.edu.ro/Pages/TaraRezultAlfa.aspx',
                        formdata={
                            'ctl00$ContentPlaceHolderBody$DropDownList2': str(self.crtPage),
                            '__VIEWSTATE': self._viewState,
                            '__VIEWSTATEGENERATOR': self._viewGenerator,
                            '__EVENTVALIDATION': self._eventValidation
                        },
                        callback = self.parse,
                        dont_filter = True
                    )
                    break
                except Exception as e:
                    print("Error when loading page ", self.crtPage, e)
                    self.errors += 1
                    if self.errors >= 2:
                        exit(0)

                    time.sleep(25)




