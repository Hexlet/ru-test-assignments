clean-pyc:
	find . -name "*.pyc" -delete

run: clean-pyc
	uvicorn main:app --port=8000 --reload