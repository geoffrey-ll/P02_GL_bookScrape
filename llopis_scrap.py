import sys

import scrap_package as sp


user_args = sys.argv


def description():
    '''
        Affiche un exemple des différentes utilisations du script.

    :return: rien.
    '''
    print('\n> python llopis_scrap.py book http://book_url'
          '\n> python llopis_scrap.py category http://category_url/index.html'
          '\n> python llopis_scrap.py all'
          '\n> python llopis_scrap.py input')


def main(user_args):
    '''
        Selon l'option du script choisit, appelle la fonction main_de_l'option.
        Les fonctions main_des_options sont dans le module main_p02_scrap.py

    :param user_args[0]: Définit l'option choisit par l'utilisateur, parmi les
        suivantes :
                        -'book'
                        -'category'
                        -'all'
                        -'input'
        Ce paramètre est à entrer dans le terminal, après le nom du script.
        :example: python llopis_scrap.py all

    :param user_args[1]: Pour les options 'book' et 'category', il est
        nécessaire de renseigner un paramétre supplémentaire. Il s'agit de l'url
        d'un livre, prise sur le site 'books.toscrape.com/', ou de l'url d'une
        category, prise sur le même site que cité précédemment.
        Exemples :
        python llopis_scrap.py book http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html
        ou
        python llopis_scrap.py category http://books.toscrape.com/catalogue/category/books/travel_2/index.html

    :type user_args[0]: str
    :type user_args[1]: str, plus précisément, une url provenant du site 'books.toscrape.com/'

    :return: Appelle la fonction correspondant à l'option choisit.

    :exception: Si les paramètres ne correspondent pas à l'utilisation du
        script, affiche le type d'erreur, puis affiche la description.
    '''
    try:
        if user_args[1] == 'book':
            return sp.main.main_with_book(user_args[2])

        elif user_args[1] == 'category':
            return sp.main.main_with_category(user_args[2])

        elif user_args[1] == 'all':
            return sp.main.main_with_all()

        elif user_args[1] == 'input':
            return sp.main.main_with_input()

        else:
            description()
    except Exception as e:
        pass
        print(str(e))
        description()


main(user_args)
