# Bridging ExtremeCloud™ IQ and StackStrom by OpenFaaS  

## ExtremeCloud™ IQ  

[ExtremeCloud™ IQ](https://extremecloudiq.com/)

## StackStorm

[![StackStorm](https://github.com/stackstorm/st2/raw/master/stackstorm_logo.png)](https://www.stackstorm.com)

**StackStorm** is a platform for integration and automation across services and tools, taking actions in response to events. Learn more at [www.stackstorm.com](http://www.stackstorm.com/product).

## OPENFAAS

![OpenFaaS Logo](https://blog.alexellis.io/content/images/2017/08/faas_side.png)

OpenFaaS&reg; makes it easy for developers to deploy event-driven functions and microservices to Kubernetes without repetitive, boiler-plate coding. Package your code or an existing binary in a Docker image to get a highly scalable endpoint with auto-scaling and metrics.

### Set up and run  

Set up OpenFaaS. Please check [https://github.com/openfaas/faas](https://github.com/openfaas/faas)  
After that.

```bash
git pull git@github.com:tknv/xiq-st2-openfaas.git
cd xiq-st2-openfaas
```

Then set keys in env.yml.

- auth_token is set in Access Token at ExtremeCloud™ IQ > Global Settings > API Data Management
- st2_webhook_host is StackStorm webhook URL
- api_key is created at StackStorm by;

```bash
st2 apikey create -k -m '{"used_by": "my integration"}'
<api_key>
```

`vim env.yml`

```yaml
environment:
  auth_token: YouCreateThisui3mvb_6_Y2GRvkkop4TH8Z8j-Eo
  st2_webhook_host: "https://xxx.xxx.xxx.xxx/api/v1/webhooks/xiq"
  api_key: CreatedAtStackStormkAMYuYzI5YmZmNjA1NmQ1ZTdlYzMyMWNlOTg4ZjMzZGViY2YwYWRjOTM0ZDkwN2IzNw
```

### Set end point  

Set below URL in Post URL at ExtremeCloud™ IQ > Global Settings > API Data Management

```bash
https://xxxxx.ngrok.io/function/xiq-st2-openfaas
```

or (preferable)

```bash
https://xxxxx.ngrok.io/async-function/xiq-st2-openfaas
```
