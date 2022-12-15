============
zyft_backend
============






Take home challenge.



Features
--------

* TODO

Requirements
------------
beautifulsoup4==4.6.0

How to run
----------
make install

make run

How to run without make
-----------------------
pip3 install -r requirements.txt

python3 zyft_backend.py

Tests
-----
make test

alternatively

pytest

Assumptions
-----------
* Task 1: Wasn't 100 percent across xpath and the requirements but tried to make it work with my best judgement.
* Task 3: Solution assumes that the model numbers are not substrings of each other. If they are, we would need to add a check to make sure that the model number is not a substring of another model number.
* Task 3: Tuples are used as input instead of list, as they provide the same functionality as a list for the usecase, but are proved to perform faster.
* python3 is used for this project and python3 is assumed to be installed on the system.
* pip3 is used for this project and pip3 is assumed to be installed on the system.
* make is used for this project and make is assumed to be installed on the system.
* Tests are not implemented yet in the interest of time. But a test framework is setup and can be used to test the code.