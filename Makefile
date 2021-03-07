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
	pip install -r requeriments.txt

install-dev:
	pip install -r requeriments-dev.txt
	pip install -e .
	mkdir FFmpeg
	mkdir MP4Box

compile-ui:
	pyside2-uic ui/ui_cd.ui -o ui_conversor_divisor/ui_cd.py
	pyside2-rcc ui/resources_cd.qrc -o ui_conversor_divisor/resources_cd_rc.py

compile:
	bash compile_linux.sh

start-app:
	python conversor_divisor/app.py

black:
	black -l 79 .