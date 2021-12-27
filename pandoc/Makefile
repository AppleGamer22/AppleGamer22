FILTERS = -L $(shell pwd)/lua/scholarly-metadata.lua \
	-L $(shell pwd)/lua/author-info-blocks.lua \
	-L $(shell pwd)/lua/diagram-generator.lua \
	--filter pandoc-crossref --citeproc --standalone

pdf:
	pandoc README.md -o README.pdf --pdf-engine lualatex $(FILTERS)

watch:
	ls README.md | entr -p $(MAKE) pdf