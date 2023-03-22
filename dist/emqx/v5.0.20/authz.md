# Authorization

## authz:file <a id='authz-file'></a>
Authorization using a static file.

| Config paths | Env overrides |
|-------------------------------------------|--------------------------------------------------|
|  <code>authorization.sources.$INDEX</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>type</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>file</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this ACL provider

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>path</h4>
Path to the file which contains the ACL rules.
If the file provisioned before starting EMQX node,
it can be placed anywhere as long as EMQX has read access to it.
That is, EMQX will treat it as read only.

In case the rule-set is created or updated from EMQX Dashboard or HTTP API,
a new file will be created and placed in `authz` subdirectory inside EMQX's `data_dir`,
and the old file will not be used anymore.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>

</ul>

## authz:http_get <a id='authz-http_get'></a>
Authorization using an external HTTP server (via GET requests).

| Config paths | Env overrides |
|-------------------------------------------|--------------------------------------------------|
|  <code>authorization.sources.$INDEX</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>type</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>http</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this ACL provider

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>url</h4>
URL of the auth server.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>request_timeout</h4>
HTTP request timeout.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>body</h4>
HTTP request body.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>connect_timeout</h4>
The timeout when connecting to the HTTP server.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_pipelining</h4>
A positive integer. Whether to send HTTP requests continuously, when set to 1, it means that after each HTTP request is sent, you need to wait for the server to return and then continue to send the next request.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>100</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_retries</h4>
Deprecated since 5.0.4.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>pool_size</h4>
The pool size.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8</code></td></tr></tbody>
</table>
</li>
<li>
<h4>request</h4>
Configure HTTP request parameters.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#connector-http-request">connector-http:request</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>retry_interval</h4>
Deprecated since 5.0.4.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>
SSL connection settings.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-ssl_client_opts">broker:ssl_client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{enable = false}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>method</h4>
HTTP method.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>get</code></td></tr></tbody>
</table>
</li>
<li>
<h4>headers</h4>
List of HTTP headers (without <code>content-type</code>).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[{binary(), binary()}]</code></td></tr><tr><td><strong>Default</strong></td><td><code>{
  accept = "application/json"
  "cache-control" = "no-cache"
  connection = "keep-alive"
  "keep-alive" = "timeout=30, max=1000"
}
</code></td></tr></tbody>
</table>
</li>

</ul>

## authz:http_post <a id='authz-http_post'></a>
Authorization using an external HTTP server (via POST requests).

| Config paths | Env overrides |
|-------------------------------------------|--------------------------------------------------|
|  <code>authorization.sources.$INDEX</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>type</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>http</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this ACL provider

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>url</h4>
URL of the auth server.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>request_timeout</h4>
HTTP request timeout.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>body</h4>
HTTP request body.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>connect_timeout</h4>
The timeout when connecting to the HTTP server.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_pipelining</h4>
A positive integer. Whether to send HTTP requests continuously, when set to 1, it means that after each HTTP request is sent, you need to wait for the server to return and then continue to send the next request.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>100</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_retries</h4>
Deprecated since 5.0.4.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>pool_size</h4>
The pool size.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8</code></td></tr></tbody>
</table>
</li>
<li>
<h4>request</h4>
Configure HTTP request parameters.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#connector-http-request">connector-http:request</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>retry_interval</h4>
Deprecated since 5.0.4.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>
SSL connection settings.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-ssl_client_opts">broker:ssl_client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{enable = false}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>method</h4>
HTTP method.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>post</code></td></tr></tbody>
</table>
</li>
<li>
<h4>headers</h4>
List of HTTP Headers.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[{binary(), binary()}]</code></td></tr><tr><td><strong>Default</strong></td><td><code>{
  accept = "application/json"
  "cache-control" = "no-cache"
  connection = "keep-alive"
  "content-type" = "application/json"
  "keep-alive" = "timeout=30, max=1000"
}
</code></td></tr></tbody>
</table>
</li>

</ul>

## authz:mnesia <a id='authz-mnesia'></a>
Authorization using a built-in database (mnesia).

| Config paths | Env overrides |
|-------------------------------------------|--------------------------------------------------|
|  <code>authorization.sources.$INDEX</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>type</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>built_in_database</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this ACL provider

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>

