# Other Configurations

## api_key <a id='api_key'></a>
API Key, can be used to request API other than the management API key and the Dashboard user management API

| Config paths | Env overrides |
|----------------------|---------------------------|
|  <code>api_key</code> | <code>EMQX_API_KEY</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>bootstrap_file</h4>
Bootstrap file is used to add an api_key when emqx is launched,
      the format is:
       ```
       7e729ae70d23144b:2QILI9AcQ9BYlVqLDHQNWN2saIjBV4egr1CZneTNKr9CpK
       ec3907f865805db0:Ee3taYltUKtoBVD9C3XjQl9C6NXheip8Z9B69BpUv5JxVHL
       ```

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>

</ul>

## dashboard <a id='dashboard'></a>
Configuration for EMQX dashboard.

| Config paths | Env overrides |
|------------------------|-----------------------------|
|  <code>dashboard</code> | <code>EMQX_DASHBOARD</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>listeners</h4>
HTTP(s) listeners are identified by their protocol type and are
used to serve dashboard UI and restful HTTP API.
Listeners must have a unique combination of port number and IP address.
For example, an HTTP listener can listen on all configured IP addresses
on a given port for a machine by specifying the IP address 0.0.0.0.
Alternatively, the HTTP listener can specify a unique IP address for each listener,
but use the same port.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="dashboard-listeners">dashboard:listeners</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>default_username</h4>
The default username of the automatically created dashboard user.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"admin"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>default_password</h4>
The initial default password for dashboard 'admin' user.
For safety, it should be changed as soon as possible.
This value is not valid when you log in to Dashboard for the first time via the web
and change to a complex password as prompted.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"public"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>sample_interval</h4>
How often to update metrics displayed in the dashboard.
Note: `sample_interval` should be a divisor of 60, default is 10s.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_s()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"10s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>token_expired_time</h4>
JWT token expiration time. Default is 60 minutes

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"60m"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>cors</h4>
Support Cross-Origin Resource Sharing (CORS).
Allows a server to indicate any origins (domain, scheme, or port) other than
its own from which a browser should permit loading resources.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>i18n_lang</h4>
Internationalization language support.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>en | zh</code></td></tr><tr><td><strong>Default</strong></td><td><code>en</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bootstrap_users_file</h4>
Deprecated, use api_key.bootstrap_file.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>

</ul>

## dashboard:http <a id='dashboard-http'></a>
Configuration for the dashboard listener (plaintext).

| Config paths | Env overrides |
|---------------------------------------|----------------------------------------------|
|  <code>dashboard.listeners.http</code> | <code>EMQX_DASHBOARD__LISTENERS__HTTP</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Ignore or enable this listener

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bind</h4>
Port without IP(18083) or port with specified IP(127.0.0.1:18083).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer() | emqx_schema:ip_port()</code></td></tr><tr><td><strong>Default</strong></td><td><code>18083</code></td></tr></tbody>
</table>
</li>
<li>
<h4>num_acceptors</h4>
Socket acceptor pool size for TCP protocols. Default is the number of schedulers online

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>20</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_connections</h4>
Maximum number of simultaneous connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>512</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backlog</h4>
Defines the maximum length that the queue of pending connections can grow to.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1024</code></td></tr></tbody>
</table>
</li>
<li>
<h4>send_timeout</h4>
Send timeout for the socket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"10s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>inet6</h4>
Enable IPv6 support, default is false, which means IPv4 only.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ipv6_v6only</h4>
Disable IPv4-to-IPv6 mapping for the listener.
The configuration is only valid when the inet6 is true.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_header</h4>
Enable support for `HAProxy` header. Be aware once enabled regular HTTP requests can't be handled anymore.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>

</ul>

## dashboard:https <a id='dashboard-https'></a>
Configuration for the dashboard listener (TLS).

| Config paths | Env overrides |
|----------------------------------------|-----------------------------------------------|
|  <code>dashboard.listeners.https</code> | <code>EMQX_DASHBOARD__LISTENERS__HTTPS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Ignore or enable this listener

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bind</h4>
Port without IP(18083) or port with specified IP(127.0.0.1:18083).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer() | emqx_schema:ip_port()</code></td></tr><tr><td><strong>Default</strong></td><td><code>18084</code></td></tr></tbody>
</table>
</li>
<li>
<h4>num_acceptors</h4>
Socket acceptor pool size for TCP protocols. Default is the number of schedulers online

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>20</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_connections</h4>
Maximum number of simultaneous connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>512</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backlog</h4>
Defines the maximum length that the queue of pending connections can grow to.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1024</code></td></tr></tbody>
</table>
</li>
<li>
<h4>send_timeout</h4>
Send timeout for the socket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"10s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>inet6</h4>
Enable IPv6 support, default is false, which means IPv4 only.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ipv6_v6only</h4>
Disable IPv4-to-IPv6 mapping for the listener.
The configuration is only valid when the inet6 is true.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proxy_header</h4>
Enable support for `HAProxy` header. Be aware once enabled regular HTTP requests can't be handled anymore.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
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

## dashboard:listeners <a id='dashboard-listeners'></a>
Configuration for the dashboard listener.

| Config paths | Env overrides |
|----------------------------------|----------------------------------------|
|  <code>dashboard.listeners</code> | <code>EMQX_DASHBOARD__LISTENERS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>http</h4>
TCP listeners

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="dashboard-http">dashboard:http</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>https</h4>
SSL listeners

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="dashboard-https">dashboard:https</a></code></td></tr></tbody>
</table>
</li>

</ul>

## exhook <a id='exhook'></a>
External hook (exhook) configuration.

| Config paths | Env overrides |
|---------------------|--------------------------|
|  <code>exhook</code> | <code>EMQX_EXHOOK</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>servers</h4>
List of exhook servers

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[<a href="exhook-server">exhook:server</a>]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>

</ul>

## exhook:server <a id='exhook-server'></a>
gRPC server configuration.

| Config paths | Env overrides |
|------------------------------------|-------------------------------------------|
|  <code>exhook.servers.$INDEX</code> | <code>EMQX_EXHOOK__SERVERS__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>name</h4>
Name of the exhook server

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Enable this Exhook server

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>url</h4>
URL of the gRPC server

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>request_timeout</h4>
The timeout of request gRPC server

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>failed_action</h4>
The value that is returned when the request to the gRPC server fails for any reason

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>deny | ignore</code></td></tr><tr><td><strong>Default</strong></td><td><code>deny</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ssl</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="exhook-ssl_conf">exhook:ssl_conf</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>socket_options</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="exhook-socket_options">exhook:socket_options</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{keepalive = true, nodelay = true}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>auto_reconnect</h4>
Whether to automatically reconnect (initialize) the gRPC server.
When gRPC is not available, Exhook tries to request the gRPC service at that interval and reinitialize the list of mounted hooks.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>false | emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"60s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>pool_size</h4>
The process pool size for gRPC client

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8</code></td></tr></tbody>
</table>
</li>

</ul>

## exhook:socket_options <a id='exhook-socket_options'></a>
Connection socket options

| Config paths | Env overrides |
|---------------------------------------------------|-----------------------------------------------------------|
|  <code>exhook.servers.$INDEX.socket_options</code> | <code>EMQX_EXHOOK__SERVERS__$INDEX__SOCKET_OPTIONS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>keepalive</h4>
Enables/disables periodic transmission on a connected socket when no other data is exchanged.
If the other end does not respond, the connection is considered broken and an error message is sent to the controlling process.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>nodelay</h4>
If true, option TCP_NODELAY is turned on for the socket,
which means that also small amounts of data are sent immediately

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>recbuf</h4>
The minimum size of receive buffer to use for the socket

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>sndbuf</h4>
The minimum size of send buffer to use for the socket

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr></tbody>
</table>
</li>

</ul>

## exhook:ssl_conf <a id='exhook-ssl_conf'></a>
SSL client configuration.

| Config paths | Env overrides |
|----------------------------------------|------------------------------------------------|
|  <code>exhook.servers.$INDEX.ssl</code> | <code>EMQX_EXHOOK__SERVERS__$INDEX__SSL</code>  |


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

## limiter:bucket_opts <a id='limiter-bucket_opts'></a>
Settings for the bucket.

