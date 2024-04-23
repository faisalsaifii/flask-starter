PORT=5000

.PHONY: run
run:
	pip install -r requirements.txt && FLASK_APP=app.py python3 -m flask --debug run -p $(PORT)