## authz:mongo_rs <a id='authz-mongo_rs'></a>
Authorization using a MongoDB replica set.

| Config paths | Env overrides |
|-------------------------------------------|--------------------------------------------------|
|  <code>authorization.sources.$INDEX</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>type</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>mongodb</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this ACL provider

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>collection</h4>
`MongoDB` collection containing the authorization data.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>atom()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>filter</h4>
Conditional expression that defines the filter condition in the query.
Filter supports the following placeholders<br/>
 - <code>${username}</code>: Will be replaced at runtime with <code>Username</code> used by the client when connecting<br/>
 - <code>${clientid}</code>: Will be replaced at runtime with <code>Client ID</code> used by the client when connecting

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mongo_type</h4>
Replica set. Must be set to 'rs' when MongoDB server is running in 'replica set' mode.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>rs</code></td></tr><tr><td><strong>Default</strong></td><td><code>rs</code></td></tr></tbody>
</table>
</li>
<li>
<h4>servers</h4>
A Node list for Cluster to connect to. The nodes should be separated with commas, such as: `Node[,Node].`
For each Node should be: The IPv4 or IPv6 address or the hostname to connect to.
A host entry has the following form: `Host[:Port]`.
The MongoDB default port 27017 is used if `[:Port]` is not specified.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>w_mode</h4>
Write mode.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>unsafe | safe</code></td></tr><tr><td><strong>Default</strong></td><td><code>unsafe</code></td></tr></tbody>
</table>
</li>
<li>
<h4>r_mode</h4>
Read mode.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>master | slave_ok</code></td></tr><tr><td><strong>Default</strong></td><td><code>master</code></td></tr></tbody>
</table>
</li>
<li>
<h4>replica_set_name</h4>
Name of the replica set.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>srv_record</h4>
Use DNS SRV record.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>pool_size</h4>
Size of the connection pool towards the bridge target service.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8</code></td></tr></tbody>
</table>
</li>
<li>
<h4>username</h4>
EMQX's username in the external database.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password</h4>
EMQX's password in the external database.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>auth_source</h4>
Database name associated with the user's credentials.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>database</h4>
Database name.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>topology</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#topology">topology</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>
SSL connection settings.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-ssl_client_opts">broker:ssl_client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{enable = false}</code></td></tr></tbody>
</table>
</li>

</ul>

## authz:mongo_sharded <a id='authz-mongo_sharded'></a>
Authorization using a sharded MongoDB cluster.

| Config paths | Env overrides |
|-------------------------------------------|--------------------------------------------------|
|  <code>authorization.sources.$INDEX</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>type</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>mongodb</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this ACL provider

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>collection</h4>
`MongoDB` collection containing the authorization data.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>atom()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>filter</h4>
Conditional expression that defines the filter condition in the query.
Filter supports the following placeholders<br/>
 - <code>${username}</code>: Will be replaced at runtime with <code>Username</code> used by the client when connecting<br/>
 - <code>${clientid}</code>: Will be replaced at runtime with <code>Client ID</code> used by the client when connecting

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mongo_type</h4>
Sharded cluster. Must be set to 'sharded' when MongoDB server is running in 'sharded' mode.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>sharded</code></td></tr><tr><td><strong>Default</strong></td><td><code>sharded</code></td></tr></tbody>
</table>
</li>
<li>
<h4>servers</h4>
A Node list for Cluster to connect to. The nodes should be separated with commas, such as: `Node[,Node].`
For each Node should be: The IPv4 or IPv6 address or the hostname to connect to.
A host entry has the following form: `Host[:Port]`.
The MongoDB default port 27017 is used if `[:Port]` is not specified.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>w_mode</h4>
Write mode.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>unsafe | safe</code></td></tr><tr><td><strong>Default</strong></td><td><code>unsafe</code></td></tr></tbody>
</table>
</li>
<li>
<h4>srv_record</h4>
Use DNS SRV record.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>pool_size</h4>
Size of the connection pool towards the bridge target service.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8</code></td></tr></tbody>
</table>
</li>
<li>
<h4>username</h4>
EMQX's username in the external database.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password</h4>
EMQX's password in the external database.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>auth_source</h4>
Database name associated with the user's credentials.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>database</h4>
Database name.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>topology</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#topology">topology</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>
SSL connection settings.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-ssl_client_opts">broker:ssl_client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{enable = false}</code></td></tr></tbody>
</table>
</li>

