install:
	pip install --upgrade pip && pip install -r requirements.txt
format:
	black gpt3datagen/gpt3datafaker/*.py
run:
	python main.py
lint:
	pylint --disable=R,C main.py
test:
	pytest -vv --cov=main.py tests/test_*.py
dist:
	python setup.py sdist bdist_wheel
clean:
	rm -rf dist build gpt3datagen.egg-info
commit:
	git add . && git  commit -m "first commit" && git  push -u origin main
pre-commit:
	pre-commit run --all-files
release:
	rm -rf build dist
	python setup.py sdist bdist_wheel
	twine upload dist/*
