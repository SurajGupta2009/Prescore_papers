# Prescore Papers — vault checks
#
#   make check      validate every figure block and every plugin claim (what CI runs)
#   make figures    alias for check
#   make plugins    plugin ID / mobile-support audit only
#   make prose      list draft wording left in the solution bodies (see docs/OPEN-ITEMS.md)
#   make coverage   which questions are missing / answer-only, per paper
#   make stats      how many of each figure block type each note has

PY ?= python3

.PHONY: help check figures plugins prose coverage stats

help:
	@echo "make check    validate figures + plugin IDs"
	@echo "make figures  validate the tikz/desmos/smiles/math blocks"
	@echo "make plugins  validate plugin IDs and mobile support"
	@echo "make prose    list scratch-pad wording left in the solutions"
	@echo "make coverage which questions are missing or answer-only"
	@echo "make stats    count figure blocks per note"

check: figures plugins

figures:
	$(PY) tools/check_figures.py

plugins:
	$(PY) tools/check_plugin_ids.py

prose:
	$(PY) tools/check_prose.py

coverage:
	$(PY) tools/check_coverage.py

stats:
	$(PY) tools/check_figures.py --quiet --stats
