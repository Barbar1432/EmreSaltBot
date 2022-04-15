import random


def salt_responses (input_txt) :
    user_inp = str(input_txt).lower()
    emresaltSus = ["sus kanka", "sus harbi sus", "sus!","sus kafa acma kanka","olum harbi salaksin, sus","topsun kanka",
                   "malsin kanka","adam degilsin lan sen . Adam musvettesisin", "Bitti mi kanka"]
    emresaltSorular = [ " sanane , sen ne bok basardin bu hayatta ? ", "sanane,bi sik becerememis kardesim " ,"sal kanka"
                        , "sal harbi sal", " sal kanka manyak oluruz", "sal harbi sal manyak ettin bizi", "sanane, aslanim"]
    emresaltSelamlama = ["Hosgeldin adam", "ooo adam .. adam hosgeldin","hosgeldin orospum",
                         "oo adam musvettesi kardesim gelmis","hosgeldin orospum. Anacigin nasil ?", "aaa salak orospu cocugu, hosgeldin"]

    sus = random.choice(emresaltSus)
    if user_inp in ("merhaba","selam","sa","selamin aleykum","hey","naber","nasilsin","nasılsın","naber?","nasilsin?"):
        selamlama =  random.choice(emresaltSelamlama)
        return selamlama

    if user_inp.__contains__("Baban"):
        return " Baba diyince bir Baris Terzioglu iki Fatih Hocam"
    if user_inp.__contains__("Babanim"):
        return " Baba diyince bir Baris Terzioglu iki Fatih Hocam"

    if user_inp.__contains__("?"):
        cevap = random.choice(emresaltSorular)
        return cevap
    return sus








