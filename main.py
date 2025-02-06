import jsonpickle
import os

# Classe représentant un Jeu
class Jeu:
    def __init__(self, nom, tag, image):
        self.nom = nom
        self.tag = tag
        self.image = image  # Ici, ce sera juste un chemin d'image

    def __str__(self):
        return f"🎮 {self.nom} | Tag: {self.tag} | Image: {self.image}"

# Classe Bibliothèque contenant une liste de jeux
class Bibliotheque:
    def __init__(self, fichier_sauvegarde="bibliotheque.json"):
        self.fichier_sauvegarde = fichier_sauvegarde
        self.jeux = self.charger_jeux()

    def ajouter_jeu(self, nom, tag, image):
        jeu = Jeu(nom, tag, image)
        self.jeux.append(jeu)
        self.sauvegarder_jeux()
        print(f"✅ Jeu ajouté : {jeu.nom}")

    def supprimer_jeu(self, nom):
        self.jeux = [jeu for jeu in self.jeux if jeu.nom != nom]
        self.sauvegarder_jeux()
        print(f"🗑 Jeu supprimé : {nom}")

    def afficher_jeux(self):
        if not self.jeux:
            print("📂 La bibliothèque est vide.")
        else:
            for jeu in self.jeux:
                print(jeu)

    def afficher_details_jeu(self, nom):
        for jeu in self.jeux:
            if jeu.nom == nom:
                print(jeu)
                return
        print("⚠ Jeu non trouvé.")

    def sauvegarder_jeux(self):
        with open(self.fichier_sauvegarde, "w") as f:
            f.write(jsonpickle.encode(self.jeux))
        print("💾 Sauvegarde effectuée.")

    def charger_jeux(self):
        if os.path.exists(self.fichier_sauvegarde):
            with open(self.fichier_sauvegarde, "r") as f:
                return jsonpickle.decode(f.read()) or []
        return []

# Fonction pour afficher le menu
def afficher_menu():
    print("\n🎮 MENU BIBLIOTHÈQUE 🎮")
    print("1️⃣ Ajouter un jeu")
    print("2️⃣ Supprimer un jeu")
    print("3️⃣ Afficher tous les jeux")
    print("4️⃣ Voir les détails d'un jeu")
    print("5️⃣ Quitter")
    
def main():
    bibliotheque = Bibliotheque()

    while True:
        afficher_menu()
        choix = input("👉 Choisissez une option : ")

        if choix == "1":
            nom = input("Nom du jeu : ")
            tag = input("Tag (ex: Action, RPG) : ")
            image = input("Chemin de l'image : ")
            bibliotheque.ajouter_jeu(nom, tag, image)

        elif choix == "2":
            nom = input("Nom du jeu à supprimer : ")
            bibliotheque.supprimer_jeu(nom)

        elif choix == "3":
            bibliotheque.afficher_jeux()

        elif choix == "4":
            nom = input("Nom du jeu à afficher : ")
            bibliotheque.afficher_details_jeu(nom)

        elif choix == "5":
            print("👋 Au revoir !")
            break

        else:
            print("❌ Choix invalide, essayez encore.")

if __name__ == "__main__":
    main()
