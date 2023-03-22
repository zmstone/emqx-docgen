# Bridges

## bridge:bridges <a id='bridge-bridges'></a>
Configuration for MQTT bridges.

| Config paths | Env overrides |
|----------------------|---------------------------|
|  <code>bridges</code> | <code>EMQX_BRIDGES</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>webhook</h4>
WebHook to an HTTP server.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_webhook-config">bridge_webhook:config</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mqtt</h4>
MQTT bridges to/from another MQTT broker

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_mqtt-config">bridge_mqtt:config</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>kafka</h4>
Kafka Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_kafka-config">bridge_kafka:config</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>hstreamdb</h4>
HStreamDB Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_hstreamdb-config">bridge_hstreamdb:config</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>gcp_pubsub</h4>
EMQX Enterprise Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_gcp_pubsub-config">bridge_gcp_pubsub:config</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mysql</h4>
MySQL Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_mysql-config">bridge_mysql:config</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>tdengine</h4>
TDengine Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_tdengine-config">bridge_tdengine:config</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mongodb_rs</h4>
MongoDB Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_mongodb-mongodb_rs">bridge_mongodb:mongodb_rs</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mongodb_sharded</h4>
MongoDB Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_mongodb-mongodb_sharded">bridge_mongodb:mongodb_sharded</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mongodb_single</h4>
MongoDB Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_mongodb-mongodb_single">bridge_mongodb:mongodb_single</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>influxdb_api_v1</h4>
InfluxDB Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_influxdb-influxdb_api_v1">bridge_influxdb:influxdb_api_v1</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>influxdb_api_v2</h4>
InfluxDB Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_influxdb-influxdb_api_v2">bridge_influxdb:influxdb_api_v2</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>redis_single</h4>
Redis Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_redis-redis_single">bridge_redis:redis_single</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>redis_sentinel</h4>
Redis Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_redis-redis_sentinel">bridge_redis:redis_sentinel</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>redis_cluster</h4>
Redis Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_redis-redis_cluster">bridge_redis:redis_cluster</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>pgsql</h4>
PostgreSQL Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_pgsql-config">bridge_pgsql:config</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>timescale</h4>
Timescale Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_pgsql-config">bridge_pgsql:config</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>matrix</h4>
Matrix Bridge Config

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="others.md#bridge_pgsql-config">bridge_pgsql:config</a>}</code></td></tr></tbody>
</table>
</li>

</ul>
