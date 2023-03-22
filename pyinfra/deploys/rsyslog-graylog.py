from pyinfra.operations import files
from pyinfra.operations import server
import os

files.file(
    name="Create new rsyslog file",
    path="/etc/rsyslog.d/90-graylog.conf",
    touch=True,
    _sudo=True
)

graylog_host = os.environ['GRAYLOG_SERVER']
graylog_syslog = f"*.* @{graylog_host}:5140;RSYSLOG_SyslogProtocol23Format"
files.line(
    name="Add graylog syslog line",
    path="/etc/rsyslog.d/90-graylog.conf",
    line=graylog_syslog,
    present=True,
    _sudo=True,
)

server.service(
    name="Restart rsyslog service",
    service="rsyslog.service",
    restarted=True,
    _sudo=True,
    _use_sudo_password=True
) # type: ignore