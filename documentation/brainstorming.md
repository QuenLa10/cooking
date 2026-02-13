# Brainstorm initial

## Idées critères de recherche :
- ingrédients
- mode de cuisson
- saison
- nb de personnes ?
- temps de préparation
- niveau/difficulté

## Système d'accomplissement Utilisateur :
- badge
- XP (1ère réalisation = + 50 XP, 2ème réalisation = + 5 XP)
- validation en déposant une photo (ok pour app téléphone mais trop compliquer pour site internet)
- grade / titre (ex: éplucheur de légume -> chef étoilé)
- débloquer des recettes
- personnaliser avatar avec système de monnaie

## IDÉES :
- liste de course (bof)
- afficher les recettes pas à pas
- styliser écriture + photo (anecdote, ...)
- augmenter le nombre de personnes -> augmente les quantités en direct
- note / étoiles pour chaque recette + commentaire
- boite à idée pour l'ajout de recette
- Créer un modèle de recette pour ajouter des recettes
- Bouton pour télécharger les recettes au format pdf
- mario maker :
	1 page avec NOS recettes / A page avec les recettes créées par les gens
- substitut à un ingrédient
- recette événement (ex: Halloween, Noël, ...)


# Recipe Card Modal

## Idée 

Quand on clique sur une recette :
- Fond légèrement assombri
- Carte centrée
- Animation douce
- Bouton "Ouvrir la recette"

## Structure interne

----------------------------------------
    Pizza Margherita      ✕          icône de rareté

	[ Image pixel 128x128 ]

  Difficulté : 
  Temps : 20 min
  XP : +10

  Petite description :
  "Un classique étudiant simple et rapide."

  Ingrédients clés :
  • Mozzarella
  • Tomates
  • Basilic

	[ Ouvrir la recette ]
----------------------------------------

## DA précise

### Carte 
- Couleur vert sauge très clair
- Bordure brun bois
- Coins légèrement arrondis
- Ombre douce
### Fond quand il y a la carte
- Overlay beige semi-transparent
- Flou léger 
- Pas trop sombre
## Interactions

- La carte apparaît avec :
	- petite montée
	- fade-in
- Bouton avec effet lorsqu'on appuie
- Quand on clique sur x :
	- fade-out
	- retour aux recettes