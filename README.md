# ssh_config

```
ssh_config.py --help
Usage: ssh_config.py [OPTIONS] [IPS]...

  Generate SSH config for a list of IPs.

  `Host` format `{prefix}.{idx}.{hostname}`.

Options:
  --hostname TEXT  Hostname.  [required]
  --prefix TEXT    Hostname prefix.  [required]
  --user TEXT      User.  [required]
  --port INTEGER   Port.
  --key TEXT       Key.
  --help           Show this message and exit.
```

## Requirements

```sh
pip install click
```
