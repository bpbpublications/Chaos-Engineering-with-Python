import pyVmomi  # VMware Python library 
from pyVmomi import vim, vmodl

# Connect to VMware vCenter Server 
def connect_to_vmware():
    try:
        # Establish a connection to your vCenter Server
        service_instance = pyVmomi.connect.SmartConnect(
            host="vcenter_server_ip", # Replace with real vCenter IP
            user="username", # Replace with real username
            pwd="password", # Replace with real password
            port = 443
        )
        return service_instance
    except Exception as e:
        print(f"Failed to connect to VMware: {str(e)}")
        return None

# Introduce CPU contention across all VMs
def introduce_cpu_contention():
    vmware_service = connect_to_vmware()
    if vmware_service:
        try:
            # Get a list of all VMs
            vm_list = vmware_service.content.viewManager.CreateContainerView(
                vmware_service.content.rootFolder,
                [pyVmomi.vim.VirtualMachine],
                True
            ).view

            # Introduce CPU contention on each VM
            for vm in vm_list:
                try:
                    print(f"Introducing CPU contention on VM: {vm.name}")
                    # Define CPU performance specification
                    spec = vim.vm.ConfigSpec()
                    spec.cpuAllocation = vim.ResourceAllocationInfo()
                    spec.cpuAllocation.reservation = 0
                    spec.cpuAllocation.expandableReservation = True
                    spec.cpuAllocation.limit = -1  # No limit
                    spec.cpuAllocation.shares = vim.Shares(level="high")

                    # Apply the CPU specification to the VM
                    vm.ReconfigVM_Task(spec=spec)

                    print(f"CPU contention introduced on VM: {vm.name}")
                except vmodl.MethodFault as e:
                    print(f"Error introducing CPU contention on VM: {vm.name}, Error: {e.msg}")

        except Exception as e:
            print(f"Failed to introduce CPU contention: {str(e)}")

# Remove CPU contention across all VMs
def remove_cpu_contention():
    vmware_service = connect_to_vmware()
    if vmware_service:
        try:
            # Get a list of all VMs
            vm_list = vmware_service.content.viewManager.CreateContainerView(
                vmware_service.content.rootFolder,
                [pyVmomi.vim.VirtualMachine],
                True
            ).view

            # Stop CPU contention on each VM
            for vm in vm_list:
                try:
                    print(f"Removing CPU contention on VM: {vm.name}")

                    # Reset CPU configuration to default values
                    spec = vim.vm.ConfigSpec()
                    spec.cpuAllocation = vim.ResourceAllocationInfo()

                    # Apply the new configuration to the VM
                    vm.ReconfigVM_Task(spec=spec)

                    print(f"CPU contention removed from VM: {vm.name}")
                except vmodl.MethodFault as e:
                    print(f"Error removing CPU contention from VM: {vm.name}, Error: {e.msg}")
                
        except Exception as e:
            print(f"Failed to remove CPU contention: {str(e)}")

# Function to get baseline CPU usage 
def get_cpu_usage_baseline(baseline):
    vmware_service = connect_to_vmware()
    if vmware_service:
        try:
            # Initialize variables
            total_cpu_usage_percentage = 0
            vm_count = 0

            # Get a list of all VMs
            vm_list = vmware_service.content.viewManager.CreateContainerView(
                vmware_service.content.rootFolder,
                [pyVmomi.vim.VirtualMachine],
                True
            ).view

            # Loop through each VM
            for vm in vm_list:
                summary = vm.summary
                if summary:
                    cpu_usage = summary.quickStats.overallCpuUsage
                    cpu_capacity = vm.config.hardware.cpuInfo.numCpuCores * vm.config.hardware.cpuInfo.numCpuThreads
                    cpu_usage_percentage = cpu_usage / cpu_capacity * 100
                    total_cpu_usage_percentage += cpu_usage_percentage
                    vm_count += 1
                else:
                    print(f"Unable to retrieve CPU usage information for VM '{vm_name}'")

            if vm_count == 0:
                raise Exception("No valid VMs found")

            # Calculate the average CPU usage
            average_cpu_usage_percentage = total_cpu_usage_percentage / vm_count
            
            # Calculate the deviation from the baseline
            deviation_percentage = abs((average_cpu_usage_percentage - baseline) / baseline) * 100
            
            return deviation_percentage

        except Exception as e:
            print(f"Failed to get CPU usage baseline: {str(e)}")    

