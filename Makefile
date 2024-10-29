install:
	poetry install

test-cov-l:
	poetry run pytest --cov=validator

test-coverage:
	poetry run pytest --cov=validator --cov-report xml
