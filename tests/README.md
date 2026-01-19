# Pure python project template

[![Python 3.14](https://img.shields.io/badge/python-3.14-green.svg)](https://www.python.org/downloads/release/python-3140/)
[![Code style: ruff](https://img.shields.io/badge/ruff-enabled-informational?logo=ruff)](https://astral.sh/ruff)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/manti-by/pdw/master/LICENSE)

## About

Author: Alexander Chaika <manti.by@gmail.com>

Source link: https://github.com/manti-by/coruscant/

## Setup python and uv

1. Install [UV tool](https://docs.astral.sh/uv/getting-started/installation/).

2. Clone sources, switch to working directory and setup environment:

    ```shell
    git clone https://github.com/manti-by/void.git
    cd coruscant/
    uv sync
    ```

3. Run a main script and pytests

    ```shell
    uv run main.py
    uv run pytest
    ```
