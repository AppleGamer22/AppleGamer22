FILTERS = -L $(shell pwd)/lua/diagram-generator.lua --filter pandoc-crossref --citeproc --template=$(shell pwd)/templates/template.tex

pdf:
	pandoc README.md -o README.pdf --pdf-engine lualatex $(FILTERS)

watch:
	ls README.md | entr -p $(MAKE) pdf