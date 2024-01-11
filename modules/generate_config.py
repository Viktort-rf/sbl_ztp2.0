from jinja2 import Environment, FileSystemLoader


def generate_config_dhcp_qsw46(template_name, subnet, netmask, range, gw, bootfile ):
    template_env = Environment(loader=FileSystemLoader("templates"))
    template = template_env.get_template(template_name)

    config = template.render(subnet=subnet,
                             netmask=netmask,
                             range=range,
                             gw=gw,
                             bootfile=bootfile)
    return config

def generate_config_dhcp_mes24(template_name, subnet, netmask, range, gw, mes24_image_name, mes24_boot_name, mes24_startup_name):
    template_env = Environment(loader=FileSystemLoader("templates"))
    template = template_env.get_template(template_name)

    config = template.render(subnet=subnet,
                             netmask=netmask,
                             range=range,
                             gw=gw,
                             mes24_image_name=mes24_image_name,
                             mes24_boot_name=mes24_boot_name,
                             mes24_startup_name=mes24_startup_name)
    return config
