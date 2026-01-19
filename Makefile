run:
	uv run main.py

test:
	uv run pytest

check:
	git add .
	uv run pre-commit run

pip:
	uv sync

ci: pip check test
