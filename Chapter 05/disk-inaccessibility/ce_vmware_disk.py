from pyVmomi import vimtypes
from pyVmomi import VirtLib
from pyVmomi import VmwareUtil
from pyVim.connect import SmartConnectNoSSL

def detach_disk(vm_name_or_dc_path, username, password):
    """
    Detaches a disk from the specified VM.

    Args:
        vm_name_or_dc_path (str): The hostname or datacenter path of the target VM.
        username (str): Username for vCenter API access.
        password (str): Password for vCenter API access.
    """
    service_instance = SmartConnectNoSSL(host="vcenter_server",
                                        user=username,
                                        pwd=password)
    content = service_instance.RetrieveContent()

    # Locate the VM by name or datacenter path
    container = content.rootFolder
    obj_view = content.viewManager.CreateContainerView(container, [vimtypes.vim.VirtualMachine], True)
    vm = [vm for vm in obj_view.view if vm.name == vm_name_or_dc_path or vm.summary.config.vmPathName == vm_name_or_dc_path]

    if not vm:
        print(f"VM '{vm_name_or_dc_path}' not found.")
        return

    vm = vm[0]

    # Get all disks attached to the VM
    hardware = vm.config.hardware
    disks = hardware.device

    # Detach the first disk 
    # **CAUTION** Detaching disks can cause data loss!
    try:
        print(f"Detaching disk: {disks[0].deviceInfo.label}")
        vm.HotRemoveDisk(key=disks[0].key)
        print("Disk detached successfully.")
    except vimtypes.vim.Fault as e:
        print(f"Failed to detach disk: {e}")

    # Reattach the disk after a delay to simulate chaos
    reconnect_delay = 5
    task = vm.HotAddDisk(reconnect=True, controllerKey=disks[0].controllerKey, deviceInfo=disks[0].deviceInfo, diskSpec=disks[0].disk)
    VmwareUtil.waitForTask(task)
    print(f"Disk reattached after {reconnect_delay} seconds.")

    service_instance.Disconnect()

    # Replace with real values
    vm_name_or_dc_path = "vm_name_or_dc_path"
    username = "username"
    password = "password"

    detach_disk(vm_name_or_dc_path, username, password)

