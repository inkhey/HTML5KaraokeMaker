HTML5KaraokeMaker
==============

HTML5KaraokeMaker est un petit programme python pour créer aisément
un karaoké en html5 comme dans le programme **html5-audio-read-along**
à partir de fichier de marqueur provenant d'Audacity.

## Pré-requis ##

* python 3 (>3.4 ?)
* un navigateur web moderne (pour tester)

## Comment l'utiliser rapidement ##

1. Tout d'abord,cloner ou télécharger ce dépôt.
2. Créer/obtener un fichier audio et convertissez le dans les formats .mp3,.ogg et .wav, puis
placez ces fichiers dans le dossier data/audio.
3. Créer un fichier marqueur audacity correspondant à votre fichier et copier le dans le dossier data.
4. Modifier la configuration du fichier data/global.ini à votre guise
5. lancez HTML5KaraokeMaker.py avec python3.
6. Déplacer juste le dossier web crée précédemment sur votre site web !

## Configuration ##

### Usage de plusieurs fichier margueur audacity ###

Il est possible d'utiliser plusieurs fichiers audacity
et d'avoir un titre (non lu) pour chacun ,voir l'exemple.


### Changer le Theme ###

le fichier data/depend/style.css est modifiable.
Vous pouvez aussi modifier data/model.html file mais
attention a ne pas casser le mécanisme du programme.

## Licences ##

Le code source est sous la double licence GPL et MIT, car basée sur
"html5-audio-read" de  Weston Ruter.

Le texte d'exemple est "Du bon usage de la Piraterie" de Florent Latrive mais
la préface (que j'ai choisi comme exemple de texte) est écrite par Lawrence Lessig.
Ce livre (et le texte que j'en ai tiré) est sous la licence GNU Free Documentation License Version 1.1.

Les fichiers audios (.mp3,.ogg,.wav) sont sous licence Creative Commons BY-NC-SA 2.0.
https://creativecommons.org/licenses/by-nc-sa/2.0/
Ils sont basée sur une version audiobook du livre lue par
Liseur,Lostaaraaf,Elrik,Chmilblick,Justine Miso,Yann G,François Schnell,Yves,Thomas Andro,Lecteur,acepack,Shalero,David,Florent Latrive,Atrayu,Quentin Renaudo,Poussinsane,Ludovic Pénet,C. Siebering,t-ry
http://www.audiocite.net/livres-audio-gratuits-planete-actuelle/florent-latrive-du-bon-usage-de-la-piraterie.html
