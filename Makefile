lint:
	rumdl check .

lint-fix:
	rumdl fmt .

check-links:
	python3 scripts/check-relative-links.py
