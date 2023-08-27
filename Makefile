clean:
	find . -name \*.pyc -delete
	find . -name \*__pycache__ -delete
	find . -name \*~ -delete

install:
	pipenv install --dev

shell:
	pipenv shell

lint:
	flake8 main.py app/*

lint/fix:
	autopep8 --global-config .flake8 --in-place --aggressive --recursive .

test:
	python -m pytest ./tests -vv

run:
	python main.py

deploy: clean
	sh deploy.sh $(NAME)

