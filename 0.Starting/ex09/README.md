Some sort of a readme file

    pyproject.toml
    source: https://packaging.python.org/en/latest/tutorials/packaging-projects/

    name: is the distribution name of your package. This can be any name as long as it only contains letters, numbers, ., _ , and -. It also must not already be taken on PyPI. Be sure to update this with your username for this tutorial, as this ensures you won’t try to upload a package with the same name as one which already exists.

    version: is the package version. (Some build backends allow it to be specified another way, such as from a file or Git tag.)

    authors: is used to identify the author of the package; you specify a name and an email for each author. You can also list maintainers in the same format.

    description: is a short, one-sentence summary of the package.

    readme: is a path to a file containing a detailed description of the package. This is shown on the package detail page on PyPI. In this case, the description is loaded from README.md (which is a common pattern). There also is a more advanced table form described in the pyproject.toml guide.

    requires-python: gives the versions of Python supported by your project. An installer like pip will look back through older versions of packages until it finds one that has a matching Python version.

    classifiers: gives the index and pip some additional metadata about your package. In this case, the package is only compatible with Python 3 and is OS-independent. You should always include at least which version(s) of Python your package works on and which operating systems your package will work on. For a complete list of classifiers, see https://pypi.org/classifiers/.

    license: is the SPDX license expression of your package.

    license-files: is the list of glob paths to the license files, relative to the directory where pyproject.toml is located.

    urls: lets you list any number of extra links to show on PyPI. Generally this could be to the source, documentation, issue trackers, etc.
