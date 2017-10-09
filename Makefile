.PHONY: readme

init:
	@pip install -U pipenv
	@pipenv install --dev

update:
	@pipenv update --dev

flake:
	@pipenv run flake8

test: flake
	@pipenv run py.test

coverage: flake
	@pipenv run py.test --cov-report term-missing:skip-covered --cov=.

readme:
	@pipenv run python -c 'from src import aturan_calendar as cal; from scripts.make_readme import write_doc; write_doc(cal, "README.rst")'

tox: readme
	@pipenv run tox --workdir ~/.cache/tox

upload: readme
	@pipenv run ./setup.py upload

test-upload: readme
	@pipenv run ./setup.py test_upload

clean:
	@find -E . -regex ".*\.py[cod]" -delete
	@find -E . -type d -name "__pycache__" -delete
	@find -E . -path "*.egg-info*" -delete
	@[ -d dist ] && rm -r dist/ || true
	@[ -f README.rst ] && rm README.rst || true
	@[ -f .coverage ] && rm .coverage || true
