# Translation assets

Source language: Portuguese. Translation was authored by agents configured as GPT-6 Luna through the Codex subscription; no API or online translator was used.

- `scripts/translate_guide.py` contains the EN/ES text maps applied to `guia/en/index.html` and `guia/es/index.html`.
- `scripts/translate_course_landing.py` contains the course overview maps and the Portuguese README language selector addition.
- `scripts/translate_shared_ui.py` contains the translated strings for the course learning UI shared across five tracks, plus locale-specific browser-storage namespace handling.
- `scripts/build_locale_structure.py` adds language selectors and `hreflang` links to generated language copies.

These scripts document the applied, project-specific translations. They are not a general HTML translation engine; run them only after reviewing diffs against the current Portuguese source. Keep code, commands, paths, IDs, fixtures, numeric values, and product states protected from translation.

All 21 lessons now have EN/ES catalogs. See `../context/trilingual-translation.md` for coverage and validation.

## Rebuilding completed lessons locally

Catalogs in `translations/track-N-lesson-M.json` map a complete Portuguese text unit to `[English, Spanish]`. Apply a catalog with:

```sh
python3 i18n/scripts/apply_text_units.py --track 1 --lesson 1 --lang en
python3 i18n/scripts/apply_text_units.py --track 1 --lesson 1 --lang es
python3 i18n/scripts/check_translations.py --track 1
```

The renderer always reads the lesson from the Portuguese source, translates only complete text units and reader-facing attributes, and handles review cards with JSON parsing. It does not translate identifiers or run inference. Change the catalog, then rebuild; avoid manual fixes that would be lost on the next build.

After all pages are assembled, run `python3 i18n/scripts/finalize_languages.py` to normalize reciprocal language links and preserve the current hash/query when switching languages. This finalizer also adds the Portuguese selectors. All scripts in this folder run locally without API access.
