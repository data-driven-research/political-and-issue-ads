TEMPLATE
==============================

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [Usage](#usage)
+ [Contributing](.github/CONTRIBUTING.md)

## About <a name = "about"></a>
Write about 1-2 paragraphs describing the purpose of your project.

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites & installing

After cloning the repository, get a development env running:

```bash
$ python -m venv env

# Windows
$ env/Scripts/activate
# Linux
$ source env/bin/activate

(env)$ python -m pip install -U pip setuptools wheel
(env)$ python -m pip install -r requirements.txt 
```

## Usage <a name = "usage"></a>

*Reproducing analysis and figures:*
run jupyter notebooks from the notebooks folder in ascending order.

*Using local package:*
```python
import src.utils
from src import make_dataset


if __name__ == "__main__":
    make_dataset.fetch()
    make_dataset.transform()
    src.utils.normalize()
```
