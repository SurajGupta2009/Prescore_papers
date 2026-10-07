# Prescore Papers — build helpers
#
#   make figures   build every figure from its source fence
#   make check     verify the committed SVGs match their sources (used by CI)
#   make restore   put the source fences back in place of the embeds
#   make prune     delete SVG files no note references any more
#   make install   install the Python deps for the figure pipeline

PY ?= python3

.PHONY: help figures check restore prune install clean

help:
	@echo "make figures   build figures from fences"
	@echo "make check     fail if a committed figure is stale"
	@echo "make restore   reinsert the source fences"
	@echo "make prune     delete unreferenced SVGs"
	@echo "make install   install python deps"

figures:
	$(PY) tools/render_figures.py

check:
	$(PY) tools/render_figures.py --check

restore:
	$(PY) tools/render_figures.py --restore

prune:
	$(PY) tools/render_figures.py --prune

install:
	$(PY) -m pip install -r tools/requirements.txt

clean:
	$(PY) tools/render_figures.py --restore --dry-run
