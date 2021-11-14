FILTERS = --lua-filter=$(shell pwd)/lua/scholarly-metadata.lua \
	--lua-filter=$(shell pwd)/lua/author-info-blocks.lua \
	--lua-filter=$(shell pwd)/lua/diagram-generator.lua \
	--filter pandoc-crossref --citeproc

pdf:
	pandoc README.md -o README.pdf --pdf-engine lualatex $(FILTERS)
