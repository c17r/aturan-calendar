.PHONY: readme

init:
	pip install -U pipenv
	pipenv install --dev

update:
	pipenv update --dev

flake:
	pipenv run flake8

test: flake
	pipenv run py.test

coverage: flake
	pipenv run py.test --cov-report term-missing:skip-covered --cov=.

tox:
	pipenv run tox

readme:
	pipenv run python -c 'from src import aturan_calendar as cal; from scripts.make_readme import write_doc; write_doc(cal, "README.rst")'

upload: readme
	pipenv run ./setup.py upload

test-upload: readme
	pipenv run ./setup.py test_upload
