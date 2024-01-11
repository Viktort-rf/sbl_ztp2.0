import subprocess

def write_dhcp_config(config_content):
    dhcp_conf_path = '/etc/dhcp/dhcpd.conf'
    with open(dhcp_conf_path, 'w') as dhcp_conf_file:
        dhcp_conf_file.write(config_content)
        print("Success change and save config isc-dhcp-server")


def restart_dhcp_service():
    try:
        subprocess.run(['systemctl', 'restart', 'isc-dhcp-server'], check=True)
        print("Success restart isc-dhcp-server")
    except subprocess.CalledProcessError as e:
        print('Failed to restart isc-dhcp-server:', e)
