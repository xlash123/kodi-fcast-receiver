from zeroconf import ServiceInfo, Zeroconf
import socket

from .util import log_and_notify

service_info: ServiceInfo = None
zeroconf = Zeroconf()

def advertise_fcast():
    global service_info, zeroconf
    # Get local ip
    ip_addr = socket.gethostbyname(socket.gethostname())

    # Create service info
    name = f"FCast-{socket.gethostname()}"
    desc = { "name": name }
    service_info = ServiceInfo(
        type_="_fcast._tcp.local.",
        name=f"{name}._fcast._tcp.local.",
        port=46899,
        server=f"{name}.local.",
        addresses=[socket.inet_aton(ip_addr)],
        weight=0,
        priority=0,
        properties=desc,
    )

    log_and_notify("Registering mdns: " + str(service_info), notify=False)

    zeroconf.register_service(service_info)

def unregister_fcast_discovery():
    global service_info, zeroconf
    zeroconf.register_service(service_info)
