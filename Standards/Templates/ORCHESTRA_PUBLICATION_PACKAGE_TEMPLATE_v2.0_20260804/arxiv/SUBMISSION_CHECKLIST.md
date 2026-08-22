# arXiv Submission Checklist

- [ ] Build `arxiv-source.zip` with `tools/build_arxiv_bundle.py`.
- [ ] Extract the ZIP into a clean directory.
- [ ] Compile twice with the documented engine.
- [ ] Confirm the output matches the reviewed `paper.pdf` in content and page count.
- [ ] Include only files needed to compile the manuscript.
- [ ] Remove build logs, temporary files, Git metadata, hidden files, private notes, credentials, and unrelated research artifacts.
- [ ] Inspect source comments for private or obsolete material.
- [ ] Confirm every included figure is referenced by the paper.
- [ ] Confirm title, authors, date, DOI, license, and version match the release metadata.
