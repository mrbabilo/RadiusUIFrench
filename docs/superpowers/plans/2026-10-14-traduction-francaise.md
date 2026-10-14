# Radius UI - Traduction française — plan d'implémentation

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Un mod de traduction qui met en français les dix mods Radius UI d'astryl.

**Architecture:** Mod sans code : `About.xml`, `LoadFolders.xml`, un fichier `Languages/French/Keyed/<même nom que l'anglais>.xml` par mod, un `DefInjected` pour le raccourci `RCB_FollowCam` chargé seulement si Colonist Bar ou son fork est actif. Un script Python vérifie chaque fichier contre l'anglais.

**Tech Stack:** XML RimWorld (Keyed, DefInjected, LoadFolders), Python 3 (script de vérification), `xmllint`, `rsync`.

**Spec:** `RadiusUIFrench/docs/superpowers/specs/2026-10-14-traduction-francaise-design.md`

## Global Constraints

- packageId `mrbabilo.RadiusUI.FrenchTranslation`, nom « Radius UI - Traduction française », auteur mrbabilo, version 1.6, aucune `modDependencies`, `loadAfter` les dix packageId.
- Nom de chaque fichier français = nom du fichier anglais du mod.
- Variables `{…}`, balises, entités XML, `\n` intacts. Vocabulaire de `RimWorld-fr`.
- Jamais de clé ajoutée ou retirée par rapport à l'anglais.
- Sources anglaises : copies locales `Rimworld-mods/RadiusUI*/Languages/English/Keyed/*.xml`.

## Review Focus

1. Clé dont la valeur anglaise contient une variable nommée (`{NAME}`, `{0}`) : la même variable dans le français (script, contrôle 3).
2. Valeur anglaise avec balise `<color=…>` ou entité `&#8230;` : conservée (script, contrôle 3).
3. Libellé court de bouton ou d'onglet : traduction courte (relecture humaine, contrôle en jeu).
4. Mod Radius absent : aucune erreur (fichiers `Keyed` toujours chargés, `DefInjected` sous `IfModActive`).
5. Valeur restée en anglais par oubli : détectée (script, contrôle 4).

---

### Task 1 : Squelette et script de vérification

**Files:** `About/About.xml`, `LoadFolders.xml`, `LICENSE`, `.gitignore`, `deploy.sh`, `tools/check_translations.py`, `README.md`, `CHANGELOG.md`

- [ ] Écrire les fichiers du squelette (contenus dans la spec).
- [ ] Écrire `tools/check_translations.py` : pour chaque fichier anglais connu, contrôle XML, parité des clés, variables et balises, valeurs identiques à l'anglais (hors liste d'exceptions) ; code de sortie non nul en cas d'écart ; un fichier français absent est signalé « à faire » sans échec.
- [ ] Lancer le script : tous les mods « à faire », sortie 0.
- [ ] Commit.

### Tasks 2 à 11 : un mod par tâche

Ordre : Everywhere, Framework, Quest Menu, Ideology, Needs Tab, Xenotypes, Faction Menu, Health Tab, Colonist Bar (+ `ColonistBar/Languages/French/DefInjected/KeyBindingDef/KeyBindings.xml`), Mission Control.

Pour chaque mod :

- [ ] Lire le fichier anglais en entier.
- [ ] Chercher dans `RimWorld-fr` les termes de jeu qu'il emploie.
- [ ] Écrire le fichier français.
- [ ] Lancer le script : le mod passe « OK », sortie 0.
- [ ] Commit `fr: <mod>`.

### Task 12 : Publication

- [ ] `deploy.sh`, vérifier le dossier publié (10 fichiers `Keyed`, le `DefInjected`, pas de `docs/` ni `tools/`).
- [ ] README (mods couverts, règle des forks, limites), CHANGELOG 1.0.0.
- [ ] Commit. Contrôle en jeu par le joueur (spec, points 5 et 6).
