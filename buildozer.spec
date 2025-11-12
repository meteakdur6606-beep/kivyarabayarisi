[app]

# Uygulama bilgileri
title = Kivy Araba Yarisi
package.name = arabaoyunu
package.domain = com.mete
source.dir = .
version = 0.1
requirements = python3,kivy  # Python ve Kivy'nin gereksinimleri
orientation = landscape      # Yatay ekran (daha iyi oyun deneyimi için)
fullscreen = 1

# Ana dosyanın adı BURADA KESİNLİKLE araba_oyunu.py OLMALI
main.py = araba_oyunu.py 

# Android API'leri ve izinleri
android.minapi = 21
android.targetapi = 30
# Bu oyun için izinler gerekli değil, ancak genel kullanım için:
# android.permissions = INTERNET

[buildozer]
log_level = 2
