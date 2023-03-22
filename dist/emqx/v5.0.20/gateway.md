# Gateways

## gateway:clientinfo_override <a id='gateway-clientinfo_override'></a>
ClientInfo override.

| Config paths | Env overrides |
|--------------------------------------------------|---------------------------------------------------------|
|  <code>gateway.coap.clientinfo_override</code> | <code>EMQX_GATEWAY__COAP__CLIENTINFO_OVERRIDE</code>  |
|  <code>gateway.exproto.clientinfo_override</code> | <code>EMQX_GATEWAY__EXPROTO__CLIENTINFO_OVERRIDE</code>  |
|  <code>gateway.lwm2m.clientinfo_override</code> | <code>EMQX_GATEWAY__LWM2M__CLIENTINFO_OVERRIDE</code>  |
|  <code>gateway.mqttsn.clientinfo_override</code> | <code>EMQX_GATEWAY__MQTTSN__CLIENTINFO_OVERRIDE</code>  |
|  <code>gateway.stomp.clientinfo_override</code> | <code>EMQX_GATEWAY__STOMP__CLIENTINFO_OVERRIDE</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>username</h4>
Template for overriding username.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password</h4>
Template for overriding password.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>clientid</h4>
Template for overriding clientid.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:coap <a id='gateway-coap'></a>
The CoAP protocol gateway provides EMQX with the access capability of the CoAP protocol.
It allows publishing, subscribing, and receiving messages to EMQX in accordance
with a certain defined CoAP message format.

| Config paths | Env overrides |
|---------------------------|---------------------------------|
|  <code>gateway.coap</code> | <code>EMQX_GATEWAY__COAP</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>heartbeat</h4>
The gateway server required minimum heartbeat interval.
When connection mode is enabled, this parameter is used to set the minimum heartbeat interval for the connection to be alive

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>connection_required</h4>
Enable or disable connection mode.
Connection mode is a feature of non-standard protocols. When connection mode is enabled, it is necessary to maintain the creation, authentication and alive of connection resources

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>notify_type</h4>
The Notification Message will be delivered to the CoAP client if a new message received on an observed topic.
The type of delivered coap message can be set to:<br/>
  - non: Non-confirmable;<br/>
  - con: Confirmable;<br/>
  - qos: Mapping from QoS type of received message, QoS0 -> non, QoS1,2 -> con

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non | con | qos</code></td></tr><tr><td><strong>Default</strong></td><td><code>qos</code></td></tr></tbody>
</table>
</li>
<li>
<h4>subscribe_qos</h4>
The Default QoS Level indicator for subscribe request.
This option specifies the QoS level for the CoAP Client when establishing a subscription membership, if the subscribe request is not carried `qos` option. The indicator can be set to:<br/>
  - qos0, qos1, qos2: Fixed default QoS level<br/>
  - coap: Dynamic QoS level by the message type of subscribe request<br/>
    * qos0: If the subscribe request is non-confirmable<br/>
    * qos1: If the subscribe request is confirmable

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>qos0 | qos1 | qos2 | coap</code></td></tr><tr><td><strong>Default</strong></td><td><code>coap</code></td></tr></tbody>
</table>
</li>
<li>
<h4>publish_qos</h4>
The Default QoS Level indicator for publish request.
This option specifies the QoS level for the CoAP Client when publishing a message to EMQX PUB/SUB system, if the publish request is not carried `qos` option. The indicator can be set to:<br/>
  - qos0, qos1, qos2: Fixed default QoS level<br/>
  - coap: Dynamic QoS level by the message type of publish request<br/>
    * qos0: If the publish request is non-confirmable<br/>
    * qos1: If the publish request is confirmable

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>qos0 | qos1 | qos2 | coap</code></td></tr><tr><td><strong>Default</strong></td><td><code>coap</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mountpoint</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>
<li>
<h4>listeners</h4>
Settings for the UDP listeners.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-udp_listeners">gateway:udp_listeners</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Whether to enable this gateway

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_stats</h4>
Whether to enable client process statistic

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>idle_timeout</h4>
The idle time of the client connection process. It has two purposes:
  1. A newly created client process that does not receive any client requests after that time will be closed directly.
  2. A running client process that does not receive any client requests after this time will go into hibernation to save resources.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>clientinfo_override</h4>
ClientInfo override.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-clientinfo_override">gateway:clientinfo_override</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication</h4>
Default authentication configs for all the gateway listeners. For per-listener overrides see <code>authentication</code>
 in listener configs

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="authn.md#authn-builtin_db-authentication">authn-builtin_db:authentication</a> | <a href="authn.md#authn-mysql-authentication">authn-mysql:authentication</a> | <a href="authn.md#authn-postgresql-authentication">authn-postgresql:authentication</a> | <a href="authn.md#authn-mongodb-standalone">authn-mongodb:standalone</a> | <a href="authn.md#authn-mongodb-replica-set">authn-mongodb:replica-set</a> | <a href="authn.md#authn-mongodb-sharded-cluster">authn-mongodb:sharded-cluster</a> | <a href="authn.md#authn-redis-standalone">authn-redis:standalone</a> | <a href="authn.md#authn-redis-cluster">authn-redis:cluster</a> | <a href="authn.md#authn-redis-sentinel">authn-redis:sentinel</a> | <a href="authn.md#authn-http-get">authn-http:get</a> | <a href="authn.md#authn-http-post">authn-http:post</a> | <a href="authn.md#authn-jwt-hmac-based">authn-jwt:hmac-based</a> | <a href="authn.md#authn-jwt-public-key">authn-jwt:public-key</a> | <a href="authn.md#authn-jwt-jwks">authn-jwt:jwks</a> | <a href="authn.md#authn-scram-builtin_db-authentication">authn-scram-builtin_db:authentication</a></code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:dtls_listener <a id='gateway-dtls_listener'></a>
Settings for the DTLS listener.