| Config paths | Env overrides |
|-----------------------------------------------------------|--------------------------------------------------------------------|
|  <code>listeners.quic.$name.limiter.bytes_in</code> | <code>EMQX_LISTENERS__QUIC__$NAME__LIMITER__BYTES_IN</code>  |
|  <code>listeners.quic.$name.limiter.connection</code> | <code>EMQX_LISTENERS__QUIC__$NAME__LIMITER__CONNECTION</code>  |
|  <code>listeners.quic.$name.limiter.message_in</code> | <code>EMQX_LISTENERS__QUIC__$NAME__LIMITER__MESSAGE_IN</code>  |
|  <code>listeners.quic.$name.limiter.message_routing</code> | <code>EMQX_LISTENERS__QUIC__$NAME__LIMITER__MESSAGE_ROUTING</code>  |
|  <code>listeners.ssl.$name.limiter.bytes_in</code> | <code>EMQX_LISTENERS__SSL__$NAME__LIMITER__BYTES_IN</code>  |
|  <code>listeners.ssl.$name.limiter.connection</code> | <code>EMQX_LISTENERS__SSL__$NAME__LIMITER__CONNECTION</code>  |
|  <code>listeners.ssl.$name.limiter.message_in</code> | <code>EMQX_LISTENERS__SSL__$NAME__LIMITER__MESSAGE_IN</code>  |
|  <code>listeners.ssl.$name.limiter.message_routing</code> | <code>EMQX_LISTENERS__SSL__$NAME__LIMITER__MESSAGE_ROUTING</code>  |
|  <code>listeners.tcp.$name.limiter.bytes_in</code> | <code>EMQX_LISTENERS__TCP__$NAME__LIMITER__BYTES_IN</code>  |
|  <code>listeners.tcp.$name.limiter.connection</code> | <code>EMQX_LISTENERS__TCP__$NAME__LIMITER__CONNECTION</code>  |
|  <code>listeners.tcp.$name.limiter.message_in</code> | <code>EMQX_LISTENERS__TCP__$NAME__LIMITER__MESSAGE_IN</code>  |
|  <code>listeners.tcp.$name.limiter.message_routing</code> | <code>EMQX_LISTENERS__TCP__$NAME__LIMITER__MESSAGE_ROUTING</code>  |
|  <code>listeners.ws.$name.limiter.bytes_in</code> | <code>EMQX_LISTENERS__WS__$NAME__LIMITER__BYTES_IN</code>  |
|  <code>listeners.ws.$name.limiter.connection</code> | <code>EMQX_LISTENERS__WS__$NAME__LIMITER__CONNECTION</code>  |
|  <code>listeners.ws.$name.limiter.message_in</code> | <code>EMQX_LISTENERS__WS__$NAME__LIMITER__MESSAGE_IN</code>  |
|  <code>listeners.ws.$name.limiter.message_routing</code> | <code>EMQX_LISTENERS__WS__$NAME__LIMITER__MESSAGE_ROUTING</code>  |
|  <code>listeners.wss.$name.limiter.bytes_in</code> | <code>EMQX_LISTENERS__WSS__$NAME__LIMITER__BYTES_IN</code>  |
|  <code>listeners.wss.$name.limiter.connection</code> | <code>EMQX_LISTENERS__WSS__$NAME__LIMITER__CONNECTION</code>  |
|  <code>listeners.wss.$name.limiter.message_in</code> | <code>EMQX_LISTENERS__WSS__$NAME__LIMITER__MESSAGE_IN</code>  |
|  <code>listeners.wss.$name.limiter.message_routing</code> | <code>EMQX_LISTENERS__WSS__$NAME__LIMITER__MESSAGE_ROUTING</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>rate</h4>
Rate for this bucket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_limiter_schema:rate()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"infinity"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>capacity</h4>
The capacity of this token bucket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_limiter_schema:capacity()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"infinity"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>initial</h4>
The initial number of tokens for this bucket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_limiter_schema:initial()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"0"</code></td></tr></tbody>
</table>
</li>

</ul>

## limiter:client_fields <a id='limiter-client_fields'></a>
Fields of the client level.

| Config paths | Env overrides |
|-----------------------------|-----------------------------------|
|  <code>limiter.client</code> | <code>EMQX_LIMITER__CLIENT</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>bytes_in</h4>
The bytes_in limiter.
This is used to limit the inbound bytes rate for this EMQX node.
Once the limit is reached, the restricted client will be slow down even be hung for a while.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-client_opts">limiter:client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>message_in</h4>
The message in limiter.
This is used to limit the inbound message numbers for this EMQX node
Once the limit is reached, the restricted client will be slow down even be hung for a while.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-client_opts">limiter:client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>connection</h4>
The connection limiter.
This is used to limit the connection rate for this EMQX node.
Once the limit is reached, new connections will be refused

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-client_opts">limiter:client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>message_routing</h4>
The message routing limiter.
This is used to limit the forwarding rate for this EMQX node.
Once the limit is reached, new publish will be refused

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-client_opts">limiter:client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>internal</h4>
Limiter for EMQX internal app.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-client_opts">limiter:client_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>

</ul>

## limiter:client_opts <a id='limiter-client_opts'></a>
Settings for the client in bucket level.

| Config paths | Env overrides |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
|  <code>limiter.client.bytes_in</code> | <code>EMQX_LIMITER__CLIENT__BYTES_IN</code>  |
|  <code>limiter.client.connection</code> | <code>EMQX_LIMITER__CLIENT__CONNECTION</code>  |
|  <code>limiter.client.internal</code> | <code>EMQX_LIMITER__CLIENT__INTERNAL</code>  |
|  <code>limiter.client.message_in</code> | <code>EMQX_LIMITER__CLIENT__MESSAGE_IN</code>  |
|  <code>limiter.client.message_routing</code> | <code>EMQX_LIMITER__CLIENT__MESSAGE_ROUTING</code>  |
|  <code>listeners.quic.$name.limiter.client.bytes_in</code> | <code>EMQX_LISTENERS__QUIC__$NAME__LIMITER__CLIENT__BYTES_IN</code>  |
|  <code>listeners.quic.$name.limiter.client.connection</code> | <code>EMQX_LISTENERS__QUIC__$NAME__LIMITER__CLIENT__CONNECTION</code>  |
|  <code>listeners.quic.$name.limiter.client.message_in</code> | <code>EMQX_LISTENERS__QUIC__$NAME__LIMITER__CLIENT__MESSAGE_IN</code>  |
|  <code>listeners.quic.$name.limiter.client.message_routing</code> | <code>EMQX_LISTENERS__QUIC__$NAME__LIMITER__CLIENT__MESSAGE_ROUTING</code>  |
|  <code>listeners.ssl.$name.limiter.client.bytes_in</code> | <code>EMQX_LISTENERS__SSL__$NAME__LIMITER__CLIENT__BYTES_IN</code>  |
|  <code>listeners.ssl.$name.limiter.client.connection</code> | <code>EMQX_LISTENERS__SSL__$NAME__LIMITER__CLIENT__CONNECTION</code>  |
|  <code>listeners.ssl.$name.limiter.client.message_in</code> | <code>EMQX_LISTENERS__SSL__$NAME__LIMITER__CLIENT__MESSAGE_IN</code>  |
|  <code>listeners.ssl.$name.limiter.client.message_routing</code> | <code>EMQX_LISTENERS__SSL__$NAME__LIMITER__CLIENT__MESSAGE_ROUTING</code>  |
|  <code>listeners.tcp.$name.limiter.client.bytes_in</code> | <code>EMQX_LISTENERS__TCP__$NAME__LIMITER__CLIENT__BYTES_IN</code>  |
|  <code>listeners.tcp.$name.limiter.client.connection</code> | <code>EMQX_LISTENERS__TCP__$NAME__LIMITER__CLIENT__CONNECTION</code>  |
|  <code>listeners.tcp.$name.limiter.client.message_in</code> | <code>EMQX_LISTENERS__TCP__$NAME__LIMITER__CLIENT__MESSAGE_IN</code>  |
|  <code>listeners.tcp.$name.limiter.client.message_routing</code> | <code>EMQX_LISTENERS__TCP__$NAME__LIMITER__CLIENT__MESSAGE_ROUTING</code>  |
|  <code>listeners.ws.$name.limiter.client.bytes_in</code> | <code>EMQX_LISTENERS__WS__$NAME__LIMITER__CLIENT__BYTES_IN</code>  |
|  <code>listeners.ws.$name.limiter.client.connection</code> | <code>EMQX_LISTENERS__WS__$NAME__LIMITER__CLIENT__CONNECTION</code>  |
|  <code>listeners.ws.$name.limiter.client.message_in</code> | <code>EMQX_LISTENERS__WS__$NAME__LIMITER__CLIENT__MESSAGE_IN</code>  |
|  <code>listeners.ws.$name.limiter.client.message_routing</code> | <code>EMQX_LISTENERS__WS__$NAME__LIMITER__CLIENT__MESSAGE_ROUTING</code>  |
|  <code>listeners.wss.$name.limiter.client.bytes_in</code> | <code>EMQX_LISTENERS__WSS__$NAME__LIMITER__CLIENT__BYTES_IN</code>  |
|  <code>listeners.wss.$name.limiter.client.connection</code> | <code>EMQX_LISTENERS__WSS__$NAME__LIMITER__CLIENT__CONNECTION</code>  |
|  <code>listeners.wss.$name.limiter.client.message_in</code> | <code>EMQX_LISTENERS__WSS__$NAME__LIMITER__CLIENT__MESSAGE_IN</code>  |
|  <code>listeners.wss.$name.limiter.client.message_routing</code> | <code>EMQX_LISTENERS__WSS__$NAME__LIMITER__CLIENT__MESSAGE_ROUTING</code>  |
|  <code>retainer.flow_control.batch_deliver_limiter.client</code> | <code>EMQX_RETAINER__FLOW_CONTROL__BATCH_DELIVER_LIMITER__CLIENT</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>rate</h4>
Rate for this bucket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_limiter_schema:rate()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"infinity"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>initial</h4>
The initial number of tokens for this bucket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_limiter_schema:initial()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"0"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>low_watermark</h4>
If the remaining tokens are lower than this value,
the check/consume will succeed, but it will be forced to wait for a short period of time.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_limiter_schema:initial()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"0"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>capacity</h4>
The capacity of per user.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_limiter_schema:capacity()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"infinity"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>divisible</h4>
Is it possible to split the number of requested tokens?

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_retry_time</h4>
The maximum retry time when acquire failed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"10s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>failure_strategy</h4>
The strategy when all the retries failed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_limiter_schema:failure_strategy()</code></td></tr><tr><td><strong>Default</strong></td><td><code>force</code></td></tr></tbody>
</table>
</li>

