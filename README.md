# Process
Image docker contenant les processus d'export et conversion de fichiers pour la revue Sens public à partir de la chaîne éditoriale [Stylo](http://stylo.ecrituresnumeriques.ca).

La version en ligne de l'outil est [ici](http://process.ecrituresnumeriques.ca)

## Installation

Pour tester process en local (pour les développeurs):

Cloner le repos et ensuite:

```
docker-compose up -d --build
```

## Usage

1. Selectionner l'identifiant de la **version** de l'article sur stylo. L'identifiant se trouve dans l'url. Les URL stylo sont construites ainsi: `https://stylo.ecrituresnumeriques.ca/write/id_article/id_version`
2. Collez l'identifiant de la version dans la case "Version)
3. Attribuez un identifiant à l'article que vous voulez exporter: l'identifiant de l'article sera le nom de vos fichiers. Ex: SP1234
4. Sélectionner le type de traitement pour faire le pdf. Xelatex a plus de chances de ne pas rencontrer de problèmes

Vous pourrez ensuite téléchager les fichiers en format zip ou télécharger seulement le pdf.

**Attention**: l'url à laquelle vous trouvez le pdf ne vous garantit pas d'avoir toujours le même fichier car le fichier est regeneré à chaque fois que le script est lancé. Cet outil sert pour télécharger les fichiers et non pour les laisser en ligne.

## Todo
1. Export à partir de l'id de l'article
2. Implémantation dans Stylo
3. Import docx vers Stylo



