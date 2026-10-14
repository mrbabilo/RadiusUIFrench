#!/usr/bin/env python3
"""Check the French files of this mod against the English files of the Radius UI mods.

For each mod: the French file parses, has exactly the English keys, keeps every placeholder ({0}, {NAME}),
tag (<color=...>) and literal \\n of the English value, and no value is still the English text (except the
EXCEPTIONS below). A mod with no French file yet is reported as "à faire" and is not an error.

English sources: the local copies of the mods, next to this mod (Rimworld-mods/<folder>/Languages/English/Keyed).
Usage: python3 tools/check_translations.py [--source <Rimworld-mods folder>]
Exit code 1 when a check fails.
"""
import argparse
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent

# (mod folder, Keyed file name), smallest first like the plan.
MODS = [
    ("RadiusUIEverywhere", "RadiusUIEverywhere.xml"),
    ("RadiusUIFramework", "RadiusUIFramework.xml"),
    ("RadiusUIQuestMenu", "RadiusUIQuestMenu.xml"),
    ("RadiusUIIdeology", "RadiusUIIdeology.xml"),
    ("RadiusUINeedsTab", "RadiusUINeedsTab.xml"),
    ("RadiusUIXenotypes", "RadiusUIXenotypes.xml"),
    ("RadiusUIFactionMenu", "RadiusUIFactionMenu.xml"),
    ("RadiusUIHealthTab", "RadiusUIHealthTab.xml"),
    ("RadiusUIColonistBar", "RadiusColonistBar.xml"),
    ("RadiusUIMissionControl", "RadiusUIMissionControl.xml"),
]

# Values allowed to stay as in English: proper names, symbols, words French writes the same way.
EXCEPTIONS = {
    "Radius UI", "Radius", "OK", "HP", "XP", "DPS", "Mission Control", "Command Center",
    "Menu", "Stock", "Auto", "Radius UI Framework", "violet", "rose", "Structure", "Styles", "Rites", "Hostile", "Radius UI - Ideology", "factions", "Factions",
}

DEF_INJECTED = HERE / "ColonistBar/Languages/French/DefInjected/KeyBindingDef/KeyBindings.xml"
DEF_KEYS = {"RCB_FollowCam.label"}

PLACEHOLDER = re.compile(r"\{[^{}]+\}")
TAG = re.compile(r"<[^<>]+>")


def load(path):
    root = ET.parse(path).getroot()
    values = {}
    dupes = []
    for el in root:
        if not isinstance(el.tag, str):
            continue
        if el.tag in values:
            dupes.append(el.tag)
        values[el.tag] = el.text or ""
    return values, dupes


def has_letters(text):
    return any(c.isalpha() for c in text)


def check_mod(source, folder, name):
    en_path = source / folder / "Languages/English/Keyed" / name
    fr_path = HERE / "Languages/French/Keyed" / name
    if not en_path.exists():
        return "absent", [f"fichier anglais introuvable : {en_path}"]
    if not fr_path.exists():
        return "à faire", []
    errors = []
    try:
        en, _ = load(en_path)
        fr, dupes = load(fr_path)
    except ET.ParseError as e:
        return "erreur", [f"XML invalide : {e}"]
    for k in dupes:
        errors.append(f"clé en double : {k}")
    for k in sorted(set(en) - set(fr)):
        errors.append(f"clé manquante : {k}")
    for k in sorted(set(fr) - set(en)):
        errors.append(f"clé en trop : {k}")
    for k in sorted(set(en) & set(fr)):
        e, f = en[k], fr[k]
        if Counter(PLACEHOLDER.findall(e)) != Counter(PLACEHOLDER.findall(f)):
            errors.append(f"variables différentes : {k} : {PLACEHOLDER.findall(e)} / {PLACEHOLDER.findall(f)}")
        if Counter(TAG.findall(e)) != Counter(TAG.findall(f)):
            errors.append(f"balises différentes : {k}")
        if e.count("\\n") != f.count("\\n"):
            errors.append(f"nombre de \\n différent : {k}")
        if not f.strip() and e.strip():
            errors.append(f"valeur vide : {k}")
        if f == e and has_letters(e) and PLACEHOLDER.sub("", e).strip() not in EXCEPTIONS:
            errors.append(f"non traduit : {k} = {e!r}")
    return ("OK" if not errors else "erreur"), errors


def check_def_injected():
    if not DEF_INJECTED.exists():
        return "à faire", []
    try:
        values, _ = load(DEF_INJECTED)
    except ET.ParseError as e:
        return "erreur", [f"XML invalide : {e}"]
    errors = [f"clé manquante : {k}" for k in sorted(DEF_KEYS - set(values))]
    errors += [f"clé en trop : {k}" for k in sorted(set(values) - DEF_KEYS)]
    return ("OK" if not errors else "erreur"), errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=HERE.parent)
    args = parser.parse_args()
    failed = False
    results = [(f"{folder} ({name})", *check_mod(args.source, folder, name)) for folder, name in MODS]
    results.append(("DefInjected KeyBindings (Colonist Bar)", *check_def_injected()))
    for label, status, errors in results:
        print(f"{status:8} {label}")
        for err in errors:
            print(f"         - {err}")
        failed |= status in ("erreur", "absent")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