</ul>

## limiter:internal <a id='limiter-internal'></a>
Internal limiter.

| Config paths | Env overrides |
|----------------------------------------------------------|-----------------------------------------------------------------|
|  <code>retainer.flow_control.batch_deliver_limiter</code> | <code>EMQX_RETAINER__FLOW_CONTROL__BATCH_DELIVER_LIMITER</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>rate</h4>
Rate for this bucket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_limiter_schema:rate()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"infinity"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>capacity</h4>
The capacity of this token bucket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_limiter_schema:capacity()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"infinity"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>initial</h4>
The initial number of tokens for this bucket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_limiter_schema:initial()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"0"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>client</h4>
The rate limit for each user of the bucket

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-client_opts">limiter:client_opts</a></code></td></tr></tbody>
</table>
</li>

</ul>

## limiter <a id='limiter'></a>
Settings for the rate limiter.

| Config paths | Env overrides |
|----------------------|---------------------------|
|  <code>limiter</code> | <code>EMQX_LIMITER</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>bytes_in</h4>
The bytes_in limiter.
This is used to limit the inbound bytes rate for this EMQX node.
Once the limit is reached, the restricted client will be slow down even be hung for a while.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-node_opts">limiter:node_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>message_in</h4>
The message in limiter.
This is used to limit the inbound message numbers for this EMQX node
Once the limit is reached, the restricted client will be slow down even be hung for a while.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-node_opts">limiter:node_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>connection</h4>
The connection limiter.
This is used to limit the connection rate for this EMQX node.
Once the limit is reached, new connections will be refused

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-node_opts">limiter:node_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>message_routing</h4>
The message routing limiter.
This is used to limit the forwarding rate for this EMQX node.
Once the limit is reached, new publish will be refused

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-node_opts">limiter:node_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>internal</h4>
Limiter for EMQX internal app.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-node_opts">limiter:node_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>client</h4>
The rate limit for each user of the bucket

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-client_fields">limiter:client_fields</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{
  bytes_in {}
  connection {}
  internal {}
  message_in {}
  message_routing {}
}
</code></td></tr></tbody>
</table>
</li>

</ul>

## limiter:listener_client_fields <a id='limiter-listener_client_fields'></a>
Fields of the client level of the listener.

| Config paths | Env overrides |
|--------------------------------------------------|-----------------------------------------------------------|
|  <code>listeners.quic.$name.limiter.client</code> | <code>EMQX_LISTENERS__QUIC__$NAME__LIMITER__CLIENT</code>  |
|  <code>listeners.ssl.$name.limiter.client</code> | <code>EMQX_LISTENERS__SSL__$NAME__LIMITER__CLIENT</code>  |
|  <code>listeners.tcp.$name.limiter.client</code> | <code>EMQX_LISTENERS__TCP__$NAME__LIMITER__CLIENT</code>  |
|  <code>listeners.ws.$name.limiter.client</code> | <code>EMQX_LISTENERS__WS__$NAME__LIMITER__CLIENT</code>  |
|  <code>listeners.wss.$name.limiter.client</code> | <code>EMQX_LISTENERS__WSS__$NAME__LIMITER__CLIENT</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>bytes_in</h4>
The bytes_in limiter.
This is used to limit the inbound bytes rate for this EMQX node.
Once the limit is reached, the restricted client will be slow down even be hung for a while.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-client_opts">limiter:client_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>message_in</h4>
The message in limiter.
This is used to limit the inbound message numbers for this EMQX node
Once the limit is reached, the restricted client will be slow down even be hung for a while.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-client_opts">limiter:client_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>connection</h4>
The connection limiter.
This is used to limit the connection rate for this EMQX node.
Once the limit is reached, new connections will be refused

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-client_opts">limiter:client_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>message_routing</h4>
The message routing limiter.
This is used to limit the forwarding rate for this EMQX node.
Once the limit is reached, new publish will be refused

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-client_opts">limiter:client_opts</a></code></td></tr></tbody>
</table>
</li>

</ul>

## limiter:listener_fields <a id='limiter-listener_fields'></a>
Fields of the listener.

| Config paths | Env overrides |
|-------------------------------------------|---------------------------------------------------|
|  <code>listeners.quic.$name.limiter</code> | <code>EMQX_LISTENERS__QUIC__$NAME__LIMITER</code>  |
|  <code>listeners.ssl.$name.limiter</code> | <code>EMQX_LISTENERS__SSL__$NAME__LIMITER</code>  |
|  <code>listeners.tcp.$name.limiter</code> | <code>EMQX_LISTENERS__TCP__$NAME__LIMITER</code>  |
|  <code>listeners.ws.$name.limiter</code> | <code>EMQX_LISTENERS__WS__$NAME__LIMITER</code>  |
|  <code>listeners.wss.$name.limiter</code> | <code>EMQX_LISTENERS__WSS__$NAME__LIMITER</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>bytes_in</h4>
The bytes_in limiter.
This is used to limit the inbound bytes rate for this EMQX node.
Once the limit is reached, the restricted client will be slow down even be hung for a while.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-bucket_opts">limiter:bucket_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>message_in</h4>
The message in limiter.
This is used to limit the inbound message numbers for this EMQX node
Once the limit is reached, the restricted client will be slow down even be hung for a while.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-bucket_opts">limiter:bucket_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>connection</h4>
The connection limiter.
This is used to limit the connection rate for this EMQX node.
Once the limit is reached, new connections will be refused

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-bucket_opts">limiter:bucket_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>message_routing</h4>
The message routing limiter.
This is used to limit the forwarding rate for this EMQX node.
Once the limit is reached, new publish will be refused

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-bucket_opts">limiter:bucket_opts</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>client</h4>
The rate limit for each user of the bucket

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-listener_client_fields">limiter:listener_client_fields</a></code></td></tr></tbody>
</table>
</li>

</ul>

## limiter:node_opts <a id='limiter-node_opts'></a>
Settings for the limiter of the node level.

| Config paths | Env overrides |
|--------------------------------------|--------------------------------------------|
|  <code>limiter.bytes_in</code> | <code>EMQX_LIMITER__BYTES_IN</code>  |
|  <code>limiter.connection</code> | <code>EMQX_LIMITER__CONNECTION</code>  |
|  <code>limiter.internal</code> | <code>EMQX_LIMITER__INTERNAL</code>  |
|  <code>limiter.message_in</code> | <code>EMQX_LIMITER__MESSAGE_IN</code>  |
|  <code>limiter.message_routing</code> | <code>EMQX_LIMITER__MESSAGE_ROUTING</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>rate</h4>
Rate for this bucket.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_limiter_schema:rate()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"infinity"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>burst</h4>
The burst, This value is based on rate.<br/>
 This value + rate = the maximum limit that can be achieved when limiter burst.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_limiter_schema:burst_rate()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"0"</code></td></tr></tbody>
</table>
</li>

</ul>

## modules:delayed <a id='modules-delayed'></a>
Settings for the delayed module.

| Config paths | Env overrides |
|----------------------|---------------------------|
|  <code>delayed</code> | <code>EMQX_DELAYED</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable this feature

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_delayed_messages</h4>
Maximum number of delayed messages (0 is no limit).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>0</code></td></tr></tbody>
</table>
</li>

</ul>

## modules:rewrite <a id='modules-rewrite'></a>
The topic rewriting function of EMQX supports rewriting topic A to topic B when the client subscribes to topics, publishes messages, and cancels subscriptions according to user-configured rules.
Each rewrite rule consists of three parts: subject filter, regular expression, and target expression.
Under the premise that the subject rewriting function is enabled, when EMQX receives a subject-based MQTT message such as a `PUBLISH` message,
it will use the subject of the message to sequentially match the subject filter part of the rule in the configuration file. If the match is successful,
the regular expression is used to extract the information in the subject, and then replaced with the target expression to form a new subject.
Variables in the format of `$N` can be used in the target expression to match the elements extracted from the regular expression.
The value of `$N` is the Nth element extracted from the regular expression. For example, `$1` is the regular expression. The first element extracted by the expression.
It should be noted that EMQX uses reverse order to read the rewrite rules in the configuration file.
When a topic can match the topic filter of multiple topic rewrite rules at the same time, EMQX will only use the first rule it matches. Rewrite.
If the regular expression in this rule does not match the subject of the MQTT message, the rewriting will fail, and no other rules will be attempted for rewriting.
Therefore, users need to carefully design MQTT message topics and topic rewriting rules when using them.

