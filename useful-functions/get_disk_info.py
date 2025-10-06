import shutil

def get_disk_info():
    '''
    Method to get disk information
    '''
    # Capture the disk usage in three different variable (Note these are in bytes)
    total_b, used_b, available_b = shutil.disk_usage('.')
    gb = 10 ** 9
    # Convert bytes to gigabytes
    total_gb = '{:6.2f} GB'.format(total_b / gb)
    used_gb = '{:6.2f} GB'.format(used_b / gb)
    available_gb = '{:6.2f} GB'.format(available_b / gb)
    # Create a dictionary with the information
    disk_info={'Total': total_gb,
           'Used': used_gb,
           'Available': available_gb}
    return disk_info