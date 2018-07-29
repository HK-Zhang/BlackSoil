```ps
az aks create --resource-group aks-poc --name akspoc --kubernetes-version 1.10.5 --max-pods 1000 --enable-addons http_application_routing --ssh-key-value "C:\Users\yxzhk\Workspace\U\ssh\id_azure.pub"
```

### reconfig Kubernetes context

```ps
kubectl create -f account.yaml
```

```ps
kubectl get serviceaccount dashboard -o jsonpath="{.secrets[0].name}"
```

```ps
kubectl get secret dashboard-token-72xjq -o jsonpath="{.data.token}" | base64 --decode
```

http://localhost:8001/api/v1/namespaces/kube-system/services/kubernetes-dashboard/proxy/#!/login

Choose for token and enter the token you gathered with the last step.