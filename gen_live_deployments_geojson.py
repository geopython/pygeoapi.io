# =================================================================
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#          Ryan Clark <ryan.clark@azgs.az.gov>
#
# Copyright (c) 2026 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import csv
import json
import sys
from io import StringIO
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def health_check_pygeoapi(url):
    """Do a terse check / smoke test on a live pygeoapi deployment"""

    try:
        _ = urlopen(url)
    except HTTPError:
        raise RuntimeError(f'HTTP problem with {url}')
    except URLError:
        raise RuntimeError(f'URL problem with {url}')
    except Exception:
        raise RuntimeError(f'Cannot open {url}')


def build_live_deployments_geojson():
    """Convert Live Deployments wiki page to GeoJSON for GitHub to render"""

    errors = 0
    dep_url = 'https://raw.githubusercontent.com/wiki/geopython/pygeoapi/LiveDeployments.md'  # noqa
    geojson = {'type': 'FeatureCollection', 'features': []}

    # grab Markdown file of Live Deployments from GitHub
    content = urlopen(dep_url).read().decode()

    # serialize as GeoJSON
    dep_reader = csv.reader(StringIO(content), delimiter='|')
    next(dep_reader)  # skip fields row
    next(dep_reader)  # skip dashed line row
    for row in dep_reader:
        url = row[2].strip()
        try:
            # health_check_pygeoapi(url)

            latitude, longitude = float(row[3]), float(row[4])

            feature = {
                'type': 'Feature',
                'properties': {
                    'url': f'<a target="_blank" href="{url}">{row[1].strip()}</a>'  # noqa
                },
                'geometry': {
                    'type': 'Point',
                    'coordinates': [longitude, latitude]
                }
            }
            geojson['features'].append(feature)
        except RuntimeError as rte:
            errors += 1
            print(f'ERROR: {rte}')

    with open('live-deployments.geojson', 'w') as output_file:
        output_file.write(json.dumps(geojson, indent=4))

    return errors


if __name__ == '__main__':
    ERRORS = build_live_deployments_geojson()
    sys.exit(ERRORS)
