---
title: Service Providers
---

# Service Providers

pygeoapi is developed and supported by a a number of businesses, organizations and individuals around the world.

Using a service provider is a great way to get started with pygeoapi and contributes to the ongoing sustainability of the project.  Services include (but are not limited to):

- training
- setup/installation/deployment
- custom integration
- bug fixing
- features/enhancements
- core development
- maintenance/packaging/distribution
- documentation

The section below provides a list of service providers who can help you in getting the best out of your pygeoapi investment.  The list is randomized on each page load.

If you are a service provider and would like to be listed on this page, please feel free to [add yourself to the service provider list](https://github.com/geopython/pygeoapi.io/blob/master/docs/community/service-providers/index.md).

<div id="service-provider-list">

  <div class="service-provider">
    <h2>EOX IT Services GmbH</h2>
    <p>
      <span><a href="https://eox.at"><img width="100" src="https://eox.at/EOX_Logo.svg"/></a></span>
      <span><a href="https://eox.at">EOX IT Services GmbH</a> (Austria) offers solutions and services in the geodata domain in general and in the Earth Observation domain in particular. EOX is strongly committed towards utilizing and contributing to Open Source Software for example by adapting pygeoapi for <a href="https://github.com/eurodatacube/pygeoapi-kubernetes-papermill">kubernetes-based cloud environments</a>. EOX furthermore provides managed compute and storage resources in the EOxHub Workspace.</span>
    </p>
  </div>

  <div class="service-provider">
    <h2>GeoBeyond Srl</h2>
    <p>TODO</p>
  </div>

  <div class="service-provider">
    <h2>GeoCat B.V.</h2>
    <p>TODO</p>
  </div>

  <div class="service-provider">
    <h2>GeoComvos Ltd</h2>
    <p>
      <span><a href="http://geocomvos.com">GeoComvos Ltd.</a> is a technical consultancy and open source geospatial service provider, specializing in the development, deployment of Free and Open Source Software Geospatial (FOSS4G) technology, particularly in the development of Spatial Data Infrastructure (SDI) platforms and Geospatial Catalogues. The company specializes in promoting, developing and contributing Open Source and Open Data solutions to governments, organizations and the private sector. GeoComvos provides support and development services for pygeoapi.</span>
    </p>
  </div>

  <div class="service-provider">
    <h2>Just Objects B.V.</h2>
    <p>TODO</p>
  </div>

</div>


<script>

// shuffle divs randomly
// from https://stackoverflow.com/a/43980082 (2022-01-15)

function shuffle() {
  var container = document.getElementById("service-provider-list");
  var elementsArray = Array.prototype.slice.call(container.getElementsByClassName("service-provider"));
  elementsArray.forEach(function(element){
    container.removeChild(element);
  })
  shuffleArray(elementsArray);
  elementsArray.forEach(function(element){
    container.appendChild(element);
  })
}

function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}

shuffle();
</script>
