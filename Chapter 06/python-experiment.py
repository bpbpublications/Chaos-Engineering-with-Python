from kubernetes import client, config
import time

# Load configuration based on the environment
def load_k8s_config():
    try:
        config.load_kube_config()
        print("Loaded kubeconfig from default location.")
    except:
        config.load_incluster_config()
        print("Loaded in-cluster configuration.")

# Delete a pod in the specified namespace
def delete_pod(namespace, pod_name):
    try:
        v1.delete_namespaced_pod(name=pod_name, namespace=namespace)
        print(f"Pod {pod_name} deleted.")
    except client.exceptions.ApiException as e:
        print(f"Exception when deleting pod {pod_name}: {e}")

# Check the status of pods matching the label selector in the specified namespace
def check_pod_status(namespace, label_selector):
    pods = v1.list_namespaced_pod(namespace, label_selector=label_selector)
    for pod in pods.items:
        print(f"Pod: {pod.metadata.name}, Status: {pod.status.phase}")

# Run the chaos experiment
def main():
    load_k8s_config()
    global v1
    v1 = client.CoreV1Api()
    
    namespace = "default"  
    label_selector = "app=frontend"  

    # Check initial status of pods
    print("Initial pod status:")
    check_pod_status(namespace, label_selector)

    # Introduce chaos by deleting a pod
    pods = v1.list_namespaced_pod(namespace, label_selector=label_selector).items
    if pods:
        pod_name = pods[0].metadata.name
        delete_pod(namespace, pod_name)

    # Wait for some time to observe the impact
    time.sleep(30)

    # Check the status of pods after chaos
    print("Pod status after chaos:")
    check_pod_status(namespace, label_selector)

if __name__ == "__main__":
    main()
