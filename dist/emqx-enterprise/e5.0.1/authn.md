# Authentication

## authn-builtin_db:authentication <a id='authn-builtin_db-authentication'></a>
Configuration of authenticator using built-in database as data source.

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>password_based</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backend</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>built_in_database</code></td></tr></tbody>
</table>
</li>
<li>
<h4>user_id_type</h4>
Specify whether to use `clientid` or `username` for authentication.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>clientid | username</code></td></tr><tr><td><strong>Default</strong></td><td><code>"username"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password_hash_algorithm</h4>
Options for password hash creation and verification.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#authn-hash-bcrypt_rw">authn-hash:bcrypt_rw</a> | <a href="others.md#authn-hash-pbkdf2">authn-hash:pbkdf2</a> | <a href="others.md#authn-hash-simple">authn-hash:simple</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{name = sha256, salt_position = prefix}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>

## authn-http:get <a id='authn-http-get'></a>
Configuration of authenticator using HTTP Server as authentication service (Using GET request).

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>method</h4>
HTTP request method.

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
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr><tr><td><strong>Default</strong></td><td><code>{
  accept = "application/json"
  "cache-control" = "no-cache"
  connection = "keep-alive"
  "keep-alive" = "timeout=30, max=1000"
}
</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>password_based</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backend</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>http</code></td></tr></tbody>
</table>
</li>
<li>
<h4>url</h4>
URL of the HTTP server.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>body</h4>
HTTP request body.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>#{term() => binary()}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>request_timeout</h4>
HTTP request timeout.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
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

</ul>

## authn-http:post <a id='authn-http-post'></a>
Configuration of authenticator using HTTP Server as authentication service (Using POST request).

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>method</h4>
HTTP request method.

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
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr><tr><td><strong>Default</strong></td><td><code>{
  accept = "application/json"
  "cache-control" = "no-cache"
  connection = "keep-alive"
  "content-type" = "application/json"
  "keep-alive" = "timeout=30, max=1000"
}
</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>password_based</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backend</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>http</code></td></tr></tbody>
</table>
</li>
<li>
<h4>url</h4>
URL of the HTTP server.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>body</h4>
HTTP request body.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>#{term() => binary()}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>request_timeout</h4>
HTTP request timeout.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
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

</ul>