</ul>

## authz:mongo_single <a id='authz-mongo_single'></a>
Authorization using a single MongoDB instance.

| Config paths | Env overrides |
|-------------------------------------------|--------------------------------------------------|
|  <code>authorization.sources.$INDEX</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>type</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>mongodb</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this ACL provider

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>collection</h4>
`MongoDB` collection containing the authorization data.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>atom()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>filter</h4>
Conditional expression that defines the filter condition in the query.
Filter supports the following placeholders<br/>
 - <code>${username}</code>: Will be replaced at runtime with <code>Username</code> used by the client when connecting<br/>
 - <code>${clientid}</code>: Will be replaced at runtime with <code>Client ID</code> used by the client when connecting

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mongo_type</h4>
Standalone instance. Must be set to 'single' when MongoDB server is running in standalone mode.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>single</code></td></tr><tr><td><strong>Default</strong></td><td><code>single</code></td></tr></tbody>
</table>
</li>
<li>
<h4>server</h4>
The IPv4 or IPv6 address or the hostname to connect to.<br/>
A host entry has the following form: `Host[:Port]`.<br/>
The MongoDB default port 27017 is used if `[:Port]` is not specified.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>w_mode</h4>
Write mode.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>unsafe | safe</code></td></tr><tr><td><strong>Default</strong></td><td><code>unsafe</code></td></tr></tbody>
</table>
</li>
<li>
<h4>srv_record</h4>
Use DNS SRV record.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>pool_size</h4>
Size of the connection pool towards the bridge target service.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8</code></td></tr></tbody>
</table>
</li>
<li>
<h4>username</h4>
EMQX's username in the external database.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password</h4>
EMQX's password in the external database.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>auth_source</h4>
Database name associated with the user's credentials.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>database</h4>
Database name.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>topology</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#topology">topology</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>
SSL connection settings.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-ssl_client_opts">broker:ssl_client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{enable = false}</code></td></tr></tbody>
</table>
</li>

</ul>

## authz:mysql <a id='authz-mysql'></a>
Authorization using a MySQL database.

| Config paths | Env overrides |
|-------------------------------------------|--------------------------------------------------|
|  <code>authorization.sources.$INDEX</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>type</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>mysql</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this ACL provider

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>server</h4>
The IPv4 or IPv6 address or the hostname to connect to.<br/>
A host entry has the following form: `Host[:Port]`.<br/>
The MySQL default port 3306 is used if `[:Port]` is not specified.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>database</h4>
Database name.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>pool_size</h4>
Size of the connection pool towards the bridge target service.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8</code></td></tr></tbody>
</table>
</li>
<li>
<h4>username</h4>
EMQX's username in the external database.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"root"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password</h4>
EMQX's password in the external database.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>auto_reconnect</h4>
Deprecated since v5.0.15.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>
SSL connection settings.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-ssl_client_opts">broker:ssl_client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{enable = false}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>prepare_statement</h4>
Key-value list of SQL prepared statements.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>query</h4>
Database query used to retrieve authorization data.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>

</ul>

## authz:postgresql <a id='authz-postgresql'></a>
Authorization using a PostgreSQL database.

| Config paths | Env overrides |
|-------------------------------------------|--------------------------------------------------|
|  <code>authorization.sources.$INDEX</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>type</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>postgresql</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this ACL provider

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>server</h4>
The IPv4 or IPv6 address or the hostname to connect to.<br/>
A host entry has the following form: `Host[:Port]`.<br/>
The PostgreSQL default port 5432 is used if `[:Port]` is not specified.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>database</h4>
Database name.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>pool_size</h4>
Size of the connection pool towards the bridge target service.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8</code></td></tr></tbody>
</table>
</li>
<li>
<h4>username</h4>
EMQX's username in the external database.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password</h4>
EMQX's password in the external database.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>auto_reconnect</h4>
Deprecated since v5.0.15.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>
SSL connection settings.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-ssl_client_opts">broker:ssl_client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{enable = false}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>prepare_statement</h4>
Key-value list of SQL prepared statements.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>query</h4>
Database query used to retrieve authorization data.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>

