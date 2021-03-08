clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf *egg-info
	rm -rf *tox/
	rm -rf docs/_build
	pip3 install -e . --no-cache

install:
	pip install .

install-dev:
	pip install -r requirements-dev.txt
	pip install -e .
	mkdir FFmpeg
	mkdir MP4Box

compile-ui:
	pyside2-uic ui/ui_cd.ui -o conversor_divisor/ui_cd.py
	pyside2-rcc ui/resources_cd.qrc -o conversor_divisor/resources_cd_rc.py

start-app:
	conversor_divisor

black:
	black -l 79 .

test:
	pytest tests/ -v --cov=conversor_divisor