## authn-jwt:hmac-based <a id='authn-jwt-hmac-based'></a>
Configuration when the JWT for authentication is issued using the HMAC algorithm.

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>use_jwks</h4>
Whether to use JWKS.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>algorithm</h4>
JWT signing algorithm, Supports HMAC (configured as <code>hmac-based</code>) and RSA, ECDSA (configured as <code>public-key</code>).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>hmac-based</code></td></tr></tbody>
</table>
</li>
<li>
<h4>secret</h4>
The key to verify the JWT using HMAC algorithm.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>secret_base64_encoded</h4>
Whether secret is base64 encoded.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>jwt</code></td></tr></tbody>
</table>
</li>
<li>
<h4>acl_claim_name</h4>
JWT claim name to use for getting ACL rules.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"acl"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>verify_claims</h4>
A list of custom claims to validate, which is a list of name/value pairs.
Values can use the following placeholders:
- <code>${username}</code>: Will be replaced at runtime with <code>Username</code> used by the client when connecting
- <code>${clientid}</code>: Will be replaced at runtime with <code>Client ID</code> used by the client when connecting
Authentication will verify that the value of claims in the JWT (taken from the Password field) matches what is required in <code>verify_claims</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[term()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>from</h4>
Field to take JWT from.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>username | password</code></td></tr><tr><td><strong>Default</strong></td><td><code>password</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>

## authn-jwt:jwks <a id='authn-jwt-jwks'></a>
Configuration when JWTs used for authentication need to be fetched from the JWKS endpoint.

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>use_jwks</h4>
Whether to use JWKS.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>endpoint</h4>
JWKS endpoint, it's a read-only endpoint that returns the server's public key set in the JWKS format.

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
<h4>refresh_interval</h4>
JWKS refresh interval.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>300</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>
SSL options.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-ssl_client_opts">broker:ssl_client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{enable = false}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>jwt</code></td></tr></tbody>
</table>
</li>
<li>
<h4>acl_claim_name</h4>
JWT claim name to use for getting ACL rules.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"acl"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>verify_claims</h4>
A list of custom claims to validate, which is a list of name/value pairs.
Values can use the following placeholders:
- <code>${username}</code>: Will be replaced at runtime with <code>Username</code> used by the client when connecting
- <code>${clientid}</code>: Will be replaced at runtime with <code>Client ID</code> used by the client when connecting
Authentication will verify that the value of claims in the JWT (taken from the Password field) matches what is required in <code>verify_claims</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[term()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>from</h4>
Field to take JWT from.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>username | password</code></td></tr><tr><td><strong>Default</strong></td><td><code>password</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>

## authn-jwt:public-key <a id='authn-jwt-public-key'></a>
Configuration when the JWT for authentication is issued using RSA or ECDSA algorithm.

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>use_jwks</h4>
Whether to use JWKS.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>algorithm</h4>
JWT signing algorithm, Supports HMAC (configured as <code>hmac-based</code>) and RSA, ECDSA (configured as <code>public-key</code>).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>public-key</code></td></tr></tbody>
</table>
</li>
<li>
<h4>public_key</h4>
The public key used to verify the JWT.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>jwt</code></td></tr></tbody>
</table>
</li>
<li>
<h4>acl_claim_name</h4>
JWT claim name to use for getting ACL rules.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"acl"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>verify_claims</h4>
A list of custom claims to validate, which is a list of name/value pairs.
Values can use the following placeholders:
- <code>${username}</code>: Will be replaced at runtime with <code>Username</code> used by the client when connecting
- <code>${clientid}</code>: Will be replaced at runtime with <code>Client ID</code> used by the client when connecting
Authentication will verify that the value of claims in the JWT (taken from the Password field) matches what is required in <code>verify_claims</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[term()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>from</h4>
Field to take JWT from.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>username | password</code></td></tr><tr><td><strong>Default</strong></td><td><code>password</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>

## authn-mongodb:replica-set <a id='authn-mongodb-replica-set'></a>
Configuration of authenticator using MongoDB (Replica Set) as authentication data source.

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>password_based</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backend</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>mongodb</code></td></tr></tbody>
</table>
</li>
<li>
<h4>collection</h4>
Collection used to store authentication data.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>filter</h4>
Conditional expression that defines the filter condition in the query.
Filter supports the following placeholders:
- <code>${username}</code>: Will be replaced at runtime with <code>Username</code> used by the client when connecting
- <code>${clientid}</code>: Will be replaced at runtime with <code>Client ID</code> used by the client when connecting

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password_hash_field</h4>
Document field that contains password hash.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"password_hash"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>salt_field</h4>
Document field that contains the password salt.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"salt"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>is_superuser_field</h4>
Document field that defines if the user has superuser privileges.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"is_superuser"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password_hash_algorithm</h4>
Options for password hash verification.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#authn-hash-bcrypt">authn-hash:bcrypt</a> | <a href="others.md#authn-hash-pbkdf2">authn-hash:pbkdf2</a> | <a href="others.md#authn-hash-simple">authn-hash:simple</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{name = sha256, salt_position = prefix}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
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

## authn-mongodb:sharded-cluster <a id='authn-mongodb-sharded-cluster'></a>
Configuration of authenticator using MongoDB (Sharded Cluster) as authentication data source.

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>password_based</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backend</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>mongodb</code></td></tr></tbody>
</table>
</li>
<li>
<h4>collection</h4>
Collection used to store authentication data.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>filter</h4>
Conditional expression that defines the filter condition in the query.
Filter supports the following placeholders:
- <code>${username}</code>: Will be replaced at runtime with <code>Username</code> used by the client when connecting
- <code>${clientid}</code>: Will be replaced at runtime with <code>Client ID</code> used by the client when connecting

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password_hash_field</h4>
Document field that contains password hash.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"password_hash"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>salt_field</h4>
Document field that contains the password salt.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"salt"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>is_superuser_field</h4>
Document field that defines if the user has superuser privileges.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"is_superuser"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password_hash_algorithm</h4>
Options for password hash verification.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#authn-hash-bcrypt">authn-hash:bcrypt</a> | <a href="others.md#authn-hash-pbkdf2">authn-hash:pbkdf2</a> | <a href="others.md#authn-hash-simple">authn-hash:simple</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{name = sha256, salt_position = prefix}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
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

## authn-mongodb:standalone <a id='authn-mongodb-standalone'></a>
Configuration of authenticator using MongoDB (Standalone) as authentication data source.

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>password_based</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backend</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>mongodb</code></td></tr></tbody>
</table>
</li>
<li>
<h4>collection</h4>
Collection used to store authentication data.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>filter</h4>
Conditional expression that defines the filter condition in the query.
Filter supports the following placeholders:
- <code>${username}</code>: Will be replaced at runtime with <code>Username</code> used by the client when connecting
- <code>${clientid}</code>: Will be replaced at runtime with <code>Client ID</code> used by the client when connecting

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password_hash_field</h4>
Document field that contains password hash.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"password_hash"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>salt_field</h4>
Document field that contains the password salt.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"salt"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>is_superuser_field</h4>
Document field that defines if the user has superuser privileges.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"is_superuser"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password_hash_algorithm</h4>
Options for password hash verification.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#authn-hash-bcrypt">authn-hash:bcrypt</a> | <a href="others.md#authn-hash-pbkdf2">authn-hash:pbkdf2</a> | <a href="others.md#authn-hash-simple">authn-hash:simple</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{name = sha256, salt_position = prefix}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
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

## authn-mysql:authentication <a id='authn-mysql-authentication'></a>
Configuration of authenticator using MySQL as authentication data source.

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>password_based</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backend</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>mysql</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password_hash_algorithm</h4>
Options for password hash verification.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#authn-hash-bcrypt">authn-hash:bcrypt</a> | <a href="others.md#authn-hash-pbkdf2">authn-hash:pbkdf2</a> | <a href="others.md#authn-hash-simple">authn-hash:simple</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{name = sha256, salt_position = prefix}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>query</h4>
SQL used to query data for authentication, such as password hash.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>query_timeout</h4>
Timeout for the SQL query.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

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

</ul>

## authn-postgresql:authentication <a id='authn-postgresql-authentication'></a>
Configuration of authenticator using PostgreSQL as authentication data source.

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>password_based</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backend</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>postgresql</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password_hash_algorithm</h4>
Options for password hash verification.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#authn-hash-bcrypt">authn-hash:bcrypt</a> | <a href="others.md#authn-hash-pbkdf2">authn-hash:pbkdf2</a> | <a href="others.md#authn-hash-simple">authn-hash:simple</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{name = sha256, salt_position = prefix}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>query</h4>
SQL used to query data for authentication, such as password hash.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

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

</ul>

## authn-redis:cluster <a id='authn-redis-cluster'></a>
Configuration of authenticator using Redis (Cluster) as authentication data source.

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>password_based</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backend</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>redis</code></td></tr></tbody>
</table>
</li>
<li>
<h4>cmd</h4>
The Redis Command used to query data for authentication such as password hash, currently only supports <code>HGET</code> and <code>HMGET</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password_hash_algorithm</h4>
Options for password hash verification.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#authn-hash-bcrypt">authn-hash:bcrypt</a> | <a href="others.md#authn-hash-pbkdf2">authn-hash:pbkdf2</a> | <a href="others.md#authn-hash-simple">authn-hash:simple</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{name = sha256, salt_position = prefix}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

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

</ul>

## authn-redis:sentinel <a id='authn-redis-sentinel'></a>
Configuration of authenticator using Redis (Sentinel) as authentication data source.

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>password_based</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backend</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>redis</code></td></tr></tbody>
</table>
</li>
<li>
<h4>cmd</h4>
The Redis Command used to query data for authentication such as password hash, currently only supports <code>HGET</code> and <code>HMGET</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password_hash_algorithm</h4>
Options for password hash verification.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#authn-hash-bcrypt">authn-hash:bcrypt</a> | <a href="others.md#authn-hash-pbkdf2">authn-hash:pbkdf2</a> | <a href="others.md#authn-hash-simple">authn-hash:simple</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{name = sha256, salt_position = prefix}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

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

</ul>

## authn-redis:standalone <a id='authn-redis-standalone'></a>
Configuration of authenticator using Redis (Standalone) as authentication data source.

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>password_based</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backend</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>redis</code></td></tr></tbody>
</table>
</li>
<li>
<h4>cmd</h4>
The Redis Command used to query data for authentication such as password hash, currently only supports <code>HGET</code> and <code>HMGET</code>.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password_hash_algorithm</h4>
Options for password hash verification.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="others.md#authn-hash-bcrypt">authn-hash:bcrypt</a> | <a href="others.md#authn-hash-pbkdf2">authn-hash:pbkdf2</a> | <a href="others.md#authn-hash-simple">authn-hash:simple</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{name = sha256, salt_position = prefix}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

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

</ul>

## authn-scram-builtin_db:authentication <a id='authn-scram-builtin_db-authentication'></a>
Settings for Salted Challenge Response Authentication Mechanism
(SCRAM) authentication.

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>authentication.$INDEX</code> | <code>EMQX_AUTHENTICATION__$INDEX</code>  |
|  <code>gateway.coap.authentication</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.authentication</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.authentication</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>mechanism</h4>
Authentication mechanism.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>scram</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backend</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>built_in_database</code></td></tr></tbody>
</table>
</li>
<li>
<h4>algorithm</h4>
Hashing algorithm.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>sha256 | sha512</code></td></tr><tr><td><strong>Default</strong></td><td><code>sha256</code></td></tr></tbody>
</table>
</li>
<li>
<h4>iteration_count</h4>
Iteration count.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>4096</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to <code>true</code> or <code>false</code> to disable this auth provider.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>
