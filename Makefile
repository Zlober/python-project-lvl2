install:
	poetry install
Gendiff:
	poetry run Gendiff
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest --cov
tests:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=. --cov-report xml