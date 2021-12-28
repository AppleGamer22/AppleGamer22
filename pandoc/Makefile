FILTERS = -L $(shell pwd)/lua/diagram-generator.lua --filter pandoc-crossref --citeproc --template=$(shell pwd)/templates/template.tex --highlight tango

pdf:
	pandoc README.md -o README.pdf --pdf-engine lualatex $(FILTERS)

watch:
	while inotifywait -e close_write README.md; do $(MAKE) pdf; done