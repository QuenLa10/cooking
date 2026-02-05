# Développement d'une application web / jeu de recettes de cuisine 

## [](#contexte-du-projet)[](#contexte-du-projet)Contexte du projet

On est deux élèves de l'école Télécom Nancy, ayant envie de créer un projet. Pour cela, on s'est posé la question suivante : Qu'est-ce que qui nous embête dans la vie ? Une réponse : Le problème de cuisiner en tant qu'étudiant ! 
Effectivement, on n'a jamais d'idées quant à ce qu'on va manger le soir, donc la flemme s'empare de soi et on cuisine toujours la même chose : des pâtes.  On souhaite ainsi créer une application web qui serait comme un jeu et qui permettrait de trouver et réaliser (ou même créer) des recettes facilement. L'objectif est d'augmenter de niveau en testant pleins de recettes différentes.

## [](#contexte-p%C3%A9dagogique)[](#contexte-p%C3%A9dagogique)Contexte pédagogique

Ce projet vise à nous placer en situation de développement complet d’un site / d'une application intégrant :

- la conception algorithmique,
- la modélisation et l’implémentation de données,
- la réalisation d’un service web avec front-end et back-end,
- la gestion de projet collaboratif.

### [](#objectifs-dapprentissage)[](#objectifs-dapprentissage)Objectifs d'apprentissage

Volet Gestion de projet :

- Définir les besoins fonctionnels et techniques à partir d’un cahier des charges simplifié.
- Planifier et suivre un projet (outils agiles, gestion des versions, documentation).
- Utiliser des outils collaboratifs (Git, GitLab, Trello/Jira, Wiki, DrawSQL etc.).
- Rédiger et présenter un rapport de projet clair et professionnel.

Volet Algorithmique :

- Analyser un problème et identifier les algorithmes pertinents.
- Évaluer la complexité et la correction des solutions envisagées.
- Implémenter et tester des algorithmes efficaces en Python.

Volet Base de données :

- Concevoir un modèle de données relationnel (MCD, MLD).
- Normaliser et documenter le schéma de la base.
- Implémenter et interroger une base relationnelle (PostgreSQL/MySQL/SQLite/DrawSQL).
- Gérer les interactions entre la base et l’application via une API.

Volet Web :

- Concevoir une architecture client-serveur.
- Développer une API REST avec Flask.
- Concevoir un front-end léger (HTML/CSS/JS ou framework minimal).
- Connecter le front-end à l’API.
- Déployer et tester une application web fonctionnelle.

## [](#p%C3%A9rim%C3%A8tre-fonctionnel)[](#p%C3%A9rim%C3%A8tre-fonctionnel)Périmètre fonctionnel (Admin)

|          **Fonctionnalité**          |                                            **Description synthétique**                                            | **Difficulté** | **Obligation** |
| :----------------------------------: | :---------------------------------------------------------------------------------------------------------------: | :------------: | :------------: |
|     **Gestion des Ingrédients**      |      CRUD (Créer, Lire, Modifier, Supprimer) la liste des ingrédients de référence (ex: "Tomate", "Pâtes").       |       🟢       |       ✅        |
|       **Gestion des Recettes**       |                Interface pour ajouter/éditer une recette (titre, temps, étapes, ingrédients liés).                |       🟡       |       ✅        |
|     **Gestion des Utilisateurs**     |                        Voir la liste des inscrits, pouvoir bannir ou supprimer un compte.                         |       🟢       |       ✅        |
|     **Algorithme de "Matching"**     |                  Moteur de recherche : Entrer des ingrédients -> Sortir les recettes possibles.                   |       🔴       |       ✅        |
|      **Système de calcul d'XP**      | Logique backend : À la validation d'une recette, ajouter X points au profil et vérifier si un niveau est franchi. |       🟡       |       ✅        |
| **Système de Badges (Achievements)** |             Déclencheur (Trigger) : Si "compteur tomate" > 10, alors débloquer le badge "Tomatovore".             |       🔴       |       🔸       |
|      **API REST (Si demandé)**       |             Créer les endpoints (URL) pour envoyer les données en format JSON (ex: `/api/recettes`).              |       🟡       |       ✅        |


## [](#p%C3%A9rim%C3%A8tre-fonctionnel)[](#p%C3%A9rim%C3%A8tre-fonctionnel)Périmètre fonctionnel (User)

