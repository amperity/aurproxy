# Copyright 2015 TellApart, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class ProxyRoute(object):
  def __init__(self,
               locations,
               empty_endpoint_status_code,
               source_group_manager,
               proxy_path,
               ratelimit=None):
    self._locations = locations
    self._empty_endpoint_status_code = empty_endpoint_status_code
    self._source_group_manager = source_group_manager
    self._proxy_path = proxy_path
    self._ratelimit = ratelimit

  @property
  def slug(self):
    return self._source_group_manager.slug

  @property
  def blueprints(self):
    return self._source_group_manager.blueprints

  @property
  def locations(self):
    return self._locations

  @property
  def endpoints(self):
    return self._source_group_manager.endpoints

  @property
  def empty_endpoint_status_code(self):
    return self._empty_endpoint_status_code

  @property
  def proxy_path(self):
    return self._proxy_path

  @property
  def ratelimit(self):
    return self._ratelimit

  def start(self, weight_adjustment_start):
    self._source_group_manager.start(weight_adjustment_start)


class ProxyRatelimit(object):
  def __init__(self,
               zone,
               burst=None,
               delay=None,
               nodelay=False,
               status=None):
    self._zone = zone
    self._burst = burst
    self._delay = delay
    self._nodelay = nodelay
    self._status = status

  @property
  def zone(self):
    return self._zone

  @property
  def burst(self):
    return self._burst

  @property
  def delay(self):
    return self._delay

  @property
  def nodelay(self):
    return self._nodelay

  @property
  def status(self):
    return self._status