| Config paths | Env overrides |
|---------------------------------------------------|------------------------------------------------------------|
|  <code>gateway.coap.listeners.dtls.$name</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME</code>  |
|  <code>gateway.exproto.listeners.dtls.$name</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>acceptors</h4>
Size of the acceptor pool.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>16</code></td></tr></tbody>
</table>
</li>
<li>
<h4>udp_options</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-udp_opts">gateway:udp_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Enable the listener.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bind</h4>
The IP address and port that the listener will bind.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:ip_port() | integer()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_connections</h4>
Maximum number of concurrent connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1024</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_conn_rate</h4>
Maximum connections per second.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication</h4>
Default authentication configs for all the gateway listeners. For per-listener overrides see <code>authentication</code>
 in listener configs

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="authn.md#authn-builtin_db-authentication">authn-builtin_db:authentication</a> | <a href="authn.md#authn-mysql-authentication">authn-mysql:authentication</a> | <a href="authn.md#authn-postgresql-authentication">authn-postgresql:authentication</a> | <a href="authn.md#authn-mongodb-standalone">authn-mongodb:standalone</a> | <a href="authn.md#authn-mongodb-replica-set">authn-mongodb:replica-set</a> | <a href="authn.md#authn-mongodb-sharded-cluster">authn-mongodb:sharded-cluster</a> | <a href="authn.md#authn-redis-standalone">authn-redis:standalone</a> | <a href="authn.md#authn-redis-cluster">authn-redis:cluster</a> | <a href="authn.md#authn-redis-sentinel">authn-redis:sentinel</a> | <a href="authn.md#authn-http-get">authn-http:get</a> | <a href="authn.md#authn-http-post">authn-http:post</a> | <a href="authn.md#authn-jwt-hmac-based">authn-jwt:hmac-based</a> | <a href="authn.md#authn-jwt-public-key">authn-jwt:public-key</a> | <a href="authn.md#authn-jwt-jwks">authn-jwt:jwks</a> | <a href="authn.md#authn-scram-builtin_db-authentication">authn-scram-builtin_db:authentication</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_authn</h4>
Set <code>true</code> (default) to enable client authentication on this listener. 
When set to <code>false</code> clients will be allowed to connect without authentication.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mountpoint</h4>
When publishing or subscribing, prefix all topics with a mountpoint string.
The prefixed string will be removed from the topic name when the message is delivered to the subscriber.
The mountpoint is a way that users can use to implement isolation of message routing between different listeners.
For example if a client A subscribes to `t` with `listeners.tcp.\<name>.mountpoint` set to `some_tenant`,
then the client actually subscribes to the topic `some_tenant/t`.
Similarly, if another client B (connected to the same listener as the client A) sends a message to topic `t`,
the message is routed to all the clients subscribed `some_tenant/t`,
so client A will receive the message, with topic name `t`. Set to `""` to disable the feature.
Variables in mountpoint string:<br/>
  - <code>${clientid}</code>: clientid<br/>
  - <code>${username}</code>: username

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>access_rules</h4>
The access control rules for this listener.
See: https://github.com/emqtt/esockd#allowdeny

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[string()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>dtls_options</h4>
DTLS socket options

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-dtls_opts">gateway:dtls_opts</a></code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:dtls_opts <a id='gateway-dtls_opts'></a>
Settings for the DTLS protocol.

| Config paths | Env overrides |
|----------------------------------------------------------------|--------------------------------------------------------------------------|
|  <code>gateway.coap.listeners.dtls.$name.dtls_options</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__DTLS_OPTIONS</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.dtls_options</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__DTLS_OPTIONS</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.dtls_options</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__DTLS_OPTIONS</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.dtls_options</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__DTLS_OPTIONS</code>  |


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
<tr><td><strong>Type</strong></td><td><code>[atom()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[dtlsv1.2, dtlsv1]</code></td></tr></tbody>
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

## gateway:exproto <a id='gateway-exproto'></a>
Settings for EMQX extension protocol (exproto).

| Config paths | Env overrides |
|------------------------------|------------------------------------|
|  <code>gateway.exproto</code> | <code>EMQX_GATEWAY__EXPROTO</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>server</h4>
Configurations for starting the <code>ConnectionAdapter</code> service

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-exproto_grpc_server">gateway:exproto_grpc_server</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>handler</h4>
Configurations for request to <code>ConnectionHandler</code> service

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-exproto_grpc_handler">gateway:exproto_grpc_handler</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>mountpoint</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>
<li>
<h4>listeners</h4>
Settings for the listeners.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-tcp_udp_listeners">gateway:tcp_udp_listeners</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Whether to enable this gateway

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_stats</h4>
Whether to enable client process statistic

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>idle_timeout</h4>
The idle time of the client connection process. It has two purposes:
  1. A newly created client process that does not receive any client requests after that time will be closed directly.
  2. A running client process that does not receive any client requests after this time will go into hibernation to save resources.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>clientinfo_override</h4>
ClientInfo override.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-clientinfo_override">gateway:clientinfo_override</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication</h4>
Default authentication configs for all the gateway listeners. For per-listener overrides see <code>authentication</code>
 in listener configs

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="authn.md#authn-builtin_db-authentication">authn-builtin_db:authentication</a> | <a href="authn.md#authn-mysql-authentication">authn-mysql:authentication</a> | <a href="authn.md#authn-postgresql-authentication">authn-postgresql:authentication</a> | <a href="authn.md#authn-mongodb-standalone">authn-mongodb:standalone</a> | <a href="authn.md#authn-mongodb-replica-set">authn-mongodb:replica-set</a> | <a href="authn.md#authn-mongodb-sharded-cluster">authn-mongodb:sharded-cluster</a> | <a href="authn.md#authn-redis-standalone">authn-redis:standalone</a> | <a href="authn.md#authn-redis-cluster">authn-redis:cluster</a> | <a href="authn.md#authn-redis-sentinel">authn-redis:sentinel</a> | <a href="authn.md#authn-http-get">authn-http:get</a> | <a href="authn.md#authn-http-post">authn-http:post</a> | <a href="authn.md#authn-jwt-hmac-based">authn-jwt:hmac-based</a> | <a href="authn.md#authn-jwt-public-key">authn-jwt:public-key</a> | <a href="authn.md#authn-jwt-jwks">authn-jwt:jwks</a> | <a href="authn.md#authn-scram-builtin_db-authentication">authn-scram-builtin_db:authentication</a></code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:exproto_grpc_handler <a id='gateway-exproto_grpc_handler'></a>
Settings for the exproto gRPC connection handler.

| Config paths | Env overrides |
|--------------------------------------|---------------------------------------------|
|  <code>gateway.exproto.handler</code> | <code>EMQX_GATEWAY__EXPROTO__HANDLER</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>address</h4>
gRPC server address.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl_options</h4>
SSL configuration for the gRPC client.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-ssl_client_opts">broker:ssl_client_opts</a></code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:exproto_grpc_server <a id='gateway-exproto_grpc_server'></a>
Settings for the exproto gRPC server.

| Config paths | Env overrides |
|-------------------------------------|--------------------------------------------|
|  <code>gateway.exproto.server</code> | <code>EMQX_GATEWAY__EXPROTO__SERVER</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>bind</h4>
Listening address and port for the gRPC server.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:ip_port() | integer()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl_options</h4>
SSL configuration for the gRPC server.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-ssl_server_opts">gateway:ssl_server_opts</a></code></td></tr></tbody>
</table>
</li>

</ul>

## gateway <a id='gateway'></a>
EMQX Gateway configuration root.

| Config paths | Env overrides |
|----------------------|---------------------------|
|  <code>gateway</code> | <code>EMQX_GATEWAY</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>stomp</h4>
The Stomp Gateway configuration.
This gateway supports v1.2/1.1/1.0

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-stomp">gateway:stomp</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>mqttsn</h4>
The MQTT-SN Gateway configuration.
This gateway only supports the v1.2 protocol

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-mqttsn">gateway:mqttsn</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>coap</h4>
The CoAP Gateway configuration.
This gateway is implemented based on RFC-7252 and https://core-wg.github.io/coap-pubsub/draft-ietf-core-pubsub.html

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-coap">gateway:coap</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>lwm2m</h4>
The LwM2M Gateway configuration. This gateway only supports the v1.0.1 protocol.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-lwm2m">gateway:lwm2m</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>exproto</h4>
The Extension Protocol configuration

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-exproto">gateway:exproto</a></code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:lwm2m <a id='gateway-lwm2m'></a>
The LwM2M protocol gateway.

| Config paths | Env overrides |
|----------------------------|----------------------------------|
|  <code>gateway.lwm2m</code> | <code>EMQX_GATEWAY__LWM2M</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>xml_dir</h4>
The Directory for LwM2M Resource definition.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>lifetime_min</h4>
Minimum value of lifetime allowed to be set by the LwM2M client.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>lifetime_max</h4>
Maximum value of lifetime allowed to be set by the LwM2M client.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"86400s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>qmode_time_window</h4>
The value of the time window during which the network link is considered valid by the LwM2M Gateway in QMode mode.
For example, after receiving an update message from a client, any messages within this time window are sent directly to the LwM2M client, and all messages beyond this time window are temporarily stored in memory.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:duration_s()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"22s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>auto_observe</h4>
Automatically observe the object list of REGISTER packet.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>update_msg_publish_condition</h4>
Policy for publishing UPDATE event message.<br/>
  - always: send update events as long as the UPDATE request is received.<br/>
  - contains_object_list: send update events only if the UPDATE request carries any Object List

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>always | contains_object_list</code></td></tr><tr><td><strong>Default</strong></td><td><code>contains_object_list</code></td></tr></tbody>
</table>
</li>
<li>
<h4>translators</h4>
Topic configuration for LwM2M's gateway publishing and subscription.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-lwm2m_translators">gateway:lwm2m_translators</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>mountpoint</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"lwm2m/${endpoint_name}/"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>listeners</h4>
Settings for the UDP listeners.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-udp_listeners">gateway:udp_listeners</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Whether to enable this gateway

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_stats</h4>
Whether to enable client process statistic

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>idle_timeout</h4>
The idle time of the client connection process. It has two purposes:
  1. A newly created client process that does not receive any client requests after that time will be closed directly.
  2. A running client process that does not receive any client requests after this time will go into hibernation to save resources.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>clientinfo_override</h4>
ClientInfo override.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-clientinfo_override">gateway:clientinfo_override</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication</h4>
Default authentication configs for all the gateway listeners. For per-listener overrides see <code>authentication</code>
 in listener configs

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="authn.md#authn-builtin_db-authentication">authn-builtin_db:authentication</a> | <a href="authn.md#authn-mysql-authentication">authn-mysql:authentication</a> | <a href="authn.md#authn-postgresql-authentication">authn-postgresql:authentication</a> | <a href="authn.md#authn-mongodb-standalone">authn-mongodb:standalone</a> | <a href="authn.md#authn-mongodb-replica-set">authn-mongodb:replica-set</a> | <a href="authn.md#authn-mongodb-sharded-cluster">authn-mongodb:sharded-cluster</a> | <a href="authn.md#authn-redis-standalone">authn-redis:standalone</a> | <a href="authn.md#authn-redis-cluster">authn-redis:cluster</a> | <a href="authn.md#authn-redis-sentinel">authn-redis:sentinel</a> | <a href="authn.md#authn-http-get">authn-http:get</a> | <a href="authn.md#authn-http-post">authn-http:post</a> | <a href="authn.md#authn-jwt-hmac-based">authn-jwt:hmac-based</a> | <a href="authn.md#authn-jwt-public-key">authn-jwt:public-key</a> | <a href="authn.md#authn-jwt-jwks">authn-jwt:jwks</a> | <a href="authn.md#authn-scram-builtin_db-authentication">authn-scram-builtin_db:authentication</a></code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:lwm2m_translators <a id='gateway-lwm2m_translators'></a>
MQTT topics that correspond to LwM2M events.

| Config paths | Env overrides |
|----------------------------------------|-----------------------------------------------|
|  <code>gateway.lwm2m.translators</code> | <code>EMQX_GATEWAY__LWM2M__TRANSLATORS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>command</h4>
The topic for receiving downstream commands.
For each new LwM2M client that succeeds in going online, the gateway creates a subscription relationship to receive downstream commands and send it to the LwM2M client

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-translator">gateway:translator</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>response</h4>
The topic for gateway to publish the acknowledge events from LwM2M client

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-translator">gateway:translator</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>notify</h4>
The topic for gateway to publish the notify events from LwM2M client.
After succeed observe a resource of LwM2M client, Gateway will send the notify events via this topic, if the client reports any resource changes

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-translator">gateway:translator</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>register</h4>
The topic for gateway to publish the register events from LwM2M client.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-translator">gateway:translator</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>update</h4>
The topic for gateway to publish the update events from LwM2M client

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-translator">gateway:translator</a></code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:mqttsn <a id='gateway-mqttsn'></a>
The MQTT-SN (MQTT for Sensor Networks) protocol gateway.

| Config paths | Env overrides |
|-----------------------------|-----------------------------------|
|  <code>gateway.mqttsn</code> | <code>EMQX_GATEWAY__MQTTSN</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>gateway_id</h4>
MQTT-SN Gateway ID.
When the <code>broadcast</code> option is enabled, the gateway will broadcast ADVERTISE message with this value

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1</code></td></tr></tbody>
</table>
</li>
<li>
<h4>broadcast</h4>
Whether to periodically broadcast ADVERTISE messages

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_qos3</h4>
Allows connectionless clients to publish messages with a Qos of -1.
This feature is defined for very simple client implementations which do not support any other features except this one. There is no connection setup nor tear down, no registration nor subscription. The client just sends its 'PUBLISH' messages to a GW

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>subs_resume</h4>
Whether to initiate all subscribed topic name registration messages to the client after the Session has been taken over by a new channel

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>predefined</h4>
The pre-defined topic IDs and topic names.
A 'pre-defined' topic ID is a topic ID whose mapping to a topic name is known in advance by both the client's application and the gateway

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[<a href="gateway-mqttsn_predefined">gateway:mqttsn_predefined</a>]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mountpoint</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>
<li>
<h4>listeners</h4>
Settings for the UDP listeners.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-udp_listeners">gateway:udp_listeners</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Whether to enable this gateway

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_stats</h4>
Whether to enable client process statistic

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>idle_timeout</h4>
The idle time of the client connection process. It has two purposes:
  1. A newly created client process that does not receive any client requests after that time will be closed directly.
  2. A running client process that does not receive any client requests after this time will go into hibernation to save resources.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>clientinfo_override</h4>
ClientInfo override.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-clientinfo_override">gateway:clientinfo_override</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication</h4>
Default authentication configs for all the gateway listeners. For per-listener overrides see <code>authentication</code>
 in listener configs

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="authn.md#authn-builtin_db-authentication">authn-builtin_db:authentication</a> | <a href="authn.md#authn-mysql-authentication">authn-mysql:authentication</a> | <a href="authn.md#authn-postgresql-authentication">authn-postgresql:authentication</a> | <a href="authn.md#authn-mongodb-standalone">authn-mongodb:standalone</a> | <a href="authn.md#authn-mongodb-replica-set">authn-mongodb:replica-set</a> | <a href="authn.md#authn-mongodb-sharded-cluster">authn-mongodb:sharded-cluster</a> | <a href="authn.md#authn-redis-standalone">authn-redis:standalone</a> | <a href="authn.md#authn-redis-cluster">authn-redis:cluster</a> | <a href="authn.md#authn-redis-sentinel">authn-redis:sentinel</a> | <a href="authn.md#authn-http-get">authn-http:get</a> | <a href="authn.md#authn-http-post">authn-http:post</a> | <a href="authn.md#authn-jwt-hmac-based">authn-jwt:hmac-based</a> | <a href="authn.md#authn-jwt-public-key">authn-jwt:public-key</a> | <a href="authn.md#authn-jwt-jwks">authn-jwt:jwks</a> | <a href="authn.md#authn-scram-builtin_db-authentication">authn-scram-builtin_db:authentication</a></code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:mqttsn_predefined <a id='gateway-mqttsn_predefined'></a>
The pre-defined topic name corresponding to the pre-defined topic
ID of N.

Note: the pre-defined topic ID of 0 is reserved.

| Config paths | Env overrides |
|-----------------------------------------------|-------------------------------------------------------|
|  <code>gateway.mqttsn.predefined.$INDEX</code> | <code>EMQX_GATEWAY__MQTTSN__PREDEFINED__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>id</h4>
Topic ID. Range: 1-65535

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>topic</h4>
Topic Name

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:ssl_listener <a id='gateway-ssl_listener'></a>
Settings for the SSL listener.

| Config paths | Env overrides |
|--------------------------------------------------|-----------------------------------------------------------|
|  <code>gateway.exproto.listeners.ssl.$name</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME</code>  |
|  <code>gateway.stomp.listeners.ssl.$name</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>acceptors</h4>
Size of the acceptor pool.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>16</code></td></tr></tbody>
</table>
</li>
<li>
<h4>tcp_options</h4>
Setting the TCP socket options.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-tcp_opts">broker:tcp_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_protocol</h4>
Enable the Proxy Protocol V1/2 if the EMQX cluster is deployed behind HAProxy or Nginx.
See: https://www.haproxy.com/blog/haproxy/proxy-protocol/

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_protocol_timeout</h4>
Timeout for proxy protocol.
EMQX will close the TCP connection if proxy protocol packet is not received within the timeout.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Enable the listener.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bind</h4>
The IP address and port that the listener will bind.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:ip_port() | integer()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_connections</h4>
Maximum number of concurrent connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1024</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_conn_rate</h4>
Maximum connections per second.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication</h4>
Default authentication configs for all the gateway listeners. For per-listener overrides see <code>authentication</code>
 in listener configs

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="authn.md#authn-builtin_db-authentication">authn-builtin_db:authentication</a> | <a href="authn.md#authn-mysql-authentication">authn-mysql:authentication</a> | <a href="authn.md#authn-postgresql-authentication">authn-postgresql:authentication</a> | <a href="authn.md#authn-mongodb-standalone">authn-mongodb:standalone</a> | <a href="authn.md#authn-mongodb-replica-set">authn-mongodb:replica-set</a> | <a href="authn.md#authn-mongodb-sharded-cluster">authn-mongodb:sharded-cluster</a> | <a href="authn.md#authn-redis-standalone">authn-redis:standalone</a> | <a href="authn.md#authn-redis-cluster">authn-redis:cluster</a> | <a href="authn.md#authn-redis-sentinel">authn-redis:sentinel</a> | <a href="authn.md#authn-http-get">authn-http:get</a> | <a href="authn.md#authn-http-post">authn-http:post</a> | <a href="authn.md#authn-jwt-hmac-based">authn-jwt:hmac-based</a> | <a href="authn.md#authn-jwt-public-key">authn-jwt:public-key</a> | <a href="authn.md#authn-jwt-jwks">authn-jwt:jwks</a> | <a href="authn.md#authn-scram-builtin_db-authentication">authn-scram-builtin_db:authentication</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_authn</h4>
Set <code>true</code> (default) to enable client authentication on this listener. 
When set to <code>false</code> clients will be allowed to connect without authentication.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mountpoint</h4>
When publishing or subscribing, prefix all topics with a mountpoint string.
The prefixed string will be removed from the topic name when the message is delivered to the subscriber.
The mountpoint is a way that users can use to implement isolation of message routing between different listeners.
For example if a client A subscribes to `t` with `listeners.tcp.\<name>.mountpoint` set to `some_tenant`,
then the client actually subscribes to the topic `some_tenant/t`.
Similarly, if another client B (connected to the same listener as the client A) sends a message to topic `t`,
the message is routed to all the clients subscribed `some_tenant/t`,
so client A will receive the message, with topic name `t`. Set to `""` to disable the feature.
Variables in mountpoint string:<br/>
  - <code>${clientid}</code>: clientid<br/>
  - <code>${username}</code>: username

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>access_rules</h4>
The access control rules for this listener.
See: https://github.com/emqtt/esockd#allowdeny

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[string()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl_options</h4>
SSL Socket options.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-listener_ssl_opts">broker:listener_ssl_opts</a></code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:ssl_server_opts <a id='gateway-ssl_server_opts'></a>
SSL configuration for the server.

| Config paths | Env overrides |
|-------------------------------------------------|---------------------------------------------------------|
|  <code>gateway.exproto.server.ssl_options</code> | <code>EMQX_GATEWAY__EXPROTO__SERVER__SSL_OPTIONS</code>  |


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

## gateway:stomp <a id='gateway-stomp'></a>
The STOMP protocol gateway provides EMQX with the ability to access STOMP
(Simple (or Streaming) Text Orientated Messaging Protocol) protocol.

| Config paths | Env overrides |
|----------------------------|----------------------------------|
|  <code>gateway.stomp</code> | <code>EMQX_GATEWAY__STOMP</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>frame</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-stomp_frame">gateway:stomp_frame</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>mountpoint</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>
<li>
<h4>listeners</h4>
Settings for the TCP listeners.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-tcp_listeners">gateway:tcp_listeners</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Whether to enable this gateway

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_stats</h4>
Whether to enable client process statistic

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>idle_timeout</h4>
The idle time of the client connection process. It has two purposes:
  1. A newly created client process that does not receive any client requests after that time will be closed directly.
  2. A running client process that does not receive any client requests after this time will go into hibernation to save resources.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>clientinfo_override</h4>
ClientInfo override.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-clientinfo_override">gateway:clientinfo_override</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication</h4>
Default authentication configs for all the gateway listeners. For per-listener overrides see <code>authentication</code>
 in listener configs

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="authn.md#authn-builtin_db-authentication">authn-builtin_db:authentication</a> | <a href="authn.md#authn-mysql-authentication">authn-mysql:authentication</a> | <a href="authn.md#authn-postgresql-authentication">authn-postgresql:authentication</a> | <a href="authn.md#authn-mongodb-standalone">authn-mongodb:standalone</a> | <a href="authn.md#authn-mongodb-replica-set">authn-mongodb:replica-set</a> | <a href="authn.md#authn-mongodb-sharded-cluster">authn-mongodb:sharded-cluster</a> | <a href="authn.md#authn-redis-standalone">authn-redis:standalone</a> | <a href="authn.md#authn-redis-cluster">authn-redis:cluster</a> | <a href="authn.md#authn-redis-sentinel">authn-redis:sentinel</a> | <a href="authn.md#authn-http-get">authn-http:get</a> | <a href="authn.md#authn-http-post">authn-http:post</a> | <a href="authn.md#authn-jwt-hmac-based">authn-jwt:hmac-based</a> | <a href="authn.md#authn-jwt-public-key">authn-jwt:public-key</a> | <a href="authn.md#authn-jwt-jwks">authn-jwt:jwks</a> | <a href="authn.md#authn-scram-builtin_db-authentication">authn-scram-builtin_db:authentication</a></code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:stomp_frame <a id='gateway-stomp_frame'></a>
Size limits for the STOMP frames.

| Config paths | Env overrides |
|----------------------------------|-----------------------------------------|
|  <code>gateway.stomp.frame</code> | <code>EMQX_GATEWAY__STOMP__FRAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>max_headers</h4>
The maximum number of Header

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>10</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_headers_length</h4>
The maximum string length of the Header Value

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1024</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_body_length</h4>
Maximum number of bytes of Body allowed per Stomp packet

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>65536</code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:tcp_listener <a id='gateway-tcp_listener'></a>
Settings for the TCP listener.

| Config paths | Env overrides |
|--------------------------------------------------|-----------------------------------------------------------|
|  <code>gateway.exproto.listeners.tcp.$name</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME</code>  |
|  <code>gateway.stomp.listeners.tcp.$name</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>acceptors</h4>
Size of the acceptor pool.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>16</code></td></tr></tbody>
</table>
</li>
<li>
<h4>tcp_options</h4>
Setting the TCP socket options.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="emqx.md#broker-tcp_opts">broker:tcp_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_protocol</h4>
Enable the Proxy Protocol V1/2 if the EMQX cluster is deployed behind HAProxy or Nginx.
See: https://www.haproxy.com/blog/haproxy/proxy-protocol/

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_protocol_timeout</h4>
Timeout for proxy protocol.
EMQX will close the TCP connection if proxy protocol packet is not received within the timeout.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Enable the listener.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bind</h4>
The IP address and port that the listener will bind.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:ip_port() | integer()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_connections</h4>
Maximum number of concurrent connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1024</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_conn_rate</h4>
Maximum connections per second.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication</h4>
Default authentication configs for all the gateway listeners. For per-listener overrides see <code>authentication</code>
 in listener configs

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="authn.md#authn-builtin_db-authentication">authn-builtin_db:authentication</a> | <a href="authn.md#authn-mysql-authentication">authn-mysql:authentication</a> | <a href="authn.md#authn-postgresql-authentication">authn-postgresql:authentication</a> | <a href="authn.md#authn-mongodb-standalone">authn-mongodb:standalone</a> | <a href="authn.md#authn-mongodb-replica-set">authn-mongodb:replica-set</a> | <a href="authn.md#authn-mongodb-sharded-cluster">authn-mongodb:sharded-cluster</a> | <a href="authn.md#authn-redis-standalone">authn-redis:standalone</a> | <a href="authn.md#authn-redis-cluster">authn-redis:cluster</a> | <a href="authn.md#authn-redis-sentinel">authn-redis:sentinel</a> | <a href="authn.md#authn-http-get">authn-http:get</a> | <a href="authn.md#authn-http-post">authn-http:post</a> | <a href="authn.md#authn-jwt-hmac-based">authn-jwt:hmac-based</a> | <a href="authn.md#authn-jwt-public-key">authn-jwt:public-key</a> | <a href="authn.md#authn-jwt-jwks">authn-jwt:jwks</a> | <a href="authn.md#authn-scram-builtin_db-authentication">authn-scram-builtin_db:authentication</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_authn</h4>
Set <code>true</code> (default) to enable client authentication on this listener. 
When set to <code>false</code> clients will be allowed to connect without authentication.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mountpoint</h4>
When publishing or subscribing, prefix all topics with a mountpoint string.
The prefixed string will be removed from the topic name when the message is delivered to the subscriber.
The mountpoint is a way that users can use to implement isolation of message routing between different listeners.
For example if a client A subscribes to `t` with `listeners.tcp.\<name>.mountpoint` set to `some_tenant`,
then the client actually subscribes to the topic `some_tenant/t`.
Similarly, if another client B (connected to the same listener as the client A) sends a message to topic `t`,
the message is routed to all the clients subscribed `some_tenant/t`,
so client A will receive the message, with topic name `t`. Set to `""` to disable the feature.
Variables in mountpoint string:<br/>
  - <code>${clientid}</code>: clientid<br/>
  - <code>${username}</code>: username

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>access_rules</h4>
The access control rules for this listener.
See: https://github.com/emqtt/esockd#allowdeny

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[string()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:tcp_listeners <a id='gateway-tcp_listeners'></a>
Settings for the TCP listeners.

| Config paths | Env overrides |
|--------------------------------------|---------------------------------------------|
|  <code>gateway.stomp.listeners</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>tcp</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="gateway-tcp_listener">gateway:tcp_listener</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="gateway-ssl_listener">gateway:ssl_listener</a>}</code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:tcp_udp_listeners <a id='gateway-tcp_udp_listeners'></a>
Settings for the listeners.

| Config paths | Env overrides |
|----------------------------------------|-----------------------------------------------|
|  <code>gateway.exproto.listeners</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>tcp</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="gateway-tcp_listener">gateway:tcp_listener</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="gateway-ssl_listener">gateway:ssl_listener</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>udp</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="gateway-udp_listener">gateway:udp_listener</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>dtls</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="gateway-dtls_listener">gateway:dtls_listener</a>}</code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:translator <a id='gateway-translator'></a>
MQTT topic that corresponds to a particular type of event.

| Config paths | Env overrides |
|-------------------------------------------------|---------------------------------------------------------|
|  <code>gateway.lwm2m.translators.command</code> | <code>EMQX_GATEWAY__LWM2M__TRANSLATORS__COMMAND</code>  |
|  <code>gateway.lwm2m.translators.notify</code> | <code>EMQX_GATEWAY__LWM2M__TRANSLATORS__NOTIFY</code>  |
|  <code>gateway.lwm2m.translators.register</code> | <code>EMQX_GATEWAY__LWM2M__TRANSLATORS__REGISTER</code>  |
|  <code>gateway.lwm2m.translators.response</code> | <code>EMQX_GATEWAY__LWM2M__TRANSLATORS__RESPONSE</code>  |
|  <code>gateway.lwm2m.translators.update</code> | <code>EMQX_GATEWAY__LWM2M__TRANSLATORS__UPDATE</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>topic</h4>
Topic Name

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>qos</h4>
QoS Level

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>qos()</code></td></tr><tr><td><strong>Default</strong></td><td><code>0</code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:udp_listener <a id='gateway-udp_listener'></a>
Settings for the UDP listener.

| Config paths | Env overrides |
|--------------------------------------------------|-----------------------------------------------------------|
|  <code>gateway.coap.listeners.udp.$name</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME</code>  |
|  <code>gateway.exproto.listeners.udp.$name</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>udp_options</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="gateway-udp_opts">gateway:udp_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Enable the listener.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bind</h4>
The IP address and port that the listener will bind.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:ip_port() | integer()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_connections</h4>
Maximum number of concurrent connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1024</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_conn_rate</h4>
Maximum connections per second.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1000</code></td></tr></tbody>
</table>
</li>
<li>
<h4>authentication</h4>
Default authentication configs for all the gateway listeners. For per-listener overrides see <code>authentication</code>
 in listener configs

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="authn.md#authn-builtin_db-authentication">authn-builtin_db:authentication</a> | <a href="authn.md#authn-mysql-authentication">authn-mysql:authentication</a> | <a href="authn.md#authn-postgresql-authentication">authn-postgresql:authentication</a> | <a href="authn.md#authn-mongodb-standalone">authn-mongodb:standalone</a> | <a href="authn.md#authn-mongodb-replica-set">authn-mongodb:replica-set</a> | <a href="authn.md#authn-mongodb-sharded-cluster">authn-mongodb:sharded-cluster</a> | <a href="authn.md#authn-redis-standalone">authn-redis:standalone</a> | <a href="authn.md#authn-redis-cluster">authn-redis:cluster</a> | <a href="authn.md#authn-redis-sentinel">authn-redis:sentinel</a> | <a href="authn.md#authn-http-get">authn-http:get</a> | <a href="authn.md#authn-http-post">authn-http:post</a> | <a href="authn.md#authn-jwt-hmac-based">authn-jwt:hmac-based</a> | <a href="authn.md#authn-jwt-public-key">authn-jwt:public-key</a> | <a href="authn.md#authn-jwt-jwks">authn-jwt:jwks</a> | <a href="authn.md#authn-scram-builtin_db-authentication">authn-scram-builtin_db:authentication</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_authn</h4>
Set <code>true</code> (default) to enable client authentication on this listener. 
When set to <code>false</code> clients will be allowed to connect without authentication.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mountpoint</h4>
When publishing or subscribing, prefix all topics with a mountpoint string.
The prefixed string will be removed from the topic name when the message is delivered to the subscriber.
The mountpoint is a way that users can use to implement isolation of message routing between different listeners.
For example if a client A subscribes to `t` with `listeners.tcp.\<name>.mountpoint` set to `some_tenant`,
then the client actually subscribes to the topic `some_tenant/t`.
Similarly, if another client B (connected to the same listener as the client A) sends a message to topic `t`,
the message is routed to all the clients subscribed `some_tenant/t`,
so client A will receive the message, with topic name `t`. Set to `""` to disable the feature.
Variables in mountpoint string:<br/>
  - <code>${clientid}</code>: clientid<br/>
  - <code>${username}</code>: username

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>access_rules</h4>
The access control rules for this listener.
See: https://github.com/emqtt/esockd#allowdeny

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[string()]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:udp_listeners <a id='gateway-udp_listeners'></a>
Settings for the UDP listeners.

| Config paths | Env overrides |
|---------------------------------------|----------------------------------------------|
|  <code>gateway.coap.listeners</code> | <code>EMQX_GATEWAY__COAP__LISTENERS</code>  |
|  <code>gateway.lwm2m.listeners</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS</code>  |
|  <code>gateway.mqttsn.listeners</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>udp</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="gateway-udp_listener">gateway:udp_listener</a>}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>dtls</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$name -> <a href="gateway-dtls_listener">gateway:dtls_listener</a>}</code></td></tr></tbody>
</table>
</li>

