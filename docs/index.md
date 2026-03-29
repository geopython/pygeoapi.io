---
title: pygeoapi - an OGC API to geospatial data
---

![pygeoapi logo](img/pygeoapi-logo.png "pygeoapi logo")

[![DOI](https://zenodo.org/badge/121585259.svg)](https://zenodo.org/badge/latestdoi/121585259)

pygeoapi is a Python server implementation of the [OGC API suite of standards](https://ogcapi.ogc.org). The project emerged as part of the next generation OGC API efforts in 2018 and provides the capability for organizations to deploy a RESTful OGC API endpoint using OpenAPI, GeoJSON, and HTML. pygeoapi is [open source](https://opensource.org) and released under an [MIT license](https://github.com/geopython/pygeoapi/blob/master/LICENSE.md).

<br/>
<a title="Certified OGC Compliant" href="https://github.com/geopython/pygeoapi/wiki/OGCCompliance"><img alt="Certified OGC Compliant" src="https://portal.ogc.org/public_ogc/compliance/OGC_Certified_Badge.png" width="164" height="64"/></a> <a title="OGC Reference Implementation" href="https://github.com/geopython/pygeoapi/wiki/OGCCompliance"><img alt="OGC Reference Implementation" src="https://portal.ogc.org/public_ogc/compliance/badge.php?s=ogcapi-features-1 1.0&r=1&n=1)" width="164" height="64"/></a> <a title="OGC Reference Implementation" href="https://github.com/geopython/pygeoapi/wiki/OGCCompliance"><img alt="OGC Reference Implementation" src="https://portal.ogc.org/public_ogc/compliance/badge.php?s=ogcapi-edr-1 1.0.1&r=1&n=1" width="164" height="64"/> <a title="OGC Reference Implementation" href="https://github.com/geopython/pygeoapi/wiki/OGCCompliance"><img alt="OGC Reference Implementation" src="https://portal.ogc.org/public_ogc/compliance/badge.php?s=ogcapi-tiles-1%201.0&r=1&n=1" width="164" height="64"/></a>  <a title="OGC Reference Implementation" href="https://github.com/geopython/pygeoapi/wiki/OGCCompliance"><img alt="OGC Reference Implementation" src="https://portal.ogc.org/public_ogc/compliance/badge.php?s=ogcapi-processes-1%201.0&n=1" width="164" height="64"/></a> <a title="OSGeo Project" href="https://www.osgeo.org/projects/pygeoapi"><img alt="OSGeo Project" src="https://raw.githubusercontent.com/OSGeo/osgeo/master/incubation/project/OSGeo_project.png" width="164" height="64"/></a><a title="FOSS4G Conference" href="https://2026.foss4g.org"><img alt="FOSS4G Conference" width="180" height="78" src="img/foss4g-2026.png"/></a><a href="https://github.com/geopython/pygeoapi/wiki/Sponsorship"><img alt="Sponsorship" width="147" height="47" src="img/btn_donateCC_LG.gif"/></a>

---

## Install in 5 minutes

```bash
# Python 3.12 recommended
python3 -m venv venv
cd venv
. bin/activate
git clone https://github.com/geopython/pygeoapi.git
cd pygeoapi
pip3 install -r requirements.txt
pip3 install .
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

- OGC Compliant: pygeoapi is certified [OGC Compliant and an OGC Reference Implementation](https://github.com/geopython/pygeoapi/wiki/OGCCompliance)
- Easy to install: install a full implementation via pip or git
- Easy to deploy: via UbuntuGIS or the official Docker image
- Flexible: built on a robust plugin framework
    - connect to custom data sources (files, services, databases, etc.)
    - serve custom output formats
    - implement custom processes and workflows
    - deploy via Flask, Django, or any Python framework
