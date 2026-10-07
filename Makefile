# Prescore Papers — vault checks
#
#   make check      validate every figure block and every plugin claim (what CI runs)
#   make figures    alias for check
#   make plugins    plugin ID / mobile-support audit only
#   make stats      how many of each figure block type each note has

PY ?= python3

.PHONY: help check figures plugins stats

help:
	@echo "make check    validate figures + plugin IDs"
	@echo "make figures  validate the tikz/desmos/smiles/math blocks"
	@echo "make plugins  validate plugin IDs and mobile support"
	@echo "make stats    count figure blocks per note"

check: figures plugins

figures:
	$(PY) tools/check_figures.py

plugins:
	$(PY) tools/check_plugin_ids.py

stats:
	$(PY) tools/check_figures.py --quiet --stats
