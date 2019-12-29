# Install Minikube
https://kubernetes.io/docs/tasks/tools/install-minikube/

# Start Minikube with some resources
minikube start --cpus 8 --memory 8192

# Git clone Airflow repo
git clone https://github.com/apache/airflow.git
git checkout 188b3193c7a5484253a13ad293e124569e8a2c04

# Start docker-for-desktop docker service

# Build docker image
bash airflow/scripts/ci/kubernetes/docker/build.sh   
- build airflow:latest image

# For mac ()
brew install gnu-sed

# Deploy image to minikube
bash ./kube/deploy.sh -d persistent_mode



=====

- Source Repo: https://github.com/helm/charts/tree/master/stable/airflow

- Start tiller service
```
tiller
```

- Clone chart and install chart
```
git clone https://github.com/helm/charts.git
cd chart/stable/airflow
helm dependency update
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
export HELM_HOST=localhost:441324
helm install --name "airflow" . -f values.yaml
```

- Wait for web server to be ready
```
helm status "airflow"
```

- Port forward
```
kubectl port-forward airflow-web-7c586c59bf-b8rsr  8080:8080
```

- Delete Helm
```
export HELM_HOST=localhost:44134
helm delete  --purge "airflow"
```

- How to reload/update DAG
  - Make change to git repository
```
helm upgrade airflow stable/airflow --set tag=v0.0.2
```