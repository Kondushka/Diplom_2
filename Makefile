test:
	pytest

all: 
	rm -rf allure_results allure.log
	pytest
	nohup allure serve allure_results > allure.log &

one:
	rm -rf allure_results allure.log
	pytest $(file)
	nohup allure serve allure_results > allure.log &