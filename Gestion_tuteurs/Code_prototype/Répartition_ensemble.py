##Répartition élèves

#ce programme distribue les eleves dans les salles et leur attribue un tuteur,chaque eleves a un tuteur, un tuteur a plusieurs eleves, il y a  au minimum 2 tuteurs par salle(contrainte de l'établissement)et il est fait en sorte qu'un eleve ait le plus souvent le meme tuteur

#l'algorithme prend en entrée les tuteurs de la semaine ainsi que la repartition des eleves de la semaine precedente

import random

def faire_repartition(tuteurs, repartition_precedente):
    # Liste des élèves
    eleves =[for i in range (80)]

    # Nombre minimum de tuteurs par salle
    min_tuteurs_par_salle = 2

    # Calcul du nombre de salles nécessaires en fonction du nombre de tuteurs disponibles
    nb_salles = len(tuteurs) // min_tuteurs_par_salle

    # Si le nombre de salles est supérieur à 8, on le limite à 8
    if nb_salles > 8:
        nb_salles = 8

    # Dictionnaire pour stocker les élèves avec leur tuteur assigné
    tutorat = {}

    # Répartition des élèves avec des tuteurs en conservant autant que possible les tuteurs de la semaine précédente
    for eleve in eleves:
        # Si l'élève a un tuteur la semaine précédente, on essaie de le conserver
        if eleve in repartition_precedente:
            tuteur_precedent = repartition_precedente[eleve]['tuteur']
            salle_precedente = repartition_precedente[eleve]['salle']
            tuteurs_possibles = [tuteur for tuteur in tuteurs if tuteur != tuteur_precedent]
        # Sinon, on sélectionne un tuteur aléatoire parmi ceux disponibles
        else:
            tuteurs_possibles = tuteurs.copy()
            salle_precedente = -1  # Valeur arbitraire pour indiquer qu'il n'y a pas de tuteur précédent
        random.shuffle(tuteurs_possibles)
        for tuteur in tuteurs_possibles:
            # Sélection de la salle en fonction de la disponibilité des tuteurs
            salle_disponible = None
            for i in range(nb_salles):
                tuteurs_salle = [eleve_tuteur[1]['tuteur'] for eleve_tuteur in tutorat.items() if eleve_tuteur[1]['salle'] == i]
                if tuteur in tuteurs_salle or len(tuteurs_salle) >= min_tuteurs_par_salle:
                    continue
                else:
                    salle_disponible = i
                    break
            # Si aucune salle n'est disponible, on passe au tuteur suivant
            if salle_disponible is None:
                continue
            # Assignation de l'élève au tuteur et à la salle
            tutorat[eleve] = {'tuteur': tuteur, 'salle': salle_disponible}
            break  # On arrête la boucle sur les tuteurs dès qu'un tuteur est assigné

    return tutorat

#il ne reste plus qu'a convertir la sortie qui est une liste de liste en tableau excel pret a etre envoyer a l'etablissement