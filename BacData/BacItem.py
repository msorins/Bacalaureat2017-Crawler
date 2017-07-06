import scrapy


class BacItem(scrapy.Item):
    # define the fields for your item here like:
    nr = scrapy.Field()
    nume = scrapy.Field()
    posIerarhieJudet = scrapy.Field()
    posIerarhieTara = scrapy.Field()
    unitInvatamant = scrapy.Field()
    judet = scrapy.Field()
    promotieAnterioara = scrapy.Field()
    formaEducatie = scrapy.Field()
    specializare = scrapy.Field()

    examenOralRomana = scrapy.Field()
    notaScrisaRomana = scrapy.Field()
    notaContestatieRomana = scrapy.Field()
    notaFinalaRomana = scrapy.Field()

    limbaMaterna = scrapy.Field()
    limbaModerna = scrapy.Field()
    notaLimbaModerna = scrapy.Field()
    disciplinaObligatorie = scrapy.Field()
    disciplinaAlegere = scrapy.Field()

    competenteDigitale = scrapy.Field()
    medie = scrapy.Field()
    rezultatFinal = scrapy.Field()

    competenteMaterna = scrapy.Field()
    notaScrisaMaterna = scrapy.Field()
    notaContestatieMaterna = scrapy.Field()
    notaFinalaMaterna = scrapy.Field()


    notaDisciplinaObligatorie = scrapy.Field()
    notaContestatieDisciplinaObligatorie = scrapy.Field()
    notaFinalaDisciplinaObligatorie = scrapy.Field()

    notaDisciplinaAlegere = scrapy.Field()
    notaContestatieDisciplinaAlegere = scrapy.Field()
    notaFinalaDisciplinaAlegere = scrapy.Field()


    pass