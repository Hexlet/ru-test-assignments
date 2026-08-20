> Локальная копия. Источник: <https://github.com/TouchTunes/backend-dev-tech-assignment>

(english version follows)

# Affectation technique du Développeur Java

L’usage du masculin dans ce document a pour unique but d’alléger le texte

## Énoncé du problème

Imaginez que vous devez produite une application Web qui permet la prise en charge à distance des réglages de jukebox. Selon les composantes matérielles propres au jukebox, il est possible qu'un réglage donné soit compatible ou non.
Exemples:

* un jukebox avec une composante "panneau DEL" est compatible avec le réglage `animation_type`.
* un jukebox sans composante "money receiver" est incompatible avec le réglage `currency`.

## L'Affectation

L'affectation consiste à produire un API REST offrant un seul point d'accès GET retournant une liste paginée de jukebox qui se conforment au réglage indiqué en paramètre. Les paramètres suivants doivent être supportés:

* `settingId` - identifiant unique d'un réglage (requis)
* `model` - filtre sur le nom du modèle (optionel)
* `offset` - indique l'indice de départ de la page (optionel)
* `limit` - indique la portée (nombre limite d'éléments) de la page (optionel)

Produire une solution _industrielle_ (prêt pour une mise en opération) et assurez-vous de faire appel aux sources de données ci-dessous.  
_Indice_: docs / error codes / tests / API docs  

Points bonis: livrer une version de votre application sous forme de conteneur Docker.

## À noter

Vous devez faire appel aux services d'API ci-dessous. Ils représentent les sources de données de référence.

### Jukebox API

Ce service fourni la liste de jukebox ainsi que certaines caractéristiques dont leur composantes.

**GET** `http://my-json-server.typicode.com/touchtunes/tech-assignment/jukes`:

```js
[{
  "id": "5ca94a8ac470d3e47cd4713c",
  "model": "fusion",
  "components": [{
    "name": "led_panel"
  }, {
    "name": "amplifier"
  }]
},
//...
]
```

### Settings API

Ce service fourni la liste de tous les réglages de jukebox disponibles. Chaque réglage contient une liste de composantes requises qu'un jukebox devrait posséder afin de se conformer à un réglage donné.

**GET** `http://my-json-server.typicode.com/touchtunes/tech-assignment/settings`:

```js
{
  "settings": [{
    "id": "e9869bbe-887f-4d0a-bb9d-b81eb55fbf0a",
    "requires": ["camera", "speaker", "pcb"]
  }, {
    "id": "db886f37-16e3-4a55-80e4-cfffc9e4e464",
    "requires": ["touchscreen", "money_pcb", "led_panel", "money_receiver"]
  },
  //...
  ]
}
```

**Note** un réglage donné est considéré comme étant supporté par un jukebox seulement si le jukebox possède _tous_ les composantes requises.

## Soumission

Soumettre le travail via un dépôt github / gitlab / bitbucket (conseil: ne pas utiliser "touchtunes" dans le nom ou la description) ou via un fichier ZIP.

## Backend Developer tech assignment

### Problem description

Imagine you are building a web application to remote control Jukebox settings. Depending on what components (hardware modules) a jukebox has, it may or may not support a setting (a key-value pair). For example a jukebox with "LED panel" component supports `animation_type` setting or a jukebox which does not have a "money_receiver" component does not support `currency` setting.

### The assignment

You need to create a REST API with a single GET endpoint which returns a paginated list of jukeboxes that suppport a given setting id. It should support following query parameters:

* `settingId` - setting id (required)
* `model` - filter by model name (optional)
* `offset` - specifies at what index start the page (optional)
* `limit` - specifies the page size (optional)

Create a production-ready implementation and make sure you use the mocked APIs listed below.  
_Hint_: docs / error codes / tests / API docs  
Bonus points: dockerize you application.

### Important notes

You need to make use of the following "mocked" APIs which will return jukebox and settings data.

#### Jukebox API

Returns a list of jukeboxes with information about them:

**GET** `http://my-json-server.typicode.com/touchtunes/tech-assignment/jukes`:

```js
[{
  "id": "5ca94a8ac470d3e47cd4713c",
  "model": "fusion",
  "components": [{
    "name": "led_panel"
  }, {
    "name": "amplifier"
  }]
},
//...
]
```

#### Settings API

Returns a list of all the available jukebox settings. Each setting contains a list of required components which a jukebox should have in order to support the setting.

**GET** `http://my-json-server.typicode.com/touchtunes/tech-assignment/settings`:

```js
{
  "settings": [{
    "id": "e9869bbe-887f-4d0a-bb9d-b81eb55fbf0a",
    "requires": ["camera", "speaker", "pcb"]
  }, {
    "id": "db886f37-16e3-4a55-80e4-cfffc9e4e464",
    "requires": ["touchscreen", "money_pcb", "led_panel", "money_receiver"]
  },
  //...
  ]
}
```

**Note** that setting is considered to be supported if jukebox has _all_ required components.

### Submission

Submit your assignment using a public github / gitlab / bitbucket repository (please don't use "touchtunes" in repo name or description) or a zip archive.
