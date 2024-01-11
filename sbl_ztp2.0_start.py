import sys
from modules.dhcpd_config import write_dhcp_config, restart_dhcp_service
from modules.generate_config import generate_config_dhcp_mes24, generate_config_dhcp_qsw46
from variables.sensitive import nb
from variables.region_ztp_net import *
from variables.dev_env import *


while True:
    region = input('Please, input region (1, 2, 3, or 4) where start configure devices:\n1. MSK\n2. EKB\n3. SPB\n4. NSK\n')
    if region in ['1', '2', '3', '4']:
        break
    else:
        print('Invalid input. Please input 1, 2, 3, or 4.')

name_device = input('Please, input device NAME: ').upper()


# Render config
try:
    response = nb.dcim.devices.get(name=name_device).render_config.create()
    content_text = response.get('content', '')
    devices = nb.dcim.devices.filter(name=name_device, status='planned', has_primary_ip=True)
    if not devices:
        print("Empty result for this filter. Check it and try again. Maybe device status not __planned__ state in NB?")
        sys.exit()
    for device in devices:
        device_type = device.device_type.slug

        if device_type == 'qsw-4610-10t-poe-ac': # Device type
            tftp_file_path = '/srv/tftp/startup.cfg'
            with open(tftp_file_path, 'w', encoding='utf-8') as file:
                file.write(content_text)
            print(f'\nRender config saved to {tftp_file_path}\n')

            if region == '1': # MSK
                config_dhcp = generate_config_dhcp_qsw46(qsw46_dhcpd_template, msk_subnet, msk_netmask, msk_range, msk_gw, qsw46_bootfile_cfg)
                write_dhcp_config(config_dhcp)
                restart_dhcp_service()

            if region == '2': # EKB
                config_dhcp = generate_config_dhcp_qsw46(qsw46_dhcpd_template, ekb_subnet, ekb_netmask, ekb_range, ekb_gw, qsw46_bootfile_cfg)
                write_dhcp_config(config_dhcp)
                restart_dhcp_service()

            if region == '3': # SPB
                config_dhcp = generate_config_dhcp_qsw46(qsw46_dhcpd_template, spb_subnet, spb_netmask, spb_range, spb_gw, qsw46_bootfile_cfg)
                write_dhcp_config(config_dhcp)
                restart_dhcp_service()

            if region == '4': # NSK
                config_dhcp = generate_config_dhcp_qsw46(qsw46_dhcpd_template, nsk_subnet, nsk_netmask, nsk_range, nsk_gw, qsw46_bootfile_cfg)
                write_dhcp_config(config_dhcp)
                restart_dhcp_service()


        elif device_type == 'mes2408p' or 'mes2448p': # Another device type
            tftp_file_path = '/srv/tftp/startup.conf'
            with open(tftp_file_path, 'w', encoding='utf-8') as file:
                file.write(content_text)
            print(f'\nRender config saved to {tftp_file_path}\n')

            if region == '1': # MSK
                config_dhcp = generate_config_dhcp_mes24(mes24_dhcpd_template, msk_subnet, msk_netmask, msk_range, msk_gw, mes24_image_name, mes24_boot_name, mes24_startup_name)

            if region == '2': # EKB
                config_dhcp = generate_config_dhcp_mes24(mes24_dhcpd_template, ekb_subnet, ekb_netmask, ekb_range, ekb_gw, mes24_image_name, mes24_boot_name, mes24_startup_name)
                write_dhcp_config(config_dhcp)
                restart_dhcp_service()

            if region == '3': # SPB
                config_dhcp = generate_config_dhcp_mes24(mes24_dhcpd_template, spb_subnet, spb_netmask, spb_range, spb_gw, mes24_image_name, mes24_boot_name, mes24_startup_name)
                write_dhcp_config(config_dhcp)
                restart_dhcp_service()

            if region == '3': # NSK
                config_dhcp = generate_config_dhcp_mes24(mes24_dhcpd_template, nsk_subnet, nsk_netmask, nsk_range, nsk_gw, mes24_image_name, mes24_boot_name, mes24_startup_name)
                write_dhcp_config(config_dhcp)
                restart_dhcp_service()
        
        else:
            print('ERROR. The device model has not been prepared yet')

except Exception as e:
    print(f'\nFailed to retrieve render config. Exception: {e}\n')
