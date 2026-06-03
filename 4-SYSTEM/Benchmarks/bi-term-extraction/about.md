---
title: Bi-term Extraction Benchmark
type: benchmark
skill: pali-biterm-extraction
---

# Bi-term Extraction Benchmark

Tests the ability to extract aligned translation term pairs from parallel Pāli–English texts and produce frequency-weighted mappings.

## Source files

| File | Description |
|------|-------------|
| `pi-dhammasangani.md` | Pāli root text — Dhammasaṅgaṇī (tipitaka.org Mūla / CSCD), 1928 verses |
| `en-dhammasangani-ai.md` | AI-assisted English translation, segment-aligned to the Pāli, 1928 verses |

## Expected outputs

One `.md` file per Pāli term, e.g. `āsava.md`, `dhamma.md`. Each file contains, in order:

1. **Senses in text** — numbered sense labels reflecting genuine lexical polysemy (not morphological variation), each with a short Pāli example phrase and its English translation from the corpus
2. **Per-sense translation frequency tables** — one table per sense, English renderings ranked by verse-level co-occurrence count
3. **Declensions in the text** — one morphological form per line, each with a short Pāli example phrase and its English translation

| File | Description |
|------|-------------|
| `āsava.md` | āsava cluster: 1 sense, 10 declensions, English frequency table |
| `dhamma.md` | dhamma cluster: 2 senses, 5 declensions, English frequency tables |

## Term cluster tested

**āsava** (lit. "outflow") and its morphological family: *sāsava*, *anāsava*, *kāmāsava*, *bhavāsava*, *diṭṭhāsava*, *avijjāsava*, *āsavasampayutta*, *āsavavippayutta*, *āsavānaṃ*.

The cluster is rendered inconsistently across the translation — primarily as **taint** and **canker**, with **influx**, **defilement**, and **defiled** appearing in specific contexts. A good extraction should recover all five English terms and their differential distribution across Pāli forms.

## Method

Co-occurrence counts are per verse (segment pair). A verse counts once per Pāli form / English term pair regardless of how many times each appears within it. Frequencies reflect verse-level alignment across 1928 parallel segments.