| Config paths | Env overrides |
|-----------------------------|-----------------------------------|
|  <code>rewrite.$INDEX</code> | <code>EMQX_REWRITE__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>action</h4>
Topic rewriting takes effect on the type of operation:
  - `subscribe`: Rewrite topic when client do subscribe.
  - `publish`: Rewrite topic when client do publish.
  - `all`: Both

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>subscribe | publish | all</code></td></tr></tbody>
</table>
</li>
<li>
<h4>source_topic</h4>
Source topic, specified by the client.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>dest_topic</h4>
Destination topic.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>re</h4>
Regular expressions

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>

</ul>

## modules:telemetry <a id='modules-telemetry'></a>
Settings for the telemetry module.

| Config paths | Env overrides |
|------------------------|-----------------------------|
|  <code>telemetry</code> | <code>EMQX_TELEMETRY</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable telemetry.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>

</ul>

## modules:topic_metrics <a id='modules-topic_metrics'></a>


| Config paths | Env overrides |
|-----------------------------------|-----------------------------------------|
|  <code>topic_metrics.$INDEX</code> | <code>EMQX_TOPIC_METRICS__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>topic</h4>
Collect metrics for the topic.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>

</ul>

## topology <a id='topology'></a>
Topology of MongoDB.

| Config paths | Env overrides |
|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
|  <code>authentication.$INDEX.topology</code> | <code>EMQX_AUTHENTICATION__$INDEX__TOPOLOGY</code>  |
|  <code>authorization.sources.$INDEX.topology</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX__TOPOLOGY</code>  |
|  <code>gateway.coap.authentication.topology</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication.topology</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication.topology</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.exproto.authentication.topology</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication.topology</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication.topology</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication.topology</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication.topology</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.lwm2m.authentication.topology</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication.topology</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication.topology</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.mqttsn.authentication.topology</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication.topology</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication.topology</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.stomp.authentication.topology</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication.topology</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication.topology</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION__TOPOLOGY</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX.topology</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX__TOPOLOGY</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX.topology</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX__TOPOLOGY</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX.topology</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX__TOPOLOGY</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX.topology</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX__TOPOLOGY</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>pool_size</h4>
Size of the connection pool towards the bridge target service.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>8</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_overflow</h4>
Max Overflow.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>0</code></td></tr></tbody>
</table>
</li>
<li>
<h4>overflow_ttl</h4>
Period of time before workers that exceed the configured pool size ("overflow") to be terminated.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>overflow_check_period</h4>
Period for checking if there are more workers than configured ("overflow").

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>local_threshold_ms</h4>
The size of the latency window for selecting among multiple suitable MongoDB instances.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>connect_timeout_ms</h4>
The duration to attempt a connection before timing out.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>socket_timeout_ms</h4>
The duration to attempt to send or to receive on a socket before the attempt times out.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>server_selection_timeout_ms</h4>
Specifies how long to block for server selection before throwing an exception.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>wait_queue_timeout_ms</h4>
The maximum duration that a worker can wait for a connection to become available.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>heartbeat_frequency_ms</h4>
Controls when the driver checks the state of the MongoDB deployment. Specify the interval between checks, counted from the end of the previous check until the beginning of the next one.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>min_heartbeat_frequency_ms</h4>
Controls the minimum amount of time to wait between heartbeats.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr></tbody>
</table>
</li>

</ul>

## zone:conn_congestion <a id='zone-conn_congestion'></a>
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
|------------------------------------------|-------------------------------------------------|
|  <code>zones.$name.conn_congestion</code> | <code>EMQX_ZONES__$NAME__CONN_CONGESTION</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable_alarm</h4>
Enable or disable connection congestion alarm.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>min_alarm_sustain_duration</h4>
Minimal time before clearing the alarm.<br/>The alarm is cleared only when there's no pending data in<br/>the queue, and at least <code>min_alarm_sustain_duration</code>milliseconds passed since the last time we considered the connection 'congested'.<br/>This is to avoid clearing and raising the alarm again too often.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr></tbody>
</table>
</li>

</ul>

## zone:flapping_detect <a id='zone-flapping_detect'></a>
This config controls the allowed maximum number of `CONNECT` packets received
from the same clientid in a time frame defined by `window_time`.
After the limit is reached, successive `CONNECT` requests are forbidden
(banned) until the end of the time period defined by `ban_time`.

| Config paths | Env overrides |
|------------------------------------------|-------------------------------------------------|
|  <code>zones.$name.flapping_detect</code> | <code>EMQX_ZONES__$NAME__FLAPPING_DETECT</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable flapping connection detection feature.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_count</h4>
The maximum number of disconnects allowed for a MQTT Client in `window_time`

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>window_time</h4>
The time window for flapping detection.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ban_time</h4>
How long the flapping clientid will be banned.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr></tbody>
</table>
</li>

</ul>

## zone:force_gc <a id='zone-force_gc'></a>
Force garbage collection in MQTT connection process after
 they process certain number of messages or bytes of data.

| Config paths | Env overrides |
|-----------------------------------|------------------------------------------|
|  <code>zones.$name.force_gc</code> | <code>EMQX_ZONES__$NAME__FORCE_GC</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable forced garbage collection.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>count</h4>
GC the process after this many received messages.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>0..inf</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bytes</h4>
GC the process after specified number of bytes have passed through.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr></tbody>
</table>
</li>

</ul>

## zone:force_shutdown <a id='zone-force_shutdown'></a>
When the process message queue length, or the memory bytes
reaches a certain value, the process is forced to close.

Note: "message queue" here refers to the "message mailbox"
of the Erlang process, not the `mqueue` of QoS 1 and QoS 2.

| Config paths | Env overrides |
|-----------------------------------------|------------------------------------------------|
|  <code>zones.$name.force_shutdown</code> | <code>EMQX_ZONES__$NAME__FORCE_SHUTDOWN</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable `force_shutdown` feature.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_message_queue_len</h4>
Maximum message queue length.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>0..inf</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_heap_size</h4>
Total heap size

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:wordsize()</code></td></tr></tbody>
</table>
</li>

</ul>

## zone:mqtt <a id='zone-mqtt'></a>
Global MQTT configuration.<br/>The configs here work as default values which can be overridden
in <code>zone</code> configs

| Config paths | Env overrides |
|-------------------------------|--------------------------------------|
|  <code>zones.$name.mqtt</code> | <code>EMQX_ZONES__$NAME__MQTT</code>  |


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
<tr><td><strong>Type</strong></td><td><code>infinity | emqx_schema:duration()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_packet_size</h4>
Maximum MQTT packet size allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_clientid_len</h4>
Maximum allowed length of MQTT Client ID.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>23..65535</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_topic_levels</h4>
Maximum topic levels allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1..65535</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_qos_allowed</h4>
Maximum QoS allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>qos()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_topic_alias</h4>
Maximum topic alias, 0 means no topic alias supported.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>0..65535</code></td></tr></tbody>
</table>
</li>
<li>
<h4>retain_available</h4>
Whether to enable support for MQTT retained message.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>wildcard_subscription</h4>
Whether to enable support for MQTT wildcard subscription.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>shared_subscription</h4>
Whether to enable support for MQTT shared subscription.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>exclusive_subscription</h4>
Whether to enable support for MQTT exclusive subscription.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>ignore_loop_deliver</h4>
Ignore loop delivery of messages for MQTT v3.1.1/v3.1.0, similar to <code>No Local</code> subscription option in MQTT 5.0.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>strict_mode</h4>
Parse MQTT messages in strict mode.
When set to true, invalid utf8 strings in for example client ID, topic name, etc. will cause the client to be disconnected

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>response_information</h4>
Specify the response information returned to the client. This feature is disabled if is set to "". Applies only to clients using MQTT 5.0.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>server_keepalive</h4>
The keep alive that EMQX requires the client to use. If configured as <code>disabled</code>, it means that the keep alive specified by the client will be used. Requires <code>Server Keep Alive</code> in MQTT 5.0, so it is only applicable to clients using MQTT 5.0 protocol.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer() | disabled</code></td></tr></tbody>
</table>
</li>
<li>
<h4>keepalive_backoff</h4>
The backoff multiplier used by the broker to determine the client keep alive timeout. If EMQX doesn't receive any packet in <code>Keep Alive * Backoff * 2</code> seconds, EMQX will close the current connection.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>number()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_subscriptions</h4>
Maximum number of subscriptions allowed per client.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1..inf | infinity</code></td></tr></tbody>
</table>
</li>
<li>
<h4>upgrade_qos</h4>
Force upgrade of QoS level according to subscription.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_inflight</h4>
Maximum number of QoS 1 and QoS 2 messages that are allowed to be delivered simultaneously before completing the acknowledgment.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>1..65535</code></td></tr></tbody>
</table>
</li>
<li>
<h4>retry_interval</h4>
Retry interval for QoS 1/2 message delivering.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_awaiting_rel</h4>
For each publisher session, the maximum number of outstanding QoS 2 messages pending on the client to send PUBREL. After reaching this limit, new QoS 2 PUBLISH requests will be rejected with `147(0x93)` until either PUBREL is received or timed out.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer() | infinity</code></td></tr></tbody>
</table>
</li>
<li>
<h4>await_rel_timeout</h4>
For client to broker QoS 2 message, the time limit for the broker to wait before the `PUBREL` message is received. The wait is aborted after timed out, meaning the packet ID is freed for new `PUBLISH` requests. Receiving a stale `PUBREL` causes a warning level log. Note, the message is delivered to subscribers before entering the wait for PUBREL.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>session_expiry_interval</h4>
Specifies how long the session will expire after the connection is disconnected, only for non-MQTT 5.0 connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_mqueue_len</h4>
Maximum queue length. Enqueued messages when persistent client disconnected, or inflight window is full.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer() | infinity</code></td></tr></tbody>
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
<tr><td><strong>Type</strong></td><td><code>map() | disabled</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mqueue_default_priority</h4>
Default topic priority, which will be used by topics not in <code>Topic Priorities</code> (<code>mqueue_priorities</code>).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>highest | lowest</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mqueue_store_qos0</h4>
Specifies whether to store QoS 0 messages in the message queue while the connection is down but the session remains.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>use_username_as_clientid</h4>
Whether to user Client ID as Username.
This setting takes effect later than <code>Use Peer Certificate as Username</code> (<code>peer_cert_as_username</code>) and <code>Use peer certificate as Client ID</code> (<code>peer_cert_as_clientid</code>).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
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
<tr><td><strong>Type</strong></td><td><code>disabled | cn | dn | crt | pem | md5</code></td></tr></tbody>
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
<tr><td><strong>Type</strong></td><td><code>disabled | cn | dn | crt | pem | md5</code></td></tr></tbody>
</table>
</li>

