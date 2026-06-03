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

| File | Description |
|------|-------------|
| `āsava-pali-to-en.md` | Pāli term → English renderings with co-occurrence frequency |
| `āsava-en-to-pali.md` | English term → Pāli source terms with co-occurrence frequency |

## Term cluster tested

**āsava** (lit. "outflow") and its morphological family: *sāsava*, *anāsava*, *kāmāsava*, *bhavāsava*, *diṭṭhāsava*, *avijjāsava*, *āsavasampayutta*, *āsavavippayutta*, *āsavānaṃ*.

The cluster is rendered inconsistently across the translation — primarily as **taint** and **canker**, with **influx**, **defilement**, and **defiled** appearing in specific contexts. A good extraction should recover all five English terms and their differential distribution across Pāli forms.

## Method

Co-occurrence counts are per verse (segment pair). A verse counts once per Pāli form / English term pair regardless of how many times each appears within it. Frequencies reflect verse-level alignment across 1928 parallel segments.
