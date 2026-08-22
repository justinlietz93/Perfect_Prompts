# Paper Source

Do not run `pdflatex` directly from this directory when the manuscript uses top-level publication figures. Use:

```bash
python tools/compile_paper.py .
```

The tool stages only declared source and figure inputs, compiles from clean bytes, and writes `paper.pdf` at the publication root.

`ARXIV_FIGURES.txt` is the explicit list of top-level figure files copied into arXiv source. One relative path per line; blank lines and `#` comments are allowed.