</ul>

## zone:overload_protection <a id='zone-overload_protection'></a>
Overload protection mechanism monitors the load of the system and temporarily
disables some features (such as accepting new connections) when the load is high.

| Config paths | Env overrides |
|----------------------------------------------|-----------------------------------------------------|
|  <code>zones.$name.overload_protection</code> | <code>EMQX_ZONES__$NAME__OVERLOAD_PROTECTION</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
React on system overload or not.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backoff_delay</h4>
The maximum duration of delay for background task execution during high load conditions.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>0..inf</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backoff_gc</h4>
When at high load, skip forceful GC.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backoff_hibernation</h4>
When at high load, skip process hibernation.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backoff_new_conn</h4>
When at high load, close new incoming connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>

</ul>

## zone:stats <a id='zone-stats'></a>
Enable/disable statistic data collection.
Statistic data such as message receive/send count/rate etc. It provides insights of system performance and helps to diagnose issues. You can find statistic data from the dashboard, or from the '/stats' API.

| Config paths | Env overrides |
|--------------------------------|---------------------------------------|
|  <code>zones.$name.stats</code> | <code>EMQX_ZONES__$NAME__STATS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable/disable statistic data collection.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>

</ul>

## authn-hash:bcrypt <a id='authn-hash-bcrypt'></a>
Settings for bcrypt password hashing algorithm.

| Config paths | Env overrides |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
|  <code>authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.coap.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.lwm2m.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.mqttsn.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.stomp.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>name</h4>
BCRYPT password hashing.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>bcrypt</code></td></tr></tbody>
</table>
</li>

</ul>

## authn-hash:bcrypt_rw <a id='authn-hash-bcrypt_rw'></a>
Settings for bcrypt password hashing algorithm (for DB backends with write capability).

| Config paths | Env overrides |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
|  <code>authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.coap.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.lwm2m.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.mqttsn.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.stomp.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>name</h4>
BCRYPT password hashing.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>bcrypt</code></td></tr></tbody>
</table>
</li>
<li>
<h4>salt_rounds</h4>
Salt rounds for BCRYPT password generation.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>10</code></td></tr></tbody>
</table>
</li>

</ul>

## authn-hash:pbkdf2 <a id='authn-hash-pbkdf2'></a>
Settings for PBKDF2 password hashing algorithm.

| Config paths | Env overrides |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
|  <code>authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.coap.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.lwm2m.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.mqttsn.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.stomp.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>name</h4>
PBKDF2 password hashing.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pbkdf2</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mac_fun</h4>
Specifies mac_fun for PBKDF2 hashing algorithm.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>md4 | md5 | ripemd160 | sha | sha224 | sha256 | sha384 | sha512</code></td></tr></tbody>
</table>
</li>
<li>
<h4>iterations</h4>
Iteration count for PBKDF2 hashing algorithm.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>dk_length</h4>
Derived length for PBKDF2 hashing algorithm. If not specified, calculated automatically based on `mac_fun`.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr></tbody>
</table>
</li>

</ul>

## authn-hash:simple <a id='authn-hash-simple'></a>
Settings for simple algorithms.

| Config paths | Env overrides |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
|  <code>authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.coap.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.lwm2m.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.mqttsn.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.stomp.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication.password_hash_algorithm</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX.password_hash_algorithm</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX__PASSWORD_HASH_ALGORITHM</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>name</h4>
Simple password hashing algorithm.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>plain | md5 | sha | sha256 | sha512</code></td></tr></tbody>
</table>
</li>
<li>
<h4>salt_position</h4>
Salt position for PLAIN, MD5, SHA, SHA256 and SHA512 algorithms.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>disable | prefix | suffix</code></td></tr><tr><td><strong>Default</strong></td><td><code>prefix</code></td></tr></tbody>
</table>
</li>

</ul>

## authn-psk:psk_authentication <a id='authn-psk-psk_authentication'></a>
PSK stands for 'Pre-Shared Keys'.
This config to enable TLS-PSK authentication.

Important! Make sure the SSL listener with only <code>tlsv1.2</code> enabled, and also PSK cipher suites
configured, such as <code>RSA-PSK-AES256-GCM-SHA384</code>.

See listener SSL options config for more details.

The IDs and secrets can be provided from a file which is configurable by the <code>init_file</code> field.

| Config paths | Env overrides |
|---------------------------------|--------------------------------------|
|  <code>psk_authentication</code> | <code>EMQX_PSK_AUTHENTICATION</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Whether to enable TLS PSK support

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>init_file</h4>
If init_file is specified, EMQX will import PSKs from the file into the built-in database at startup for use by the runtime.
The file has to be structured line-by-line, each line must be in the format of <code>PSKIdentity:SharedSecret</code>.
For example: <code>mydevice1:c2VjcmV0</code>

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>separator</h4>
The separator between <code>PSKIdentity</code> and <code>SharedSecret</code> in the PSK file

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>":"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>chunk_size</h4>
The size of each chunk used to import to the built-in database from PSK file

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>50</code></td></tr></tbody>
</table>
</li>

</ul>

## auto_subscribe <a id='auto_subscribe'></a>
After the device logs in successfully, the subscription is automatically completed for the device through the pre-defined subscription representation. Supports the use of placeholders.

| Config paths | Env overrides |
|-----------------------------|----------------------------------|
|  <code>auto_subscribe</code> | <code>EMQX_AUTO_SUBSCRIBE</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>topics</h4>
After the device logs in successfully, the subscription is automatically completed for the device through the pre-defined subscription representation. Supports the use of placeholders.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[<a href="auto_subscribe-topic">auto_subscribe:topic</a>]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>

</ul>

## auto_subscribe:topic <a id='auto_subscribe-topic'></a>
Topic name, placeholders are supported. For example: client/${clientid}/username/${username}/host/${host}/port/${port}
Required field, and cannot be empty string

| Config paths | Env overrides |
|-------------------------------------------|--------------------------------------------------|
|  <code>auto_subscribe.topics.$INDEX</code> | <code>EMQX_AUTO_SUBSCRIBE__TOPICS__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>topic</h4>
Topic name, placeholders are supported. For example: client/${clientid}/username/${username}/host/${host}/port/${port}
Required field, and cannot be empty string

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>qos</h4>
Default value 0. Quality of service.
At most once (0)
At least once (1)
Exactly once (2)

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>qos()</code></td></tr><tr><td><strong>Default</strong></td><td><code>0</code></td></tr></tbody>
</table>
</li>
<li>
<h4>rh</h4>
Default value 0. This option is used to specify whether the server forwards the retained message to the client when establishing a subscription.
Retain Handling is equal to 0, as long as the client successfully subscribes, the server will send the retained message.
Retain Handling is equal to 1, if the client successfully subscribes and this subscription does not exist previously, the server sends the retained message. After all, sometimes the client re-initiate the subscription just to change the QoS, but it does not mean that it wants to receive the reserved messages again.
Retain Handling is equal to 2, even if the client successfully subscribes, the server does not send the retained message.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>0..2</code></td></tr><tr><td><strong>Default</strong></td><td><code>0</code></td></tr></tbody>
</table>
</li>
<li>
<h4>rap</h4>
Default value 0. This option is used to specify whether the server retains the RETAIN mark when forwarding messages to the client, and this option does not affect the RETAIN mark in the retained message. Therefore, when the option Retain As Publish is set to 0, the client will directly distinguish whether this is a normal forwarded message or a retained message according to the RETAIN mark in the message, instead of judging whether this message is the first received after subscribing(the forwarded message may be sent before the retained message, which depends on the specific implementation of different brokers).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>0..1</code></td></tr><tr><td><strong>Default</strong></td><td><code>0</code></td></tr></tbody>
</table>
</li>
<li>
<h4>nl</h4>
Default value 0.
MQTT v3.1.1： if you subscribe to the topic published by yourself, you will receive all messages that you published.
MQTT v5: if you set this option as 1 when subscribing, the server will not forward the message you published to you.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>0..1</code></td></tr><tr><td><strong>Default</strong></td><td><code>0</code></td></tr></tbody>
</table>
</li>

