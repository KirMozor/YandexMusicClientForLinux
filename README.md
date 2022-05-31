
# Yamux
Описание: Это клиент для Яндекс Музыки в Unix

##Сборка на C# (актуальна)
В вашей системе должна находится библиотека Bass (в Yamux она используется для вывода звука). Для установки в ArchLinux используется следующая команда:

```
git clone https://aur.archlinux.org/libbass.git
cd libbass
makepkg -si
```
#### А как установить библиотеку не в ArchLinux, а на Ubuntu например?
Если посмотреть PKGBUILD, то там можно увидеть что скачивается архив по ссылке http://www.un4seen.com/files/bass24-linux.zip. Потом он распоковывается и происходит такая магия:

```
package() {
  case "$CARCH" in
    i686) Если архитектура i686, распоковать libbass.so в /usr/lib и по той-же аналогии перемещайте файлы
      install -D -m644 libbass.so "$pkgdir/usr/lib/libbass.so"
	  ;;
    x86_64)
      install -D -m644 x64/libbass.so "$pkgdir/usr/lib/libbass.so"
	  ;;
    armv6h|armv7h)
      install -D -m644 hardfp/libbass.so "$pkgdir/usr/lib/libbass.so"
	  ;;
    aarch64)
      install -D -m644 aarch64/libbass.so "$pkgdir/usr/lib/libbass.so"
	  ;;
  esac

  install -D -m644 bass.h "$pkgdir/usr/include/bass.h"
  install -D -m644 bass.chm "$pkgdir/usr/share/doc/libbass/bass.chm"
  install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
```
### И так, я установил библиотеку, что дальше? (лучше бы скрипт сделал для установки :(  )
Теперь вам нужно установить dotnet 6 версии, команду для своего дистрибутива сами делайте (да, опять вам всё самим). Потом после установки, введите следующие команды:

```
git clone https://github.com/KirMozor/Yamux.git
cd Yamux/C#
dotnet build --configuration Release
cp -r Svg bin/Release/net6.0/
```
А теперь файл для запуска будет лежать по пути bin/Release/net6.0/Yamux. Наслаждайтесь! (после такой инструкции наслаждения мало получишь (⌣̀_⌣́ ) )


##Сборка на Python (устарела)
### Установка зависимостей

Моя программа требует токен от Яндекс Музыки, для его получения надо знать логин и пароль от вашего профиля (не волнуйтесь, ваши данные я передаю Яндексу, ваши токены я не ворую, можете посмотреть исходники если не верите). Ещё надо установить зависимости при помощи этой команды:

`pip install -U -r reqs.txt`

Иногда для работы программы надо установить пакеты `python-pyqt5` или `python3-pyqt5`. В ArchLinux это делается так

`sudo pacman -S python-pyqt5`

Если ваша система использует apt, то устанавливайие при помощи этой команды

`sudo apt install python3-pyqt5`

Также вам необходим GStreamer и плагин для Qt, в ArchLinux устанавливается так:

`sudo pacman -S gstreamer qt-gstreamer phonon-qt5-gstreamer`

### Запуск

Для запуска надо запустить main.py в корне программы, для этого введите эту команду

`python3 main.py`

### Кстатиии

У меня есть телеграм блог куда я пишу прогресс разработки. Ссылочка внизу, подписывайся!
https://t.me/kirmozor
