.PHONY: readme

init:
	pip install -r requirements.lock

test:
	py.test -v test_aturan_calendar.py

coverage:
	py.test --verbose --cov-report term-missing --cov=aturan_calendar test_aturan_calendar.py

readme:
	python -c 'import aturan_calendar as cal; from scripts.make_readme import write_doc; write_doc(cal, "README")'