</ul>

## bridge_mqtt:config <a id='bridge_mqtt-config'></a>
The config for MQTT Bridges.

| Config paths | Env overrides |
|---------------------------------|----------------------------------------|
|  <code>bridges.mqtt.$name</code> | <code>EMQX_BRIDGES__MQTT__$NAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable or disable this bridge

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>resource_opts</h4>
Resource options.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="bridge_mqtt-creation_opts">bridge_mqtt:creation_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>mode</h4>
The mode of the MQTT Bridge.<br/>
- cluster_shareload: create an MQTT connection on each node in the emqx cluster.<br/>
In 'cluster_shareload' mode, the incoming load from the remote broker is shared by
using shared subscription.<br/>
Note that the 'clientid' is suffixed by the node name, this is to avoid
clientid conflicts between different nodes. And we can only use shared subscription
topic filters for <code>remote.topic</code> of ingress connections.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>cluster_shareload</code></td></tr><tr><td><strong>Default</strong></td><td><code>cluster_shareload</code></td></tr></tbody>
</table>
</li>
<li>
<h4>server</h4>
The host and port of the remote MQTT broker

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>clientid_prefix</h4>
Optional prefix to prepend to the clientid used by egress bridges.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>reconnect_interval</h4>
Deprecated since v5.0.16.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>proto_ver</h4>
The MQTT protocol version

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>v3 | v4 | v5</code></td></tr><tr><td><strong>Default</strong></td><td><code>v4</code></td></tr></tbody>
</table>
</li>
<li>
<h4>bridge_mode</h4>
If enable bridge mode.
NOTE: This setting is only for MQTT protocol version older than 5.0, and the remote MQTT
broker MUST support this feature.
If bridge_mode is set to true, the bridge will indicate to the remote broker that it is a bridge not an ordinary client.
This means that loop detection will be more effective and that retained messages will be propagated correctly.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>username</h4>
The username of the MQTT protocol

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>password</h4>
The password of the MQTT protocol

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>clean_start</h4>
Whether to start a clean session when reconnecting a remote broker for ingress bridge

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>keepalive</h4>
MQTT Keepalive. Time interval is a string that contains a number followed by time unit:<br/>- `ms` for milliseconds,
- `s` for seconds,
- `m` for minutes,
- `h` for hours;
<br/>or combination of whereof: `1h5m0s`

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"300s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>retry_interval</h4>
Message retry interval. Delay for the MQTT bridge to retry sending the QoS1/QoS2 messages in case of ACK not received. Time interval is a string that contains a number followed by time unit:<br/>- `ms` for milliseconds,
- `s` for seconds,
- `m` for minutes,
- `h` for hours;
<br/>or combination of whereof: `1h5m0s`

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_inflight</h4>
Max inflight (sent, but un-acked) messages of the MQTT protocol

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>32</code></td></tr></tbody>
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
<h4>ingress</h4>
The ingress config defines how this bridge receive messages from the remote MQTT broker, and then
        send them to the local broker.<br/>
        Template with variables is allowed in 'remote.qos', 'local.topic', 'local.qos', 'local.retain', 'local.payload'.<br/>
        NOTE: if this bridge is used as the input of a rule, and also 'local.topic' is
        configured, then messages got from the remote broker will be sent to both the 'local.topic' and
        the rule.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="connector-mqtt-ingress">connector-mqtt:ingress</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>egress</h4>
The egress config defines how this bridge forwards messages from the local broker to the remote broker.<br/>
Template with variables is allowed in 'remote.topic', 'local.qos', 'local.retain', 'local.payload'.<br/>
NOTE: if this bridge is used as the action of a rule, and also 'local.topic'
is configured, then both the data got from the rule and the MQTT messages that matches
'local.topic' will be forwarded.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="connector-mqtt-egress">connector-mqtt:egress</a></code></td></tr></tbody>
</table>
</li>

</ul>

## bridge_mqtt:creation_opts <a id='bridge_mqtt-creation_opts'></a>
Creation options.

| Config paths | Env overrides |
|-----------------------------------------------|-------------------------------------------------------|
|  <code>bridges.mqtt.$name.resource_opts</code> | <code>EMQX_BRIDGES__MQTT__$NAME__RESOURCE_OPTS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>worker_pool_size</h4>
The number of buffer workers. Only applicable for egress type bridges.
For bridges only have ingress direction data flow, it can be set to 0 otherwise must be greater than 0.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>16</code></td></tr></tbody>
</table>
</li>
<li>
<h4>health_check_interval</h4>
Health check interval.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>start_after_created</h4>
Whether start the resource right after created.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"true"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>start_timeout</h4>
Time interval to wait for an auto-started resource to become healthy before responding resource creation requests.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>auto_restart_interval</h4>
The auto restart interval after the resource is disconnected.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>infinity | emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"60s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>query_mode</h4>
Query mode. Optional 'sync/async', default 'async'.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>sync | async</code></td></tr><tr><td><strong>Default</strong></td><td><code>async</code></td></tr></tbody>
</table>
</li>
<li>
<h4>request_timeout</h4>
Starting from the moment when the request enters the buffer, if the request remains in the buffer for the specified time or is sent but does not receive a response or acknowledgement in time, the request is considered expired.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>infinity | emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>async_inflight_window</h4>
Async query inflight window.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>100</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_queue</h4>
Deprecated since v5.0.14.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_queue_bytes</h4>
Maximum number of bytes to buffer for each buffer worker.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"100MB"</code></td></tr></tbody>
</table>
</li>

</ul>

## bridge_webhook:config <a id='bridge_webhook-config'></a>
Configuration for an HTTP bridge.

| Config paths | Env overrides |
|------------------------------------|-------------------------------------------|
|  <code>bridges.webhook.$name</code> | <code>EMQX_BRIDGES__WEBHOOK__$NAME</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable or disable this bridge

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>resource_opts</h4>
Resource options.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="bridge_webhook-creation_opts">bridge_webhook:creation_opts</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
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
<h4>retry_interval</h4>
Deprecated since 5.0.4.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>pool_type</h4>
The type of the pool. Can be one of `random`, `hash`.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_connector_http:pool_type()</code></td></tr><tr><td><strong>Default</strong></td><td><code>random</code></td></tr></tbody>
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
<h4>enable_pipelining</h4>
A positive integer. Whether to send HTTP requests continuously, when set to 1, it means that after each HTTP request is sent, you need to wait for the server to return and then continue to send the next request.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>100</code></td></tr></tbody>
</table>
</li>
<li>
<h4>request</h4>
Configure HTTP request parameters.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="connector-http-request">connector-http:request</a></code></td></tr></tbody>
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
<h4>url</h4>
The URL of the HTTP Bridge.<br/>
Template with variables is allowed in the path, but variables cannot be used in the scheme, host,
or port part.<br/>
For example, <code> http://localhost:9901/${topic} </code> is allowed, but
<code> http://${host}:9901/message </code> or <code> http://localhost:${port}/message </code>
is not allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>direction</h4>
Deprecated since 5.0.12.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>egress</code></td></tr></tbody>
</table>
</li>
<li>
<h4>local_topic</h4>
The MQTT topic filter to be forwarded to the HTTP server. All MQTT 'PUBLISH' messages with the topic
matching the local_topic will be forwarded.<br/>
NOTE: if this bridge is used as the action of a rule (EMQX rule engine), and also local_topic is
configured, then both the data got from the rule and the MQTT messages that match local_topic
will be forwarded.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>method</h4>
The method of the HTTP request. All the available methods are: post, put, get, delete.<br/>
Template with variables is allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>post | put | get | delete</code></td></tr><tr><td><strong>Default</strong></td><td><code>post</code></td></tr></tbody>
</table>
</li>
<li>
<h4>headers</h4>
The headers of the HTTP request.<br/>
Template with variables is allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr><tr><td><strong>Default</strong></td><td><code>{
  accept = "application/json"
  "cache-control" = "no-cache"
  connection = "keep-alive"
  "content-type" = "application/json"
  "keep-alive" = "timeout=5"
}
</code></td></tr></tbody>
</table>
</li>
<li>
<h4>body</h4>
The body of the HTTP request.<br/>
If not provided, the body will be a JSON object of all the available fields.<br/>
There, 'all the available fields' means the context of a MQTT message when
this webhook is triggered by receiving a MQTT message (the `local_topic` is set),
or the context of the event when this webhook is triggered by a rule (i.e. this
webhook is used as an action of a rule).<br/>
Template with variables is allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_retries</h4>
HTTP request max retry times if failed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>2</code></td></tr></tbody>
</table>
</li>
<li>
<h4>request_timeout</h4>
HTTP request timeout.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>

