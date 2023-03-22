# EMQX

## Root Config Keys <a id='root-config-keys'></a>




**Fields**

<ul class="field-list">
<li>
<h4>listeners</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-listeners">broker:listeners</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>zones</h4>
A zone is a set of configs grouped by the zone <code>name</code>.
For flexible configuration mapping, the <code>name</code> can be set to a listener's <code>zone</code> config.
NOTE: A built-in zone named <code>default</code> is auto created and can not be deleted.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="broker-zone">broker:zone</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mqtt</h4>
Global MQTT configuration.
The configs here work as default values which can be overridden in <code>zone</code> configs

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-mqtt">broker:mqtt</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication</h4>
Default authentication configs for all MQTT listeners.

For per-listener overrides see <code>authentication</code> in listener configs

This option can be configured with:
<ul>
  <li><code>[]</code>: The default value, it allows *ALL* logins</li>
  <li>one: For example <code>{enable:true,backend:"built_in_database",mechanism="password_based"}</code></li>
  <li>chain: An array of structs.</li>
</ul>

When a chain is configured, the login credentials are checked against the backends per the configured order, until an 'allow' or 'deny' decision can be made.

If there is no decision after a full chain exhaustion, the login is rejected.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[<a href="authn.md#authn-builtin_db-authentication">authn-builtin_db:authentication</a> | <a href="authn.md#authn-mysql-authentication">authn-mysql:authentication</a> | <a href="authn.md#authn-postgresql-authentication">authn-postgresql:authentication</a> | <a href="authn.md#authn-mongodb-standalone">authn-mongodb:standalone</a> | <a href="authn.md#authn-mongodb-replica-set">authn-mongodb:replica-set</a> | <a href="authn.md#authn-mongodb-sharded-cluster">authn-mongodb:sharded-cluster</a> | <a href="authn.md#authn-redis-standalone">authn-redis:standalone</a> | <a href="authn.md#authn-redis-cluster">authn-redis:cluster</a> | <a href="authn.md#authn-redis-sentinel">authn-redis:sentinel</a> | <a href="authn.md#authn-http-get">authn-http:get</a> | <a href="authn.md#authn-http-post">authn-http:post</a> | <a href="authn.md#authn-jwt-hmac-based">authn-jwt:hmac-based</a> | <a href="authn.md#authn-jwt-public-key">authn-jwt:public-key</a> | <a href="authn.md#authn-jwt-jwks">authn-jwt:jwks</a> | <a href="authn.md#authn-scram-builtin_db-authentication">authn-scram-builtin_db:authentication</a>]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>authorization</h4>
Authorization a.k.a. ACL.<br/>
In EMQX, MQTT client access control is extremely flexible.<br/>
An out-of-the-box set of authorization data sources are supported.
For example,<br/>
'file' source is to support concise and yet generic ACL rules in a file;<br/>
'built_in_database' source can be used to store per-client customizable rule sets,
natively in the EMQX node;<br/>
'http' source to make EMQX call an external HTTP API to make the decision;<br/>
'PostgreSQL' etc. to look up clients or rules from external databases

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="authorization">authorization</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>node</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="node">node</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>cluster</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="cluster">cluster</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>log</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="log">log</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>rpc</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="rpc">rpc</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>broker</h4>
Message broker options.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker">broker</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>sys_topics</h4>
System topics configuration.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-sys_topics">broker:sys_topics</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>force_shutdown</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-force_shutdown">broker:force_shutdown</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>overload_protection</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-overload_protection">broker:overload_protection</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>force_gc</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-force_gc">broker:force_gc</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>conn_congestion</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-conn_congestion">broker:conn_congestion</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>stats</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-stats">broker:stats</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>sysmon</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-sysmon">broker:sysmon</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>alarm</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-alarm">broker:alarm</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>flapping_detect</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-flapping_detect">broker:flapping_detect</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>persistent_session_store</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-persistent_session_store">broker:persistent_session_store</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>trace</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-trace">broker:trace</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>bridges</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="bridges.md#bridge-bridges">bridge:bridges</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>retainer</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#retainer">retainer</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>statsd</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#statsd">statsd</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>auto_subscribe</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#auto_subscribe">auto_subscribe</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>delayed</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#modules-delayed">modules:delayed</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>telemetry</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#modules-telemetry">modules:telemetry</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>rewrite</h4>
List of topic rewrite rules.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[<a href="others.md#modules-rewrite">modules:rewrite</a>]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>topic_metrics</h4>
List of topics whose metrics are reported.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[<a href="others.md#modules-topic_metrics">modules:topic_metrics</a>]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>plugins</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#plugin-plugins">plugin:plugins</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>dashboard</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#dashboard">dashboard</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>gateway</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway.md#gateway">gateway</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>prometheus</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#prometheus">prometheus</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>rule_engine</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="rule.md#rule_engine">rule_engine</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>exhook</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#exhook">exhook</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>psk_authentication</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#authn-psk-psk_authentication">authn-psk:psk_authentication</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>limiter</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#limiter">limiter</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>slow_subs</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#slow_subs">slow_subs</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>api_key</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#api_key">api_key</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>license</h4>
Defines the EMQX Enterprise license. 


The default license has 100 connections limit, it is issued on 2023-01-09 and valid for 5 years (1825 days).

EMQX comes with a default trial license.  For production use, please 
visit https://www.emqx.com/apply-licenses/emqx to apply.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="license.md#key_license">key_license</a></code></td></tr></tbody>
</table>
</li>

</ul>

## broker:alarm <a id='broker-alarm'></a>
Settings for the alarms.

| Config paths | Env overrides |
|--------------------|-------------------------|
|  <code>alarm</code> | <code>EMQX_ALARM</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>actions</h4>
The actions triggered when the alarm is activated.<br/>Currently, the following actions are supported: <code>log</code> and <code>publish</code>.
<code>log</code> is to write the alarm to log (console or file).
<code>publish</code> is to publish the alarm as an MQTT message to the system topics:
<code>$SYS/brokers/emqx@xx.xx.xx.x/alarms/activate</code> and
<code>$SYS/brokers/emqx@xx.xx.xx.x/alarms/deactivate</code>

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[atom()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[log, publish]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>size_limit</h4>
The maximum total number of deactivated alarms to keep as history.<br/>When this limit is exceeded, the oldest deactivated alarms are deleted to cap the total number.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1..3000</code></td></tr><tr><td><strong>Default</strong></td><td><code>1000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>validity_period</h4>
Retention time of deactivated alarms. Alarms are not deleted immediately
when deactivated, but after the retention time.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"24h"</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:authz_cache <a id='broker-authz_cache'></a>
Settings for the authorization cache.

| Config paths | Env overrides |
|----------------------------------|----------------------------------------|
|  <code>authorization.cache</code> | <code>EMQX_AUTHORIZATION__CACHE</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable or disable the authorization cache.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_size</h4>
Maximum number of cached items.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1..1048576</code></td></tr><tr><td><strong>Default</strong></td><td><code>32</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ttl</h4>
Time to live for the cached data.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1m"</code></td></tr></tbody>
</table>
</li>

</ul>

## broker <a id='broker'></a>
Message broker options.

| Config paths | Env overrides |
|---------------------|--------------------------|
|  <code>broker</code> | <code>EMQX_BROKER</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable_session_registry</h4>
Enable session registry

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>session_locking_strategy</h4>
Session locking strategy in a cluster.
  - `local`: only lock the session on the current node
  - `one`: select only one remote node to lock the session
  - `quorum`: select some nodes to lock the session
  - `all`: lock the session on all the nodes in the cluster

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>local | leader | quorum | all</code></td></tr><tr><td><strong>Default</strong></td><td><code>quorum</code></td></tr></tbody>
</table>
</li>
<li>
<h4>shared_subscription_strategy</h4>
Dispatch strategy for shared subscription.
  - `random`: dispatch the message to a random selected subscriber
  - `round_robin`: select the subscribers in a round-robin manner
  - `sticky`: always use the last selected subscriber to dispatch, until the subscriber disconnects.
  - `hash`: select the subscribers by the hash of `clientIds`

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>random | round_robin | round_robin_per_group | sticky | local | hash_topic | hash_clientid</code></td></tr><tr><td><strong>Default</strong></td><td><code>round_robin</code></td></tr></tbody>
</table>
</li>
<li>
<h4>shared_dispatch_ack_enabled</h4>
Deprecated, will be removed in 5.1.
Enable/disable shared dispatch acknowledgement for QoS 1 and QoS 2 messages.
This should allow messages to be dispatched to a different subscriber in the group in case the picked (based on `shared_subscription_strategy`) subscriber is offline.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>route_batch_clean</h4>
Enable batch clean for deleted routes.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>perf</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-broker_perf">broker:broker_perf</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>shared_subscription_group</h4>
Per group dispatch strategy for shared subscription.
This config is a map from shared subscription group name to the strategy
name. The group name should be of format `[A-Za-z0-9]`. i.e. no
special characters are allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="broker-shared_subscription_group">broker:shared_subscription_group</a>}</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:broker_perf <a id='broker-broker_perf'></a>
Broker performance tuning parameters.

| Config paths | Env overrides |
|--------------------------|--------------------------------|
|  <code>broker.perf</code> | <code>EMQX_BROKER__PERF</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>route_lock_type</h4>
Performance tuning for subscribing/unsubscribing a wildcard topic.
Change this parameter only when there are many wildcard topics.

NOTE: when changing from/to `global` lock, it requires all nodes in the cluster to be stopped before the change.
  - `key`: mnesia transactional updates with per-key locks. Recommended for a single-node setup.
  - `tab`: mnesia transactional updates with table lock. Recommended for a cluster setup.
  - `global`: updates are protected with a global lock. Recommended for large clusters.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>key | tab | global</code></td></tr><tr><td><strong>Default</strong></td><td><code>key</code></td></tr></tbody>
</table>
</li>
<li>
<h4>trie_compaction</h4>
Enable trie path compaction.
Enabling it significantly improves wildcard topic subscribe rate, if wildcard topics have unique prefixes like: 'sensor/{{id}}/+/', where ID is unique per subscriber.
Topic match performance (when publishing) may degrade if messages are mostly published to topics with large number of levels.

NOTE: This is a cluster-wide configuration. It requires all nodes to be stopped before changing it.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:conn_congestion <a id='broker-conn_congestion'></a>
Settings for `conn_congestion` alarm.

Sometimes the MQTT connection (usually an MQTT subscriber) may
get "congested", because there are too many packets to be sent.
The socket tries to buffer the packets until the buffer is
full. If more packets arrive after that, the packets will be
"pending" in the queue, and we consider the connection
congested.

Note: `sndbuf` can be set to larger value if the
alarm is triggered too often.
The name of the alarm is of format `conn_congestion/<ClientID>/<Username>`,
where the `<ClientID>` is the client ID of the congested MQTT connection,
and `<Username>` is the username or `unknown_user`.

| Config paths | Env overrides |
|------------------------------|-----------------------------------|
|  <code>conn_congestion</code> | <code>EMQX_CONN_CONGESTION</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable_alarm</h4>
Enable or disable connection congestion alarm.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>min_alarm_sustain_duration</h4>
Minimal time before clearing the alarm.<br/>The alarm is cleared only when there's no pending data in<br/>the queue, and at least <code>min_alarm_sustain_duration</code>milliseconds passed since the last time we considered the connection 'congested'.<br/>This is to avoid clearing and raising the alarm again too often.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1m"</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:deflate_opts <a id='broker-deflate_opts'></a>
Compression options.

| Config paths | Env overrides |
|---------------------------------------------------------|------------------------------------------------------------------|
|  <code>listeners.ws.$name.websocket.deflate_opts</code> | <code>EMQX_LISTENERS__WS__$NAME__WEBSOCKET__DEFLATE_OPTS</code>  |
|  <code>listeners.wss.$name.websocket.deflate_opts</code> | <code>EMQX_LISTENERS__WSS__$NAME__WEBSOCKET__DEFLATE_OPTS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>level</h4>
Compression level.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>none | default | best_compression | best_speed</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mem_level</h4>
Specifies the size of the compression state.<br/>
Lower values decrease memory usage per connection.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1..9</code></td></tr><tr><td><strong>Default</strong></td><td><code>8</code></td></tr></tbody>
</table>
</li>
<li>
<h4>strategy</h4>
Specifies the compression strategy.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>default | filtered | huffman_only | rle</code></td></tr><tr><td><strong>Default</strong></td><td><code>default</code></td></tr></tbody>
</table>
</li>
<li>
<h4>server_context_takeover</h4>
Takeover means the compression state is retained between server messages.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>takeover | no_takeover</code></td></tr><tr><td><strong>Default</strong></td><td><code>takeover</code></td></tr></tbody>
</table>
</li>
<li>
<h4>client_context_takeover</h4>
Takeover means the compression state is retained between client messages.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>takeover | no_takeover</code></td></tr><tr><td><strong>Default</strong></td><td><code>takeover</code></td></tr></tbody>
</table>
</li>
<li>
<h4>server_max_window_bits</h4>
Specifies the size of the compression context for the server.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>8..15</code></td></tr><tr><td><strong>Default</strong></td><td><code>15</code></td></tr></tbody>
</table>
</li>
<li>
<h4>client_max_window_bits</h4>
Specifies the size of the compression context for the client.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>8..15</code></td></tr><tr><td><strong>Default</strong></td><td><code>15</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:event_names <a id='broker-event_names'></a>
Enable or disable client lifecycle event publishing.

The following options affect MQTT clients as well as
gateway clients. The types of the clients
are distinguished by the topic prefix:

- For the MQTT clients, the format is:
`$SYS/broker/<node>/clients/<clientid>/<event>`
- For the Gateway clients, it is
`$SYS/broker/<node>/gateway/<gateway-name>/clients/<clientid>/<event>`


| Config paths | Env overrides |
|--------------------------------------------|--------------------------------------------------|
|  <code>sys_topics.sys_event_messages</code> | <code>EMQX_SYS_TOPICS__SYS_EVENT_MESSAGES</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>client_connected</h4>
Enable to publish client connected event messages

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>client_disconnected</h4>
Enable to publish client disconnected event messages.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>client_subscribed</h4>
Enable to publish event message that client subscribed a topic successfully.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>client_unsubscribed</h4>
Enable to publish event message that client unsubscribed a topic successfully.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:flapping_detect <a id='broker-flapping_detect'></a>
This config controls the allowed maximum number of `CONNECT` packets received
from the same clientid in a time frame defined by `window_time`.
After the limit is reached, successive `CONNECT` requests are forbidden
(banned) until the end of the time period defined by `ban_time`.

