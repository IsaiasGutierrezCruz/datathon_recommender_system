SHELL=/bin/bash


install:
	@[ ! -d .venv ] && python3 -m venv .venv ||:;
	@( \
		source .venv/bin/activate; \
		pip install -r requirements-dev.txt; \
		pip install -r requirements.txt; \
	)