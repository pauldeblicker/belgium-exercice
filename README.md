# Belgium exercice

### Enoncé

Créer un fichier geojson contenant les provinces
belges fusionnées avec la région de Bruxelles-Capitale.

### Explication

N'étant pas particulièrement familier du format geojson, j'ai commencé par consulter les différents fichier geojson. Je me suis donc rendu compte que chacun d'eux correspondait à un niveau "administratif" différent:

* Region => niveau 4
* Province => niveau 6

Pour résoudre cette exercice, j'ai donc choisi de réaliser un script python permettant de récupérer une "feature" via son id dans le fichier des régions, puis d'ajouter cette dernière à celui des provinces.

Une fois cette première étape réalisé, j'ai fait en sorte que l'on puisse passer par l'intermédiare d'arguments les chemin des deux fichier ainsi que l'id de la features que l'on souhaite déplacer, rendant ainsi ce script capable de déplacer n'importe quelle "feature" d'un fichier vers un autre.

### Pré-requis

#### Version

* python >= 3.6.1

### Utilisation

Executer le script 'add_feature_to_file' en passant les arguments de la façon suivante:

```python add_feature_to_file.py [path_to_src_file] [feature_id] [path_to_dest_file]```

C'est-à-dire :

```python add_feature_to_file.py asset/admin_level_4.geojson 54094 asset/admin_level_6.geojson```


### Information utiles

* l'id de la Région de Bruxelles-Capitale est **54094**
* Vous trouverez les différents fichier au format geojson dansle dossier asset
* dans le cadre de la résolution de cet exercice, il faut utiliser les fichiers **admin_level_4.geojson** (régions) et  **admin_level_6.geojson**
