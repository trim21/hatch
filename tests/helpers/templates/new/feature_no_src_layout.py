from hatch.template import File
from hatch.utils.fs import Path

from ..licenses import MIT


def get_files(**kwargs):
    description = kwargs.get('description', '')

    return [
        File(
            Path('LICENSE.txt'),
            MIT.replace('<year>', f"{kwargs['year']}-present", 1).replace(
                '<copyright holders>', f"{kwargs['author']} <{kwargs['email']}>", 1
            ),
        ),
        File(
            Path(kwargs['package_name'], '__init__.py'),
            f"""\
# SPDX-FileCopyrightText: {kwargs['year']}-present {kwargs['author']} <{kwargs['email']}>
#
# SPDX-License-Identifier: MIT
""",
        ),
        File(
            Path(kwargs['package_name'], '__about__.py'),
            f"""\
# SPDX-FileCopyrightText: {kwargs['year']}-present {kwargs['author']} <{kwargs['email']}>
#
# SPDX-License-Identifier: MIT
__version__ = "0.0.1"
""",
        ),
        File(
            Path('tests', '__init__.py'),
            f"""\
# SPDX-FileCopyrightText: {kwargs['year']}-present {kwargs['author']} <{kwargs['email']}>
#
# SPDX-License-Identifier: MIT
""",
        ),
        File(
            Path('README.md'),
            f"""\
# {kwargs['project_name']}

[![PyPI - Version](https://img.shields.io/pypi/v/{kwargs['project_name_normalized']}.svg)](https://pypi.org/project/{kwargs['project_name_normalized']})
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{kwargs['project_name_normalized']}.svg)](https://pypi.org/project/{kwargs['project_name_normalized']})

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install {kwargs['project_name_normalized']}
```

## License

`{kwargs['project_name_normalized']}` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
""",  # noqa: E501
        ),
        File(
            Path('pyproject.toml'),
            f"""\
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "{kwargs['project_name_normalized']}"
dynamic = ["version"]
description = '{description}'
readme = "README.md"
requires-python = ">=3.8"
license = "MIT"
keywords = []
authors = [
  {{ name = "{kwargs['author']}", email = "{kwargs['email']}" }},
]
classifiers = [
  "Development Status :: 4 - Beta",
  "Programming Language :: Python",
  "Programming Language :: Python :: 3.8",
  "Programming Language :: Python :: 3.9",
  "Programming Language :: Python :: 3.10",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: 3.12",
  "Programming Language :: Python :: Implementation :: CPython",
  "Programming Language :: Python :: Implementation :: PyPy",
]
dependencies = []

[project.urls]
Documentation = "https://github.com/{kwargs['author']}/{kwargs['project_name_normalized']}#readme"
Issues = "https://github.com/{kwargs['author']}/{kwargs['project_name_normalized']}/issues"
Source = "https://github.com/{kwargs['author']}/{kwargs['project_name_normalized']}"

[tool.hatch.version]
path = "{kwargs['package_name']}/__about__.py"

[tool.hatch.envs.types]
extra-dependencies = [
  "mypy>=1.0.0",
]
[tool.hatch.envs.types.scripts]
check = "mypy --install-types --non-interactive {{args:{kwargs['package_name']} tests}}"

[tool.coverage.run]
source_pkgs = ["{kwargs['package_name']}", "tests"]
branch = true
parallel = true
omit = [
  "{kwargs['package_name']}/__about__.py",
]

[tool.coverage.paths]
{kwargs['package_name']} = ["{kwargs['package_name']}", "*/{kwargs['project_name_normalized']}/{kwargs['package_name']}"]
tests = ["tests", "*/{kwargs['project_name_normalized']}/tests"]

[tool.coverage.report]
exclude_lines = [
  "no cov",
  "if __name__ == .__main__.:",
  "if TYPE_CHECKING:",
]
""",  # noqa: E501
        ),
    ]
