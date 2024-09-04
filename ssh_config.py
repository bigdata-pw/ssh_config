import click
from typing import List

@click.command()
@click.argument("ips", nargs=-1, type=str)
@click.option("--hostname", required=True, type=str, help="Hostname.")
@click.option("--prefix", required=True, type=str, help="Hostname prefix.")
@click.option("--user", required=True, type=str, help="User.")
@click.option("--port", default=22, type=int, help="Port.")
@click.option("--key", default="~/.ssh/id_ed25519", type=str, help="Key.")
def config(ips: List[str], hostname: str, prefix: str, user: str, port: int, key: str):
    """
    Generate SSH config for a list of IPs.

    `Host` format `{prefix}.{idx}.{hostname}`.
    """
    template = """
Host {prefix}.{idx}.{hostname}
  HostName {ip}
  User {user}
  Port {port}
  IdentityFile {key}
"""

    output = ""

    for idx, ip in enumerate(ips):
        output += template.format(
            prefix=prefix,
            idx=idx,
            hostname=hostname,
            ip=ip,
            user=user,
            port=port,
            key=key,
        )

    click.echo(output)


if __name__ == "__main__":
    config()
