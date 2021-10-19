DOCKER_RUN = docker run --rm -it -v ${PWD}:/app --env-file configs/.env.development -w /app --network=host python:3.8-alpine sh -c
REQUIREMENTS = pip install --upgrade pip -r requirements.txt

.PHONY: test

run:
	@${DOCKER_RUN} '${REQUIREMENTS} && python3 -m src.main'

test:
	@${DOCKER_RUN} '${REQUIREMENTS} && python3 -m unittest discover test "*Test.py"'