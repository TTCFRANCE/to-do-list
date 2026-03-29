print("Ecris help pour voir toutes les commandes")
commandes_connues = ["help", "add", "list", "delete", "check", "done_list", "modify", "clear_tasks", "clear_done"]
tasks = []
done = []

while True:
    commande = input(">>> ")  # Input for user

    if commande in commandes_connues:
        if commande == "help":
            print(
                "Voici toutes les commandes possibles :\n"
                "help : affiche toutes les commandes\n"
                "add : ajoute une tâche\n"
                "list : affiche la liste des tâches à faire\n"
                "done_list : affiche la liste des tâches faites\n"
                "delete : supprime une tâche\n"
                "check : coche une tâche\n"
                "modify : modifie le nom d'une tâche (uniquement dans la liste à faire)"
                "clear_tasks : supprime toutes les tâches dans la liste à faire"
                "clear_done : supprime toutes les tâches dans la liste faites"
            )
        #Ajouter une tâche
        elif commande == "add":
            titre = input("Titre de la tâche : ")
            tasks.append(titre)
            print(f"Tâche '{titre}' ajoutée !")

        #Afficher les tâches à faire
        elif commande == "list":
            print("Vous avez", len(tasks), "à faire :")
            for task in tasks:
                print(task)

        #Supprimer une tâche
        elif commande == "delete":
            titre = input("Titre de la tâche à supprimer : ")
            if titre in tasks:
                tasks.remove(titre)
                print(f"Tâche '{titre}' supprimée !")
            else:
                print("Cette tâche n'existe pas.")
                continue

        #Cocher une tâche comme faite
        elif commande == "check":
            titre = input("Quelle tâche avez vous fait ? ")
            if titre in tasks:
                tasks.remove(titre)
                done.append(titre)
                print(f"La tâche '{titre}' est marquée comme faite")
            else:
                print("Cette tâche n'existe pas.")
                continue
        
        #Afficher les tâches faites
        elif commande == "done_list":
            print("Vous avez fait", len(done), "tâches.")
            for done_task in done:
                print(done_task)

        #Modifier le nom d'une tâche
        elif commande == "modify":
            ancien_titre = input("Quelle tâche voulez-vous modifier ? ")
            nouveau_titre = input("Comment voulez-vous renommer la tâche ? ")
            if ancien_titre in tasks:
                tasks.remove(ancien_titre)
                tasks.append(nouveau_titre)
                print(f"La tâche '{ancien_titre}' à été renommer par : '{nouveau_titre}'")
            else:
                print("Cette tâche n'existe pas.")
                continue

        #Supprimer toutes les tâches à faire
        elif commande == "clear_tasks":
            tasks.clear()
            print("Les tâches à faire ont bien toutes été supprimées !")

        #Supprime toutes les tâches finis
        elif commande == "clear_done":
            done.clear()
            print("Toutes les tâches finis on été supprimées.")
    else:
        print("Commande inconnue")
        print("Ecris help pour voir toutes les commandes")