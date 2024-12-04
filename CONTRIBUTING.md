# Contributing

Contributions are welcome, and they are greatly appreciated! Every little
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs to [our issue page][gh-issues]. If you are reporting a bug, please
include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
"enhancement" and "help wanted" is open to whoever wants to implement it.

### Write Documentation

The ZDS slide set material could always use more documentation and content,
whether as part of the official documentation, in [reStructuredText][rst-doc],
or even on the web in blog posts, articles, and such.

Further readings for you as new contributor:

- [reStructuredText User Documentation][rst-doc]
- [reStructuredText Primer by Sphinx][rst-primer]
- [Sphinx User Documentation][sphinx-doc]
- [Sphinx Primer by Li-Pro.Net][sphinx-primer]

### Submit Feedback

The best way to send feedback [our issue page][gh-issues] on GitHub. If you
are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions are
  welcome 😊

## System Requirements

The ideal development environment is a Linux based system. A current Ubuntu LTS,
i.e. 24.04, 22.04 or 20.04, is recommended and should be used. Windows 10 or 11
as well as MacOS are conceivable but are not preferred or recommended. Most
notations are written in such a way that these systems could also be used in
theory.

### How to install newer Python 3 in Ubuntu LTS

Lates Python releases are easy to install in all current Ubuntu releases
by using the popular [Deadsnakes PPA][deadsnakes-ppa]:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
```

See also:
[How to install Python 3.10 in Ubuntu][ubhb-202101-install-py310-ubuntu], or
[How to install Python 3.12 in Ubuntu][ubhb-202305-install-py312-ubuntu].

### System packages for Python 3

The pivot point as "programmed documentation" is a fully functioning Python 3
runtime environment. For later setup of a local Python 3 Virtual Environment
the following system packages are mandatory and must be installed:

```bash
$ sudo apt install --yes $(cat dpkg-tools-reqirements.txt)
$ sudo apt install --yes $(cat dpkg-python3-reqirements.txt)
```

… or as alternative without an already checked out local repository:

```bash
$ sudo apt install --yes \
       $(git archive \
             --remote=ssh://git@github.com:tiacsys/bridle-tutorials.git \
             --format=tar main dpkg-tools-reqirements.txt 2>/dev/null | tar xO)
$ sudo apt install --yes \
       $(git archive \
             --remote=ssh://git@github.com:tiacsys/bridle-tutorials.git \
             --format=tar main dpkg-python3-reqirements.txt 2>/dev/null | tar xO)
```

### System packages for spell checking

If you consider running Sphinx's spell checking extension, the following
system packages must be installed:

```bash
$ sudo apt install --yes $(cat dpkg-spelling-reqirements.txt)
```

… or as alternative without an already checked out local repository:

```bash
$ sudo apt install --yes \
       $(git archive \
             --remote=ssh://git@github.com:tiacsys/bridle-tutorials.git \
             --format=tar main dpkg-spelling-reqirements.txt 2>/dev/null | tar xO)
```

## Get Started!

Ready to contribute? Here's how to set yourself up for local development.

1. Fork the repo on GitHub. Clone locally and change into the folder.

1. Create and activate a project specific
   [Python 3 virtual environment](https://docs.python.org/3/library/venv.html):

   ```bash
   $ python3.10 -m venv --prompt="$(basename $(pwd))[$(python3.10 --version)]" \
                     --clear --copies .venv
   $ source .venv/bin/activate

   $ pip3.10 install --upgrade pip setuptools
   $ pip3.10 install --upgrade poetry
   ```

1. Install the project dependencies with [Poetry](https://python-poetry.org):

   ```bash
   $ poetry install --no-root
   ```

1. Create a branch for local development:

   ```bash
   $ git checkout -b name-of-your-bugfix-or-feature
   ```

   Now you can make your changes locally.

1. When you're done making changes, check that your changes pass our tests:

   ```bash
   $ ### NOT YET ### poetry run pytest
   $ ### NOT YET ### make doctest
   $ ### NOT YET ### make coverage ; cat docs/build/coverage/python.txt
   $ make -C cytron-maker-rp2040 spelling
   $ make -C cytron-maker-rp2040 linkcheck
   ```

1. Linting is done through [pre-commit](https://pre-commit.com). Provided you
   have the tool installed globally, you can run them all as one-off:

   ```bash
   $ pre-commit run -a
   ```

   Or better, install the hooks once and have them run automatically each time
   you commit:

   ```bash
   $ pre-commit install --hook-type pre-commit --hook-type commit-msg
   ```

1. Optional run tests on documentation and build them offline:

   ```bash
   $ make -C cytron-maker-rp2040 html
   $ python3.10 -m http.server -d cytron-maker-rp2040/build/html 8000
   $ xdg-open http://localhost:8000/
   ```

1. Optional run tests on the PDF manual and build them offline:

   ```
   $ make -C cytron-maker-rp2040 rinoh
   $ xdg-open cytron-maker-rp2040/build/rinoh/bridle-tutorial.pdf
   ```

1. Commit your changes and push your branch to GitHub:

   ```bash
   $ git add .
   $ git commit -m "feat(something): your detailed description of your changes"
   $ git push origin name-of-your-bugfix-or-feature
   ```

   Note: the commit message should follow
   [the conventional commits](https://www.conventionalcommits.org). **NOT
   YET** ~~We run
   [`commitlint` on CI](https://github.com/wagoid/commitlint-github-action) to
   validate it, and if you have installed pre-commit hooks at the previous
   step, the message will be checked at commit time.~~ **NOT YET**

1. Submit a pull request through the GitHub website or using the GitHub CLI
   (if you have it installed):

   ```bash
   $ gh pr create --fill
   ```

## Pull Request Guidelines

We like to have the pull request open as soon as possible, that's a great
place to discuss any piece of work, even unfinished. You can use draft pull
request if it's still a work in progress. Here are a few guidelines to follow:

1. Include tests for feature or bug fixes.
1. Update the documentation for significant features.
1. Ensure tests are passing on CI.

## Tips

To run a subset of tests:

```bash
$ ### NOT YET ### make pytest tests
```

## Making a new release

The deployment should be automated and can be triggered from the Semantic
Release workflow in GitHub. The next version will be based on
[the commit logs](https://python-semantic-release.readthedocs.io/en/latest/commit-log-parsing.html#commit-log-parsing).
**NOT YET** ~~This is done by
[python-semantic-release](https://python-semantic-release.readthedocs.io/en/latest/index.html)
via a GitHub action.~~ **NOT YET**

[deadsnakes-ppa]: https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa
[gh-issues]: https://github.com/tiacsys/bridle-tutorials/issues
[rst-doc]: https://docutils.sourceforge.io/rst.html
[rst-primer]: https://www.sphinx-doc.org/en/master/usage/restructuredtext
[sphinx-doc]: https://www.sphinx-doc.org/
[sphinx-primer]: https://lpn-doc-sphinx-primer.readthedocs.io/
[ubhb-202101-install-py310-ubuntu]: https://ubuntuhandbook.org/index.php/2021/01/install-python-3-10-alpha-ubuntu-20-04-ubuntu-18-04
[ubhb-202305-install-py312-ubuntu]: https://ubuntuhandbook.org/index.php/2023/05/install-python-3-12-ubuntu
