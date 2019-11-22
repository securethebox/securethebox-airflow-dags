# Docker for Desktop (mac)
- Source Repo: https://github.com/helm/charts/tree/master/stable/airflow

- Start tiller service
```
tiller
```

- Clone chart and install chart
```
git clone https://github.com/helm/charts.git
cd chart/stable/airflow
```

- Configure values.yaml
  - Set the github repository to your github airflow dags repo
```
git:
    ## url to clone the git repository
    url: https://github.com/securethebox/securethebox-airflow-dags.git
```


- Deploy Helm Chart
```
export HELM_HOST=localhost:44134
helm install --name "airflow" stable/airflow -f values.yaml
```

- Wait for web server to be ready
```
helm status "airflow"
```

- Port forward
```
kubectl port-forward airflow-web-5f7bc47587-g8j9j 8080:8080
```

- Delete Helm
```
helm delete  --purge "airflow"
```

- Update DAG
```
helm upgrade airflow-prod charts/airflow --set tag=v0.0.2
```