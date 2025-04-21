@echo off
:: Navigate to the project directory
cd /d "%~dp0"

:: Run tests and generate HTML report
pytest --html=Reports/report.html --self-contained-html

:: Uncomment this line to generate Allure reports (requires Allure installed)
:: pytest --alluredir=Reports/allure-results
:: allure serve Reports/allure-results

pause
