# Build-Targets:
#   make chapter/<buch>/<N>   einzelnes Kapitel als PDF (Smoke-Test)
#   make book/<buch>          ganzes Buch als PDF + EPUB
#   make clean/<buch>

PY     := .venv/bin/python
PANDOC := pandoc -d shared/pandoc/defaults.yaml

chapter/%:
	$(eval BOOK := $(word 1,$(subst /, ,$*)))
	$(eval NUM  := $(word 2,$(subst /, ,$*)))
	$(eval PAD  := $(shell printf '%02d' $(NUM)))
	$(PY) scripts/build_chapter.py $(BOOK) $(NUM)
	$(PANDOC) --metadata-file=books/$(BOOK)/book.yaml \
	  books/$(BOOK)/build/rendered/$(PAD)-*.md \
	  -o books/$(BOOK)/build/kapitel-$(PAD).pdf
	@echo "→ books/$(BOOK)/build/kapitel-$(PAD).pdf"

book/%:
	$(PY) scripts/build_chapter.py $* --all
	$(PANDOC) --metadata-file=books/$*/book.yaml \
	  books/$*/build/rendered/*.md \
	  -o books/$*/build/$*.pdf
	$(PANDOC) --metadata-file=books/$*/book.yaml \
	  --css=shared/pandoc/epub.css \
	  books/$*/build/rendered/*.md \
	  -o books/$*/build/$*.epub
	@echo "→ books/$*/build/$*.pdf + .epub"

clean/%:
	rm -rf books/$*/build

.PHONY: chapter/% book/% clean/%
