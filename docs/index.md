---
title: pygeoapi - an OGC API to geospatial data
---

![pygeoapi logo](img/pygeoapi-logo.png "pygeoapi logo")

<h4>pygeoapi is a Python server implementation of the <a href="https://www.opengeospatial.org/blog/2996">OGC API suite of standards</a>. The project emerged as part of the next generation OGC API efforts in 2018 and provides the capability for organizations to deploy an RESTful OGC API endpoint using OpenAPI, GeoJSON, and HTML. pygeoapi is <a href="https://opensource.org">open source</a> and released under an <a href="https://github.com/geopython/pygeoapi/blob/master/LICENSE.md">MIT license</a>. <a title="OSGeo Community Project" href="https://osgeo.org"><img alt="OSGeo Community Project" src="https://raw.githubusercontent.com/OSGeo/osgeo/master/incubation/community/OSGeo_community.png" height="64"/></a></h4>


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
			
		<br />
		<div class="container">
			<div class="row justify-content-center">
				<div class="col-6">
                    At a glance:
                    <ul>
                        <li>Easy to install: install a full implementation via pip or git</li>
                        <li>Easy to deploy: via UbuntuGIS or the official Docker image</li>
                        <li>Flexible: built on a robust plugin framework
                            <ul>
                                <li>connect to custom data sources (files, services, databases, etc.)</li>
                                <li>serve custom output formats</li>
                                <li>implement custom processes and workflows</li>
                                <li>deploy via Flask, Django, or any Python framework</li>
                            </ul>
                        <li>Compliant: passes OGC Compliance testing</li>
                    </ul>
				</div>
			</div>
		</div>
		<br />

		<div class="d-flex flex-row flex-wrap justify-content-center">
			<div class="p-2">
				<div class="card" style="width: 18rem;">
					<div class="card-body">
						<h5 class="card-title text-center"><strong>Code and Docs</strong></h5>
						<h6 class="card-subtitle mb-2 text-muted text-center">GitHub repository</h6>
						<p class="card-text text-center">Code repository and docs</p>
						<p class="card-text text-center">
							<a href="https://github.com/geopython/pygeoapi" target="_blank"
								class="card-link text-center">GitHub</a>
						</p>
						<p class="card-text text-center">
							<a href="https://docs.pygeoapi.io" target="_blank" class="card-link text-center">Docs</a>
							<a href="presentations/default/index.html" target="_blank"
								class="card-link text-center">Presentation</a>
							<a href="https://media.ccc.de/v/bucharest-32-next-generation-ogc-web-services-with-pygeoapi" target="_blank"
								class="card-link text-center">Video</a>
						</p>
					</div>
				</div>
			</div><!-- end p-2 -->
			<div class="p-2">
			<div class="card" style="width: 18rem;">
					<div class="card-body">
						<h5 class="card-title text-center"><strong>Demo</strong></h5>
						<h6 class="card-subtitle mb-2 text-muted text-center">Live demonstration</h6>
						<p class="card-text text-center">Demonstration of pygeoapi in action</p>
						<p class="card-text text-center">
							<a href="https://demo.pygeoapi.io" target="_blank"
								class="card-link text-center">demo.pygeoapi.io</a>
						</p>
					</div>
			</div> <!--  end card -->
			</div>
			<div class="p-2">
			<div class="card" style="width: 18rem;">
					<div class="card-body">
						<h5 class="card-title text-center"><strong>Docker images</strong></h5>
						<h6 class="card-subtitle mb-2 text-muted text-center">Images hosted in Docker Hub</h6>
						<p class="card-text text-center">Docker images/composition to run pygeoapi</p>
						<p class="card-text text-center">
							<a href="https://hub.docker.com/r/geopython/pygeoapi" target=""
								class="card-link text-center">Docker Hub</a>
						</p>
					</div>
			</div> <!--  end card -->			
			</div> <!-- end p-2 -->
		</div> <!-- end flex-row -->
		<div class="d-flex flex-row flex-wrap justify-content-center">
		<div class="p-2">
		<div class="card" style="width: 18rem;">
					<div class="card-body">
						<h5 class="card-title text-center"><strong>WFS 3.0</strong></h5>
						<h6 class="card-subtitle mb-2 text-muted text-center">Proto-WFS 3.0 docs</h6>
						<p class="card-text text-center">Live documentation of future WFS 3.0 standard</p>
						<p class="card-text text-center">
							<a href="https://github.com/opengeospatial/WFS_FES" target="_blank"
								class="card-link text-center">WFS 3.0 repository</a>
						</p>
					</div>
			</div> <!--  end card -->
		</div> <!-- end p-2 -->

		<div class="p-2">
		<div class="card" style="width: 18rem;">
					<div class="card-body">
						<h5 class="card-title text-center"><strong>Client Tools</strong></h5>
						<h6 class="card-subtitle mb-2 text-muted text-center">WFS clients</h6>
						<p class="card-text text-center">Client tools to work with WFS 3.0</p>
						<p class="card-text text-center">
							<a href="https://gdal.org/drv_wfs3.html" target="_blank"
								class="card-link text-center">GDAL driver</a>
						</p>
						<p class="card-text text-center">
							<a href="https://geopython.github.io/OWSLib/#wfs-3-0" target="_blank"
								class="card-link text-center">OWSLib</a>
						</p>
					</div>
			</div> <!--  end card -->
		</div> <!-- end p-2 -->

        <div class="p-2">
		<div class="card" style="width: 18rem;">
					<div class="card-body">
						<h5 class="card-title text-center"><strong>Community</strong></h5>
						<h6 class="card-subtitle mb-2 text-muted text-center">Support</h6>
						<p class="card-text text-center">Talk to the developers or help us with code and suggestions</p>
						<p class="card-text text-center">
							<a href="https://gitter.im/geopython/pygeoapi" target="_blank"
								class="card-link text-center">Gitter</a>
						</p>
						<p class="card-text text-center">
							<a href="https://lists.osgeo.org/mailman/listinfo/pygeoapi" target="_blank"
								class="card-link text-center">Mailing list</a>
						</p>
					</div>
			</div> <!--  end card -->
		</div> <!-- end p-2 -->

		</div> <!-- end flex-row -->

	</div><!-- end main-page -->