</ul>

## bridge_webhook:creation_opts <a id='bridge_webhook-creation_opts'></a>
Creation options.

| Config paths | Env overrides |
|--------------------------------------------------|----------------------------------------------------------|
|  <code>bridges.webhook.$name.resource_opts</code> | <code>EMQX_BRIDGES__WEBHOOK__$NAME__RESOURCE_OPTS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>worker_pool_size</h4>
The number of buffer workers. Only applicable for egress type bridges.
For bridges only have ingress direction data flow, it can be set to 0 otherwise must be greater than 0.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>16</code></td></tr></tbody>
</table>
</li>
<li>
<h4>health_check_interval</h4>
Health check interval.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>start_after_created</h4>
Whether start the resource right after created.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"true"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>start_timeout</h4>
Time interval to wait for an auto-started resource to become healthy before responding resource creation requests.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>auto_restart_interval</h4>
The auto restart interval after the resource is disconnected.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>infinity | emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"60s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>query_mode</h4>
Query mode. Optional 'sync/async', default 'async'.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>sync | async</code></td></tr><tr><td><strong>Default</strong></td><td><code>async</code></td></tr></tbody>
</table>
</li>
<li>
<h4>request_timeout</h4>
Starting from the moment when the request enters the buffer, if the request remains in the buffer for the specified time or is sent but does not receive a response or acknowledgement in time, the request is considered expired.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>infinity | emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>async_inflight_window</h4>
Async query inflight window.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>100</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable_queue</h4>
Deprecated since v5.0.14.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_queue_bytes</h4>
Maximum number of bytes to buffer for each buffer worker.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"100MB"</code></td></tr></tbody>
</table>
</li>

</ul>

## connector-http:request <a id='connector-http-request'></a>


| Config paths | Env overrides |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
|  <code>authentication.$INDEX.request</code> | <code>EMQX_AUTHENTICATION__$INDEX__REQUEST</code>  |
|  <code>authorization.sources.$INDEX.request</code> | <code>EMQX_AUTHORIZATION__SOURCES__$INDEX__REQUEST</code>  |
|  <code>bridges.webhook.$name.request</code> | <code>EMQX_BRIDGES__WEBHOOK__$NAME__REQUEST</code>  |
|  <code>gateway.coap.authentication.request</code> | <code>EMQX_GATEWAY__COAP__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.coap.listeners.dtls.$name.authentication.request</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__DTLS__$NAME__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.coap.listeners.udp.$name.authentication.request</code> | <code>EMQX_GATEWAY__COAP__LISTENERS__UDP__$NAME__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.exproto.authentication.request</code> | <code>EMQX_GATEWAY__EXPROTO__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.exproto.listeners.dtls.$name.authentication.request</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__DTLS__$NAME__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.exproto.listeners.ssl.$name.authentication.request</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__SSL__$NAME__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.exproto.listeners.tcp.$name.authentication.request</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__TCP__$NAME__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.exproto.listeners.udp.$name.authentication.request</code> | <code>EMQX_GATEWAY__EXPROTO__LISTENERS__UDP__$NAME__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.lwm2m.authentication.request</code> | <code>EMQX_GATEWAY__LWM2M__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.lwm2m.listeners.dtls.$name.authentication.request</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__DTLS__$NAME__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.lwm2m.listeners.udp.$name.authentication.request</code> | <code>EMQX_GATEWAY__LWM2M__LISTENERS__UDP__$NAME__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.mqttsn.authentication.request</code> | <code>EMQX_GATEWAY__MQTTSN__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.mqttsn.listeners.dtls.$name.authentication.request</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__DTLS__$NAME__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.mqttsn.listeners.udp.$name.authentication.request</code> | <code>EMQX_GATEWAY__MQTTSN__LISTENERS__UDP__$NAME__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.stomp.authentication.request</code> | <code>EMQX_GATEWAY__STOMP__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.stomp.listeners.ssl.$name.authentication.request</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__SSL__$NAME__AUTHENTICATION__REQUEST</code>  |
|  <code>gateway.stomp.listeners.tcp.$name.authentication.request</code> | <code>EMQX_GATEWAY__STOMP__LISTENERS__TCP__$NAME__AUTHENTICATION__REQUEST</code>  |
|  <code>listeners.ssl.$name.authentication.$INDEX.request</code> | <code>EMQX_LISTENERS__SSL__$NAME__AUTHENTICATION__$INDEX__REQUEST</code>  |
|  <code>listeners.tcp.$name.authentication.$INDEX.request</code> | <code>EMQX_LISTENERS__TCP__$NAME__AUTHENTICATION__$INDEX__REQUEST</code>  |
|  <code>listeners.ws.$name.authentication.$INDEX.request</code> | <code>EMQX_LISTENERS__WS__$NAME__AUTHENTICATION__$INDEX__REQUEST</code>  |
|  <code>listeners.wss.$name.authentication.$INDEX.request</code> | <code>EMQX_LISTENERS__WSS__$NAME__AUTHENTICATION__$INDEX__REQUEST</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>method</h4>
HTTP method.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>path</h4>
URL path.

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
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>headers</h4>
List of HTTP headers.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_retries</h4>
Max retry times if error on sending request.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>request_timeout</h4>
HTTP request timeout.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr></tbody>
</table>
</li>

</ul>

## connector-mqtt:egress <a id='connector-mqtt-egress'></a>
The egress config defines how this bridge forwards messages from the local broker to the remote broker.<br/>
Template with variables is allowed in 'remote.topic', 'local.qos', 'local.retain', 'local.payload'.<br/>
NOTE: if this bridge is used as the action of a rule, and also 'local.topic'
is configured, then both the data got from the rule and the MQTT messages that matches
'local.topic' will be forwarded.

| Config paths | Env overrides |
|----------------------------------------|------------------------------------------------|
|  <code>bridges.mqtt.$name.egress</code> | <code>EMQX_BRIDGES__MQTT__$NAME__EGRESS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>local</h4>
The configs about receiving messages from local broker.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="connector-mqtt-egress_local">connector-mqtt:egress_local</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>remote</h4>
The configs about sending message to the remote broker.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="connector-mqtt-egress_remote">connector-mqtt:egress_remote</a></code></td></tr></tbody>
</table>
</li>

</ul>

## connector-mqtt:egress_local <a id='connector-mqtt-egress_local'></a>
The configs about receiving messages from local broker.

| Config paths | Env overrides |
|----------------------------------------------|-------------------------------------------------------|
|  <code>bridges.mqtt.$name.egress.local</code> | <code>EMQX_BRIDGES__MQTT__$NAME__EGRESS__LOCAL</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>topic</h4>
The local topic to be forwarded to the remote broker

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>

</ul>

## connector-mqtt:egress_remote <a id='connector-mqtt-egress_remote'></a>
The configs about sending message to the remote broker.

| Config paths | Env overrides |
|-----------------------------------------------|--------------------------------------------------------|
|  <code>bridges.mqtt.$name.egress.remote</code> | <code>EMQX_BRIDGES__MQTT__$NAME__EGRESS__REMOTE</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>topic</h4>
Forward to which topic of the remote broker.<br/>
Template with variables is allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>qos</h4>
The QoS of the MQTT message to be sent.<br/>
Template with variables is allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>qos() | binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1</code></td></tr></tbody>
</table>
</li>
<li>
<h4>retain</h4>
The 'retain' flag of the MQTT message to be sent.<br/>
Template with variables is allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean() | binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>payload</h4>
The payload of the MQTT message to be sent.<br/>
Template with variables is allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>

</ul>

## connector-mqtt:ingress <a id='connector-mqtt-ingress'></a>
The ingress config defines how this bridge receive messages from the remote MQTT broker, and then
        send them to the local broker.<br/>
        Template with variables is allowed in 'remote.qos', 'local.topic', 'local.qos', 'local.retain', 'local.payload'.<br/>
        NOTE: if this bridge is used as the input of a rule, and also 'local.topic' is
        configured, then messages got from the remote broker will be sent to both the 'local.topic' and
        the rule.

| Config paths | Env overrides |
|-----------------------------------------|-------------------------------------------------|
|  <code>bridges.mqtt.$name.ingress</code> | <code>EMQX_BRIDGES__MQTT__$NAME__INGRESS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>remote</h4>
The configs about subscribing to the remote broker.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="connector-mqtt-ingress_remote">connector-mqtt:ingress_remote</a></code></td></tr></tbody>
</table>
</li>
<li>
<h4>local</h4>
The configs about sending message to the local broker.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="connector-mqtt-ingress_local">connector-mqtt:ingress_local</a></code></td></tr></tbody>
</table>
</li>

</ul>

## connector-mqtt:ingress_local <a id='connector-mqtt-ingress_local'></a>
The configs about sending message to the local broker.