| Config paths | Env overrides |
|------------------------------|-----------------------------------|
|  <code>flapping_detect</code> | <code>EMQX_FLAPPING_DETECT</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable flapping connection detection feature.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_count</h4>
The maximum number of disconnects allowed for a MQTT Client in `window_time`

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>15</code></td></tr></tbody>
</table>
</li>
<li>
<h4>window_time</h4>
The time window for flapping detection.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1m"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ban_time</h4>
How long the flapping clientid will be banned.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5m"</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:force_gc <a id='broker-force_gc'></a>
Force garbage collection in MQTT connection process after
 they process certain number of messages or bytes of data.

| Config paths | Env overrides |
|-----------------------|----------------------------|
|  <code>force_gc</code> | <code>EMQX_FORCE_GC</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable forced garbage collection.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>count</h4>
GC the process after this many received messages.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>0..inf</code></td></tr><tr><td><strong>Default</strong></td><td><code>16000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bytes</h4>
GC the process after specified number of bytes have passed through.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"16MB"</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:force_shutdown <a id='broker-force_shutdown'></a>
When the process message queue length, or the memory bytes
reaches a certain value, the process is forced to close.

Note: "message queue" here refers to the "message mailbox"
of the Erlang process, not the `mqueue` of QoS 1 and QoS 2.

| Config paths | Env overrides |
|-----------------------------|----------------------------------|
|  <code>force_shutdown</code> | <code>EMQX_FORCE_SHUTDOWN</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable `force_shutdown` feature.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_message_queue_len</h4>
Maximum message queue length.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>0..inf</code></td></tr><tr><td><strong>Default</strong></td><td><code>1000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_heap_size</h4>
Total heap size

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:wordsize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"32MB"</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:listener_quic_ssl_opts <a id='broker-listener_quic_ssl_opts'></a>
TLS options for QUIC transport.

| Config paths | Env overrides |
|-----------------------------------------------|-------------------------------------------------------|
|  <code>listeners.quic.$name.ssl_options</code> | <code>EMQX_LISTENERS__QUIC__$NAME__SSL_OPTIONS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>cacertfile</h4>
Trusted PEM format CA certificates bundle file.<br/>
The certificates in this file are used to verify the TLS peer's certificates.
Append new certificates to the file if new CAs are to be trusted.
There is no need to restart EMQX to have the updated file loaded, because
the system regularly checks if file has been updated (and reload).<br/>
NOTE: invalidating (deleting) a certificate from the file will not affect
already established connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>certfile</h4>
PEM format certificates chain file.<br/>
The certificates in this file should be in reversed order of the certificate
issue chain. That is, the host's certificate should be placed in the beginning
of the file, followed by the immediate issuer certificate and so on.
Although the root CA certificate is optional, it should be placed at the end of
the file if it is to be added.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>keyfile</h4>
PEM format private key file.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>verify</h4>
Enable or disable peer verification.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>verify_peer | verify_none</code></td></tr><tr><td><strong>Default</strong></td><td><code>verify_none</code></td></tr></tbody>
</table>
</li>
<li>
<h4>reuse_sessions</h4>
Deprecated since 5.0.20.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>depth</h4>
Deprecated since 5.0.20.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password</h4>
Deprecated since 5.0.20.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>versions</h4>
Deprecated since 5.0.20.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[atom()]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ciphers</h4>
Deprecated since 5.0.20.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[string()]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>user_lookup_fun</h4>
Deprecated since 5.0.20.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>secure_renegotiate</h4>
Deprecated since 5.0.20.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>hibernate_after</h4>
Deprecated since 5.0.20.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>dhfile</h4>
Deprecated since 5.0.20.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>fail_if_no_peer_cert</h4>
Deprecated since 5.0.20.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>honor_cipher_order</h4>
Deprecated since 5.0.20.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>client_renegotiation</h4>
Deprecated since 5.0.20.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>handshake_timeout</h4>
Deprecated since 5.0.20.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>gc_after_handshake</h4>
Deprecated since 5.0.20.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:listener_ssl_opts <a id='broker-listener_ssl_opts'></a>
Socket options for SSL connections.

