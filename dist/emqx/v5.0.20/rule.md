# Rule Engine

## rule_engine:builtin_action_console <a id='rule_engine-builtin_action_console'></a>
Configuration for a built-in action.

| Config paths | Env overrides |
|---------------------------------------------------|------------------------------------------------------------|
|  <code>rule_engine.rules.$id.actions.$INDEX</code> | <code>EMQX_RULE_ENGINE__RULES__$ID__ACTIONS__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>function</h4>
Print the actions to the console

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>console</code></td></tr></tbody>
</table>
</li>

</ul>

## rule_engine:builtin_action_republish <a id='rule_engine-builtin_action_republish'></a>
Configuration for a built-in action.

| Config paths | Env overrides |
|---------------------------------------------------|------------------------------------------------------------|
|  <code>rule_engine.rules.$id.actions.$INDEX</code> | <code>EMQX_RULE_ENGINE__RULES__$ID__ACTIONS__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>function</h4>
Republish the message as a new MQTT message

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>republish</code></td></tr></tbody>
</table>
</li>
<li>
<h4>args</h4>


<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code><a href="rule_engine-republish_args">rule_engine:republish_args</a></code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>

</ul>

## rule_engine:republish_args <a id='rule_engine-republish_args'></a>
The arguments of the built-in 'republish' action.One can use variables in the args.
The variables are selected by the rule. For example, if the rule SQL is defined as following:
<code>
    SELECT clientid, qos, payload FROM "t/1"
</code>
Then there are 3 variables available: <code>clientid</code>, <code>qos</code> and
<code>payload</code>. And if we've set the args to:
<code>
    {
        topic = "t/${clientid}"
        qos = "${qos}"
        payload = "msg: ${payload}"
    }
</code>
When the rule is triggered by an MQTT message with payload = `hello`, qos = 1,
clientid = `Steve`, the rule will republish a new MQTT message to topic `t/Steve`,
payload = `msg: hello`, and `qos = 1`.

| Config paths | Env overrides |
|--------------------------------------------------------|------------------------------------------------------------------|
|  <code>rule_engine.rules.$id.actions.$INDEX.args</code> | <code>EMQX_RULE_ENGINE__RULES__$ID__ACTIONS__$INDEX__ARGS</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>topic</h4>
The target topic of message to be re-published.
Template with variables is allowed, see description of the 'republish_args'.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>qos</h4>
The qos of the message to be re-published.
Template with variables is allowed, see description of the 'republish_args'.
Defaults to ${qos}. If variable ${qos} is not found from the selected result of the rule,
0 is used.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>qos() | binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"${qos}"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>retain</h4>
The 'retain' flag of the message to be re-published.
Template with variables is allowed, see description of the 'republish_args'.
Defaults to ${retain}. If variable ${retain} is not found from the selected result
of the rule, false is used.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean() | binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"${retain}"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>payload</h4>
The payload of the message to be re-published.
Template with variables is allowed, see description of the 'republish_args'.
Defaults to ${payload}. If variable ${payload} is not found from the selected result
of the rule, then the string "undefined" is used.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"${payload}"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>user_properties</h4>
From which variable should the MQTT message's User-Property pairs be taken from.
The value must be a map.
You may configure it to <code>${pub_props.'User-Property'}</code> or
use <code>SELECT *,pub_props.'User-Property' as user_properties</code>
to forward the original user properties to the republished message.
You may also call <code>map_put</code> function like
<code>map_put('my-prop-name', 'my-prop-value', user_properties) as user_properties</code>
to inject user properties.
NOTE: MQTT spec allows duplicated user property names, but EMQX Rule-Engine does not.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"${user_properties}"</code></td></tr></tbody>
</table>
</li>

</ul>

## rule_engine <a id='rule_engine'></a>
Configuration for the EMQX Rule Engine.

