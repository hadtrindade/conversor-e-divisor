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
	pip install -e .['dev'] --no-cache

install:
	pip install .

install-dev:
	python -m venv .venv && source .venv/bin/activate && pip3 install -e .['dev']

compile-ui:
	pyside2-uic ui/ui_cd.ui -o conversor_divisor/ui.py
	pyside2-rcc ui/resources_cd.qrc -o conversor_divisor/resources.py

start:
	conversor-divisor

lint:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format:
	isort --recursive conversor_divisor
	blue conversor_divisor

test:
	pytest tests/ -v --cov=conversor_divisor

build:
	@python setup.py sdist bdist_wheel

publish:
	@twine upload dist/*