|         **Fonctionnalité**         |                                    **Description synthétique**                                     | **Difficulté** | **Obligation** |
| :--------------------------------: | :------------------------------------------------------------------------------------------------: | :------------: | :------------: |
|        **Authentification**        |                          Inscription, Connexion, Déconnexion (Sécurisée).                          |       🟡       |       ✅        |
|    **Tableau de bord (Profil)**    |          Affichage de l'avatar, de la barre d'XP, du niveau actuel et des badges obtenus.          |       🟢       |       ✅        |
|     **Catalogue de recettes**      |             Liste des recettes avec filtres (Saison, Temps, Difficulté) et pagination.             |       🟢       |       ✅        |
|   **Fiche Recette "Pas à pas"**    |           Affichage clair d'une recette unique avec les cases à cocher pour les étapes.            |       🟢       |       ✅        |
|       **Recherche "Frigo"**        |          Champ de recherche où l'on tape ses restes pour trouver une recette compatible.           |       🔴       |       ✅        |
| **Action "Cuisiner" (Validation)** |        Bouton "J'ai cuisiné ça" -> Upload d'une photo (ou simple validation) -> Gain d'XP.         |       🟡       |       ✅        |
|   **Création de recette (UGC)**    | Formulaire pour qu'un utilisateur propose sa propre recette (mise en attente de validation admin). |       🔴       |       🔸       |
|       **Mode "Mario Maker"**       |            Affichage distinct : "Recettes Officielles" vs "Recettes de la Communauté".             |       🟡       |       ⭕        |
|         **Génération PDF**         |                          Bouton pour télécharger la fiche recette en PDF.                          |       🔴       |       🔸       |

### [](#l%C3%A9gende-des-niveaux-de-difficult%C3%A9)[](#l%C3%A9gende-des-niveaux-de-difficult%C3%A9)Légende des niveaux de difficulté

- 🟢 **Facile** : peut être réalisé dès les premières séances avec l'appui du tutoriel Flask.
- 🟡 **Moyen** : nécessite de combiner plusieurs notions (formulaires + relations BDD par exemple).
- 🔴 **Difficile** : demande des recherches supplémentaires ou l'utilisation d'API externes.
- ✅ **Obligatoire** : à livrer pour valider le projet.
- 🔸 **Optionnel** : à choisir si le temps le permet ou pour aller plus loin.
- ⭕ **Bonus** : réservé aux équipes très à l'aise.

## [](#architecture-et-contraintes-techniques)[](#architecture-et-contraintes-techniques)Architecture et contraintes techniques

**Framework** : Flask + Jinja2.

**Base de données** : SQLite (par défaut). Passage à PostgreSQL = 🟡 Moyen, ⭕ Bonus.

**Authentification** : Flask-Login conseillé (si non utilisé, gérer sessions manuellement).

**Interface** : HTML/CSS minimal. JavaScript optionnel.

## [](#jalons-indicatifs)[](#jalons-indicatifs)Jalons indicatifs

**Jalon 1 : Mise en place et bases**

- Objectifs : Formation Flask, dépôt Git, authentification simple, modélisation BDD pour clients/prospects.
- Livrables : Application de base fonctionnelle avec base de données pour clients contactés.

**Jalon 2 : Affichage des recette**

- Objectifs : CRUD (_Create, Read, Update, Delete_) pour créer les recettes, 
- Livrables : Interfaces de gestion et tableau de bord.

**Jalon 3 : Création de compte**

- Objectifs : Système d'accomplissement, XP, propre compte
- Livrables : Page de profil.

**Jalon 4 : Recherche de recettes**

- Objectifs : Recherche d'une recette selon critères
- Livrables : Page de recherche intelligente

**Jalon 5 : Affichage personnalisé**

- Objectifs : Affichage type jeu
- Livrables : Jeu fonctionnel

**Jalon 6 : Création/Publication de recette**

- Objectifs : Créer ses propres recettes, et les publier (à part du jeu principal)
- Livrables : Page des recettes de tous



## [](#rendu-final)[](#rendu-final)Rendu final

**Code source** : Livraison du code source complet et proprement organisé (ex : `app.py`, `models.py`, `routes.py`, `forms.py`, `templates/`)

**Tests unitaires** : Un ensemble de tests unitaires accompagnant le code source.

**Documentations** : Comprend un guide d'installation, un court manuel utilisateur, une description des détails techniques et notamment de la modélisation de la base de données relationnelles.

**État de l'art** : Rapport de l’état de l’art sur les algorithmes d’intelligence artificielle applicables et appliqués.

**Gestion de projet** : Comprend tous les éléments de gestion de projet que vous aurez produits (fiche de projet, comptes-rendus de réunion, planification et répartition des tâches, analyse post-mortem des efforts individuels et de l'atteinte des objectifs, etc.).

**Tous ces éléments seront déposés de manière organisée dans le dépôt git de votre projet.**