| Config paths | Env overrides |
|--------------------------------------------------------------|------------------------------------------------------------------------|
|  <code>gateway.exproto.listeners.ssl.$name.ssl_options</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__SSL_OPTIONS</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.ssl_options</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__SSL_OPTIONS</code>  |
|  <code>listeners.ssl.$name.ssl_options</code> | <code>EMQX_LISTENERS__SSL__$NAME__SSL_OPTIONS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>cacertfile</h4>
Trusted PEM format CA certificates bundle file.<br/>
The certificates in this file are used to verify the TLS peer's certificates.
Append new certificates to the file if new CAs are to be trusted.
There is no need to restart EMQX to have the updated file loaded, because
the system regularly checks if file has been updated (and reload).<br/>
NOTE: invalidating (deleting) a certificate from the file will not affect
already established connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>certfile</h4>
PEM format certificates chain file.<br/>
The certificates in this file should be in reversed order of the certificate
issue chain. That is, the host's certificate should be placed in the beginning
of the file, followed by the immediate issuer certificate and so on.
Although the root CA certificate is optional, it should be placed at the end of
the file if it is to be added.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>keyfile</h4>
PEM format private key file.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>verify</h4>
Enable or disable peer verification.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>verify_peer | verify_none</code></td></tr><tr><td><strong>Default</strong></td><td><code>verify_none</code></td></tr></tbody>
</table>
</li>
<li>
<h4>reuse_sessions</h4>
Enable TLS session reuse.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>depth</h4>
Maximum number of non-self-issued intermediate certificates that can follow the peer certificate in a valid certification path.
So, if depth is 0 the PEER must be signed by the trusted ROOT-CA directly;<br/>
if 1 the path can be PEER, Intermediate-CA, ROOT-CA;<br/>
if 2 the path can be PEER, Intermediate-CA1, Intermediate-CA2, ROOT-CA.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>10</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password</h4>
String containing the user's password. Only used if the private key file is password-protected.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>versions</h4>
All TLS/DTLS versions to be supported.<br/>
NOTE: PSK ciphers are suppressed by 'tlsv1.3' version config.<br/>
In case PSK cipher suites are intended, make sure to configure
<code>['tlsv1.2', 'tlsv1.1']</code> here.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[atom()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[tlsv1.3, tlsv1.2, tlsv1.1, tlsv1]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ciphers</h4>
This config holds TLS cipher suite names separated by comma,
or as an array of strings. e.g.
<code>"TLS_AES_256_GCM_SHA384,TLS_AES_128_GCM_SHA256"</code> or
<code>["TLS_AES_256_GCM_SHA384","TLS_AES_128_GCM_SHA256"]</code>.
<br/>
Ciphers (and their ordering) define the way in which the
client and server encrypts information over the network connection.
Selecting a good cipher suite is critical for the
application's data security, confidentiality and performance.

The names should be in OpenSSL string format (not RFC format).
All default values and examples provided by EMQX config
documentation are all in OpenSSL format.<br/>

NOTE: Certain cipher suites are only compatible with
specific TLS <code>versions</code> ('tlsv1.1', 'tlsv1.2' or 'tlsv1.3')
incompatible cipher suites will be silently dropped.
For instance, if only 'tlsv1.3' is given in the <code>versions</code>,
configuring cipher suites for other versions will have no effect.
<br/>

NOTE: PSK ciphers are suppressed by 'tlsv1.3' version config<br/>
If PSK cipher suites are intended, 'tlsv1.3' should be disabled from <code>versions</code>.<br/>
PSK cipher suites: <code>"RSA-PSK-AES256-GCM-SHA384,RSA-PSK-AES256-CBC-SHA384,
RSA-PSK-AES128-GCM-SHA256,RSA-PSK-AES128-CBC-SHA256,
RSA-PSK-AES256-CBC-SHA,RSA-PSK-AES128-CBC-SHA,
RSA-PSK-DES-CBC3-SHA,RSA-PSK-RC4-SHA"</code>

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[string()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>user_lookup_fun</h4>
EMQX-internal callback that is used to lookup pre-shared key (PSK) identity.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"emqx_tls_psk:lookup"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>secure_renegotiate</h4>
SSL parameter renegotiation is a feature that allows a client and a server
to renegotiate the parameters of the SSL connection on the fly.
RFC 5746 defines a more secure way of doing this. By enabling secure renegotiation,
you drop support for the insecure renegotiation, prone to MitM attacks.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>hibernate_after</h4>
 Hibernate the SSL process after idling for amount of time reducing its memory footprint. 

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>dhfile</h4>
Path to a file containing PEM-encoded Diffie-Hellman parameters
to be used by the server if a cipher suite using Diffie-Hellman
key exchange is negotiated. If not specified, default parameters
are used.<br/>
NOTE: The <code>dhfile</code> option is not supported by TLS 1.3.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>fail_if_no_peer_cert</h4>
Used together with {verify, verify_peer} by an TLS/DTLS server.
If set to true, the server fails if the client does not have a
certificate to send, that is, sends an empty certificate.
If set to false, it fails only if the client sends an invalid
certificate (an empty certificate is considered valid).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>honor_cipher_order</h4>
An important security setting, it forces the cipher to be set based
 on the server-specified order instead of the client-specified order,
 hence enforcing the (usually more properly configured) security
 ordering of the server administrator.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>client_renegotiation</h4>
In protocols that support client-initiated renegotiation,
the cost of resources of such an operation is higher for the server than the client.
This can act as a vector for denial of service attacks.
The SSL application already takes measures to counter-act such attempts,
but client-initiated renegotiation can be strictly disabled by setting this option to false.
The default value is true. Note that disabling renegotiation can result in
long-lived connections becoming unusable due to limits on
the number of messages the underlying cipher suite can encipher.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>handshake_timeout</h4>
Maximum time duration allowed for the handshake to complete

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>gc_after_handshake</h4>
Memory usage tuning. If enabled, will immediately perform a garbage collection after the TLS/SSL handshake.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:listener_wss_opts <a id='broker-listener_wss_opts'></a>
Socket options for WebSocket/SSL connections.

| Config paths | Env overrides |
|----------------------------------------------|------------------------------------------------------|
|  <code>listeners.wss.$name.ssl_options</code> | <code>EMQX_LISTENERS__WSS__$NAME__SSL_OPTIONS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>cacertfile</h4>
Trusted PEM format CA certificates bundle file.<br/>
The certificates in this file are used to verify the TLS peer's certificates.
Append new certificates to the file if new CAs are to be trusted.
There is no need to restart EMQX to have the updated file loaded, because
the system regularly checks if file has been updated (and reload).<br/>
NOTE: invalidating (deleting) a certificate from the file will not affect
already established connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>certfile</h4>
PEM format certificates chain file.<br/>
The certificates in this file should be in reversed order of the certificate
issue chain. That is, the host's certificate should be placed in the beginning
of the file, followed by the immediate issuer certificate and so on.
Although the root CA certificate is optional, it should be placed at the end of
the file if it is to be added.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>keyfile</h4>
PEM format private key file.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>verify</h4>
Enable or disable peer verification.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>verify_peer | verify_none</code></td></tr><tr><td><strong>Default</strong></td><td><code>verify_none</code></td></tr></tbody>
</table>
</li>
<li>
<h4>reuse_sessions</h4>
Enable TLS session reuse.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>depth</h4>
Maximum number of non-self-issued intermediate certificates that can follow the peer certificate in a valid certification path.
So, if depth is 0 the PEER must be signed by the trusted ROOT-CA directly;<br/>
if 1 the path can be PEER, Intermediate-CA, ROOT-CA;<br/>
if 2 the path can be PEER, Intermediate-CA1, Intermediate-CA2, ROOT-CA.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>10</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password</h4>
String containing the user's password. Only used if the private key file is password-protected.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>versions</h4>
All TLS/DTLS versions to be supported.<br/>
NOTE: PSK ciphers are suppressed by 'tlsv1.3' version config.<br/>
In case PSK cipher suites are intended, make sure to configure
<code>['tlsv1.2', 'tlsv1.1']</code> here.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[atom()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[tlsv1.3, tlsv1.2, tlsv1.1, tlsv1]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ciphers</h4>
This config holds TLS cipher suite names separated by comma,
or as an array of strings. e.g.
<code>"TLS_AES_256_GCM_SHA384,TLS_AES_128_GCM_SHA256"</code> or
<code>["TLS_AES_256_GCM_SHA384","TLS_AES_128_GCM_SHA256"]</code>.
<br/>
Ciphers (and their ordering) define the way in which the
client and server encrypts information over the network connection.
Selecting a good cipher suite is critical for the
application's data security, confidentiality and performance.

The names should be in OpenSSL string format (not RFC format).
All default values and examples provided by EMQX config
documentation are all in OpenSSL format.<br/>

NOTE: Certain cipher suites are only compatible with
specific TLS <code>versions</code> ('tlsv1.1', 'tlsv1.2' or 'tlsv1.3')
incompatible cipher suites will be silently dropped.
For instance, if only 'tlsv1.3' is given in the <code>versions</code>,
configuring cipher suites for other versions will have no effect.
<br/>

NOTE: PSK ciphers are suppressed by 'tlsv1.3' version config<br/>
If PSK cipher suites are intended, 'tlsv1.3' should be disabled from <code>versions</code>.<br/>
PSK cipher suites: <code>"RSA-PSK-AES256-GCM-SHA384,RSA-PSK-AES256-CBC-SHA384,
RSA-PSK-AES128-GCM-SHA256,RSA-PSK-AES128-CBC-SHA256,
RSA-PSK-AES256-CBC-SHA,RSA-PSK-AES128-CBC-SHA,
RSA-PSK-DES-CBC3-SHA,RSA-PSK-RC4-SHA"</code>

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[string()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>user_lookup_fun</h4>
EMQX-internal callback that is used to lookup pre-shared key (PSK) identity.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"emqx_tls_psk:lookup"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>secure_renegotiate</h4>
SSL parameter renegotiation is a feature that allows a client and a server
to renegotiate the parameters of the SSL connection on the fly.
RFC 5746 defines a more secure way of doing this. By enabling secure renegotiation,
you drop support for the insecure renegotiation, prone to MitM attacks.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>hibernate_after</h4>
 Hibernate the SSL process after idling for amount of time reducing its memory footprint. 

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>dhfile</h4>
Path to a file containing PEM-encoded Diffie-Hellman parameters
to be used by the server if a cipher suite using Diffie-Hellman
key exchange is negotiated. If not specified, default parameters
are used.<br/>
NOTE: The <code>dhfile</code> option is not supported by TLS 1.3.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>fail_if_no_peer_cert</h4>
Used together with {verify, verify_peer} by an TLS/DTLS server.
If set to true, the server fails if the client does not have a
certificate to send, that is, sends an empty certificate.
If set to false, it fails only if the client sends an invalid
certificate (an empty certificate is considered valid).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>honor_cipher_order</h4>
An important security setting, it forces the cipher to be set based
 on the server-specified order instead of the client-specified order,
 hence enforcing the (usually more properly configured) security
 ordering of the server administrator.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>client_renegotiation</h4>
In protocols that support client-initiated renegotiation,
the cost of resources of such an operation is higher for the server than the client.
This can act as a vector for denial of service attacks.
The SSL application already takes measures to counter-act such attempts,
but client-initiated renegotiation can be strictly disabled by setting this option to false.
The default value is true. Note that disabling renegotiation can result in
long-lived connections becoming unusable due to limits on
the number of messages the underlying cipher suite can encipher.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>handshake_timeout</h4>
Maximum time duration allowed for the handshake to complete

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:listeners <a id='broker-listeners'></a>
MQTT listeners identified by their protocol type and assigned names

| Config paths | Env overrides |
|------------------------|-----------------------------|
|  <code>listeners</code> | <code>EMQX_LISTENERS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>tcp</h4>
TCP listeners.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="broker-mqtt_tcp_listener">broker:mqtt_tcp_listener</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>
SSL listeners.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="broker-mqtt_ssl_listener">broker:mqtt_ssl_listener</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ws</h4>
HTTP websocket listeners.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="broker-mqtt_ws_listener">broker:mqtt_ws_listener</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>wss</h4>
HTTPS websocket listeners.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="broker-mqtt_wss_listener">broker:mqtt_wss_listener</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>quic</h4>
QUIC listeners.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="broker-mqtt_quic_listener">broker:mqtt_quic_listener</a>}</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:mqtt <a id='broker-mqtt'></a>
Global MQTT configuration.<br/>The configs here work as default values which can be overridden
in <code>zone</code> configs

| Config paths | Env overrides |
|-------------------|------------------------|
|  <code>mqtt</code> | <code>EMQX_MQTT</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>idle_timeout</h4>
After the TCP connection is established, if the MQTT CONNECT packet from the client is
not received within the time specified by <code>idle_timeout</code>, the connection will be disconnected.
After the CONNECT packet has been accepted by EMQX, if the connection idles for this long time,
then the Erlang process is put to hibernation to save OS resources. Note: long <code>idle_timeout</code>
interval may impose risk at the system if large number of malicious clients only establish connections
but do not send any data.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>infinity | emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_packet_size</h4>
Maximum MQTT packet size allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1MB"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_clientid_len</h4>
Maximum allowed length of MQTT Client ID.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>23..65535</code></td></tr><tr><td><strong>Default</strong></td><td><code>65535</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_topic_levels</h4>
Maximum topic levels allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1..65535</code></td></tr><tr><td><strong>Default</strong></td><td><code>128</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_qos_allowed</h4>
Maximum QoS allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>qos()</code></td></tr><tr><td><strong>Default</strong></td><td><code>2</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_topic_alias</h4>
Maximum topic alias, 0 means no topic alias supported.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>0..65535</code></td></tr><tr><td><strong>Default</strong></td><td><code>65535</code></td></tr></tbody>
</table>
</li>
<li>
<h4>retain_available</h4>
Whether to enable support for MQTT retained message.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>wildcard_subscription</h4>
Whether to enable support for MQTT wildcard subscription.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>shared_subscription</h4>
Whether to enable support for MQTT shared subscription.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>exclusive_subscription</h4>
Whether to enable support for MQTT exclusive subscription.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ignore_loop_deliver</h4>
Ignore loop delivery of messages for MQTT v3.1.1/v3.1.0, similar to <code>No Local</code> subscription option in MQTT 5.0.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>strict_mode</h4>
Parse MQTT messages in strict mode.
When set to true, invalid utf8 strings in for example client ID, topic name, etc. will cause the client to be disconnected

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>response_information</h4>
Specify the response information returned to the client. This feature is disabled if is set to "". Applies only to clients using MQTT 5.0.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>
<li>
<h4>server_keepalive</h4>
The keep alive that EMQX requires the client to use. If configured as <code>disabled</code>, it means that the keep alive specified by the client will be used. Requires <code>Server Keep Alive</code> in MQTT 5.0, so it is only applicable to clients using MQTT 5.0 protocol.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer() | disabled</code></td></tr><tr><td><strong>Default</strong></td><td><code>disabled</code></td></tr></tbody>
</table>
</li>
<li>
<h4>keepalive_backoff</h4>
The backoff multiplier used by the broker to determine the client keep alive timeout. If EMQX doesn't receive any packet in <code>Keep Alive * Backoff * 2</code> seconds, EMQX will close the current connection.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>number()</code></td></tr><tr><td><strong>Default</strong></td><td><code>0.75</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_subscriptions</h4>
Maximum number of subscriptions allowed per client.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1..inf | infinity</code></td></tr><tr><td><strong>Default</strong></td><td><code>infinity</code></td></tr></tbody>
</table>
</li>
<li>
<h4>upgrade_qos</h4>
Force upgrade of QoS level according to subscription.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_inflight</h4>
Maximum number of QoS 1 and QoS 2 messages that are allowed to be delivered simultaneously before completing the acknowledgment.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1..65535</code></td></tr><tr><td><strong>Default</strong></td><td><code>32</code></td></tr></tbody>
</table>
</li>
<li>
<h4>retry_interval</h4>
Retry interval for QoS 1/2 message delivering.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_awaiting_rel</h4>
For each publisher session, the maximum number of outstanding QoS 2 messages pending on the client to send PUBREL. After reaching this limit, new QoS 2 PUBLISH requests will be rejected with `147(0x93)` until either PUBREL is received or timed out.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer() | infinity</code></td></tr><tr><td><strong>Default</strong></td><td><code>100</code></td></tr></tbody>
</table>
</li>
<li>
<h4>await_rel_timeout</h4>
For client to broker QoS 2 message, the time limit for the broker to wait before the `PUBREL` message is received. The wait is aborted after timed out, meaning the packet ID is freed for new `PUBLISH` requests. Receiving a stale `PUBREL` causes a warning level log. Note, the message is delivered to subscribers before entering the wait for PUBREL.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"300s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>session_expiry_interval</h4>
Specifies how long the session will expire after the connection is disconnected, only for non-MQTT 5.0 connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"2h"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_mqueue_len</h4>
Maximum queue length. Enqueued messages when persistent client disconnected, or inflight window is full.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer() | infinity</code></td></tr><tr><td><strong>Default</strong></td><td><code>1000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mqueue_priorities</h4>
Topic priorities. Priority number [1-255]
There's no priority table by default, hence all messages are treated equal.

**NOTE**: Comma and equal signs are not allowed for priority topic names.
**NOTE**: Messages for topics not in the priority table are treated as either highest or lowest priority depending on the configured value for <code>mqtt.mqueue_default_priority</code>.

**Examples**:
To configure <code>"topic/1" > "topic/2"</code>:
<code>mqueue_priorities: {"topic/1": 10, "topic/2": 8}</code>

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map() | disabled</code></td></tr><tr><td><strong>Default</strong></td><td><code>disabled</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mqueue_default_priority</h4>
Default topic priority, which will be used by topics not in <code>Topic Priorities</code> (<code>mqueue_priorities</code>).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>highest | lowest</code></td></tr><tr><td><strong>Default</strong></td><td><code>lowest</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mqueue_store_qos0</h4>
Specifies whether to store QoS 0 messages in the message queue while the connection is down but the session remains.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>use_username_as_clientid</h4>
Whether to user Client ID as Username.
This setting takes effect later than <code>Use Peer Certificate as Username</code> (<code>peer_cert_as_username</code>) and <code>Use peer certificate as Client ID</code> (<code>peer_cert_as_clientid</code>).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>peer_cert_as_username</h4>
Use the CN, DN field in the peer certificate or the entire certificate content as Username. Only works for the TLS connection.
Supported configurations are the following:
- <code>cn</code>: Take the CN field of the certificate as Username
- <code>dn</code>: Take the DN field of the certificate as Username
- <code>crt</code>: Take the content of the <code>DER</code> or <code>PEM</code> certificate as Username
- <code>pem</code>: Convert <code>DER</code> certificate content to <code>PEM</code> format as Username
- <code>md5</code>: Take the MD5 value of the content of the <code>DER</code> or <code>PEM</code> certificate as Username

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>disabled | cn | dn | crt | pem | md5</code></td></tr><tr><td><strong>Default</strong></td><td><code>disabled</code></td></tr></tbody>
</table>
</li>
<li>
<h4>peer_cert_as_clientid</h4>
Use the CN, DN field in the peer certificate or the entire certificate content as Client ID. Only works for the TLS connection.
Supported configurations are the following:
- <code>cn</code>: Take the CN field of the certificate as Client ID
- <code>dn</code>: Take the DN field of the certificate as Client ID
- <code>crt</code>: Take the content of the <code>DER</code> or <code>PEM</code> certificate as Client ID
- <code>pem</code>: Convert <code>DER</code> certificate content to <code>PEM</code> format as Client ID
- <code>md5</code>: Take the MD5 value of the content of the <code>DER</code> or <code>PEM</code> certificate as Client ID

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>disabled | cn | dn | crt | pem | md5</code></td></tr><tr><td><strong>Default</strong></td><td><code>disabled</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:mqtt_quic_listener <a id='broker-mqtt_quic_listener'></a>
Settings for the MQTT over QUIC listener.

| Config paths | Env overrides |
|-----------------------------------|------------------------------------------|
|  <code>listeners.quic.$name</code> | <code>EMQX_LISTENERS__QUIC__$NAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>certfile</h4>
Path to the certificate file. Will be deprecated in 5.1, use .ssl_options.certfile instead.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>keyfile</h4>
Path to the secret key file. Will be deprecated in 5.1, use .ssl_options.keyfile instead.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ciphers</h4>
This config holds TLS cipher suite names separated by comma,
or as an array of strings. e.g.
<code>"TLS_AES_256_GCM_SHA384,TLS_AES_128_GCM_SHA256"</code> or
<code>["TLS_AES_256_GCM_SHA384","TLS_AES_128_GCM_SHA256"]</code>.
<br/>
Ciphers (and their ordering) define the way in which the
client and server encrypts information over the network connection.
Selecting a good cipher suite is critical for the
application's data security, confidentiality and performance.

The names should be in OpenSSL string format (not RFC format).
All default values and examples provided by EMQX config
documentation are all in OpenSSL format.<br/>

NOTE: Certain cipher suites are only compatible with
specific TLS <code>versions</code> ('tlsv1.1', 'tlsv1.2' or 'tlsv1.3')
incompatible cipher suites will be silently dropped.
For instance, if only 'tlsv1.3' is given in the <code>versions</code>,
configuring cipher suites for other versions will have no effect.
<br/>

NOTE: PSK ciphers are suppressed by 'tlsv1.3' version config<br/>
If PSK cipher suites are intended, 'tlsv1.3' should be disabled from <code>versions</code>.<br/>
PSK cipher suites: <code>"RSA-PSK-AES256-GCM-SHA384,RSA-PSK-AES256-CBC-SHA384,
RSA-PSK-AES128-GCM-SHA256,RSA-PSK-AES128-CBC-SHA256,
RSA-PSK-AES256-CBC-SHA,RSA-PSK-AES128-CBC-SHA,
RSA-PSK-DES-CBC3-SHA,RSA-PSK-RC4-SHA"</code><br/>

NOTE: QUIC listener supports only 'tlsv1.3' ciphers

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[string()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>["TLS_AES_256_GCM_SHA384", "TLS_AES_128_GCM_SHA256", "TLS_CHACHA20_POLY1305_SHA256"]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>idle_timeout</h4>
How long a connection can go idle before it is gracefully shut down. 0 to disable

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>0</code></td></tr></tbody>
</table>
</li>
<li>
<h4>handshake_idle_timeout</h4>
How long a handshake can idle before it is discarded.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"10s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>keep_alive_interval</h4>
How often to send PING frames to keep a connection alive. 0 means disabled.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>0</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl_options</h4>
TLS options for QUIC transport

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-listener_quic_ssl_opts">broker:listener_quic_ssl_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>enabled</h4>
Enable listener.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bind</h4>
IP address and port for the listening socket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:ip_port() | integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>14567</code></td></tr></tbody>
</table>
</li>
<li>
<h4>acceptors</h4>
The size of the listener's receiving pool.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>16</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_connections</h4>
The maximum number of concurrent connections allowed by the listener.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>infinity | pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"infinity"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mountpoint</h4>
When publishing or subscribing, prefix all topics with a mountpoint string.
The prefixed string will be removed from the topic name when the message
is delivered to the subscriber. The mountpoint is a way that users can use
to implement isolation of message routing between different listeners.
For example if a client A subscribes to `t` with `listeners.tcp.\<name>.mountpoint`
set to `some_tenant`, then the client actually subscribes to the topic
`some_tenant/t`. Similarly, if another client B (connected to the same listener
as the client A) sends a message to topic `t`, the message is routed
to all the clients subscribed `some_tenant/t`, so client A will receive the
message, with topic name `t`.<br/>
Set to `""` to disable the feature.<br/>

Variables in mountpoint string:
  - <code>${clientid}</code>: clientid
  - <code>${username}</code>: username

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>
<li>
<h4>zone</h4>
The configuration zone to which the listener belongs.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>atom()</code></td></tr><tr><td><strong>Default</strong></td><td><code>default</code></td></tr></tbody>
</table>
</li>
<li>
<h4>limiter</h4>
Type of the rate limit.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#limiter-listener_fields">limiter:listener_fields</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{
  connection {capacity = 1000, rate = "1000/s"}
}
</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_authn</h4>
Set <code>true</code> (default) to enable client authentication on this listener, the authentication
process goes through the configured authentication chain.
When set to <code>false</code> to allow any clients with or without authentication information such as username or password to log in.
When set to <code>quick_deny_anonymous</code>, it behaves like when set to <code>true</code>, but clients will be
denied immediately without going through any authenticators if <code>username</code> is not provided. This is useful to fence off
anonymous clients early.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>true | false | quick_deny_anonymous</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:mqtt_ssl_listener <a id='broker-mqtt_ssl_listener'></a>
Settings for the MQTT over SSL listener.

| Config paths | Env overrides |
|----------------------------------|-----------------------------------------|
|  <code>listeners.ssl.$name</code> | <code>EMQX_LISTENERS__SSL__$NAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enabled</h4>
Enable listener.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bind</h4>
IP address and port for the listening socket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:ip_port() | integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8883</code></td></tr></tbody>
</table>
</li>
<li>
<h4>acceptors</h4>
The size of the listener's receiving pool.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>16</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_connections</h4>
The maximum number of concurrent connections allowed by the listener.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>infinity | pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"infinity"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mountpoint</h4>
When publishing or subscribing, prefix all topics with a mountpoint string.
The prefixed string will be removed from the topic name when the message
is delivered to the subscriber. The mountpoint is a way that users can use
to implement isolation of message routing between different listeners.
For example if a client A subscribes to `t` with `listeners.tcp.\<name>.mountpoint`
set to `some_tenant`, then the client actually subscribes to the topic
`some_tenant/t`. Similarly, if another client B (connected to the same listener
as the client A) sends a message to topic `t`, the message is routed
to all the clients subscribed `some_tenant/t`, so client A will receive the
message, with topic name `t`.<br/>
Set to `""` to disable the feature.<br/>

Variables in mountpoint string:
  - <code>${clientid}</code>: clientid
  - <code>${username}</code>: username

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>
<li>
<h4>zone</h4>
The configuration zone to which the listener belongs.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>atom()</code></td></tr><tr><td><strong>Default</strong></td><td><code>default</code></td></tr></tbody>
</table>
</li>
<li>
<h4>limiter</h4>
Type of the rate limit.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#limiter-listener_fields">limiter:listener_fields</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{
  connection {capacity = 1000, rate = "1000/s"}
}
</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_authn</h4>
Set <code>true</code> (default) to enable client authentication on this listener, the authentication
process goes through the configured authentication chain.
When set to <code>false</code> to allow any clients with or without authentication information such as username or password to log in.
When set to <code>quick_deny_anonymous</code>, it behaves like when set to <code>true</code>, but clients will be
denied immediately without going through any authenticators if <code>username</code> is not provided. This is useful to fence off
anonymous clients early.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>true | false | quick_deny_anonymous</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>access_rules</h4>
The access control rules for this listener.<br/>See: https://github.com/emqtt/esockd#allowdeny

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[string()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>["allow all"]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_protocol</h4>
Enable the Proxy Protocol V1/2 if the EMQX cluster is deployed behind HAProxy or Nginx.<br/>
See: https://www.haproxy.com/blog/haproxy/proxy-protocol/

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_protocol_timeout</h4>
Timeout for proxy protocol. EMQX will close the TCP connection if proxy protocol packet is not received within the timeout.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"3s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication</h4>
Per-listener authentication override.
Authentication can be one single authenticator instance or a chain of authenticators as an array.
When authenticating a login (username, client ID, etc.) the authenticators are checked in the configured order.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[<a href="authn.md#authn-builtin_db-authentication">authn-builtin_db:authentication</a> | <a href="authn.md#authn-mysql-authentication">authn-mysql:authentication</a> | <a href="authn.md#authn-postgresql-authentication">authn-postgresql:authentication</a> | <a href="authn.md#authn-mongodb-standalone">authn-mongodb:standalone</a> | <a href="authn.md#authn-mongodb-replica-set">authn-mongodb:replica-set</a> | <a href="authn.md#authn-mongodb-sharded-cluster">authn-mongodb:sharded-cluster</a> | <a href="authn.md#authn-redis-standalone">authn-redis:standalone</a> | <a href="authn.md#authn-redis-cluster">authn-redis:cluster</a> | <a href="authn.md#authn-redis-sentinel">authn-redis:sentinel</a> | <a href="authn.md#authn-http-get">authn-http:get</a> | <a href="authn.md#authn-http-post">authn-http:post</a> | <a href="authn.md#authn-jwt-hmac-based">authn-jwt:hmac-based</a> | <a href="authn.md#authn-jwt-public-key">authn-jwt:public-key</a> | <a href="authn.md#authn-jwt-jwks">authn-jwt:jwks</a> | <a href="authn.md#authn-scram-builtin_db-authentication">authn-scram-builtin_db:authentication</a>]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>tcp_options</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-tcp_opts">broker:tcp_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl_options</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-listener_ssl_opts">broker:listener_ssl_opts</a></code></td></tr></tbody>
</table>
</li>

</ul>

## broker:mqtt_tcp_listener <a id='broker-mqtt_tcp_listener'></a>
Settings for the MQTT over TCP listener.

| Config paths | Env overrides |
|----------------------------------|-----------------------------------------|
|  <code>listeners.tcp.$name</code> | <code>EMQX_LISTENERS__TCP__$NAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enabled</h4>
Enable listener.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bind</h4>
IP address and port for the listening socket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:ip_port() | integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1883</code></td></tr></tbody>
</table>
</li>
<li>
<h4>acceptors</h4>
The size of the listener's receiving pool.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>16</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_connections</h4>
The maximum number of concurrent connections allowed by the listener.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>infinity | pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"infinity"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mountpoint</h4>
When publishing or subscribing, prefix all topics with a mountpoint string.
The prefixed string will be removed from the topic name when the message
is delivered to the subscriber. The mountpoint is a way that users can use
to implement isolation of message routing between different listeners.
For example if a client A subscribes to `t` with `listeners.tcp.\<name>.mountpoint`
set to `some_tenant`, then the client actually subscribes to the topic
`some_tenant/t`. Similarly, if another client B (connected to the same listener
as the client A) sends a message to topic `t`, the message is routed
to all the clients subscribed `some_tenant/t`, so client A will receive the
message, with topic name `t`.<br/>
Set to `""` to disable the feature.<br/>

Variables in mountpoint string:
  - <code>${clientid}</code>: clientid
  - <code>${username}</code>: username

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>
<li>
<h4>zone</h4>
The configuration zone to which the listener belongs.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>atom()</code></td></tr><tr><td><strong>Default</strong></td><td><code>default</code></td></tr></tbody>
</table>
</li>
<li>
<h4>limiter</h4>
Type of the rate limit.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#limiter-listener_fields">limiter:listener_fields</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{
  connection {capacity = 1000, rate = "1000/s"}
}
</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_authn</h4>
Set <code>true</code> (default) to enable client authentication on this listener, the authentication
process goes through the configured authentication chain.
When set to <code>false</code> to allow any clients with or without authentication information such as username or password to log in.
When set to <code>quick_deny_anonymous</code>, it behaves like when set to <code>true</code>, but clients will be
denied immediately without going through any authenticators if <code>username</code> is not provided. This is useful to fence off
anonymous clients early.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>true | false | quick_deny_anonymous</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>access_rules</h4>
The access control rules for this listener.<br/>See: https://github.com/emqtt/esockd#allowdeny

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[string()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>["allow all"]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_protocol</h4>
Enable the Proxy Protocol V1/2 if the EMQX cluster is deployed behind HAProxy or Nginx.<br/>
See: https://www.haproxy.com/blog/haproxy/proxy-protocol/

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_protocol_timeout</h4>
Timeout for proxy protocol. EMQX will close the TCP connection if proxy protocol packet is not received within the timeout.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"3s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication</h4>
Per-listener authentication override.
Authentication can be one single authenticator instance or a chain of authenticators as an array.
When authenticating a login (username, client ID, etc.) the authenticators are checked in the configured order.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[<a href="authn.md#authn-builtin_db-authentication">authn-builtin_db:authentication</a> | <a href="authn.md#authn-mysql-authentication">authn-mysql:authentication</a> | <a href="authn.md#authn-postgresql-authentication">authn-postgresql:authentication</a> | <a href="authn.md#authn-mongodb-standalone">authn-mongodb:standalone</a> | <a href="authn.md#authn-mongodb-replica-set">authn-mongodb:replica-set</a> | <a href="authn.md#authn-mongodb-sharded-cluster">authn-mongodb:sharded-cluster</a> | <a href="authn.md#authn-redis-standalone">authn-redis:standalone</a> | <a href="authn.md#authn-redis-cluster">authn-redis:cluster</a> | <a href="authn.md#authn-redis-sentinel">authn-redis:sentinel</a> | <a href="authn.md#authn-http-get">authn-http:get</a> | <a href="authn.md#authn-http-post">authn-http:post</a> | <a href="authn.md#authn-jwt-hmac-based">authn-jwt:hmac-based</a> | <a href="authn.md#authn-jwt-public-key">authn-jwt:public-key</a> | <a href="authn.md#authn-jwt-jwks">authn-jwt:jwks</a> | <a href="authn.md#authn-scram-builtin_db-authentication">authn-scram-builtin_db:authentication</a>]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>tcp_options</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-tcp_opts">broker:tcp_opts</a></code></td></tr></tbody>
</table>
</li>

</ul>

## broker:mqtt_ws_listener <a id='broker-mqtt_ws_listener'></a>
Settings for the MQTT over WebSocket listener.

| Config paths | Env overrides |
|---------------------------------|----------------------------------------|
|  <code>listeners.ws.$name</code> | <code>EMQX_LISTENERS__WS__$NAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enabled</h4>
Enable listener.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bind</h4>
IP address and port for the listening socket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:ip_port() | integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8083</code></td></tr></tbody>
</table>
</li>
<li>
<h4>acceptors</h4>
The size of the listener's receiving pool.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>16</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_connections</h4>
The maximum number of concurrent connections allowed by the listener.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>infinity | pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"infinity"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mountpoint</h4>
When publishing or subscribing, prefix all topics with a mountpoint string.
The prefixed string will be removed from the topic name when the message
is delivered to the subscriber. The mountpoint is a way that users can use
to implement isolation of message routing between different listeners.
For example if a client A subscribes to `t` with `listeners.tcp.\<name>.mountpoint`
set to `some_tenant`, then the client actually subscribes to the topic
`some_tenant/t`. Similarly, if another client B (connected to the same listener
as the client A) sends a message to topic `t`, the message is routed
to all the clients subscribed `some_tenant/t`, so client A will receive the
message, with topic name `t`.<br/>
Set to `""` to disable the feature.<br/>

Variables in mountpoint string:
  - <code>${clientid}</code>: clientid
  - <code>${username}</code>: username

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>
<li>
<h4>zone</h4>
The configuration zone to which the listener belongs.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>atom()</code></td></tr><tr><td><strong>Default</strong></td><td><code>default</code></td></tr></tbody>
</table>
</li>
<li>
<h4>limiter</h4>
Type of the rate limit.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#limiter-listener_fields">limiter:listener_fields</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{
  connection {capacity = 1000, rate = "1000/s"}
}
</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_authn</h4>
Set <code>true</code> (default) to enable client authentication on this listener, the authentication
process goes through the configured authentication chain.
When set to <code>false</code> to allow any clients with or without authentication information such as username or password to log in.
When set to <code>quick_deny_anonymous</code>, it behaves like when set to <code>true</code>, but clients will be
denied immediately without going through any authenticators if <code>username</code> is not provided. This is useful to fence off
anonymous clients early.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>true | false | quick_deny_anonymous</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>access_rules</h4>
The access control rules for this listener.<br/>See: https://github.com/emqtt/esockd#allowdeny

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[string()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>["allow all"]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_protocol</h4>
Enable the Proxy Protocol V1/2 if the EMQX cluster is deployed behind HAProxy or Nginx.<br/>
See: https://www.haproxy.com/blog/haproxy/proxy-protocol/

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_protocol_timeout</h4>
Timeout for proxy protocol. EMQX will close the TCP connection if proxy protocol packet is not received within the timeout.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"3s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication</h4>
Per-listener authentication override.
Authentication can be one single authenticator instance or a chain of authenticators as an array.
When authenticating a login (username, client ID, etc.) the authenticators are checked in the configured order.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[<a href="authn.md#authn-builtin_db-authentication">authn-builtin_db:authentication</a> | <a href="authn.md#authn-mysql-authentication">authn-mysql:authentication</a> | <a href="authn.md#authn-postgresql-authentication">authn-postgresql:authentication</a> | <a href="authn.md#authn-mongodb-standalone">authn-mongodb:standalone</a> | <a href="authn.md#authn-mongodb-replica-set">authn-mongodb:replica-set</a> | <a href="authn.md#authn-mongodb-sharded-cluster">authn-mongodb:sharded-cluster</a> | <a href="authn.md#authn-redis-standalone">authn-redis:standalone</a> | <a href="authn.md#authn-redis-cluster">authn-redis:cluster</a> | <a href="authn.md#authn-redis-sentinel">authn-redis:sentinel</a> | <a href="authn.md#authn-http-get">authn-http:get</a> | <a href="authn.md#authn-http-post">authn-http:post</a> | <a href="authn.md#authn-jwt-hmac-based">authn-jwt:hmac-based</a> | <a href="authn.md#authn-jwt-public-key">authn-jwt:public-key</a> | <a href="authn.md#authn-jwt-jwks">authn-jwt:jwks</a> | <a href="authn.md#authn-scram-builtin_db-authentication">authn-scram-builtin_db:authentication</a>]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>tcp_options</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-tcp_opts">broker:tcp_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>websocket</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-ws_opts">broker:ws_opts</a></code></td></tr></tbody>
</table>
</li>

</ul>

## broker:mqtt_wss_listener <a id='broker-mqtt_wss_listener'></a>
Settings for the MQTT over WebSocket/SSL listener.

| Config paths | Env overrides |
|----------------------------------|-----------------------------------------|
|  <code>listeners.wss.$name</code> | <code>EMQX_LISTENERS__WSS__$NAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enabled</h4>
Enable listener.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bind</h4>
IP address and port for the listening socket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:ip_port() | integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8084</code></td></tr></tbody>
</table>
</li>
<li>
<h4>acceptors</h4>
The size of the listener's receiving pool.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>16</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_connections</h4>
The maximum number of concurrent connections allowed by the listener.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>infinity | pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"infinity"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mountpoint</h4>
When publishing or subscribing, prefix all topics with a mountpoint string.
The prefixed string will be removed from the topic name when the message
is delivered to the subscriber. The mountpoint is a way that users can use
to implement isolation of message routing between different listeners.
For example if a client A subscribes to `t` with `listeners.tcp.\<name>.mountpoint`
set to `some_tenant`, then the client actually subscribes to the topic
`some_tenant/t`. Similarly, if another client B (connected to the same listener
as the client A) sends a message to topic `t`, the message is routed
to all the clients subscribed `some_tenant/t`, so client A will receive the
message, with topic name `t`.<br/>
Set to `""` to disable the feature.<br/>

Variables in mountpoint string:
  - <code>${clientid}</code>: clientid
  - <code>${username}</code>: username

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>
<li>
<h4>zone</h4>
The configuration zone to which the listener belongs.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>atom()</code></td></tr><tr><td><strong>Default</strong></td><td><code>default</code></td></tr></tbody>
</table>
</li>
<li>
<h4>limiter</h4>
Type of the rate limit.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#limiter-listener_fields">limiter:listener_fields</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{
  connection {capacity = 1000, rate = "1000/s"}
}
</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_authn</h4>
Set <code>true</code> (default) to enable client authentication on this listener, the authentication
process goes through the configured authentication chain.
When set to <code>false</code> to allow any clients with or without authentication information such as username or password to log in.
When set to <code>quick_deny_anonymous</code>, it behaves like when set to <code>true</code>, but clients will be
denied immediately without going through any authenticators if <code>username</code> is not provided. This is useful to fence off
anonymous clients early.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>true | false | quick_deny_anonymous</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>access_rules</h4>
The access control rules for this listener.<br/>See: https://github.com/emqtt/esockd#allowdeny

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[string()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>["allow all"]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_protocol</h4>
Enable the Proxy Protocol V1/2 if the EMQX cluster is deployed behind HAProxy or Nginx.<br/>
See: https://www.haproxy.com/blog/haproxy/proxy-protocol/

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_protocol_timeout</h4>
Timeout for proxy protocol. EMQX will close the TCP connection if proxy protocol packet is not received within the timeout.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"3s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication</h4>
Per-listener authentication override.
Authentication can be one single authenticator instance or a chain of authenticators as an array.
When authenticating a login (username, client ID, etc.) the authenticators are checked in the configured order.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[<a href="authn.md#authn-builtin_db-authentication">authn-builtin_db:authentication</a> | <a href="authn.md#authn-mysql-authentication">authn-mysql:authentication</a> | <a href="authn.md#authn-postgresql-authentication">authn-postgresql:authentication</a> | <a href="authn.md#authn-mongodb-standalone">authn-mongodb:standalone</a> | <a href="authn.md#authn-mongodb-replica-set">authn-mongodb:replica-set</a> | <a href="authn.md#authn-mongodb-sharded-cluster">authn-mongodb:sharded-cluster</a> | <a href="authn.md#authn-redis-standalone">authn-redis:standalone</a> | <a href="authn.md#authn-redis-cluster">authn-redis:cluster</a> | <a href="authn.md#authn-redis-sentinel">authn-redis:sentinel</a> | <a href="authn.md#authn-http-get">authn-http:get</a> | <a href="authn.md#authn-http-post">authn-http:post</a> | <a href="authn.md#authn-jwt-hmac-based">authn-jwt:hmac-based</a> | <a href="authn.md#authn-jwt-public-key">authn-jwt:public-key</a> | <a href="authn.md#authn-jwt-jwks">authn-jwt:jwks</a> | <a href="authn.md#authn-scram-builtin_db-authentication">authn-scram-builtin_db:authentication</a>]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>tcp_options</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-tcp_opts">broker:tcp_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl_options</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-listener_wss_opts">broker:listener_wss_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>websocket</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-ws_opts">broker:ws_opts</a></code></td></tr></tbody>
</table>
</li>

</ul>

## broker:overload_protection <a id='broker-overload_protection'></a>
Overload protection mechanism monitors the load of the system and temporarily
disables some features (such as accepting new connections) when the load is high.

| Config paths | Env overrides |
|----------------------------------|---------------------------------------|
|  <code>overload_protection</code> | <code>EMQX_OVERLOAD_PROTECTION</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
React on system overload or not.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backoff_delay</h4>
The maximum duration of delay for background task execution during high load conditions.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>0..inf</code></td></tr><tr><td><strong>Default</strong></td><td><code>1</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backoff_gc</h4>
When at high load, skip forceful GC.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backoff_hibernation</h4>
When at high load, skip process hibernation.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backoff_new_conn</h4>
When at high load, close new incoming connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:persistent_session_builtin <a id='broker-persistent_session_builtin'></a>
Settings for the built-in storage engine of persistent messages.

| Config paths | Env overrides |
|-----------------------------------------------|-----------------------------------------------------|
|  <code>persistent_session_store.backend</code> | <code>EMQX_PERSISTENT_SESSION_STORE__BACKEND</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>type</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>builtin</code></td></tr><tr><td><strong>Default</strong></td><td><code>builtin</code></td></tr></tbody>
</table>
</li>
<li>
<h4>session</h4>
Performance tuning options for built-in session table.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-persistent_table_mria_opts">broker:persistent_table_mria_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>session_messages</h4>
Performance tuning options for built-in session messages table.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-persistent_table_mria_opts">broker:persistent_table_mria_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>messages</h4>
Performance tuning options for built-in messages table.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-persistent_table_mria_opts">broker:persistent_table_mria_opts</a></code></td></tr></tbody>
</table>
</li>

</ul>

## broker:persistent_session_store <a id='broker-persistent_session_store'></a>
Settings for message persistence.

| Config paths | Env overrides |
|---------------------------------------|--------------------------------------------|
|  <code>persistent_session_store</code> | <code>EMQX_PERSISTENT_SESSION_STORE</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enabled</h4>
Use the database to store information about persistent sessions.
This makes it possible to migrate a client connection to another
cluster node if a node is stopped.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>on_disc</h4>
Save information about the persistent sessions on disc.
If this option is enabled, persistent sessions will survive full restart of the cluster.
Otherwise, all the data will be stored in RAM, and it will be lost when all the nodes in the cluster are stopped.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ram_cache</h4>
Maintain a copy of the data in RAM for faster access.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backend</h4>
Database management system used to store information about persistent sessions and messages.
- `builtin`: Use the embedded database (mria)

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-persistent_session_builtin">broker:persistent_session_builtin</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{
  messages {ram_cache = "false"}
  session {ram_cache = "true"}
  session_messages {ram_cache = "true"}
  type = "builtin"
}
</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_retain_undelivered</h4>
The time messages that was not delivered to a persistent session
is stored before being garbage collected if the node the previous
session was handled on restarts of is stopped.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1h"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>message_gc_interval</h4>
The starting interval for garbage collection of undelivered messages to
a persistent session. This affects how often the "max_retain_undelivered"
is checked for removal.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1h"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>session_message_gc_interval</h4>
The starting interval for garbage collection of transient data for
persistent session messages. This does not affect the lifetime length
of persistent session messages.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1m"</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:persistent_table_mria_opts <a id='broker-persistent_table_mria_opts'></a>
Tuning options for the mria table.

| Config paths | Env overrides |
|----------------------------------------------------------------|-----------------------------------------------------------------------|
|  <code>persistent_session_store.backend.messages</code> | <code>EMQX_PERSISTENT_SESSION_STORE__BACKEND__MESSAGES</code>  |
|  <code>persistent_session_store.backend.session</code> | <code>EMQX_PERSISTENT_SESSION_STORE__BACKEND__SESSION</code>  |
|  <code>persistent_session_store.backend.session_messages</code> | <code>EMQX_PERSISTENT_SESSION_STORE__BACKEND__SESSION_MESSAGES</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>ram_cache</h4>
Maintain a copy of the data in RAM for faster access.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:shared_subscription_group <a id='broker-shared_subscription_group'></a>
Per group dispatch strategy for shared subscription

| Config paths | Env overrides |
|-----------------------------------------------------|------------------------------------------------------------|
|  <code>broker.shared_subscription_group.$name</code> | <code>EMQX_BROKER__SHARED_SUBSCRIPTION_GROUP__$NAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>strategy</h4>
Dispatch strategy for shared subscription.
- `random`: dispatch the message to a random selected subscriber
- `round_robin`: select the subscribers in a round-robin manner
- `round_robin_per_group`: select the subscribers in round-robin fashion within each shared subscriber group
- `sticky`: always use the last selected subscriber to dispatch,
until the subscriber disconnects.
- `hash`: select the subscribers by the hash of `clientIds`
- `local`: send to a random local subscriber. If local
subscriber was not found, send to a random subscriber cluster-wide

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>random | round_robin | round_robin_per_group | sticky | local | hash_topic | hash_clientid</code></td></tr><tr><td><strong>Default</strong></td><td><code>random</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:ssl_client_opts <a id='broker-ssl_client_opts'></a>
Socket options for SSL clients.

| Config paths | Env overrides |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------|
|  <code>authentication.$INDEX.ssl</code> | <code>EMQX_AUTHENTICATION__$INDEX__SSL</code>  |
|  <code>authorization.sources.$INDEX.ssl</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX__SSL</code>  |
|  <code>bridges.influxdb_api_v1.$name.ssl</code> | <code>EMQX_BRIDGES__INFLUXDB_API_V1__$NAME__SSL</code>  |
|  <code>bridges.influxdb_api_v2.$name.ssl</code> | <code>EMQX_BRIDGES__INFLUXDB_API_V2__$NAME__SSL</code>  |
|  <code>bridges.kafka.$name.ssl</code> | <code>EMQX_BRIDGES__KAFKA__$NAME__SSL</code>  |
|  <code>bridges.matrix.$name.ssl</code> | <code>EMQX_BRIDGES__MATRIX__$NAME__SSL</code>  |
|  <code>bridges.mongodb_rs.$name.ssl</code> | <code>EMQX_BRIDGES__MONGODB_RS__$NAME__SSL</code>  |
|  <code>bridges.mongodb_sharded.$name.ssl</code> | <code>EMQX_BRIDGES__MONGODB_SHARDED__$NAME__SSL</code>  |
|  <code>bridges.mongodb_single.$name.ssl</code> | <code>EMQX_BRIDGES__MONGODB_SINGLE__$NAME__SSL</code>  |
|  <code>bridges.mqtt.$name.ssl</code> | <code>EMQX_BRIDGES__MQTT__$NAME__SSL</code>  |
|  <code>bridges.mysql.$name.ssl</code> | <code>EMQX_BRIDGES__MYSQL__$NAME__SSL</code>  |
|  <code>bridges.pgsql.$name.ssl</code> | <code>EMQX_BRIDGES__PGSQL__$NAME__SSL</code>  |
|  <code>bridges.redis_cluster.$name.ssl</code> | <code>EMQX_BRIDGES__REDIS_CLUSTER__$NAME__SSL</code>  |
|  <code>bridges.redis_sentinel.$name.ssl</code> | <code>EMQX_BRIDGES__REDIS_SENTINEL__$NAME__SSL</code>  |
|  <code>bridges.redis_single.$name.ssl</code> | <code>EMQX_BRIDGES__REDIS_SINGLE__$NAME__SSL</code>  |
|  <code>bridges.timescale.$name.ssl</code> | <code>EMQX_BRIDGES__TIMESCALE__$NAME__SSL</code>  |
|  <code>bridges.webhook.$name.ssl</code> | <code>EMQX_BRIDGES__WEBHOOK__$NAME__SSL</code>  |
|  <code>cluster.etcd.ssl</code> | <code>EMQX_CLUSTER__ETCD__SSL</code>  |
|  <code>gateway.coap.authentication.ssl</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION__SSL</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication.ssl</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION__SSL</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication.ssl</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION__SSL</code>  |
|  <code>gateway.exproto.authentication.ssl</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION__SSL</code>  |
|  <code>gateway.exproto.handler.ssl_options</code> | <code>EMQX_GATEWAY__EXPROTO__HANDLER__SSL_OPTIONS</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication.ssl</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION__SSL</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication.ssl</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION__SSL</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication.ssl</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION__SSL</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication.ssl</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION__SSL</code>  |
|  <code>gateway.lwm2m.authentication.ssl</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION__SSL</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication.ssl</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION__SSL</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication.ssl</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION__SSL</code>  |
|  <code>gateway.mqttsn.authentication.ssl</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION__SSL</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication.ssl</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION__SSL</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication.ssl</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION__SSL</code>  |
|  <code>gateway.stomp.authentication.ssl</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION__SSL</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication.ssl</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION__SSL</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication.ssl</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION__SSL</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX.ssl</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX__SSL</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX.ssl</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX__SSL</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX.ssl</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX__SSL</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX.ssl</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX__SSL</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>cacertfile</h4>
Trusted PEM format CA certificates bundle file.<br/>
The certificates in this file are used to verify the TLS peer's certificates.
Append new certificates to the file if new CAs are to be trusted.
There is no need to restart EMQX to have the updated file loaded, because
the system regularly checks if file has been updated (and reload).<br/>
NOTE: invalidating (deleting) a certificate from the file will not affect
already established connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>certfile</h4>
PEM format certificates chain file.<br/>
The certificates in this file should be in reversed order of the certificate
issue chain. That is, the host's certificate should be placed in the beginning
of the file, followed by the immediate issuer certificate and so on.
Although the root CA certificate is optional, it should be placed at the end of
the file if it is to be added.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>keyfile</h4>
PEM format private key file.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>verify</h4>
Enable or disable peer verification.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>verify_peer | verify_none</code></td></tr><tr><td><strong>Default</strong></td><td><code>verify_none</code></td></tr></tbody>
</table>
</li>
<li>
<h4>reuse_sessions</h4>
Enable TLS session reuse.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>depth</h4>
Maximum number of non-self-issued intermediate certificates that can follow the peer certificate in a valid certification path.
So, if depth is 0 the PEER must be signed by the trusted ROOT-CA directly;<br/>
if 1 the path can be PEER, Intermediate-CA, ROOT-CA;<br/>
if 2 the path can be PEER, Intermediate-CA1, Intermediate-CA2, ROOT-CA.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>10</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password</h4>
String containing the user's password. Only used if the private key file is password-protected.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>versions</h4>
All TLS/DTLS versions to be supported.<br/>
NOTE: PSK ciphers are suppressed by 'tlsv1.3' version config.<br/>
In case PSK cipher suites are intended, make sure to configure
<code>['tlsv1.2', 'tlsv1.1']</code> here.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[atom()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[tlsv1.3, tlsv1.2, tlsv1.1, tlsv1]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ciphers</h4>
This config holds TLS cipher suite names separated by comma,
or as an array of strings. e.g.
<code>"TLS_AES_256_GCM_SHA384,TLS_AES_128_GCM_SHA256"</code> or
<code>["TLS_AES_256_GCM_SHA384","TLS_AES_128_GCM_SHA256"]</code>.
<br/>
Ciphers (and their ordering) define the way in which the
client and server encrypts information over the network connection.
Selecting a good cipher suite is critical for the
application's data security, confidentiality and performance.

The names should be in OpenSSL string format (not RFC format).
All default values and examples provided by EMQX config
documentation are all in OpenSSL format.<br/>

NOTE: Certain cipher suites are only compatible with
specific TLS <code>versions</code> ('tlsv1.1', 'tlsv1.2' or 'tlsv1.3')
incompatible cipher suites will be silently dropped.
For instance, if only 'tlsv1.3' is given in the <code>versions</code>,
configuring cipher suites for other versions will have no effect.
<br/>

NOTE: PSK ciphers are suppressed by 'tlsv1.3' version config<br/>
If PSK cipher suites are intended, 'tlsv1.3' should be disabled from <code>versions</code>.<br/>
PSK cipher suites: <code>"RSA-PSK-AES256-GCM-SHA384,RSA-PSK-AES256-CBC-SHA384,
RSA-PSK-AES128-GCM-SHA256,RSA-PSK-AES128-CBC-SHA256,
RSA-PSK-AES256-CBC-SHA,RSA-PSK-AES128-CBC-SHA,
RSA-PSK-DES-CBC3-SHA,RSA-PSK-RC4-SHA"</code>

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[string()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>user_lookup_fun</h4>
EMQX-internal callback that is used to lookup pre-shared key (PSK) identity.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"emqx_tls_psk:lookup"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>secure_renegotiate</h4>
SSL parameter renegotiation is a feature that allows a client and a server
to renegotiate the parameters of the SSL connection on the fly.
RFC 5746 defines a more secure way of doing this. By enabling secure renegotiation,
you drop support for the insecure renegotiation, prone to MitM attacks.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>hibernate_after</h4>
 Hibernate the SSL process after idling for amount of time reducing its memory footprint. 

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Enable TLS.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>server_name_indication</h4>
Specify the host name to be used in TLS Server Name Indication extension.<br/>
For instance, when connecting to "server.example.net", the genuine server
which accepts the connection and performs TLS handshake may differ from the
host the TLS client initially connects to, e.g. when connecting to an IP address
or when the host has multiple resolvable DNS records <br/>
If not specified, it will default to the host name string which is used
to establish the connection, unless it is IP addressed used.<br/>
The host name is then also used in the host name verification of the peer
certificate.<br/> The special value 'disable' prevents the Server Name
Indication extension from being sent and disables the hostname
verification check.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>disable | string()</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:stats <a id='broker-stats'></a>
Enable/disable statistic data collection.
Statistic data such as message receive/send count/rate etc. It provides insights of system performance and helps to diagnose issues. You can find statistic data from the dashboard, or from the '/stats' API.

| Config paths | Env overrides |
|--------------------|-------------------------|
|  <code>stats</code> | <code>EMQX_STATS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable/disable statistic data collection.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:sys_topics <a id='broker-sys_topics'></a>
The EMQX Broker periodically publishes its own status, message statistics,
client online and offline events to the system topic starting with `$SYS/`.

The following options control the behavior of `$SYS` topics.

| Config paths | Env overrides |
|-------------------------|------------------------------|
|  <code>sys_topics</code> | <code>EMQX_SYS_TOPICS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>sys_msg_interval</h4>
Time interval of publishing `$SYS` messages.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>disabled | emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1m"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>sys_heartbeat_interval</h4>
Time interval for publishing following heartbeat messages:
  - `$SYS/brokers/<node>/uptime`
  - `$SYS/brokers/<node>/datetime`

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>disabled | emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>sys_event_messages</h4>
Client events messages.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-event_names">broker:event_names</a></code></td></tr></tbody>
</table>
</li>

</ul>

## broker:sysmon <a id='broker-sysmon'></a>
Features related to system monitoring and introspection.

| Config paths | Env overrides |
|---------------------|--------------------------|
|  <code>sysmon</code> | <code>EMQX_SYSMON</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>vm</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-sysmon_vm">broker:sysmon_vm</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>os</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-sysmon_os">broker:sysmon_os</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>top</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-sysmon_top">broker:sysmon_top</a></code></td></tr></tbody>
</table>
</li>

</ul>

## broker:sysmon_os <a id='broker-sysmon_os'></a>
This part of the configuration is responsible for monitoring
 the host OS health, such as free memory, disk space, CPU load, etc.

| Config paths | Env overrides |
|------------------------|------------------------------|
|  <code>sysmon.os</code> | <code>EMQX_SYSMON__OS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>cpu_check_interval</h4>
The time interval for the periodic CPU check.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"60s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>cpu_high_watermark</h4>
The threshold, as percentage of system CPU load,
 for how much system cpu can be used before the corresponding alarm is raised.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:percent()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"80%"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>cpu_low_watermark</h4>
The threshold, as percentage of system CPU load,
 for how much system cpu can be used before the corresponding alarm is cleared.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:percent()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"60%"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mem_check_interval</h4>
The time interval for the periodic memory check.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>disabled | emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"60s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>sysmem_high_watermark</h4>
The threshold, as percentage of system memory,
 for how much system memory can be allocated before the corresponding alarm is raised.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:percent()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"70%"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>procmem_high_watermark</h4>
The threshold, as percentage of system memory,
 for how much system memory can be allocated by one Erlang process before
 the corresponding alarm is raised.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:percent()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5%"</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:sysmon_top <a id='broker-sysmon_top'></a>
This part of the configuration is responsible for monitoring
 the Erlang processes in the VM. This information can be sent to an external
 PostgreSQL database. This feature is inactive unless the PostgreSQL sink is configured.

| Config paths | Env overrides |
|-------------------------|-------------------------------|
|  <code>sysmon.top</code> | <code>EMQX_SYSMON__TOP</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>num_items</h4>
The number of top processes per monitoring group

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>10</code></td></tr></tbody>
</table>
</li>
<li>
<h4>sample_interval</h4>
Specifies how often process top should be collected

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"2s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_procs</h4>
Stop collecting data when the number of processes
in the VM exceeds this value

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1000000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>db_hostname</h4>
Hostname of the PostgreSQL database that collects the data points

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>
<li>
<h4>db_port</h4>
Port of the PostgreSQL database that collects the data points.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>5432</code></td></tr></tbody>
</table>
</li>
<li>
<h4>db_username</h4>
Username of the PostgreSQL database

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"system_monitor"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>db_password</h4>
EMQX user password in the PostgreSQL database

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"system_monitor_password"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>db_name</h4>
PostgreSQL database name

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"postgres"</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:sysmon_vm <a id='broker-sysmon_vm'></a>
This part of the configuration is responsible for collecting
 BEAM VM events, such as long garbage collection, traffic congestion in the inter-broker
 communication, etc.

| Config paths | Env overrides |
|------------------------|------------------------------|
|  <code>sysmon.vm</code> | <code>EMQX_SYSMON__VM</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>process_check_interval</h4>
The time interval for the periodic process limit check.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>process_high_watermark</h4>
The threshold, as percentage of processes, for how many
 processes can simultaneously exist at the local node before the corresponding
 alarm is raised.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:percent()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"80%"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>process_low_watermark</h4>
The threshold, as percentage of processes, for how many
 processes can simultaneously exist at the local node before the corresponding
 alarm is cleared.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:percent()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"60%"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>long_gc</h4>
When an Erlang process spends long time to perform garbage collection, a warning level <code>long_gc</code> log is emitted,
and an MQTT message is published to the system topic <code>$SYS/sysmon/long_gc</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>disabled | emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>disabled</code></td></tr></tbody>
</table>
</li>
<li>
<h4>long_schedule</h4>
When the Erlang VM detect a task scheduled for too long, a warning level 'long_schedule' log is emitted,
and an MQTT message is published to the system topic <code>$SYS/sysmon/long_schedule</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>disabled | emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"240ms"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>large_heap</h4>
When an Erlang process consumed a large amount of memory for its heap space,
the system will write a warning level <code>large_heap</code> log, and an MQTT message is published to
the system topic <code>$SYS/sysmon/large_heap</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>disabled | emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"32MB"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>busy_dist_port</h4>
When the RPC connection used to communicate with other nodes in the cluster is overloaded,
there will be a <code>busy_dist_port</code> warning log,
and an MQTT message is published to system topic <code>$SYS/sysmon/busy_dist_port</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>busy_port</h4>
When a port (e.g. TCP socket) is overloaded, there will be a <code>busy_port</code> warning log,
and an MQTT message is published to the system topic <code>$SYS/sysmon/busy_port</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:tcp_opts <a id='broker-tcp_opts'></a>
TCP listener options.

| Config paths | Env overrides |
|--------------------------------------------------------------|------------------------------------------------------------------------|
|  <code>gateway.exproto.listeners.ssl.$name.tcp_options</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__TCP_OPTIONS</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.tcp_options</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__TCP_OPTIONS</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.tcp_options</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__TCP_OPTIONS</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.tcp_options</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__TCP_OPTIONS</code>  |
|  <code>listeners.ssl.$name.tcp_options</code> | <code>EMQX_LISTENERS__SSL__$NAME__TCP_OPTIONS</code>  |
|  <code>listeners.tcp.$name.tcp_options</code> | <code>EMQX_LISTENERS__TCP__$NAME__TCP_OPTIONS</code>  |
|  <code>listeners.ws.$name.tcp_options</code> | <code>EMQX_LISTENERS__WS__$NAME__TCP_OPTIONS</code>  |
|  <code>listeners.wss.$name.tcp_options</code> | <code>EMQX_LISTENERS__WSS__$NAME__TCP_OPTIONS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>active_n</h4>
Specify the {active, N} option for this Socket.<br/>
See: https://erlang.org/doc/man/inet.html#setopts-2

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>100</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backlog</h4>
TCP backlog defines the maximum length that the queue of
pending connections can grow to.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1024</code></td></tr></tbody>
</table>
</li>
<li>
<h4>send_timeout</h4>
The TCP send timeout for the connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>send_timeout_close</h4>
Close the connection if send timeout.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>recbuf</h4>
The TCP receive buffer (OS kernel) for the connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>sndbuf</h4>
The TCP send buffer (OS kernel) for the connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>buffer</h4>
The size of the user-space buffer used by the driver.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"4KB"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>high_watermark</h4>
The socket is set to a busy state when the amount of data queued internally
by the VM socket implementation reaches this limit.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1MB"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>nodelay</h4>
The TCP_NODELAY flag for the connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>reuseaddr</h4>
The SO_REUSEADDR flag for the connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:trace <a id='broker-trace'></a>
Real-time filtering logs for the ClientID or Topic or IP for debugging.

| Config paths | Env overrides |
|--------------------|-------------------------|
|  <code>trace</code> | <code>EMQX_TRACE</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>payload_encode</h4>
Determine the format of the payload format in the trace file.<br/>
`text`: Text-based protocol or plain text protocol.
 It is recommended when payload is JSON encoded.<br/>
`hex`: Binary hexadecimal encode. It is recommended when payload is a custom binary protocol.<br/>
`hidden`: payload is obfuscated as `******`

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>hex | text | hidden</code></td></tr><tr><td><strong>Default</strong></td><td><code>text</code></td></tr></tbody>
</table>
</li>

</ul>

## broker:ws_opts <a id='broker-ws_opts'></a>
WebSocket listener options.

| Config paths | Env overrides |
|--------------------------------------------|----------------------------------------------------|
|  <code>listeners.ws.$name.websocket</code> | <code>EMQX_LISTENERS__WS__$NAME__WEBSOCKET</code>  |
|  <code>listeners.wss.$name.websocket</code> | <code>EMQX_LISTENERS__WSS__$NAME__WEBSOCKET</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>mqtt_path</h4>
WebSocket's MQTT protocol path. So the address of EMQX Broker's WebSocket is:
<code>ws://{ip}:{port}/mqtt</code>

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"/mqtt"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mqtt_piggyback</h4>
Whether a WebSocket message is allowed to contain multiple MQTT packets.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>single | multiple</code></td></tr><tr><td><strong>Default</strong></td><td><code>multiple</code></td></tr></tbody>
</table>
</li>
<li>
<h4>compress</h4>
If <code>true</code>, compress WebSocket messages using <code>zlib</code>.<br/>
The configuration items under <code>deflate_opts</code> belong to the compression-related parameter configuration.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>idle_timeout</h4>
Close transport-layer connections from the clients that have not sent MQTT CONNECT message within this interval.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"7200s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_frame_size</h4>
The maximum length of a single MQTT packet.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>infinity | integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>infinity</code></td></tr></tbody>
</table>
</li>
<li>
<h4>fail_if_no_subprotocol</h4>
If <code>true</code>, the server will return an error when
 the client does not carry the <code>Sec-WebSocket-Protocol</code> field.
 <br/>Note: WeChat applet needs to disable this verification.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>supported_subprotocols</h4>
Comma-separated list of supported subprotocols.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:comma_separated_list()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"mqtt, mqtt-v3, mqtt-v3.1.1, mqtt-v5"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>check_origin_enable</h4>
If <code>true</code>, <code>origin</code> HTTP header will be
 validated against the list of allowed origins configured in <code>check_origins</code>
 parameter.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>allow_origin_absence</h4>
If <code>false</code> and <code>check_origin_enable</code> is
 <code>true</code>, the server will reject requests that don't have <code>origin</code>
 HTTP header.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>check_origins</h4>
List of allowed origins.<br/>See <code>check_origin_enable</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:comma_separated_binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"http://localhost:18083, http://127.0.0.1:18083"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_address_header</h4>
HTTP header used to pass information about the client IP address.
Relevant when the EMQX cluster is deployed behind a load-balancer.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"x-forwarded-for"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_port_header</h4>
HTTP header used to pass information about the client port. Relevant when the EMQX cluster is deployed behind a load-balancer.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"x-forwarded-port"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>deflate_opts</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-deflate_opts">broker:deflate_opts</a></code></td></tr></tbody>
</table>
</li>

</ul>

## broker:zone <a id='broker-zone'></a>
A `Zone` defines a set of configuration items (such as the maximum number of connections) that can be shared between multiple listeners.

`Listener` can refer to a `Zone` through the configuration item <code>listener.\<Protocol>.\<Listener Name>.zone</code>.

The configs defined in the zones will override the global configs with the same key.

For example, given the following config:
```
a {
    b: 1, c: 1
}
zone.my_zone {
  a {
    b:2
  }
}
```

The global config `a` is overridden by the configs `a` inside the zone `my_zone`.

If there is a listener using the zone `my_zone`, the value of config `a` will be: `{b:2, c: 1}`.
Note that although the default value of `a.c` is `0`, the global value is used, i.e. configs in the zone have no default values. To override `a.c` one must configure it explicitly in the zone.

All the global configs that can be overridden in zones are:
 - `stats.*`
 - `mqtt.*`
 - `authorization.*`
 - `flapping_detect.*`
 - `force_shutdown.*`
 - `conn_congestion.*`
 - `force_gc.*`



| Config paths | Env overrides |
|--------------------------|--------------------------------|
|  <code>zones.$name</code> | <code>EMQX_ZONES__$NAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>mqtt</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#zone-mqtt">zone:mqtt</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>stats</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#zone-stats">zone:stats</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>flapping_detect</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#zone-flapping_detect">zone:flapping_detect</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>force_shutdown</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#zone-force_shutdown">zone:force_shutdown</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>conn_congestion</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#zone-conn_congestion">zone:conn_congestion</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>force_gc</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#zone-force_gc">zone:force_gc</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>overload_protection</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#zone-overload_protection">zone:overload_protection</a></code></td></tr></tbody>
</table>
</li>

</ul>

## cluster_dns <a id='cluster_dns'></a>
Service discovery via DNS SRV records.

| Config paths | Env overrides |
|--------------------------|--------------------------------|
|  <code>cluster.dns</code> | <code>EMQX_CLUSTER__DNS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>name</h4>
The domain name from which to discover peer EMQX nodes' IP addresses.
Applicable when <code>cluster.discovery_strategy = dns</code>

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"localhost"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>record_type</h4>
DNS record type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>a | srv</code></td></tr><tr><td><strong>Default</strong></td><td><code>a</code></td></tr></tbody>
</table>
</li>

</ul>

## cluster_etcd <a id='cluster_etcd'></a>
Service discovery using 'etcd' service.

| Config paths | Env overrides |
|---------------------------|---------------------------------|
|  <code>cluster.etcd</code> | <code>EMQX_CLUSTER__ETCD</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>server</h4>
List of endpoint URLs of the etcd cluster

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:comma_separated_list()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>prefix</h4>
Key prefix used for EMQX service discovery.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"emqxcl"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>node_ttl</h4>
Expiration time of the etcd key associated with the node.
It is refreshed automatically, as long as the node is alive.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1m"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>
Options for the TLS connection to the etcd cluster.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-ssl_client_opts">broker:ssl_client_opts</a></code></td></tr></tbody>
</table>
</li>

</ul>

## cluster_k8s <a id='cluster_k8s'></a>
Service discovery via Kubernetes API server.

| Config paths | Env overrides |
|--------------------------|--------------------------------|
|  <code>cluster.k8s</code> | <code>EMQX_CLUSTER__K8S</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>apiserver</h4>
Kubernetes API endpoint URL.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"http://10.110.111.204:8080"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>service_name</h4>
EMQX broker service name.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"emqx"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>address_type</h4>
Address type used for connecting to the discovered nodes.
Setting <code>cluster.k8s.address_type</code> to <code>ip</code> will
make EMQX to discover IP addresses of peer nodes from Kubernetes API.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>ip | dns | hostname</code></td></tr><tr><td><strong>Default</strong></td><td><code>ip</code></td></tr></tbody>
</table>
</li>
<li>
<h4>namespace</h4>
Kubernetes namespace.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"default"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>suffix</h4>
Node name suffix.<br/>
Note: this parameter is only relevant when <code>address_type</code> is <code>dns</code>
or <code>hostname</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"pod.local"</code></td></tr></tbody>
</table>
</li>

</ul>

## cluster_mcast <a id='cluster_mcast'></a>
Service discovery via UDP multicast.

| Config paths | Env overrides |
|----------------------------|----------------------------------|
|  <code>cluster.mcast</code> | <code>EMQX_CLUSTER__MCAST</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>addr</h4>
Multicast IPv4 address.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"239.192.0.1"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ports</h4>
List of UDP ports used for service discovery.<br/>
Note: probe messages are broadcast to all the specified ports.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[integer()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[4369,4370]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>iface</h4>
Local IP address the node discovery service needs to bind to.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"0.0.0.0"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ttl</h4>
Time-to-live (TTL) for the outgoing UDP datagrams.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>0..255</code></td></tr><tr><td><strong>Default</strong></td><td><code>255</code></td></tr></tbody>
</table>
</li>
<li>
<h4>loop</h4>
If <code>true</code>, loop UDP datagrams back to the local socket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>sndbuf</h4>
Size of the kernel-level buffer for outgoing datagrams.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"16KB"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>recbuf</h4>
Size of the kernel-level buffer for incoming datagrams.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"16KB"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>buffer</h4>
Size of the user-level buffer.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"32KB"</code></td></tr></tbody>
</table>
</li>

</ul>

## cluster_static <a id='cluster_static'></a>
Service discovery via static nodes.
The new node joins the cluster by connecting to one of the bootstrap nodes.

| Config paths | Env overrides |
|-----------------------------|-----------------------------------|
|  <code>cluster.static</code> | <code>EMQX_CLUSTER__STATIC</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>seeds</h4>
List EMQX node names in the static cluster. See <code>node.name</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[atom()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>

</ul>

## authorization <a id='authorization'></a>
Settings that control client authorization.

| Config paths | Env overrides |
|----------------------------|---------------------------------|
|  <code>authorization</code> | <code>EMQX_AUTHORIZATION</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>no_match</h4>
Default access control action if the user or client matches no ACL rules,
or if no such user or client is found by the configurable authorization
sources such as built_in_database, an HTTP API, or a query against PostgreSQL.
Find more details in 'authorization.sources' config.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>allow | deny</code></td></tr><tr><td><strong>Default</strong></td><td><code>allow</code></td></tr></tbody>
</table>
</li>
<li>
<h4>deny_action</h4>
The action when the authorization check rejects an operation.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>ignore | disconnect</code></td></tr><tr><td><strong>Default</strong></td><td><code>ignore</code></td></tr></tbody>
</table>
</li>
<li>
<h4>cache</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="broker-authz_cache">broker:authz_cache</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>sources</h4>
Authorization data sources.<br/>
An array of authorization (ACL) data providers.
It is designed as an array, not a hash-map, so the sources can be
ordered to form a chain of access controls.<br/>

When authorizing a 'publish' or 'subscribe' action, the configured
sources are checked in order. When checking an ACL source,
in case the client (identified by username or client ID) is not found,
it moves on to the next source. And it stops immediately
once an 'allow' or 'deny' decision is returned.<br/>

If the client is not found in any of the sources,
the default action configured in 'authorization.no_match' is applied.<br/>

NOTE:
The source elements are identified by their 'type'.
It is NOT allowed to configure two or more sources of the same type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[<a href="authz.md#authz-file">authz:file</a> | <a href="authz.md#authz-http_get">authz:http_get</a> | <a href="authz.md#authz-http_post">authz:http_post</a> | <a href="authz.md#authz-mnesia">authz:mnesia</a> | <a href="authz.md#authz-mongo_single">authz:mongo_single</a> | <a href="authz.md#authz-mongo_rs">authz:mongo_rs</a> | <a href="authz.md#authz-mongo_sharded">authz:mongo_sharded</a> | <a href="authz.md#authz-mysql">authz:mysql</a> | <a href="authz.md#authz-postgresql">authz:postgresql</a> | <a href="authz.md#authz-redis_single">authz:redis_single</a> | <a href="authz.md#authz-redis_sentinel">authz:redis_sentinel</a> | <a href="authz.md#authz-redis_cluster">authz:redis_cluster</a>]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>

</ul>

## cluster <a id='cluster'></a>
EMQX nodes can form a cluster to scale up the total capacity.<br/>
      Here holds the configs to instruct how individual nodes can discover each other.

| Config paths | Env overrides |
|----------------------|---------------------------|
|  <code>cluster</code> | <code>EMQX_CLUSTER</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>name</h4>
Human-friendly name of the EMQX cluster.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>atom()</code></td></tr><tr><td><strong>Default</strong></td><td><code>emqxcl</code></td></tr></tbody>
</table>
</li>
<li>
<h4>discovery_strategy</h4>
Service discovery method for the cluster nodes. Possible values are:
- manual: Use <code>emqx ctl cluster</code> command to manage cluster.<br/>
- static: Configure static nodes list by setting <code>seeds</code> in config file.<br/>
- dns: Use DNS A record to discover peer nodes.<br/>
- etcd: Use etcd to discover peer nodes.<br/>
- k8s: Use Kubernetes API to discover peer pods.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>manual | static | mcast | dns | etcd | k8s</code></td></tr><tr><td><strong>Default</strong></td><td><code>manual</code></td></tr></tbody>
</table>
</li>
<li>
<h4>core_nodes</h4>
List of core nodes that the replicant will connect to.<br/>
Note: this parameter only takes effect when the <code>backend</code> is set
to <code>rlog</code> and the <code>role</code> is set to <code>replicant</code>.<br/>
This value needs to be defined for manual or static cluster discovery mechanisms.<br/>
If an automatic cluster discovery mechanism is being used (such as <code>etcd</code>),
there is no need to set this value.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:comma_separated_atoms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>autoclean</h4>
Remove disconnected nodes from the cluster after this interval.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5m"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>autoheal</h4>
If <code>true</code>, the node will try to heal network partitions automatically.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proto_dist</h4>
The Erlang distribution protocol for the cluster.<br/>
- inet_tcp: IPv4 TCP <br/>
- inet_tls: IPv4 TLS, works together with <code>etc/ssl_dist.conf</code>

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>inet_tcp | inet6_tcp | inet_tls</code></td></tr><tr><td><strong>Default</strong></td><td><code>inet_tcp</code></td></tr></tbody>
</table>
</li>
<li>
<h4>static</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="cluster_static">cluster_static</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>mcast</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="cluster_mcast">cluster_mcast</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>dns</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="cluster_dns">cluster_dns</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>etcd</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="cluster_etcd">cluster_etcd</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>k8s</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="cluster_k8s">cluster_k8s</a></code></td></tr></tbody>
</table>
</li>

</ul>

## cluster_call <a id='cluster_call'></a>
Options for the 'cluster call' feature that allows to execute a callback on all nodes in the cluster.

| Config paths | Env overrides |
|--------------------------------|--------------------------------------|
|  <code>node.cluster_call</code> | <code>EMQX_NODE__CLUSTER_CALL</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>retry_interval</h4>
Time interval to retry after a failed call.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1m"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_history</h4>
Retain the maximum number of completed transactions (for queries).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1..500</code></td></tr><tr><td><strong>Default</strong></td><td><code>100</code></td></tr></tbody>
</table>
</li>
<li>
<h4>cleanup_interval</h4>
Time interval to clear completed but stale transactions.
Ensure that the number of completed transactions is less than the <code>max_history</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5m"</code></td></tr></tbody>
</table>
</li>

</ul>

## console_handler <a id='console_handler'></a>
Log handler that prints log events to the EMQX console.

| Config paths | Env overrides |
|----------------------------------|----------------------------------------|
|  <code>log.console_handler</code> | <code>EMQX_LOG__CONSOLE_HANDLER</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable this log handler.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>level</h4>
The log level for the current log handler.
Defaults to warning.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_conf_schema:log_level()</code></td></tr><tr><td><strong>Default</strong></td><td><code>warning</code></td></tr></tbody>
</table>
</li>
<li>
<h4>time_offset</h4>
The time offset to be used when formatting the timestamp.
Can be one of:
  - <code>system</code>: the time offset used by the local system
  - <code>utc</code>: the UTC time offset
  - <code>+-[hh]:[mm]</code>: user specified time offset, such as "-02:00" or "+00:00"
Defaults to: <code>system</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"system"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>chars_limit</h4>
Set the maximum length of a single log message. If this length is exceeded, the log message will be truncated.
NOTE: Restrict char limiter if formatter is JSON , it will get a truncated incomplete JSON data, which is not recommended.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>unlimited | 100..inf</code></td></tr><tr><td><strong>Default</strong></td><td><code>unlimited</code></td></tr></tbody>
</table>
</li>
<li>
<h4>formatter</h4>
Choose log formatter. <code>text</code> for free text, and <code>json</code> for structured logging.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>text | json</code></td></tr><tr><td><strong>Default</strong></td><td><code>text</code></td></tr></tbody>
</table>
</li>
<li>
<h4>single_line</h4>
Print logs in a single line if set to true. Otherwise, log messages may span multiple lines.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>sync_mode_qlen</h4>
As long as the number of buffered log events is lower than this value,
all log events are handled asynchronously. This means that the client process sending the log event,
by calling a log function in the Logger API, does not wait for a response from the handler
but continues executing immediately after the event is sent.
It is not affected by the time it takes the handler to print the event to the log device.
If the message queue grows larger than this value,
the handler starts handling log events synchronously instead,
meaning that the client process sending the event must wait for a response.
When the handler reduces the message queue to a level below the sync_mode_qlen threshold,
asynchronous operation is resumed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>100</code></td></tr></tbody>
</table>
</li>
<li>
<h4>drop_mode_qlen</h4>
When the number of buffered log events is larger than this value, the new log events are dropped.
When drop mode is activated or deactivated, a message is printed in the logs.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>3000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>flush_qlen</h4>
If the number of buffered log events grows larger than this threshold, a flush (delete) operation takes place.
To flush events, the handler discards the buffered log messages without logging.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>overload_kill</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="log_overload_kill">log_overload_kill</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>burst_limit</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="log_burst_limit">log_burst_limit</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>supervisor_reports</h4>
Type of supervisor reports that are logged. Defaults to <code>error</code><br/>
  - <code>error</code>: only log errors in the Erlang processes<br/>.
  - <code>progress</code>: log process startup.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>error | progress</code></td></tr><tr><td><strong>Default</strong></td><td><code>error</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_depth</h4>
Maximum depth for Erlang term log formatting and Erlang process message queue inspection.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>unlimited | non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>100</code></td></tr></tbody>
</table>
</li>

</ul>

## log <a id='log'></a>
EMQX logging supports multiple sinks for the log events.
Each sink is represented by a _log handler_, which can be configured independently.

| Config paths | Env overrides |
|------------------|-----------------------|
|  <code>log</code> | <code>EMQX_LOG</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>console_handler</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="console_handler">console_handler</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>file_handlers</h4>
File-based log handlers.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="log_file_handler">log_file_handler</a>}</code></td></tr></tbody>
</table>
</li>

</ul>

## log_burst_limit <a id='log_burst_limit'></a>
Large bursts of log events produced in a short time can potentially cause problems, such as:
 - Log files grow very large
 - Log files are rotated too quickly, and useful information gets overwritten
 - Overall performance impact on the system

Log burst limit feature can temporarily disable logging to avoid these issues.

| Config paths | Env overrides |
|--------------------------------------------------|----------------------------------------------------------|
|  <code>log.console_handler.burst_limit</code> | <code>EMQX_LOG__CONSOLE_HANDLER__BURST_LIMIT</code>  |
|  <code>log.file_handlers.$name.burst_limit</code> | <code>EMQX_LOG__FILE_HANDLERS__$NAME__BURST_LIMIT</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable log burst control feature.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_count</h4>
Maximum number of log events to handle within a `window_time` interval. After the limit is reached, successive events are dropped until the end of the `window_time`.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>10000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>window_time</h4>
See <code>max_count</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1s"</code></td></tr></tbody>
</table>
</li>

</ul>

## log_file_handler <a id='log_file_handler'></a>
Log handler that prints log events to files.

| Config paths | Env overrides |
|--------------------------------------|---------------------------------------------|
|  <code>log.file_handlers.$name</code> | <code>EMQX_LOG__FILE_HANDLERS__$NAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>file</h4>
Name the log file.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_conf_schema:file()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>rotation</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="log_rotation">log_rotation</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_size</h4>
This parameter controls log file rotation. The value `infinity` means the log file will grow indefinitely, otherwise the log file will be rotated once it reaches `max_size` in bytes.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>infinity | emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"50MB"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Enable this log handler.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>level</h4>
The log level for the current log handler.
Defaults to warning.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_conf_schema:log_level()</code></td></tr><tr><td><strong>Default</strong></td><td><code>warning</code></td></tr></tbody>
</table>
</li>
<li>
<h4>time_offset</h4>
The time offset to be used when formatting the timestamp.
Can be one of:
  - <code>system</code>: the time offset used by the local system
  - <code>utc</code>: the UTC time offset
  - <code>+-[hh]:[mm]</code>: user specified time offset, such as "-02:00" or "+00:00"
Defaults to: <code>system</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"system"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>chars_limit</h4>
Set the maximum length of a single log message. If this length is exceeded, the log message will be truncated.
NOTE: Restrict char limiter if formatter is JSON , it will get a truncated incomplete JSON data, which is not recommended.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>unlimited | 100..inf</code></td></tr><tr><td><strong>Default</strong></td><td><code>unlimited</code></td></tr></tbody>
</table>
</li>
<li>
<h4>formatter</h4>
Choose log formatter. <code>text</code> for free text, and <code>json</code> for structured logging.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>text | json</code></td></tr><tr><td><strong>Default</strong></td><td><code>text</code></td></tr></tbody>
</table>
</li>
<li>
<h4>single_line</h4>
Print logs in a single line if set to true. Otherwise, log messages may span multiple lines.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>sync_mode_qlen</h4>
As long as the number of buffered log events is lower than this value,
all log events are handled asynchronously. This means that the client process sending the log event,
by calling a log function in the Logger API, does not wait for a response from the handler
but continues executing immediately after the event is sent.
It is not affected by the time it takes the handler to print the event to the log device.
If the message queue grows larger than this value,
the handler starts handling log events synchronously instead,
meaning that the client process sending the event must wait for a response.
When the handler reduces the message queue to a level below the sync_mode_qlen threshold,
asynchronous operation is resumed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>100</code></td></tr></tbody>
</table>
</li>
<li>
<h4>drop_mode_qlen</h4>
When the number of buffered log events is larger than this value, the new log events are dropped.
When drop mode is activated or deactivated, a message is printed in the logs.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>3000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>flush_qlen</h4>
If the number of buffered log events grows larger than this threshold, a flush (delete) operation takes place.
To flush events, the handler discards the buffered log messages without logging.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>overload_kill</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="log_overload_kill">log_overload_kill</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>burst_limit</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="log_burst_limit">log_burst_limit</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>supervisor_reports</h4>
Type of supervisor reports that are logged. Defaults to <code>error</code><br/>
  - <code>error</code>: only log errors in the Erlang processes<br/>.
  - <code>progress</code>: log process startup.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>error | progress</code></td></tr><tr><td><strong>Default</strong></td><td><code>error</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_depth</h4>
Maximum depth for Erlang term log formatting and Erlang process message queue inspection.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>unlimited | non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>100</code></td></tr></tbody>
</table>
</li>

</ul>

## log_overload_kill <a id='log_overload_kill'></a>
Log overload kill features an overload protection that activates when the log handlers use too much memory or have too many buffered log messages.<br/>
When the overload is detected, the log handler is terminated and restarted after a cooldown period.

| Config paths | Env overrides |
|----------------------------------------------------|------------------------------------------------------------|
|  <code>log.console_handler.overload_kill</code> | <code>EMQX_LOG__CONSOLE_HANDLER__OVERLOAD_KILL</code>  |
|  <code>log.file_handlers.$name.overload_kill</code> | <code>EMQX_LOG__FILE_HANDLERS__$NAME__OVERLOAD_KILL</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable log handler overload kill feature.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mem_size</h4>
Maximum memory size that the log handler process is allowed to use.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30MB"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>qlen</h4>
Maximum allowed queue length.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>20000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>restart_after</h4>
The handler restarts automatically after a delay in the event of termination, unless the value `infinity` is set, which blocks any subsequent restarts.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms() | infinity</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5s"</code></td></tr></tbody>
</table>
</li>

</ul>

## log_rotation <a id='log_rotation'></a>
By default, the logs are stored in `./log` directory (for installation from zip file) or in `/var/log/emqx` (for binary installation).<br/>
This section of the configuration controls the number of files kept for each log handler.

| Config paths | Env overrides |
|-----------------------------------------------|-------------------------------------------------------|
|  <code>log.file_handlers.$name.rotation</code> | <code>EMQX_LOG__FILE_HANDLERS__$NAME__ROTATION</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable log rotation feature.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>count</h4>
Maximum number of log files.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1..2048</code></td></tr><tr><td><strong>Default</strong></td><td><code>10</code></td></tr></tbody>
</table>
</li>

</ul>

## node <a id='node'></a>
Node name, cookie, config & data directories and the Erlang virtual machine (BEAM) boot parameters.

| Config paths | Env overrides |
|-------------------|------------------------|
|  <code>node</code> | <code>EMQX_NODE</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>name</h4>
Unique name of the EMQX node. It must follow <code>%name%@FQDN</code> or
<code>%name%@IPv4</code> format.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"emqx@127.0.0.1"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>cookie</h4>
Secret cookie is a random string that should be the same on all nodes in
the given EMQX cluster, but unique per EMQX cluster. It is used to prevent EMQX nodes that
belong to different clusters from accidentally connecting to each other.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>process_limit</h4>
Maximum number of simultaneously existing processes for this Erlang system.
The actual maximum chosen may be much larger than the Number passed.
For more information, see: https://www.erlang.org/doc/man/erl.html

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1024..134217727</code></td></tr><tr><td><strong>Default</strong></td><td><code>2097152</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_ports</h4>
Maximum number of simultaneously existing ports for this Erlang system.
The actual maximum chosen may be much larger than the Number passed.
For more information, see: https://www.erlang.org/doc/man/erl.html

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1024..134217727</code></td></tr><tr><td><strong>Default</strong></td><td><code>1048576</code></td></tr></tbody>
</table>
</li>
<li>
<h4>dist_buffer_size</h4>
Erlang's distribution buffer busy limit in kilobytes.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1..2097151</code></td></tr><tr><td><strong>Default</strong></td><td><code>8192</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_ets_tables</h4>
Max number of ETS tables

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>262144</code></td></tr></tbody>
</table>
</li>
<li>
<h4>data_dir</h4>
Path to the persistent data directory.<br/>
Possible auto-created subdirectories are:<br/>
- `mnesia/<node_name>`: EMQX's built-in database directory.<br/>
For example, `mnesia/emqx@127.0.0.1`.<br/>
There should be only one such subdirectory.<br/>
Meaning, in case the node is to be renamed (to e.g. `emqx@10.0.1.1`),<br/>
the old dir should be deleted first.<br/>
- `configs`: Generated configs at boot time, and cluster/local override configs.<br/>
- `patches`: Hot-patch beam files are to be placed here.<br/>
- `trace`: Trace log files.<br/>

**NOTE**: One data dir cannot be shared by two or more EMQX nodes.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>global_gc_interval</h4>
Periodic garbage collection interval. Set to <code>disabled</code> to have it disabled.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>disabled | emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15m"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>crash_dump_file</h4>
Location of the crash dump file.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_conf_schema:file()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"log/erl_crash.dump"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>crash_dump_seconds</h4>
This variable gives the number of seconds that the emulator is allowed to spend writing a crash dump. When the given number of seconds have elapsed, the emulator is terminated.<br/>
- If setting to 0 seconds, the runtime system does not even attempt to write the crash dump file. It only terminates.<br/>
- If setting to a positive value S, wait for S seconds to complete the crash dump file and then terminates the runtime system with a SIGALRM signal.<br/>
- A negative value causes the termination of the runtime system to wait indefinitely until the crash dump file has been completely written.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_s()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>crash_dump_bytes</h4>
This variable sets the maximum size of a crash dump file in bytes.
The crash dump will be truncated if this limit is exceeded.
If setting it to 0, the runtime system does not even attempt to write a crash dump file.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"100MB"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>dist_net_ticktime</h4>
This is the approximate time an EMQX node may be unresponsive until it is considered down and thereby disconnected.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_s()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"2m"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backtrace_depth</h4>
Maximum depth of the call stack printed in error messages and
<code>process_info</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>23</code></td></tr></tbody>
</table>
</li>
<li>
<h4>applications</h4>
List of Erlang applications that shall be rebooted when the EMQX broker joins the cluster.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:comma_separated_atoms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>etc_dir</h4>
Deprecated since 5.0.8.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>cluster_call</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="cluster_call">cluster_call</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>db_backend</h4>
Select the backend for the embedded database.<br/>
<code>rlog</code> is the default backend,
that is suitable for very large clusters.<br/>
<code>mnesia</code> is a backend that offers decent performance in small clusters.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>mnesia | rlog</code></td></tr><tr><td><strong>Default</strong></td><td><code>rlog</code></td></tr></tbody>
</table>
</li>
<li>
<h4>db_role</h4>
Select a node role.<br/>
<code>core</code> nodes provide durability of the data, and take care of writes.
It is recommended to place core nodes in different racks or different availability zones.<br/>
<code>replicant</code> nodes are ephemeral worker nodes. Removing them from the cluster
doesn't affect database redundancy<br/>
It is recommended to have more replicant nodes than core nodes.<br/>
Note: this parameter only takes effect when the <code>backend</code> is set
to <code>rlog</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>core | replicant</code></td></tr><tr><td><strong>Default</strong></td><td><code>core</code></td></tr></tbody>
</table>
</li>
<li>
<h4>rpc_module</h4>
Protocol used for pushing transaction logs to the replicant nodes.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>gen_rpc | rpc</code></td></tr><tr><td><strong>Default</strong></td><td><code>gen_rpc</code></td></tr></tbody>
</table>
</li>
<li>
<h4>tlog_push_mode</h4>
In sync mode the core node waits for an ack from the replicant nodes before sending the next
transaction log entry.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>sync | async</code></td></tr><tr><td><strong>Default</strong></td><td><code>async</code></td></tr></tbody>
</table>
</li>

</ul>

## rpc <a id='rpc'></a>
EMQX uses a library called <code>gen_rpc</code> for inter-broker communication.<br/>
Most of the time the default config should work,
but in case you need to do performance fine-tuning or experiment a bit,
this is where to look.

| Config paths | Env overrides |
|------------------|-----------------------|
|  <code>rpc</code> | <code>EMQX_RPC</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>mode</h4>
In <code>sync</code> mode the sending side waits for the ack from the receiving side.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>sync | async</code></td></tr><tr><td><strong>Default</strong></td><td><code>async</code></td></tr></tbody>
</table>
</li>
<li>
<h4>driver</h4>
Transport protocol used for inter-broker communication

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>tcp | ssl</code></td></tr><tr><td><strong>Default</strong></td><td><code>tcp</code></td></tr></tbody>
</table>
</li>
<li>
<h4>async_batch_size</h4>
The maximum number of batch messages sent in asynchronous mode.
      Note that this configuration does not work in synchronous mode.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>256</code></td></tr></tbody>
</table>
</li>
<li>
<h4>port_discovery</h4>
<code>manual</code>: discover ports by <code>tcp_server_port</code>.<br/>
<code>stateless</code>: discover ports in a stateless manner, using the following algorithm.
If node name is <code>emqxN@127.0.0.1</code>, where the N is an integer,
then the listening port will be 5370 + N.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>manual | stateless</code></td></tr><tr><td><strong>Default</strong></td><td><code>stateless</code></td></tr></tbody>
</table>
</li>
<li>
<h4>tcp_server_port</h4>
Listening port used by RPC local service.<br/>
Note that this config only takes effect when rpc.port_discovery is set to manual.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>5369</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl_server_port</h4>
Listening port used by RPC local service.<br/>
Note that this config only takes effect when rpc.port_discovery is set to manual
and <code>driver</code> is set to <code>ssl</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>5369</code></td></tr></tbody>
</table>
</li>
<li>
<h4>tcp_client_num</h4>
Set the maximum number of RPC communication channels initiated by this node to each remote node.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1..256</code></td></tr><tr><td><strong>Default</strong></td><td><code>10</code></td></tr></tbody>
</table>
</li>
<li>
<h4>connect_timeout</h4>
Timeout for establishing an RPC connection.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>certfile</h4>
Path to TLS certificate file used to validate identity of the cluster nodes.
Note that this config only takes effect when <code>rpc.driver</code> is set to <code>ssl</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_conf_schema:file()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>keyfile</h4>
Path to the private key file for the <code>rpc.certfile</code>.<br/>
Note: contents of this file are secret, so it's necessary to set permissions to 600.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_conf_schema:file()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>cacertfile</h4>
Path to certification authority TLS certificate file used to validate <code>rpc.certfile</code>.<br/>
Note: certificates of all nodes in the cluster must be signed by the same CA.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_conf_schema:file()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>send_timeout</h4>
Timeout for sending the RPC request.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication_timeout</h4>
Timeout for the remote node authentication.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>call_receive_timeout</h4>
Timeout for the reply to a synchronous RPC.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>socket_keepalive_idle</h4>
How long the connections between the brokers should remain open after the last message is sent.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_s()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15m"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>socket_keepalive_interval</h4>
The interval between keepalive messages.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_s()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"75s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>socket_keepalive_count</h4>
How many times the keepalive probe message can fail to receive a reply
until the RPC connection is considered lost.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>9</code></td></tr></tbody>
</table>
</li>
<li>
<h4>socket_sndbuf</h4>
TCP tuning parameters. TCP sending buffer size.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1MB"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>socket_recbuf</h4>
TCP tuning parameters. TCP receiving buffer size.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1MB"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>socket_buffer</h4>
TCP tuning parameters. Socket buffer size in user mode.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1MB"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>insecure_fallback</h4>
Enable compatibility with old RPC authentication.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>
