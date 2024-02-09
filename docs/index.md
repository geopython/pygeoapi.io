---
title: pygeoapi - an OGC API to geospatial data
---

![pygeoapi logo](img/pygeoapi-logo.png "pygeoapi logo")

[![DOI](https://zenodo.org/badge/121585259.svg)](https://zenodo.org/badge/latestdoi/121585259)

<h4>pygeoapi is a Python server implementation of the <a href="https://ogcapi.ogc.org">OGC API suite of standards</a>. The project emerged as part of the next generation OGC API efforts in 2018 and provides the capability for organizations to deploy a RESTful OGC API endpoint using OpenAPI, GeoJSON, and HTML. pygeoapi is <a href="https://opensource.org">open source</a> and released under an <a href="https://github.com/geopython/pygeoapi/blob/master/LICENSE.md">MIT license</a>.

<br/>
<a title="Certified OGC Compliant" href="https://www.opengeospatial.org/resource/products/details/?pid=1663"><img alt="Certified OGC Compliant" src="https://portal.ogc.org/public_ogc/compliance/OGC_Certified_Badge.png" width="164" height="64"/></a> <a title="OGC Reference Implementation" href="https://www.opengeospatial.org/resource/products/details/?pid=1663"><img alt="OGC Reference Implementation" src="https://portal.ogc.org/public_ogc/compliance/badge.php?s=ogcapi-features-1 1.0&r=1&n=1)" width="164" height="64"/></a> <a title="OGC Reference Implementation" href="https://www.opengeospatial.org/resource/products/details/?pid=1663"><img alt="OGC Reference Implementation" src="https://portal.ogc.org/public_ogc/compliance/badge.php?s=ogcapi-edr-1 1.0.1&r=1&n=1" width="164" height="64"/> <a title="OGC Reference Implementation" href="https://www.opengeospatial.org/resource/products/details/?pid=1663"><img alt="OGC Reference Implementation" src="https://portal.ogc.org/public_ogc/compliance/badge.php?s=ogcapi-tiles-1%201.0&r=1&n=1" width="164" height="64"/></a> <a title="OSGeo Project" href="https://www.osgeo.org/projects/pygeoapi"><img alt="OSGeo Project" src="https://raw.githubusercontent.com/OSGeo/osgeo/master/incubation/project/OSGeo_project.png" width="164" height="64"/></a><a href="https://github.com/geopython/pygeoapi/wiki/Sponsorship"><img alt="Sponsorship" width="147" height="47" src="img/btn_donateCC_LG.gif"/></a>

</h4>

## Install in 5 minutes
```python
python3 -m venv pygeoapi
cd pygeoapi
. bin/activate
git clone https://github.com/geopython/pygeoapi.git
cd pygeoapi
pip3 install -r requirements.txt
python3 setup.py install
cp pygeoapi-config.yml example-config.yml
vi example-config.yml  # edit as required
export PYGEOAPI_CONFIG=example-config.yml
export PYGEOAPI_OPENAPI=example-openapi.yml
pygeoapi openapi generate $PYGEOAPI_CONFIG --output-file $PYGEOAPI_OPENAPI
pygeoapi serve
# in another terminal
curl http://localhost:5000  # or open in a web browser
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
- OGC Compliant: pygeoapi is certified [OGC Compliant and an OGC Reference Implementation](https://www.opengeospatial.org/resource/products/details/?pid=1663)
