# Radius UI - Traduction française

Date : 2026-10-14. Statut : design proposé, à relire avant le plan d'implémentation.

## Objectif

Un mod de traduction qui met en français les dix mods de la suite Radius UI d'astryl, qui n'existent qu'en anglais. Le joueur l'active avec n'importe quel sous-ensemble de la suite.

Hors périmètre :

- Radius UI - Inspector Plus : il a déjà son français.
- Radius UI - Colonist Bar Plus (fork en préparation) : il traduira lui-même ses nouvelles clés (voir « Règle avec les forks »).
- Les textes écrits en dur dans le code des mods (exemple : l'infobulle anglaise du constructeur de `FloatMenuOptionSub` dans Colonist Bar). Un mod de traduction ne peut pas les atteindre.

## Critères de réussite

- Avec le jeu en français, chaque texte traduisible des dix mods s'affiche en français.
- Aucune erreur de traduction au chargement, quel que soit le sous-ensemble de mods Radius actifs.
- Chaque fichier français a exactement les clés du fichier anglais correspondant, ni plus ni moins.
- Les variables (`{0}`, `{NAME}`…), les balises (`<color>`, `<b>`…) et les sauts de ligne (`\n`) sont conservés.

## Mods couverts

Inventaire fait dans les copies locales des mods (fichiers `Languages/English/Keyed`) :

| Mod | packageId | Fichier anglais | Chaînes | Préfixe des clés |
|---|---|---|---|---|
| Radius UI Framework | `astryl.RadiusUI.Framework` | `RadiusUIFramework.xml` | 57 | `RadiusUI.` |
| Colonist Bar | `astryl.RadiusUI.ColonistBar` | `RadiusColonistBar.xml` | 390 | `RCB_` |
| Everywhere | `astryl.RadiusUI.Everywhere` | `RadiusUIEverywhere.xml` | 42 | `RadiusUI.` |
| Faction Menu | `astryl.RadiusUI.FactionMenu` | `RadiusUIFactionMenu.xml` | 180 | `RUIFM.` |
| Health Tab | `astryl.RadiusUI.HealthTab` | `RadiusUIHealthTab.xml` | 241 | `RadiusUI.` |
| Ideology | `astryl.RadiusUI.Ideology` | `RadiusUIIdeology.xml` | 100 | `RadiusIdeo_` |
| Mission Control | `astryl.RadiusUI.MissionControl` | `RadiusUIMissionControl.xml` | 589 | `MN_` |
| Needs Tab | `astryl.RadiusUI.NeedsTab` | `RadiusUINeedsTab.xml` | 112 | `RadiusUI.` |
| Quest Menu | `astryl.RadiusUI.QuestMenu` | `RadiusUIQuestMenu.xml` | 77 | `RadiusQM.` |
| Xenotypes | `astryl.RadiusUI.Xenotypes` | `RadiusUIXenotypes.xml` | 131 | `RadiusUIXeno.` |

Total : 1 919 chaînes. Vérifié : aucune clé n'apparaît dans deux mods, malgré le préfixe `RadiusUI.` partagé par quatre d'entre eux. Les dix fichiers peuvent donc cohabiter dans un même dossier de langue.

Seul `Def` à traduire : le `KeyBindingDef` `RCB_FollowCam` de Colonist Bar (`Defs/KeyBindings.xml`, libellé « follow selected pawn (Radius UI) »).

## Structure du mod

Dossier `RadiusUIFrench/` (dépôt git propre, branche `main`) :

```
About/About.xml
LoadFolders.xml
Languages/French/Keyed/<même nom que le fichier anglais>.xml   (10 fichiers)
ColonistBar/Languages/French/DefInjected/KeyBindingDef/KeyBindings.xml
README.md
CHANGELOG.md
LICENSE
deploy.sh
docs/
```

- `About.xml` : nom « Radius UI - Traduction française », packageId `mrbabilo.RadiusUI.FrenchTranslation`, auteur mrbabilo, version 1.6. Aucune `modDependencies`. `loadAfter` : les dix packageId du tableau, pour passer après les fichiers anglais.
- Fichiers `Keyed` : une clé de langue d'un mod absent est ignorée par le jeu, sans erreur. Ces fichiers se chargent donc toujours.
- `DefInjected` : une traduction de Def absent produit une erreur au chargement. Le dossier `ColonistBar/` ne se charge que si Colonist Bar ou son fork est actif :

  ```xml
  <LoadFolders>
    <v1.6>
      <li>/</li>
      <li IfModActive="astryl.RadiusUI.ColonistBar, mrbabilo.RadiusUI.ColonistBarPlus">ColonistBar</li>
    </v1.6>
  </LoadFolders>
  ```

  `IfModActive` accepte une liste : il suffit qu'un des mods soit actif (vérifié dans `Verse.LoadFolder`, champ `requiredAnyOfPackageIds`, test `ModLister.AnyModActiveNoSuffix`).
- `deploy.sh` : copie du dossier, sans `docs/`, `deploy.sh` ni `.git*`, vers `RimWorld.app/Mods/RadiusUIFrench` avec `rsync --delete`. Pas de build : le mod ne contient pas de code.
- `LICENSE` : MIT pour la traduction. Les textes source restent ceux d'astryl (MIT).

## Règles de traduction

- **Vocabulaire** : celui de la traduction française officielle du jeu, dans le dépôt local `RimWorld-fr` (`Core`, `Ideology`, `Biotech`, `Anomaly`, `Odyssey`). Exemples : *drafted* → « mobilisé », *colonist* → « colon », *mood* → « humeur », *mental break* → « crise mentale », *bill* → « facture ». En cas de doute, chercher le terme dans `RimWorld-fr` avant de le choisir.
- **Cohérence avec Inspector Plus** : mêmes choix pour les termes partagés (exemple : « Panneau de gauche », « Réinitialiser »).
- **Intouchable** : variables entre accolades, balises, entités XML (`&#8230;`, `&amp;`), `\n`, noms propres de mods. Seule la partie lisible change.
- **Longueur** : le français est souvent 15 à 30 % plus long. Pour les libellés courts de boutons, d'onglets et de pastilles, choisir la forme la plus courte qui reste claire. Les textes longs (infobulles, descriptions de réglages) n'ont pas cette contrainte.
- **Typographie** : guillemets « », espace insécable avant « : ; ? ! » quand l'interface le permet. L'apostrophe droite `'` reste, comme dans la traduction officielle.
- **Majuscules** : on garde la casse de l'anglais là où le jeu l'affiche telle quelle (titres, boutons). On ne met pas de majuscule à chaque mot comme l'anglais.

## Règle avec les forks

Une clé `Keyed` définie deux fois dans la même langue est refusée la seconde fois, avec l'erreur de chargement « Duplicate keyed translation key » (`Verse.LoadedLanguage`) : la première valeur chargée gagne, sans garantie sur laquelle. Donc :

- ce mod traduit toutes les clés d'origine des dix mods ;
- un fork (Inspector Plus, Colonist Bar Plus) ne traduit dans son propre dossier `French` que les clés qu'il ajoute, jamais une clé d'origine.

Inspector Plus suit déjà cette règle : il n'a aucune clé `RadiusUI.` en français. Colonist Bar Plus devra la suivre (à ajouter à sa spec).

## Vérification

Contrôles par script, à chaque fichier :

1. `xmllint --noout` sur chaque fichier.
2. Même ensemble de clés que le fichier anglais (comparaison des listes de clés triées).
3. Pour chaque clé, mêmes variables `{…}` et mêmes balises qu'en anglais.
4. Aucune valeur encore identique à l'anglais, sauf une liste d'exceptions justifiées (noms propres, sigles), écrite dans le script.

Contrôle en jeu, à faire par le joueur :

5. Jeu en français avec toute la suite active : Player.log sans erreur de traduction, textes affichés en français, libellés courts non coupés.
6. Jeu avec un seul mod Radius actif : aucune erreur (vérifie le `LoadFolders` et l'absence d'erreurs `Keyed`).

## Ordre de travail

Un commit par mod, du plus petit au plus grand : Everywhere, Framework, Quest Menu, Ideology, Needs Tab, Xenotypes, Faction Menu, Health Tab, Colonist Bar (avec le `DefInjected`), Mission Control. Puis `README`, `CHANGELOG`, déploiement dans `Mods`.

## Mise à jour quand un mod d'astryl évolue

Le script de vérification (point 2) signale les clés ajoutées ou retirées en comparant avec les fichiers anglais des copies locales `RadiusUI*/`. Il faut donc recopier un mod mis à jour depuis le Workshop avant de relancer le script.
