.PHONY: check build

build:
	python3 scripts/build.py
	python3 eval/detector.py --write
	python3 scripts/render_preview.py
	python3 scripts/package_skill.py

check:
	python3 scripts/validate_catalog.py
	python3 scripts/build.py --check
	python3 eval/detector.py --check
	python3 eval/test_detector.py
