default: format

format:
	black examples


run:
	uvicorn examples.main:app --reload --host 0.0.0.0

test:
	pytest ./tests


.PHONY: default run