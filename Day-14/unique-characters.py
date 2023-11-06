def benzersiz_karakterleri_bul(metin):
    benzersiz_karakterler = []
    
    for karakter in metin:
        if karakter not in benzersiz_karakterler:
            benzersiz_karakterler.append(karakter)
    
    return benzersiz_karakterler

ornek_metin = "merhaba dunya"
benzersiz_karakterler = benzersiz_karakterleri_bul(ornek_metin)

print("Benzersiz karakterler:", benzersiz_karakterler)

   

   
