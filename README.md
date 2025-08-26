# ASCII-Console-Video
Это программа, которая анализирует видео с помощью Open-CV и отображает его в формате ASCII.

<img width="1189" height="276" alt="Logo" src="https://github.com/user-attachments/assets/47b512d4-1c97-44fa-922c-ef9166ac824b" />

Предварительное видео:
[Видео](https://github.com/user-attachments/assets/850365d7-770a-455b-aeaf-09d36f484430)

(В видео есть пробелы во время проигрывания, но в реальной жизни таких пробелов нет.)

# Перевод

-  English: [English](https://github.com/PiaPsyker918/ASCII-Console-Video/tree/main)

# Требования
* argparse
* os
* subprocess
* sys
* time
* cv2
* pygame
* numpy
* PIL

# Установка

1. Установите zip-файл.
2. Откройте CMD и напишите.
```
pip install requements.txt
```
3. Скачайте .mp4 файл.
4. Следующие шаги в "Как использовать".

# Как использовать

В CMD напишите
Windows
```
.\main.py -f video_file.mp4
```
Linux
```
$ ./main.py -f video_file.mp4
```

# Опции
```-f``` - Укажите имя файла с расширением .mp4. ОН ДОЛЖЕН НАХОДИТЬСЯ В ТОМ ЖЕ КАТАЛОГЕ, ЧТО И СКРИПТ.

```-c``` - Если видео цветное, консоль отобразит цветное видео в формате ASCII.

<img width="1372" height="660" alt="Preview" src="https://github.com/user-attachments/assets/66305e3f-46eb-4221-badb-5872a500b19f" />

# Как это работает

Каждый кадр обрабатывается с помощью Open-CV

<img width="899" height="221" alt="VideoToASCII" src="https://github.com/user-attachments/assets/4f1a1005-1e9a-4297-8f50-f63d9b2e64fa" />

Затем получаем размер терминала X и Y,
как только у нас будет размер терминала, мы преобразуем каждый кадр в тот же кадр, но с меньшим разрешением

<img width="810" height="347" alt="Simpsons" src="https://github.com/user-attachments/assets/75e55a5e-c31d-48ca-b242-009240df34c1" />

После преобразования мы берем цвет каждого пикселя и преобразуем его в символ ASCII в зависимости от интенсивности цвета.

```chars = " .:-=+*#%@"```

0-255 RGB в ASCII.
И мы получаем ASCII кадр.

<img width="1094" height="716" alt="Frame" src="https://github.com/user-attachments/assets/dbe6e314-5691-4c81-bd3a-4b9872c548fa" />

# Контакты

[<img width="100" height="100" alt="telegram-circle-icon-for-web-design-free-png" src="https://github.com/user-attachments/assets/1e4c0cb3-a856-417b-86d1-29354b2d92a8" />](https://t.me/Girlanda228)