</ul>

## gateway:udp_opts <a id='gateway-udp_opts'></a>
Settings for the UDP sockets.

| Config paths | Env overrides |
|---------------------------------------------------------------|-------------------------------------------------------------------------|
|  <code>gateway.coap.listeners.dtls.$name.udp_options</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__UDP_OPTIONS</code>  |
|  <code>gateway.coap.listeners.udp.$name.udp_options</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__UDP_OPTIONS</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.udp_options</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__UDP_OPTIONS</code>  |
|  <code>gateway.exproto.listeners.udp.$name.udp_options</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__UDP_OPTIONS</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.udp_options</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__UDP_OPTIONS</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.udp_options</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__UDP_OPTIONS</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.udp_options</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__UDP_OPTIONS</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.udp_options</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__UDP_OPTIONS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>active_n</h4>
Specify the {active, N} option for the socket.
See: https://erlang.org/doc/man/inet.html#setopts-2

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>100</code></td></tr></tbody>
</table>
</li>
<li>
<h4>recbuf</h4>
Size of the kernel-space receive buffer for the socket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:bytesize()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>sndbuf</h4>
Size of the kernel-space send buffer for the socket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:bytesize()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>buffer</h4>
Size of the user-space buffer for the socket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_gateway_schema:bytesize()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>reuseaddr</h4>
Allow local reuse of port numbers.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>
