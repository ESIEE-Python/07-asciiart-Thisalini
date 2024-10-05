#### Imports et définition des variables globales

"""encoder une chaine de caractères par une liste de tuples"""

#### Fonctions secondaires
def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument
        s (str): la chaîne de caractères à encoder
        Returns: list: la liste des tuples (caractère, nombre d'occurences)
    """
    c=[s[0]]
    o=[1]
    k = 1
    n=len(s)
    while k < n:
        if s[k]==s[k-1]:
            o[-1]+= 1
        else:
            c.append(s[k])
            o.append(1)
        k+= 1
    return list(zip(c,o))

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée 
    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    # code de base
    if not s:
        return []
    # recherche nombre de caractère identique
    k = 1
    while k < len(s) and s[0]==s[k]:
        k +=1
    #appel recursive
    return [(s[0],k)]+artcode_r(s[k:])

#### Fonction principale

def main():
    """ fait appel aux fonctions secondaires pour vérifier leur bon fonctionnement"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
