# Quickstart

This path gets a local Gateway running, opens the Control UI, and verifies the installation before you connect external channels.

## 1. Check the environment

The official installer supports macOS, Linux, Windows, and WSL2. If you manage Node yourself, use a currently supported release; the official guide recommends Node 24.

```bash
node --version
```

## 2. Install

### macOS, Linux, or WSL2

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

### Windows PowerShell

```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

If you prefer to manage Node and npm yourself:

```bash
npm install -g openclaw@latest
```

## 3. Run guided onboarding

```bash
openclaw onboard --install-daemon
```

The wizard configures a provider, credential, Gateway, workspace, and optional channels. You can revisit optional settings later:

```bash
openclaw configure
```

## 4. Verify before adding channels

```bash
openclaw gateway status
openclaw dashboard
```

The Gateway normally listens on loopback at `127.0.0.1:18789`. Do not expose this port directly to the public internet.

## 5. Run a baseline health check

```bash
openclaw status
openclaw doctor
openclaw security audit
```

Resolve blocking findings before enabling tools that can execute commands, browse authenticated sites, modify files, or send messages.

## 6. Connect one channel

Use onboarding or:

```bash
openclaw channels add
openclaw channels status --probe
```

Start with one private channel and an explicit sender allowlist. Verify routing and approval behavior before adding groups or public rooms.

## Completion checklist

- [ ] Gateway reports healthy.
- [ ] Control UI opens locally.
- [ ] `openclaw doctor` has no blocking findings.
- [ ] `openclaw security audit` has been reviewed.
- [ ] Only expected senders can reach the agent.
- [ ] Sensitive tools require approval or are denied.
- [ ] Workspace instructions contain no secrets.

## Official references

- [Getting started](https://docs.openclaw.ai/start/getting-started)
- [Installation](https://docs.openclaw.ai/install)
- [Onboarding](https://docs.openclaw.ai/start/wizard)
- [Channel setup](https://docs.openclaw.ai/channels)
