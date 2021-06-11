![open_class_rooms](https://img.shields.io/badge/OpenClassRooms-Project02-limegreen?labelColor=blueviolet&style=plastic)
![built_by](https://img.shields.io/badge/Built%20by-Developers%20%3Cgeoffrey_ll%3E-black?labelColor=orange&style=plastic)

![made_with_python](https://img.shields.io/badge/Made%20With-Python-darkgreen?logo=python&labelColor=red&style=plastic)
![IDE use](https://img.shields.io/badge/IDE%20use-PyCharm-darkgreen?logo=pycharm&labelColor=red&style=plastic)
![OS_use](https://img.shields.io/badge/OS%20use-Windows-blue?labelColor=red&style=plastic&logo=windows)

![open_source](https://img.shields.io/badge/licence-libre-darkkhaki?labelColor=red&style=plastic)


# llopis_scraper_books_online.py #

1.  [Description](#description)
2.  [Utilisation](#utilisation)
3.  [Installation](#installation)
    1.  [Environnement virtuel](#environnement-virtuel)
    2.  [Requierements](#requierements)
4.  [À propos](#a-propos)
    1.  [Package](#package)
    2.  [Bugs connus](#bugs-connus)
    3.  [Idées d'améliorations](#idees-d-ameliorations)


## 1. Description ##


Ce script à été réalisé dans le cadre d'un projet du parcours 'Développeur d'application - Python' d'OpenClassROoms.

llopis_scrap.py est un outil de scraping utilisable uniquement sur le site [books to scrape](http://books.toscrape.com/), une simulation de librairie en ligne. Il permet de recueillir diverses informations sur les livres, et de les écrire dans un .csv, ainsi que de télécharger les images de couverture des livres.

Pour illustrer, voici le .csv de la catégorie 'Contemporary' contenant 3 livres,\
![csv_contemporary_category](readme/csv_contemporary.jpg)\
et les diffentes couvertures récupérées.\
![folder_contemporary_covers](readme/folder_contemporary_covers.jpg)

\
Pour chacune des catégorie scraper, le script crée un dossier au nom de la catégorie contenant le .csv et le dossier de couverture des livres. Chacun de ces dossiers sont rangés dans le dossier 'output' du répertoire du script (dossier crée par le script si inexsistant).

Voici à quoi ressemble le dossier 'output' après le scrap des 50 catégories du site,\
![folder_output_all](readme/folder_output_all.jpg)\
et le dossier contemporary.\
![folder_contemporary](readme/folder_contemporary.jpg)

\
Le script affiche sa progression en cours d'éxécution.\
![message_progression](readme/message_progression.jpg)

\
**Attention :**
- Le .csv utilise '|' comme séparateur de colonnes.
- Les .csv et la couverture des livres ne sont pas mis à jour en direct.
- Relancer le llopis_scrap.py réécrira le .csv de la catégorie, mais ne retéléchargera pas les couvertures si celles-ci existent déjà. 


## 2. Utilisation ##

Le script s'utilise à partir d'un terminal, de 4 façons différentes.

![option_scrap.py](readme/option_scrap.py.jpg)
1. L'option 'book' suivit de l'url d'un livre spécifique, pour recueillir les données d'un seul livre.\
Tous les .csv écrits et les couvertures des livres téléchargées via cette option, sont stockés dans le dossier './output/zingle'\
![two_books_of_contemporary_category_in_folder_zingle](readme/two_books_of_contemporary_category_in_folder_zingle.jpg)

2. L'option 'category', suivit le l'url de la page '^.index.html' d'une catégorie, pour recueillir les informations de toutes une catégorie.\
 **Attention**, si la catégorie a plusieurs pages, il faut impérativement renseigner la première page qui finit en '/index.html'
 
3. L'option 'all' pour recueillir les données pour tous les livres de toutes les catégorie de livre.

4. L'option input, pour recueillir les données d'une ou plusieurs catégories, via un menu à utiliser dans le terminal. \
![option_input_menu_home](readme/option_input_menu_home.jpg)\
Via cette option, ont peut sélectionner toutes les catégories du site, ou n'en sélectionner que quelques unes.\
Les .csv et couvertures de livres sont stockés au même endroit.\
La sélection se fait par demande d'input à l'utilisateur.


## 3. Installation ##

Dans les sous-sections suivantes, les lignes de commande sont illustrées depuis le répertoire de travail :\
![working_directory](readme/working_directory.jpg)\
Les différents fichiers du script s'y trouvent.\
Pour utiliser les lignes de commandes, il faut que votre répertoire de travail, soit celui où se trouvent les différents fichiers du script.


### i. Environnement virtuel ###

Sous Windows, avec l'IDE PyCharm.

- Pour créer l'environnement virtuel lancer la commande suivante :\
![command_line_create_env](readme/command_line_create_env.jpg)\
Cela créra un environement virtuel nommé 'env'

- Si l'environnement virtuel est actif, son nom apparaîtra au début de la ligne de commande, comme suit :\
![env_activate](readme/env_activate.jpg)

- Sinon, pour activer l'env, il faut lancer la commande :\
![command_line_activate_env](readme/command_line_activate_env.jpg)


### ii. Requierements ###

Une fois l'environnement virtuel activé, lancer la commande suivante :\
![command_line_install_requierements](readme/command_line_install_requierements.jpg)\
Cela installera tous les modules renseignés dans le fichier requierements.txt.


## 4. À propos <a name="a-propos"></a> ###

### i. Package ###

llopis_scrap.py utilise un ensemble de modules locals, réunis dans le package scrap_package.

Pour chaque module, une description, sa structure, ses inputs, ses transformations et ses ouputs.

- a_collect_url_home_all_category.py\
\
Ce module sert lors des options 'all' et 'input'. Il récupére les http://category_url/index.html de toutes les catégories de livres présentent sur le site. Cette collecte ce fait depuis l'url de page d'accueil du site.\
    - Input : Une constante 'URL_site', qui sert à vérifier que l'url du site est valide.
    - Transformation : Depuis la page d'accueil du site, récupére tous les href commençant par 'catalogue/category/books/', et les utilise pour reconstruire les url en output.
    - Ouput : Les url des catégories type 'http://category_url/index.html'

- b_selection_category_to_scrap.py\
\
Ce module sert à l'option 'input'. Il permet l'apparition du menu et la sélection des catégories à scraper via des input utilisateur.
    - Input : Les différents choix de l'utilateur, tels que les catégories à scraper ou la demande d'affichage des catégories disponible.
    - Transformation : Diverses gestions d'erreurs, de manipulations d'input, de messages utilisateur etc…
    - Output : Les url des catégories type 'http://category_url/index.html' que l'utilisateur aura choisit.

- c_scrap_books_urls_in_category.py\
\
Ce module sert au option 'category', 'all' et 'input'. Il permet la collecte de toutes les url des livres d'un catégorie.
    - Input : L'url d'une catégorie (type '/index.html')
    - Transformation : Évalue le nombre de pages que possède la catégorie, selon le nombre de livres qu'elle contient. Contruit les url des autres pages de la catégories. Pour chaque page de la catégorie, récupére les href de tout les h3 de la page. Puis reconstruit les urls des livres.
    - Output : Toutes les url des livres de la catégorie donnée en input.

- d_check_url_books.py\
\
Ce module sert dans toutes les options. Il permet de renvoyer un message d'erreur si l'url d'un livre est érronée. Dans notre cas il n'est pas utile, car notre site fictif n'est pas sujet à modification. Mais dans le cas d'un véritable projet, il serait pertinant de ce pencher sur cette fonctionnalité.
    - Input : L'ensemble des url des livres d'une catégorie (ou l'url du livre renseignée avec l'option 'book').
    - Transformation : Fais une requête pour chaque url.
    - Output : L'ensemble des url de livres contenues dans l'input ou un message d'erreur indiquant l' (les) url invalide(s).

- e_scrap_data.py\
\
Ce module sert dans toutes les options. Il récupére l'ensemble des données voulu pour chaque url de livre contenues en input.
    - Input : L'ensemble des url de livres d'une catégorie. (ou l'url du livre renseignée avec l'option 'book') 
    - Transformation : Crée un dictionnaire vide ayant pour keys les données voulues. Pour chaque url, récupére les informations à différents endroit de la page du livre et les stockent dans le dictionnaire.
    - Output : Le dictionnaire contenant toutes les informations désirées, pour l'ensemble des url de livres contenues en input.

- f_write_csv.py\
\
Ce module sert dans toutes les options. Il écrit le .csv, avec pour en-têtes, les keys du dictionnaire, pour séparateur '|' et pour contenu, l'ensemble des informations pour tous les livres d'une catégorie (ou du livre renseignée avec l'option 'book').
    - Input : Dictionnaire d'une catégorie (ou du livre renseignée avec l'option 'book').
    - Transformation : Détermine la catégorie concernée. Si le dossier './output' n'existe pas, le crée. Recconnait si l'on vient depuis l'option 'book', dans ce cas écrit le .csv dans le dossier '.output/zingle/nom_livre_upc.csv', sinon écrit le fichier dans le dossier './output/name_category/data_books_in_name_category_category.csv'. Crée le dossier './output/name_category' s'il n'existe pas.
    - Output : le fichier .csv.

- g_cover_download.py\
\
Ce module sert dans toutes les options. Il télécharge l'image de couverture de tous les livres d'une catégorie (ou du livre erneignée avec l'option 'book').
    - Input : Dictionnaire d'une catégorie (ou du livre renseignée avec l'option 'book')
    - Transformation : Détermine la catégorie concernée. Si le dossier './output/' n'existe pas, le crée. Reconnait si l'on vient depuis l'option 'book', dans ce cas stock l'image dans le dossier './output/zingle/name_book_upc.jpg', sinon les stockent dans le dossier './output/name_category/cover_name_category/'. Limite le nom du chemin à 245 caractère (260 limite par défault de windows, 15 nécessaire au module), tronque dans le nom du livre si besoin.
    - Output : Les images au format 'jpg',  dont l'url est présente dans le dictionnaire en input.

- main_p02_scrap.py\
\
Ce module sert de main pour les 4 options disponible.
    - Input : Pour les options 'book' et 'catégory', l'url renseignée, sinon pas d'input.
    - Transformation : Principalement des appels de fonctions.
    - Output : Le bon enchaînement des modules.


### ii. Bugs connus  ###

- Lors de la sélection manuelle via l'option 'input', si l'utilisateur entre ex : '-crime-novels' au lieu de '-crime -novels', la catégorie 'crime' ne sera pas reconnu et le script demandera à l'utilisateur de reformuler le nom.

- Si l'on tente d'écrire le .csv d'une catégorie, dans un chemin proche de la limite des 260 caractères autorisés par défault sur Windows, l'écriture échouera. Il faut rajouter la gestion de la longueur du chemin pour l'écriture d'une catégorie (comme c'est le cas lors de l'écriture d'un livre) et en profiter pour moduler cette gestion d'erreur.

Si vous trouver un bug, merci de me le signaler sur l'adresse llopis@bug.com


### iii. Idées d'amélioration <a name="idees-d-ameliorations"></a> ###

- Synthétiser le code, réduire le nombre de lignes et en faciliter la lecture ! Et autant que possible, respecter la PEP 8.

- Accentuer la modularité de l’application. Il y a des redites, par exemple la gestion d’erreur de longueur de chemin se trouve dans f_write_csv et dans g_cover_download.

- Finir les docstrings (reStructuredText). Quels soients complètes selon les standard et faire celles qui n'existens pas encore.

- Faire plus de place à l'anglais dans les commentaires ou les docstrings. Mon niveau actuel ne me le permet pas. 

- Permettre à l’utilisateur de choisir le répertoire de stockage des données,. Éventuellement son arborescence et sa nomenclature.

- Harmoniser et croiser les données scraper sur les différents sites. Je m’explique. Books to scrap n’indique pas l’auteur des livres, il est probable que d’autres librairie mentionne l’auteur. Si l’auteur est récupéré sur un site et que sur autre il ne sont pas indique alors faire une recherche pour ajouter l’info manquantes. Soit dans nos infos collectées, soit sur le web.

- Une gestion d’erreur qui vérifierait que le site ne mettent pas les données qui nous intéressent dans d’autres balises. Les mises à jour de site ne sont pas si fréquentes, mais elle ne sont pas rare non plus.

- Passer à une interface graphique qui reprenne dans l’idée, le menu input. Sélection par cliquer ou en entrant le numéro de la catégorie.

- Ajouter une fonctionnalité d’archivage. Au lieu d’écraser à chaque fois le csv déjà existant, il faudrait l’archiver et ensuite écrire le nouveau. L’archivage gagnera en importance lors du la mise à jour vers une surveillance en direct.

- Dans la suite logique de l’archivage, il faudrait exploiter l’archivage pour construire un historique des prix.
 -Si l’on scrap vers des librairies avec des devises différents, ajouter un module de conversion des devises. Il irait récupérer le taux de change sur des sites bancaires fiables et s’actualiserait dans certaines conditions, comme lorsque l’utilisateur consulte les prix ou leur historiques (du coup plusieurs modules pas qu’un seul)

- Permettre à l'utilisateur de définir le nombre de caractères à utiliser pour le nom de cover.
