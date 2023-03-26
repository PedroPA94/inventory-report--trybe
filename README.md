# Welcome to the Inventory Report project!

This project is an inventory report generator. It receives data from CSV, JSON, or XML files and generates a report on this data in Python using Object-Oriented Programming (OOP) concepts. It outputs two versions of the report: a simple and a complete version. 

I've also implemented some tests in this project using the Pytest library.

This was my first project using OOP with Python. At the time, I was studying Desing Patterns and one of the objectives of this project was to practice the use of the Strategy and Iterator patterns. It was definetely a challenge to use both OOP and Design Patterns, but I enjoyed the journey! It was also challenging to work with files, especially XML, which is a type of data I'm not used with.

This project was developed while studying Computer Science [@betrybe](https://github.com/betrybe). I got approval on 100% of this project's requirements.

The files I worked on are in the ```inventory_report/importer```, ```inventory_report/inventory``` (except _products.py_), ```inventory_report/reports``` (except _colored_report.py_) folders, and also the following files: `main.py`, `test_product.py`, `test_product_report.py` and `test_report_decorator.py`.

## Main languages and tools used

- Python
- Pytest
- Design Patterns
- Venv

## Installation

- Clone the repository
- Create a virtual environment with `python3 -m venv .venv` and start it with `source .venv/bin/activate`
- Install the dependencies with `python3 -m pip install -r dev-requirements.txt`
- Run the project with `inventory_report argument1 argument2`, where argument1 is the path to a csv, json or xml file, and argument2 is the type of report (`simples` or `completo`). You can use the files available at `inventory_report/data`
- Run the tests with `python3 -m pytest` or `python3 -m pytest tests/filename.py`
