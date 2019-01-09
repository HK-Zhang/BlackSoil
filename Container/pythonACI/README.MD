## Build Image

```ps
$ACR_NAME = 'ContainerBank'
az acr build --registry $ACR_NAME --image pythonaci:v1 .
```
