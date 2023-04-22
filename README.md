Introduction
------------

This repository contains basic example of usage PageObject
pattern with Selenium and Python (PyTest + Selenium).


Files
-----

[conftest.py](conftest.py) contains general fixtures, settings and plugins for tests.

[pages/base.py](pages/base.py) contains PageObject pattern implementation for Python.

[pages/page.py](pages/elements.py) contains helper class to working with web elements on web pages.

[pages/locators.py](pages/locators.py)contains web elements locators.

[tests/tests_yandex_page.py](tests/tests_yandex_page.py) contains searching test and images test for yandex page(https://ya.ru/)


How To Run Tests
----------------

1) Clone the repository:

    ```bash
    git clone https://github.com/EvgeniyPrivalov1986/tests_yandex_page.git
    ```

2) Install all requirements:

    ```bash
    pip install -r requirements.txt
    ```

3) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

4) Run tests:

    ```bash
    pytest tests_yandex_page.py 
    ```