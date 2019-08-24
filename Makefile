test: lint doctest unittest

realtest: doctest realunittest

# Because there's a dir named "docs", we need
# a PHONY here to force run this target
.PHONY: docs
docs:
	cd docs && make autobuild

unittest:
	poetry run python -m unittest

# Test without using HTTP cache
realunittest:
	IGNORE_VCR=1 poetry run python -m unittest

doctest:
	cd docs && make doctest

lint:
	poetry run flake8
	poetry run black --check **/*.py
	poetry run isort --check-only

publish:
	poetry publish --build

clean:
	rm -rf dist
	cd docs && make clean
