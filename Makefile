init:
	pip install -r requirements-dev.txt
unit:
	python -m pytest tests/unit/ -s
