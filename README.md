# Radius UI - Traduction française

Mod RimWorld 1.6 qui traduit en français la suite **Radius UI** d'astryl. Il ne contient aucun code et ne touche pas aux sauvegardes.

- packageId : `mrbabilo.RadiusUI.FrenchTranslation`
- Aucune dépendance. À placer après les mods Radius UI dans la liste (`loadAfter` le fait).

## Mods couverts

| Mod | Fichier | Chaînes |
|---|---|---|
| Radius UI Framework | `RadiusUIFramework.xml` | 57 |
| Colonist Bar | `RadiusColonistBar.xml` + raccourci `RCB_FollowCam` | 390 |
| Everywhere | `RadiusUIEverywhere.xml` | 42 |
| Faction Menu | `RadiusUIFactionMenu.xml` | 180 |
| Health Tab | `RadiusUIHealthTab.xml` | 241 |
| Ideology | `RadiusUIIdeology.xml` | 100 |
| Mission Control | `RadiusUIMissionControl.xml` | 588 |
| Needs Tab | `RadiusUINeedsTab.xml` | 112 |
| Quest Menu | `RadiusUIQuestMenu.xml` | 77 |
| Xenotypes | `RadiusUIXenotypes.xml` | 131 |

Le mod s'active avec n'importe quel sous-ensemble de la suite : une traduction de mod absent est ignorée par le jeu. Le raccourci clavier de Colonist Bar (`DefInjected`) ne se charge que si Colonist Bar ou son fork Colonist Bar Plus est actif (`LoadFolders.xml`).

## Ce qui n'est pas traduit

- **Radius UI - Inspector Plus** a déjà son français.
- Les textes écrits directement dans le code d'un mod (par exemple l'infobulle des sous-menus et les boutons de la carte de survol de Colonist Bar, ou « no active conditions » dans la chronologie de Health Tab) : un mod de traduction ne peut pas les atteindre. Colonist Bar Plus, le fork de Colonist Bar, les affiche en français.
- Les libellés que le mod place dans une case de largeur fixe gardent une traduction courte : « Now » de Health Tab devient « Auj. », car « Maintenant » déborde sur le texte voisin. De même, l'étiquette « Drafted » sous le portrait dans Colonist Bar devient « Mobil. », car « Mobilisé » est coupé.

## Vocabulaire

Les termes de jeu suivent la traduction française officielle (dépôt `RimWorld-fr`) : mobiliser, colon, crise de nerfs, idéoligion, éléments marquants, plaisir, bonne entente, console de com…

## Règle avec les forks

Une même clé traduite par deux mods est refusée la seconde fois (« Duplicate keyed translation key »). Ce mod traduit les clés d'origine des mods d'astryl. Un fork (Inspector Plus, Colonist Bar Plus) ne traduit dans son propre dossier `French` que les clés qu'il ajoute.

## Vérifier

```sh
python3 tools/check_translations.py
```

Pour chaque mod, le script compare le français à l'anglais des copies locales (`Rimworld-mods/<mod>/Languages/English/Keyed`) : XML valide, mêmes clés, mêmes variables et balises, mêmes `\n`, aucune valeur restée en anglais (sauf la liste `EXCEPTIONS`). Quand un mod d'astryl est mis à jour, recopier sa nouvelle version depuis le Workshop puis relancer le script : il signale les clés ajoutées ou retirées.

`deploy.sh` lance le script puis publie le mod dans le dossier `Mods` du jeu (sans `docs/` ni `tools/`).

## Licence

MIT, voir `LICENSE`. Les textes source sont d'astryl (MIT).
