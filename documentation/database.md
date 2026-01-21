
Ici, les explications de la création de la base de données.

# Choix de la structure sur le projet

- On a crée un fichier `init_db.py` qui définit la **structure**. Celui-ci permet de créer la base **UNE FOIS** de façon correcte. Comme cela, si on veut apporter des modifications à notre base, on a juste à modifier ce fichier. Cela garantit d'avoir la même base.

- On a mit dans le `.gitignore` la base, comme cela il n'y aura pas de conflit.

- On a crée un dossier `db/` pour tout ce qui est structure de données, que cela ne se mélange pas avec la logique métier ni l'interface.

- On a aussi crée un fichier `data_db.py` qui définit **l'état initial**, il permet d'avoir des données pour tester l'application.

**ATTENTION :** Quand on exécute pour ajouter toutes les valeurs, si on réexécute, cela voudra replacer les nouvelles valeurs. **Par unicité**, il y a une erreur !
Ainsi, on ne lance **jamais automatiquement** au lancement de l’app ces deux fichiers.

