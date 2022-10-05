#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:

    if values is None:
        input_string = input("Veuillez entrer 10 valeurs "
                             "séparées par un espace: ")
        values = input_string.split()

    values.sort()

    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        input_string = input("Entrez 2 mots séparés par un espace pour "
                             "vérifier s'ils sont des anagrames: ")
        words = input_string.split()

    return sorted(words[0]) == sorted(words[1])


def contains_doubles(items: list) -> bool:
    return len(set(items)) != len(items)


def best_grades(student_grades: dict) -> dict:
    # Retourner un dictionnaire contenant le nom de l'étudiant
    # ayant la meilleure moyenne ainsi que sa moyenne
    meilleur_nom = ""
    meilleure_moyenne = 0

    for nom, notes in student_grades.items():
        moyenne = 0
        for note in notes:
            moyenne += note
        moyenne /= len(notes)

        if moyenne > meilleure_moyenne:
            meilleure_moyenne = moyenne
            meilleur_nom = nom

    return {meilleur_nom: meilleure_moyenne}


def frequence(sentence: str) -> dict:
    # Afficher les lettres les plus fréquentes
    # Retourner le tableau de lettres

    # Initialiser un dictionnaire qui va contenir
    # le nombre d'apparition de chaque lettre
    freq = {}

    max_freq = 0

    for letter in sentence:
        if not letter.isalnum():
            continue

        if letter not in freq:
            freq[letter] = 1
        else:
            freq[letter] += 1

        if freq[letter] > max_freq:
            max_freq = freq[letter]

    for i in range(max_freq, 5, -1):
        for key, value in freq.items():
            if value == i:
                print(f"Le caractère \"{key}\" revient {value} fois.")

    return freq


def get_recipes():
    # Demander le nom d'une recette, puis ses ingredients
    # et enregistrer dans une structure de données
    nom = input("Nom de la recette: ").lower()
    ingredients = {}
    ingredient = [" "]
    print("Entrez les ingrédients sous la forme \"quantité ingrédient\""
          "\n(Appuyez deux fois sur entrée une fois la saisie terminée: ")
    while ingredient != []:
        ingredient = input("Ingrédient: ").split()

        # Vérifier qu'on a une quantité et un nom par ingrédient
        if len(ingredient) < 2 and ingredient != []:
            print("Mauvais format! \"quantité ingrédient\" Attendu")
            continue

        if ingredient != []:
            ingredients[" ".join(ing.lower()
                                 for ing in ingredient[1:])] = ingredient[0]

    return {nom: ingredients}


def print_recipe(recettes) -> None:
    # Demander le nom d'une recette, puis l'afficher si elle existe
    nom = input("Veuillez entrer le nom d'une recette à afficher: ").lower()

    if nom not in recettes:
        print(f"La recette {nom} n'existe pas.")
        return

    print(f"Recette {nom}:")
    for ingredient, quantite in recettes[nom].items():
        print(f"{quantite:>8} {ingredient}")


def main() -> None:
    print("On essaie d'ordonner les valeurs...")
    order()

    print("On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(
        f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
