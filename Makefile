.PHONY: test lint clean
test:
	python -m pytest || true
lint:
	python -m flake8 . || true
clean:
	rm -rf __pycache__ *.pyc .pytest_cache