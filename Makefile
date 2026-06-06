# Build-Targets:
#   make chapter/<buch>/<N>   einzelnes Kapitel als PDF (Smoke-Test)
#   make book/<buch>          ganzes Buch als PDF + EPUB (nach build/)
#   make release/<buch>       wie book/, Artefakte zusätzlich nach dist/ (committet)
#   make site                 komplette GitHub-Pages-Site nach _site/
#   make clean/<buch>

PY     ?= .venv/bin/python
PANDOC ?= pandoc

chapter/%:
	$(eval BOOK := $(word 1,$(subst /, ,$*)))
	$(eval NUM  := $(word 2,$(subst /, ,$*)))
	$(eval PAD  := $(shell printf '%02d' $(NUM)))
	$(PY) scripts/build_chapter.py $(BOOK) $(NUM)
	$(PANDOC) -d shared/pandoc/pdf.yaml --metadata-file=books/$(BOOK)/book.yaml \
	  books/$(BOOK)/build/rendered/$(PAD)-*.md \
	  -o books/$(BOOK)/build/kapitel-$(PAD).pdf
	@echo "→ books/$(BOOK)/build/kapitel-$(PAD).pdf"

book/%:
	$(PY) scripts/build_chapter.py $* --all
	$(PANDOC) -d shared/pandoc/pdf.yaml --metadata-file=books/$*/book.yaml \
	  books/$*/build/rendered/*.md \
	  -o books/$*/build/$*.pdf
	$(PANDOC) -d shared/pandoc/epub.yaml --metadata-file=books/$*/book.yaml \
	  books/$*/build/rendered/*.md \
	  -o books/$*/build/$*.epub
	@echo "→ books/$*/build/$*.pdf + .epub"

release/%: book/%
	mkdir -p books/$*/dist
	cp books/$*/build/$*.pdf books/$*/build/$*.epub books/$*/dist/
	@echo "→ books/$*/dist/ (committen nicht vergessen)"

site:
	$(PY) scripts/build_site.py

clean/%:
	rm -rf books/$*/build

.PHONY: site chapter/% book/% release/% clean/%
