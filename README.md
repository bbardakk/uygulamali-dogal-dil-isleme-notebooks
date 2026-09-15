# Uygulamalı Doğal Dil İşleme — Notebooks

Companion Jupyter notebooks for **Applied Natural Language Processing — From Tokens to Agents**
(*Uygulamalı Doğal Dil İşleme — Token'lardan Ajanlara*).

- Book: <https://bbardakk.github.io/uygulamali-dogal-dil-isleme/> · source: [bbardakk/uygulamali-dogal-dil-isleme](https://github.com/bbardakk/uygulamali-dogal-dil-isleme)
- Slides: [bbardakk/uygulamali-dogal-dil-isleme-slides](https://github.com/bbardakk/uygulamali-dogal-dil-isleme-slides)

## Layout

The folders mirror the book repository, one folder per chapter, named with the chapter's own file slug:

| book | notebook |
|:--|:--|
| `en/chapters/01-why-nlp-now.qmd` | `en/chapters/01-why-nlp-now/01-why-nlp-now.ipynb` |
| `tr/chapters/01-neden-nlp.qmd` | `tr/chapters/01-neden-nlp/01-neden-nlp.ipynb` (Turkish notebooks: planned) |

A chapter folder may also hold small data files or helpers that only its notebook uses.
`python3 scripts/check-structure.py` checks every folder against the book's chapter list.

| chapter | English | Türkçe |
|:--|:--|:--|
| 01 Why NLP, Why Now | [notebook](en/chapters/01-why-nlp-now/01-why-nlp-now.ipynb) | — |

## Running

```bash
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -r requirements.txt
jupyter lab
```

Each notebook states the versions its numbers came from in its first cell. Cells that need a local
model server (`ollama`) are skipped cleanly when none is running.

## License

Code is MIT; the prose in the notebooks is CC BY 4.0, the same split as the book. Datasets keep their
own licences, which each notebook names where it loads them. See [LICENSE](LICENSE).
