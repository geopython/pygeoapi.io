---
title: Community
---

<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<style>
  #map {
    width: 650px;
    height: 300px;
  }
  .leaflet-marker-icon {
    background: transparent !important;
    box-shadow: none;
  }
</style>

# Community

## Live deployments map
<div id="map"></div>

Want to add your deployment?  Add it to the [wiki page](https://github.com/geopython/pygeoapi/wiki/LiveDeployments) (map is updated hourly).

<script>
  const map = L.map('map', {
    attributionControl: false
  }).setView([20, 0], 1);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  const icon = L.icon({
    iconUrl: 'marker.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    shadowUrl: null
  });

  fetch('https://raw.githubusercontent.com/geopython/pygeoapi.io/gh-pages/community/live-deployments.geojson')
    .then(r => r.json())
    .then(data => {
      const layer = L.geoJSON(data, {
        pointToLayer: (feature, latlng) => {
          return L.marker(latlng);
        },
        onEachFeature: (feature, layer) => {
          layer.bindPopup(
            feature.properties.url
          );
        }
      }).addTo(map);

      map.fitBounds(layer.getBounds());
    });
</script>

<div class="pygeoapi-powered">
  <a href="https://www.ga.gov.au"><img alt="Geoscience Australia" src="/img/org-logos/aus-ga.png"/></a>
  <a href="https://ec.gc.ca"><img alt="Environment and Climate Change Canada" src="/img/org-logos/can-eccc.jpg"/></a>
  <a href="https://idee.es"><img alt="National Cartographic System of Spain" src="/img/org-logos/esp-idee.png"/></a>
  <a href="https://ign.es"><img alt="National Geographic Institute of Spain" src="/img/org-logos/esp-ign.png"/></a>
  <a href="https://www.bgs.ac.uk"><img alt="British Geological Survery" src="/img/org-logos/gbr-bgs.png" style="vertical-align: top";/></a>
  <a href="https://wmo.int/site/knowledge-hub/programmes-and-initiatives/global-atmosphere-watch-programme-gaw"><img alt="World Meteorological Organization, Global Atmospheric Watch" src="/img/org-logos/int-wmo-gaw.jpg" style="vertical-align: top;"/></a>
  <a href="https://wmo.int"><img alt="World Meteorological Organization" src="/img/org-logos/int-wmo.jpg" style="vertical-align: top;"/></a>
  <a href="https://www.dgterritorio.gov.pt"><img alt="Direção-Geral do Território (DGT)" src="/img/org-logos/prt-dgt.png" style="vertical-align: middle;"/></a>
  <a href="https://www.geoplatform.gov"><img alt="US Geoplatform.gov" src="/img/org-logos/usa-geoplatform.jpg" style="vertical-align: middle;"/></a>
  <a href="https://internetofwater.org"><img alt="The Internet of Water Coalition" src="/img/org-logos/usa-iow.png" style="vertical-align: middle;"/></a>
  <a href="https://usgs.gov"><img alt="United States Geological Survey" src="/img/org-logos/usa-usgs.jpg" style="vertical-align: top;"/></a>
  <a href="https://www.ingv.it"><img alt="Istituto Nazionale di Geofisica e Vulcanologia" src="/img/org-logos/ita-ingv.png" style="vertical-align: middle;"/></a>
  <a href="https://www.cityofathens.gr"><img alt="Municipality of Athens, Greece" src="/img/org-logos/grc-city-of-athens.svg" style="vertical-align: middle;"/></a>
  <a href="https://eoepca.org"><img alt="ESA Earth Observation Exploitation Platform Common Architecture (EOEPCA)" src="/img/org-logos/int-eoepca.png" style="vertical-align: middle;"/></a>
  <a href="https://www.rostock.de"><img alt="Hanse- und Universitätsstadt Rostock" src="/img/org-logos/ger-hro.png" style="vertical-align: middle;"/></a>
</div>

## Code of Conduct

In support of an inclusive and welcoming community, the pygeoapi code of conduct can always be found at [https://github.com/geopython/pygeoapi/blob/master/CODE_OF_CONDUCT.md](https://github.com/geopython/pygeoapi/blob/master/CODE_OF_CONDUCT.md).

There are numerous ways to interact with the pygeoapi community.

## Mailing list

The pygeoapi mailing list enables users and developers to exchange ideas, discuss improvements / issues, and ask questions. To subscribe, visit [https://lists.osgeo.org/mailman/listinfo/pygeoapi](https://lists.osgeo.org/mailman/listinfo/pygeoapi).

Mailing list archives are available at [https://lists.osgeo.org/pipermail/pygeoapi](https://lists.osgeo.org/pipermail/pygeoapi).

## GitHub Discussions

pygeoapi also provides [GitHub Discussions](https://github.com/geopython/pygeoapi/discussions) as a collaborative community space for general questions, ideas, and more.

## Chat

pygeoapi provides open communication in real-time, and provides chat via Gitter, Slack, or IRC (note: connecting via either Gitter or Slack or IRC plugs you in to the same chat).

PSC discussions, meetings and user discussion can typically be found in pygeoapi's chat.

### Gitter

Gitter provides a web-based instant messaging and chatroom.  The pygeoapi [Gitter chatroom](https://app.gitter.im/#/room/#geopython_pygeoapi:gitter.im) is public and open to anyone.

### Slack

The OSGeo Slack is provided at [https://osgeo.slack.com/pygeoapi](https://osgeo.slack.com/pygeoapi).

### IRC

The pygeoapi IRC can be found at [irc://irc.freenode.net#pygeoapi](irc://irc.freenode.net#pygeoapi).

For those wishing only to follow repository changes/updates, the pygeoapi-activity IRC can be found at [irc://irc.freenode.net#pygeoapi-activity](irc://irc.freenode.net#pygeoapi-activity).

## Twitter

The official pygeoapi Twitter handle is at [https://twitter.com/pygeoapi](https://twitter.com/pygeoapi).

## Mastodon

The official pygeoapi Mastodon handle is at [https://noc.social/@pygeoapi](https://noc.social/@pygeoapi).

## Stack Overflow

pygeoapi discussions on Stack Overflow can be found with the [pygeoapi](https://stackoverflow.com/questions/tagged/pygeoapi) tag.

## Service Providers

pygeoapi service providers (core development, support, training) can be found on the [Service Providers page](service-providers/).

Service providers are also listed on the [OSGeo Service Provider Directory](https://www.osgeo.org/service-providers).

## Swag

pygeoapi swag (t-shirts, hoodies, stickers, etc.) are available and can be purchased via the [OSGeo Redbubble shop](https://www.redbubble.com/shop/ap/146590645).

## GitHub (Wiki, Issues, Code)

The pygeoapi [wiki](https://github.com/geopython/pygeoapi/wiki) provides an area for supporting information that frequently changes and / or is outside the scope of the formal documentation.

The pygeoapi [issue tracker](https://github.com/geopython/pygeoapi/issues) is the place to report bugs or request enhancements.  To submit a [bug](https://github.com/geopython/pygeoapi/issues/) be sure to specify the version you are using, the appropriate component, a description of how to reproduce the bug, as well as what version of Python and platform.

GitHub provides the ability for users to issue [Pull Requests](https://help.github.com/articles/creating-a-pull-request), and is the preferred way to have your contributions added to pygeoapi, although patches and other mechanisms are welcome as well.

All pygeoapi [source code](https://github.com/geopython/pygeoapi) is managed on GitHub, which includes the latest (`master`) and other supported branches.

## Security issues

If you encounter a security vulnerability in pygeoapi please report as per our [Security Policy](https://github.com/geopython/pygeoapi/blob/master/SECURITY.md)

## Getting Involved

Users, developers and others are more than welcome!  There are plenty of ways to get involved:

- Documentation
- Fixing bugs
- Testing
- Core development (bug fixing, feature implementation, etc.)

See [https://github.com/geopython/pygeoapi/blob/master/CONTRIBUTING.md](https://github.com/geopython/pygeoapi/blob/master/CONTRIBUTING.md) for more information on contributing.


<script src="//code.jquery.com/jquery-4.0.0.min.js"></script>
<script type="text/javascript">
  function makeSimpleSlideshow(container) {
    container.addClass('slideshow').hide().slideDown('slow');
    $('a', container).each(function() {
      $(this).attr('title', $('img', this).attr('alt'));
    }).clone().appendTo(container);
    var links = $('a', container).wrapAll('<div class=items></div>');
    var items = $('div.items', container);
    var firstLink = $(links[0]);
    var lastLink = $(links[links.length / 2 - 1]);
    var pixels = lastLink.offset().left - firstLink.offset().left + lastLink.width();

    function scroll() {
      items.animate({left: -pixels + 'px'}, pixels * 20, 'linear', function() {
        items.css('left', '0px');
        scroll();
      });
    }
    scroll();
  }

  $(document).ready(function() {
      var powered = $('div.pygeoapi-powered');
      if (powered.length > 0)
          makeSimpleSlideshow(powered);
  });
</script>
