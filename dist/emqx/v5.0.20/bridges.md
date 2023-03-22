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

</ul>
