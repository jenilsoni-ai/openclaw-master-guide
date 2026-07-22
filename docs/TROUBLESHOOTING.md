# Troubleshooting

Start with the standard command ladder. Capture the first failing layer before changing configuration.

```bash
openclaw status
openclaw gateway status
openclaw logs --follow
openclaw doctor
openclaw channels status --probe
```

## Fast triage table

| Symptom | First check | Likely layer |
| --- | --- | --- |
| Dashboard does not open | `openclaw gateway status --deep` | service, bind, or stale process |
| Channel receives nothing | `openclaw channels status --probe` | auth, pairing, or channel policy |
| Model calls fail | `openclaw status --all` | provider credential or route |
| Tool is denied | Gateway logs | tool policy, sandbox, or approval |
| Behavior ignores workspace changes | new session, then doctor | bootstrap injection or wrong workspace |
| Problems begin after update | version and update status | stale binary or protocol mismatch |
| Skill is missing | logs and skill roots | discovery, gating, or symlink containment |

## After an update

```bash
openclaw status --all
openclaw update status --json
openclaw gateway status --deep
openclaw doctor --fix
openclaw gateway restart
```

Then verify which binary is active:

```bash
which openclaw
openclaw --version
openclaw config get meta.lastTouchedVersion
```

## Tool-policy failures

An execution failure can come from three independent layers:

1. Tool allow/deny policy.
2. Sandbox availability and scope.
3. Host or node approval policy.

Read the corresponding Gateway log entry before relaxing any boundary. Grant the narrowest capability that fixes the intended workflow.

## Safe diagnostic sharing

Prefer:

```bash
openclaw status --all
```

It is designed to produce a pasteable, redacted snapshot. Review output before sharing it. Avoid posting raw auth files, full logs, session databases, or the entire state directory.

## Official references

- [Gateway troubleshooting](https://docs.openclaw.ai/gateway/troubleshooting)
- [FAQ](https://docs.openclaw.ai/help/faq)
- [CLI reference](https://docs.openclaw.ai/cli)