| Config paths | Env overrides |
|-----------------------------------------------|--------------------------------------------------------|
|  <code>bridges.mqtt.$name.ingress.local</code> | <code>EMQX_BRIDGES__MQTT__$NAME__INGRESS__LOCAL</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>topic</h4>
Send messages to which topic of the local broker.<br/>
Template with variables is allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>qos</h4>
The QoS of the MQTT message to be sent.<br/>
Template with variables is allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>qos() | binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"${qos}"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>retain</h4>
The 'retain' flag of the MQTT message to be sent.<br/>
Template with variables is allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean() | binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"${retain}"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>payload</h4>
The payload of the MQTT message to be sent.<br/>
Template with variables is allowed.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>

</ul>

## connector-mqtt:ingress_remote <a id='connector-mqtt-ingress_remote'></a>
The configs about subscribing to the remote broker.

| Config paths | Env overrides |
|------------------------------------------------|---------------------------------------------------------|
|  <code>bridges.mqtt.$name.ingress.remote</code> | <code>EMQX_BRIDGES__MQTT__$NAME__INGRESS__REMOTE</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>topic</h4>
Receive messages from which topic of the remote broker

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>qos</h4>
The QoS level to be used when subscribing to the remote broker

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>qos()</code></td></tr><tr><td><strong>Default</strong></td><td><code>1</code></td></tr></tbody>
</table>
</li>

</ul>

## plugin:plugins <a id='plugin-plugins'></a>
Manage EMQX plugins.<br/>
Plugins can be pre-built as a part of EMQX package,
or installed as a standalone package in a location specified by
<code>install_dir</code> config key<br/>
The standalone-installed plugins are referred to as 'external' plugins.

| Config paths | Env overrides |
|----------------------|---------------------------|
|  <code>plugins</code> | <code>EMQX_PLUGINS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>states</h4>
An array of plugins in the desired states.<br/>
The plugins are started in the defined order

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[<a href="plugin-state">plugin:state</a>]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>install_dir</h4>
The installation directory for the external plugins.
The plugin beam files and configuration files should reside in
the subdirectory named as <code>emqx_foo_bar-0.1.0</code>.
<br/>
NOTE: For security reasons, this directory should **NOT** be writable
by anyone except <code>emqx</code> (or any user which runs EMQX).

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"plugins"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>check_interval</h4>
Check interval: check if the status of the plugins in the cluster is consistent, <br/>
if the results of 3 consecutive checks are not consistent, then alarm.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"5s"</code></td></tr></tbody>
</table>
</li>

</ul>

## plugin:state <a id='plugin-state'></a>
A per-plugin config to describe the desired state of the plugin.

| Config paths | Env overrides |
|------------------------------------|-------------------------------------------|
|  <code>plugins.states.$INDEX</code> | <code>EMQX_PLUGINS__STATES__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>name_vsn</h4>
The {name}-{version} of the plugin.<br/>
It should match the plugin application name-version as the for the plugin release package name<br/>
For example: my_plugin-0.1.0.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Set to 'true' to enable this plugin

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr></tbody>
</table>
</li>

</ul>

## prometheus <a id='prometheus'></a>
Settings for reporting metrics to Prometheus

| Config paths | Env overrides |
|-------------------------|------------------------------|
|  <code>prometheus</code> | <code>EMQX_PROMETHEUS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>push_gateway_server</h4>
URL of Prometheus server

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"http://127.0.0.1:9091"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>interval</h4>
Data reporting interval

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"15s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>headers</h4>
A list of HTTP Headers when pushing to Push Gateway.<br/>
For example, <code> { Authorization = "some-authz-tokens"}</code>

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[{string(), string()}]</code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>job_name</h4>
Job Name that is pushed to the Push Gateway. Available variables:<br/>
- ${name}: Name of EMQX node.<br/>
- ${host}: Host name of EMQX node.<br/>
For example, when the EMQX node name is <code>emqx@127.0.0.1</code> then the <code>name</code> variable takes value <code>emqx</code> and the <code>host</code> variable takes value <code>127.0.0.1</code>.<br/>
Default value is: <code>${name}/instance/${name}~${host}</code>

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"${name}/instance/${name}~${host}"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Turn Prometheus data pushing on or off

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>

</ul>

## retainer:flow_control <a id='retainer-flow_control'></a>
Retainer batching and rate limiting.

| Config paths | Env overrides |
|------------------------------------|------------------------------------------|
|  <code>retainer.flow_control</code> | <code>EMQX_RETAINER__FLOW_CONTROL</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>batch_read_number</h4>
Size of the batch when reading messages from storage. 0 means no limit.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>0</code></td></tr></tbody>
</table>
</li>
<li>
<h4>batch_deliver_number</h4>
The number of retained messages can be delivered per batch.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>0..1000</code></td></tr><tr><td><strong>Default</strong></td><td><code>0</code></td></tr></tbody>
</table>
</li>
<li>
<h4>batch_deliver_limiter</h4>
The rate limiter name for retained messages' delivery.
Limiter helps to avoid delivering too many messages to the client at once, which may cause the client to block or crash, or drop messages due to exceeding the size of the message queue.
The names of the available rate limiters are taken from the existing rate limiters under `limiter.batch`.
If this field is empty, limiter is not used.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="limiter-internal">limiter:internal</a></code></td></tr></tbody>
</table>
</li>

</ul>

## retainer:mnesia_config <a id='retainer-mnesia_config'></a>
Configuration of the internal database storing retained messages.

| Config paths | Env overrides |
|-------------------------------|-------------------------------------|
|  <code>retainer.backend</code> | <code>EMQX_RETAINER__BACKEND</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>type</h4>
Backend type.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>built_in_database</code></td></tr><tr><td><strong>Default</strong></td><td><code>built_in_database</code></td></tr></tbody>
</table>
</li>
<li>
<h4>storage_type</h4>
Specifies whether the messages are stored in RAM or persisted on disc.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>ram | disc</code></td></tr><tr><td><strong>Default</strong></td><td><code>ram</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_retained_messages</h4>
Maximum number of retained messages. 0 means no limit.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>non_neg_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>0</code></td></tr></tbody>
</table>
</li>
<li>
<h4>index_specs</h4>
Retainer index specifications: list of arrays of positive ascending integers. Each array specifies an index. Numbers in an index specification are 1-based word positions in topics. Words from specified positions will be used for indexing.<br/>For example, it is good to have <code>[2, 4]</code> index to optimize <code>+/X/+/Y/...</code> topic wildcard subscriptions.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[[integer()]]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[
  [1, 2, 3],
  [1, 3],
  [2, 3],
  [3]
]
</code></td></tr></tbody>
</table>
</li>

</ul>

## retainer <a id='retainer'></a>
Configuration related to handling `PUBLISH` packets with a `retain` flag set to 1.

| Config paths | Env overrides |
|-----------------------|----------------------------|
|  <code>retainer</code> | <code>EMQX_RETAINER</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable retainer feature

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>msg_expiry_interval</h4>
Message retention time. 0 means message will never be expired.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"0s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>msg_clear_interval</h4>
Periodic interval for cleaning up expired messages.
Never clear if the value is 0.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"0s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>flow_control</h4>
Flow control.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="retainer-flow_control">retainer:flow_control</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>max_payload_size</h4>
Maximum retained message size.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:bytesize()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"1MB"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>stop_publish_clear_msg</h4>
When the retained flag of the `PUBLISH` message is set and Payload is empty,
whether to continue to publish the message.
See:
http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html#_Toc398718038

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>backend</h4>
Settings for the database storing the retained messages.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="retainer-mnesia_config">retainer:mnesia_config</a></code></td></tr></tbody>
</table>
</li>

</ul>

## slow_subs <a id='slow_subs'></a>
Configuration for `slow_subs` feature.

| Config paths | Env overrides |
|------------------------|-----------------------------|
|  <code>slow_subs</code> | <code>EMQX_SLOW_SUBS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable this feature

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>threshold</h4>
The latency threshold for statistics

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"500ms"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>expire_interval</h4>
The eviction time of the record, which in the statistics record table

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"300s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>top_k_num</h4>
The maximum number of records in the slow subscription statistics record table

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>pos_integer()</code></td></tr><tr><td><strong>Default</strong></td><td><code>10</code></td></tr></tbody>
</table>
</li>
<li>
<h4>stats_type</h4>
The method to calculate the latency

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>whole | internal | response</code></td></tr><tr><td><strong>Default</strong></td><td><code>whole</code></td></tr></tbody>
</table>
</li>

</ul>

## statsd <a id='statsd'></a>
StatsD metrics collection and push configuration.

| Config paths | Env overrides |
|---------------------|--------------------------|
|  <code>statsd</code> | <code>EMQX_STATSD</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>enable</h4>
Enable or disable StatsD metrics collection and push service.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>false</code></td></tr></tbody>
</table>
</li>
<li>
<h4>server</h4>
StatsD server address.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>string()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"127.0.0.1:8125"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>sample_time_interval</h4>
The sampling interval for metrics.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>flush_time_interval</h4>
The push interval for metrics.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"30s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>tags</h4>
The tags for metrics.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>

</ul>
