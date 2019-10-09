---
title: pygeoapi - an OGC API to geospatial data
---

![pygeoapi logo](img/pygeoapi-logo.png "pygeoapi logo")

<h4>pygeoapi is a Python server implementation of the <a href="https://www.opengeospatial.org/blog/2996">OGC API suite of standards</a>. The project emerged as part of the next generation OGC API efforts in 2018 and provides the capability for organizations to deploy an RESTful OGC API endpoint using OpenAPI, GeoJSON, and HTML. pygeoapi is <a href="https://opensource.org">open source</a> and released under an <a href="https://github.com/geopython/pygeoapi/blob/master/LICENSE.md">MIT license</a>. <a title="OSGeo Community Project" href="https://osgeo.org"><img alt="OSGeo Community Project" src="https://raw.githubusercontent.com/OSGeo/osgeo/master/incubation/community/OSGeo_community.png" height="64"/></a></h4>

## Install in 5 minutes
```python
python3 -m venv pygeoapi
cd pygeoapi
. bin/activate
git clone https://github.com/geopython/pygeoapi.git
cd pygeoapi
pip install -r requirements.txt
python setup.py install
cp pygeoapi-config.yml example-config.yml
vi example-config.yml
export PYGEOAPI_CONFIG=example-config.yml
export PYGEOAPI_OPENAPI=example-openapi.yml
pygeoapi generate-openapi-document -c $PYGEOAPI_CONFIG > $PYGEOAPI_OPENAPI
pygeoapi serve
curl http://localhost:5000
```

## Features

At a glance:

- Easy to install: install a full implementation via pip or git
- Easy to deploy: via UbuntuGIS or the official Docker image
- Flexible: built on a robust plugin framework
    - connect to custom data sources (files, services, databases, etc.)
    - serve custom output formats
    - implement custom processes and workflows
    - deploy via Flask, Django, or any Python framework
- Compliant: passes OGC Compliance testing