</ul>

## authz:redis_cluster <a id='authz-redis_cluster'></a>
Authorization using a Redis cluster.

| Config paths | Env overrides |
|-------------------------------------------|--------------------------------------------------|
|  <code>authorization.sources.$INDEX</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>type</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>redis</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this ACL provider

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>servers</h4>
A Node list for Cluster to connect to. The nodes should be separated with commas, such as: `Node[,Node].`
For each Node should be: The IPv4 or IPv6 address or the hostname to connect to.
A host entry has the following form: `Host[:Port]`.
The Redis default port 6379 is used if `[:Port]` is not specified.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>redis_type</h4>
Cluster mode. Must be set to 'cluster' when Redis server is running in clustered mode.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>cluster</code></td></tr><tr><td><strong>Default</strong></td><td><code>cluster</code></td></tr></tbody>
</table>
</li>
<li>
<h4>pool_size</h4>
Size of the connection pool towards the bridge target service.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password</h4>
EMQX's password in the external database.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>auto_reconnect</h4>
Deprecated since v5.0.15.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>
SSL connection settings.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-ssl_client_opts">broker:ssl_client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{enable = false}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>cmd</h4>
Database query used to retrieve authorization data.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>

</ul>

## authz:redis_sentinel <a id='authz-redis_sentinel'></a>
Authorization using a Redis Sentinel.

| Config paths | Env overrides |
|-------------------------------------------|--------------------------------------------------|
|  <code>authorization.sources.$INDEX</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>type</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>redis</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this ACL provider

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>servers</h4>
A Node list for Cluster to connect to. The nodes should be separated with commas, such as: `Node[,Node].`
For each Node should be: The IPv4 or IPv6 address or the hostname to connect to.
A host entry has the following form: `Host[:Port]`.
The Redis default port 6379 is used if `[:Port]` is not specified.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>redis_type</h4>
Sentinel mode. Must be set to 'sentinel' when Redis server is running in sentinel mode.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>sentinel</code></td></tr><tr><td><strong>Default</strong></td><td><code>sentinel</code></td></tr></tbody>
</table>
</li>
<li>
<h4>sentinel</h4>
The cluster name in Redis sentinel mode.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>pool_size</h4>
Size of the connection pool towards the bridge target service.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password</h4>
EMQX's password in the external database.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>database</h4>
Redis database ID.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>0</code></td></tr></tbody>
</table>
</li>
<li>
<h4>auto_reconnect</h4>
Deprecated since v5.0.15.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>
SSL connection settings.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-ssl_client_opts">broker:ssl_client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{enable = false}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>cmd</h4>
Database query used to retrieve authorization data.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>

</ul>

## authz:redis_single <a id='authz-redis_single'></a>
Authorization using a single Redis instance.

| Config paths | Env overrides |
|-------------------------------------------|--------------------------------------------------|
|  <code>authorization.sources.$INDEX</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>type</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>redis</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this ACL provider

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>server</h4>
The IPv4 or IPv6 address or the hostname to connect to.<br/>
A host entry has the following form: `Host[:Port]`.<br/>
The Redis default port 6379 is used if `[:Port]` is not specified.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>redis_type</h4>
Single mode. Must be set to 'single' when Redis server is running in single mode.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>single</code></td></tr><tr><td><strong>Default</strong></td><td><code>single</code></td></tr></tbody>
</table>
</li>
<li>
<h4>pool_size</h4>
Size of the connection pool towards the bridge target service.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password</h4>
EMQX's password in the external database.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>database</h4>
Redis database ID.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>0</code></td></tr></tbody>
</table>
</li>
<li>
<h4>auto_reconnect</h4>
Deprecated since v5.0.15.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>
SSL connection settings.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-ssl_client_opts">broker:ssl_client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{enable = false}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>cmd</h4>
Database query used to retrieve authorization data.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>

</ul>
