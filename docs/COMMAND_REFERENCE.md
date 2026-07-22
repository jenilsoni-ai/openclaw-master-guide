# Verified command reference

These commands are drawn from the official documentation. Check `openclaw <command> --help` on your installed version before scripting behavior around flags.

## Setup

```bash
openclaw onboard --install-daemon
openclaw configure
openclaw setup
```

## Gateway and UI

```bash
openclaw gateway status
openclaw gateway status --deep
openclaw gateway restart
openclaw dashboard
openclaw health
```

## Diagnostics

```bash
openclaw status
openclaw status --all
openclaw logs --follow
openclaw doctor
openclaw doctor --deep
openclaw doctor --fix
```

## Channels

```bash
openclaw channels add
openclaw channels login
openclaw channels status --probe
```

## Security

```bash
openclaw security audit
openclaw security audit --deep
openclaw approvals get
```

## Updates

```bash
openclaw update status --json
openclaw update --dry-run
openclaw update
```

## Configuration inspection

```bash
openclaw config get meta.lastTouchedVersion
```

## Important distinction

Commands in the industry use-case pages are design sketches unless explicitly labeled **Verified command** and linked to the official CLI reference. Names such as `inventory-manager` or `route-optimizer` describe capabilities you would need to install or implement; they are not promised built-ins.

## Official references

- [CLI index](https://docs.openclaw.ai/cli)
- [Getting started](https://docs.openclaw.ai/start/getting-started)
- [Troubleshooting command ladder](https://docs.openclaw.ai/gateway/troubleshooting)
