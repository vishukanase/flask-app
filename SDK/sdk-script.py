from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.containerservice import ContainerServiceClient
from azure.mgmt.containerservice.models import (
    ManagedCluster,
    ManagedClusterAgentPoolProfile,
    ManagedClusterServicePrincipalProfile,
    ContainerServiceNetworkProfile
)

# Replace these variables with your values
SUBSCRIPTION_ID = 'your-subscription-id'
RESOURCE_GROUP_NAME = 'your-resource-group'
AKS_CLUSTER_NAME = 'your-aks-cluster'
LOCATION = 'eastus'
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'

# Authenticate with Azure
credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, SUBSCRIPTION_ID)
containerservice_client = ContainerServiceClient(credential, SUBSCRIPTION_ID)

# Create a resource group
resource_group_params = {'location': LOCATION}
resource_client.resource_groups.create_or_update(
    RESOURCE_GROUP_NAME,
    resource_group_params
)

# Create the AKS cluster
aks_cluster = ManagedCluster(
    location=LOCATION,
    dns_prefix=AKS_CLUSTER_NAME,
    agent_pool_profiles=[
        ManagedClusterAgentPoolProfile(
            name='agentpool',
            count=3,
            vm_size='Standard_DS2_v2',
            os_type='Linux'
        )
    ],
    service_principal_profile=ManagedClusterServicePrincipalProfile(
        client_id=CLIENT_ID,
        secret=CLIENT_SECRET
    ),
    network_profile=ContainerServiceNetworkProfile(
        network_plugin='azure'
    )
)

# Begin creation of the AKS cluster
containerservice_client.managed_clusters.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    AKS_CLUSTER_NAME,
    aks_cluster
).result()

print(f"AKS cluster '{AKS_CLUSTER_NAME}' created successfully!")
