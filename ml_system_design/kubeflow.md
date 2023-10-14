# Pre-requsite

1. minikube is local Kubernetes, focusing on making it easy to learn and develop for Kubernetes.
2. installation link: https://www.kubeflow.org/docs/components/pipelines/v2/installation/quickstart/
3. installation link : https://www.kubeflow.org/docs/components/pipelines/v1/installation/localcluster-deployment/
4. https://www.youtube.com/watch?v=KPEGKKNB63Q

You can use `kubectl` commands to get a list of all pods, deployments, and services in a Kubernetes cluster. Here's how you can do it:

1. **Get All Pods**:

   To list all the pods in your cluster, use the following command:

   ```shell
   kubectl get pods --all-namespaces
   ```

2. **Get All Deployments**:

   To list all the deployments in your cluster, use the following command:

   ```shell
   kubectl get deployments --all-namespaces
   ```

3. **Get All Services**:

   To list all the services in your cluster, use the following command:

   ```shell
   kubectl get services --all-namespaces
   ```

4. **Check pod status**
   ```shell
   kubectl logs -n kubeflow <pod-name>
   ```

5. **Delete all pods**
   ```shell
   kubectl delete pods --all --all-namespaces
   kubectl delete pods --all -n <namespace>
   ```


These commands will provide you with a list of pods, deployments, and services in your Kubernetes cluster, along with their respective namespaces and other metadata. You can use these commands to get a quick overview of the resources in your cluster.

