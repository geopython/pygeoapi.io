[![Build Status](https://github.com/geopython/pygeoapi.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/geopython/pygeoapi.io/actions)
[![Join the chat at https://app.gitter.im/#/room/#geopython_pygeoapi:gitter.img](https://badges.gitter.im/Join%20Chat.svg)](https://app.gitter.im/#/room/#geopython_pygeoapi:gitter.im)

# pygeoapi.io website

The pygeoapi [website](https://pygeoapi.io) is powered
by [MkDocs](https://www.mkdocs.org) which facilitates easy management
of website content and publishing.

## Setting up the website environment locally

```bash
# build a virtual Python environment in isolation
python3 -m venv pygeoapi-website
cd pygeoapi-website
# download the website from GitHub
git clone https://github.com/geopython/pygeoapi.io.git
cd pygeoapi.io
# install required dependencies
pip3 install -r requirements.txt
# build the website
mkdocs build
# serve locally
mkdocs serve  # website is made available on http://localhost:8000/
```

## Content management workflow

### Overview

To manage content you require an account on GitHub.  From here you can either
1. fork the repository, make your own changes and issue a pull request, or 2.
edit the content directly.  For option 2 the necessary permissions are required.

The basic workflow is as follows:

- manage content
- commit updates
- publish to the live site

### Adding a page

```bash
vi docs/new-page.md  # add content
vi mkdocs.yml  # add to navigation section
# edit any other files necessary which may want to link to the new page
git add docs/new-page.md
git commit -m 'add new page on topic x' docs/new-page.md mkdocs.yml
git push origin master
```

### Updating a page

```bash
vi content/page.md  # update content
git commit -m 'update page' content/page.md
git push origin master
```

## Publishing updates to the live site

Website updates are automatically published via GitHub Actions, but just in case:

```bash
# NOTE: you require access privileges to the GitHub repository
# to publish live updates
mkdocs gh-deploy -m 'add new page on topic x'
```