| Config paths | Env overrides |
|--------------------------|-------------------------------|
|  <code>rule_engine</code> | <code>EMQX_RULE_ENGINE</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>ignore_sys_message</h4>
When set to 'true' (default), rule-engine will ignore messages published to $SYS topics.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>rules</h4>
The rules

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>{$id -> <a href="rule_engine-rules">rule_engine:rules</a>}</code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>
<li>
<h4>jq_function_default_timeout</h4>
Default timeout for the `jq` rule engine function

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>emqx_schema:duration_ms()</code></td></tr><tr><td><strong>Default</strong></td><td><code>"10s"</code></td></tr></tbody>
</table>
</li>
<li>
<h4>jq_implementation_module</h4>
The implementation module for the jq rule engine function. The two options are jq_nif and jq_port. With the jq_nif option an Erlang NIF library is used while with the jq_port option an implementation based on Erlang port programs is used. The jq_nif option (the default option) is the fastest implementation of the two but jq_port is safer as the jq programs will not execute in the same process as the Erlang VM.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>jq_nif | jq_port</code></td></tr><tr><td><strong>Default</strong></td><td><code>jq_nif</code></td></tr></tbody>
</table>
</li>

</ul>

## rule_engine:rules <a id='rule_engine-rules'></a>
Configuration for a rule.

| Config paths | Env overrides |
|------------------------------------|-------------------------------------------|
|  <code>rule_engine.rules.$id</code> | <code>EMQX_RULE_ENGINE__RULES__$ID</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>name</h4>
The name of the rule

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>
<li>
<h4>sql</h4>
SQL query to transform the messages.
Example: <code>SELECT * FROM "test/topic" WHERE payload.x = 1</code>

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>actions</h4>
A list of actions of the rule.
An action can be a string that refers to the channel ID of an EMQX bridge, or an object
that refers to a function.
There a some built-in functions like "republish" and "console", and we also support user
provided functions in the format: "{module}:{function}".
The actions in the list are executed sequentially.
This means that if one of the action is executing slowly, all the following actions will not
be executed until it returns.
If one of the action crashed, all other actions come after it will still be executed, in the
original order.
If there's any error when running an action, there will be an error message, and the 'failure'
counter of the function action or the bridge channel will increase.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>[binary() | <a href="rule_engine-builtin_action_republish">rule_engine:builtin_action_republish</a> | <a href="rule_engine-builtin_action_console">rule_engine:builtin_action_console</a> | <a href="rule_engine-user_provided_function">rule_engine:user_provided_function</a>]</code></td></tr><tr><td><strong>Default</strong></td><td><code>[]</code></td></tr></tbody>
</table>
</li>
<li>
<h4>enable</h4>
Enable or disable the rule

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>boolean()</code></td></tr><tr><td><strong>Default</strong></td><td><code>true</code></td></tr></tbody>
</table>
</li>
<li>
<h4>description</h4>
The description of the rule

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr><tr><td><strong>Default</strong></td><td><code>""</code></td></tr></tbody>
</table>
</li>
<li>
<h4>metadata</h4>
Rule metadata, do not change manually

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr></tbody>
</table>
</li>

</ul>

## rule_engine:user_provided_function <a id='rule_engine-user_provided_function'></a>
Configuration for a built-in action.

| Config paths | Env overrides |
|---------------------------------------------------|------------------------------------------------------------|
|  <code>rule_engine.rules.$id.actions.$INDEX</code> | <code>EMQX_RULE_ENGINE__RULES__$ID__ACTIONS__$INDEX</code>  |


**Fields**

<ul class="field-list">
<li>
<h4>function</h4>
The user provided function. Should be in the format: '{module}:{function}'.
Where {module} is the Erlang callback module and {function} is the Erlang function.

To write your own function, checkout the function <code>console</code> and
<code>republish</code> in the source file:
<code>apps/emqx_rule_engine/src/emqx_rule_actions.erl</code> as an example.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>binary()</code></td></tr></tbody>
</table>
</li>
<li>
<h4>args</h4>
The args will be passed as the 3rd argument to module:function/3,
checkout the function <code>console</code> and <code>republish</code> in the source file:
<code>apps/emqx_rule_engine/src/emqx_rule_actions.erl</code> as an example.

<table>
<tbody>
<tr><td><strong>Type</strong></td><td><code>map()</code></td></tr><tr><td><strong>Default</strong></td><td><code>{}</code></td></tr></tbody>
</table>
</li>

</ul>
