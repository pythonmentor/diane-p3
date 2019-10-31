# La structure (départ, emplacement des murs, arrivée), devra être enregistrée dans un fichier pour la modifier facilement au besoin.
import random
# Message de bienvenue 
print("Bienvenue MacGyver ! Vous êtes enfermé dans un labyrinthe dont la sortie est protégée par un garde. Les élèments suivants y sont dispersés : de l'éther, une aiguille et un tube en plastique, saisissez-les et endormez le garde pour pouvoir sortir ! ")

class Player:
    
    def __init__ (self, pseudo, health, objets, position):
        self.pseudo = pseudo
        self.health = health
        self.objets = objets
        self.position = position
        print("Bienvenue au joueur", pseudo, "/ Points de vie:", health, "/ Attaque:", attack)

    # MacGyver sera contrôlé par les touches directionnelles du clavier.
    # MacGyver devra donc se déplacer de case en case, avec 15 cases sur la longueur de la fenêtre
    def marcher(self):
        pass

    # Il récupèrera un objet simplement en se déplaçant dessus.
    def add_objet(self, objets)
        self.objets = self.objets + 1

    def get_objets(self, objets)
        return self.objets

    def get_pseudo(self):
        return self.pseudo
        
    def get_health(self):
        return self.health
        
    def get_attack(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage
        print("Aïe...  venez de subir", damage, "dégâts !")

player1 = Player("MacGyver", 3, random)

player2 = Player("Garde", 3, sortie)

Labyrinthe = []
# La fenêtre du jeu sera un carré pouvant afficher 15 sprites sur la longueur. 

class Objet:
    # Pour le distraire, il vous faut réunir les éléments suivants (dispersés dans le labyrinthe) : une aiguille, un petit tube en plastique et de l'éther. 
    
    def __init__(self, name, damage, position):
        self.name = name
        self.position = position
        self.damage = damage

    # Les objets seront répartis aléatoirement dans le labyrinthe et changeront d’emplacement si l'utilisateur ferme le jeu et le relance.
    def random_objet_place():
        import random
# Return a random item in a list
def random_item_in(object_list):
    rand_numb = random.randint(0, len(object_list) - 1)
    return object_list[rand_numb]

objet1.random_objet_place
objet2.random_objet_place
objet3.random_objet_place

objet1 = Objet("une aiguille", 1, objet1.position)
objet2 = Objet("un petit tube en plastique", 1, objet1.position)
objet3 = Objet("de l'éther", 1, objet1.position)

# Ils permettront à MacGyver de créer une seringue et d'endormir notre garde. 
serum_soporifique = objet1.damage + objet2.damage + objet3.damage


def main_loop():
    while True:
        print_random_sentence()
        message = ('Voulez-vous voir une autre citation ? '
                   'Pour sortir du programme, tapez [B].')
        choice = input(message).upper()
        if choice == 'B':
            break
            # This will stop the loop!

if __name__ == '__main__':
    main_loop()
        

# Fin du programme
# Le programme s'arrête uniquement si MacGyver a bien récupéré tous les objets et trouvé la sortie du labyrinthe.

def exit():
    if player1.position is sortie and player2.health = 0
    exit 

exit()

# S'il n'a pas tous les objets et qu'il se présente devant le garde, il meurt (la vie est cruelle pour les héros).
def exit2():
    if player1.position is sortie and player1.objets != 3
    print("Vous êtes mort. Désolé !")



Fichiers nécessaires au programme
Un ami graphiste, soucieux de votre santé, a décidé de vous aider un peu et vous a envoyé certains éléments graphiques nécessaires au jeu. Les voici :
Murs, fonds et accessoires : [Téléchargez [.zip - 387ko]](https://s3-eu-west-1.amazonaws.com/course.oc-static.com/projects/macgyver_ressources.zip)
MacGyver : ![](https://user.oc-static.com/upload/2017/04/21/14927753100739_macgyver-32-43.png)
Gardien : ![](https://user.oc-static.com/upload/2017/04/21/14927753225921_murdoc-32.png)
Ces ressources ont été mises à disposition originellement sous licence WTFPL sur le site http://jessefreeman.com/Etapes
1 - Créer le cadre de départ
Initialisez un repo Git et envoyez-le sur Github.
Commencez par créer le labyrinthe sans l’interface graphique. Quand la logique de votre labyrinthe est faite, utilisez le module PyGame pour dessiner l’interface graphique.
Puis intéressez-vous aux trois éléments principaux du jeu : le gardien, MacGyver et les objets. Comment les représenter dans votre programme ? Où sont-ils placés au commencement du jeu ?  
2 - Animer le personnage
Le seul élément mouvant est MacGyver. Créez les méthodes de classe qui permettent de l'animer et de trouver la sortie. Pour l'instant, faites une version simplifiée du jeu dans laquelle MacGyver gagne en arrivant face au gardien.
3 - Récupérer les objets
Ajoutez la gestion des objets. Comment MacGyver les ramasse-t-il ?  Ajoutez également un compteur qui les listera.
4 - Gagner !
Enfin, changez la fin du jeu : MacGyver gagne s'il a bien ramassé tous les objets et endormi le garde. Sinon, il perd.
Livrables
Programme hébergé par Github,
Document texte expliquant votre démarche et comprenant le lien vers votre code source (sur Github). Développez notamment le choix de l'algorithme. Expliquez également les difficultés rencontrées et les solutions trouvées. Le document doit être en format pdf et ne pas excéder 2 pages A4.Contraintes
Vous versionnerez votre code en utilisant Git et le publierez sur Github pour que votre mentor puisse le commenter,
Vous respecterez les bonnes pratiques de la PEP 8 et développerez dans un environnement virtuel utilisant Python 3,
Votre code devra être écrit en anglais : nom des variables, commentaires, fonctions...Pensez à mettre à jour votre page de profil quand votre mentor aura validé votre projet ! 
Compétences évaluées
Lire et comprendre une documentation de module
Gérer les différentes versions de Python et ses modules en fonction des projets
Créer des scripts pour le web en utilisant Python
Utiliser un algorithme pour résoudre un besoin technique
Coder efficacement en utilisant les outils adéquats
Conceptualiser l'ensemble de son application en décrivant sa structure (Entités / Domain Objects)





2

Étant un grand fan de Richard Dean Anderson, vous imaginez un labyrinthe 2D dans lequel MacGyver aurait été enfermé. La sortie est surveillée par un garde du corps dont la coiffure ferait pâlir Tina Turner. Pour le distraire, il vous faut réunir les éléments suivants (dispersés dans le labyrinthe) : une aiguille, un petit tube en plastique et de l'éther. Ils permettront à MacGyver de créer une seringue et d'endormir notre garde.
Fonctionnalités

Il n'y a qu'un seul niveau. La structure (départ, emplacement des murs, arrivée), devra être enregistrée dans un fichier pour la modifier facilement au besoin.
MacGyver sera contrôlé par les touches directionnelles du clavier.
Les objets seront répartis aléatoirement dans le labyrinthe et changeront d’emplacement si l'utilisateur ferme le jeu et le relance.
La fenêtre du jeu sera un carré pouvant afficher 15 sprites sur la longueur.
MacGyver devra donc se déplacer de case en case, avec 15 cases sur la longueur de la fenêtre !
Il récupèrera un objet simplement en se déplaçant dessus.
Le programme s'arrête uniquement si MacGyver a bien récupéré tous les objets et trouvé la sortie du labyrinthe. S'il n'a pas tous les objets et qu'il se présente devant le garde, il meurt (la vie est cruelle pour les héros).
Le programme sera standalone, c'est-à-dire qu'il pourra être exécuté sur n'importe quel ordinateur.
Fichiers nécessaires au programme
Un ami graphiste, soucieux de votre santé, a décidé de vous aider un peu et vous a envoyé certains éléments graphiques nécessaires au jeu. Les voici :
Murs, fonds et accessoires : [Téléchargez [.zip - 387ko]](https://s3-eu-west-1.amazonaws.com/course.oc-static.com/projects/macgyver_ressources.zip)
MacGyver : ![](https://user.oc-static.com/upload/2017/04/21/14927753100739_macgyver-32-43.png)
Gardien : ![](https://user.oc-static.com/upload/2017/04/21/14927753225921_murdoc-32.png)
Ces ressources ont été mises à disposition originellement sous licence WTFPL sur le site http://jessefreeman.com/Etapes
1 - Créer le cadre de départ
Initialisez un repo Git et envoyez-le sur Github.
Commencez par créer le labyrinthe sans l’interface graphique. Quand la logique de votre labyrinthe est faite, utilisez le module PyGame pour dessiner l’interface graphique.
Puis intéressez-vous aux trois éléments principaux du jeu : le gardien, MacGyver et les objets. Comment les représenter dans votre programme ? Où sont-ils placés au commencement du jeu ?  
2 - Animer le personnage
Le seul élément mouvant est MacGyver. Créez les méthodes de classe qui permettent de l'animer et de trouver la sortie. Pour l'instant, faites une version simplifiée du jeu dans laquelle MacGyver gagne en arrivant face au gardien.
3 - Récupérer les objets
Ajoutez la gestion des objets. Comment MacGyver les ramasse-t-il ?  Ajoutez également un compteur qui les listera.
4 - Gagner !
Enfin, changez la fin du jeu : MacGyver gagne s'il a bien ramassé tous les objets et endormi le garde. Sinon, il perd.
Livrables
Programme hébergé par Github,
Document texte expliquant votre démarche et comprenant le lien vers votre code source (sur Github). Développez notamment le choix de l'algorithme. Expliquez également les difficultés rencontrées et les solutions trouvées. Le document doit être en format pdf et ne pas excéder 2 pages A4.Contraintes
Vous versionnerez votre code en utilisant Git et le publierez sur Github pour que votre mentor puisse le commenter,
Vous respecterez les bonnes pratiques de la PEP 8 et développerez dans un environnement virtuel utilisant Python 3,
Votre code devra être écrit en anglais : nom des variables, commentaires, fonctions...Pensez à mettre à jour votre page de profil quand votre mentor aura validé votre projet ! 
Compétences évaluées
Lire et comprendre une documentation de module
Gérer les différentes versions de Python et ses modules en fonction des projets
Créer des scripts pour le web en utilisant Python
Utiliser un algorithme pour résoudre un besoin technique
Coder efficacement en utilisant les outils adéquats
Conceptualiser l'ensemble de son application en décrivant sa structure (Entités / Domain Objects)
















