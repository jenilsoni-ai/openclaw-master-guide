# Workspace files

Workspace files turn a generic installation into a consistent agent. They are injected into new sessions as project context, so keep them precise, small, and free of secrets.

## Bootstrap file map

| File | Purpose | Put here | Keep out |
| --- | --- | --- | --- |
| `AGENTS.md` | Operating rules | workflow, authority, quality bar | personality prose |
| `SOUL.md` | Persona and boundaries | tone, values, behavioral limits | credentials, long procedures |
| `IDENTITY.md` | Identity | name, role, short description | user profile |
| `USER.md` | User context | address, timezone, preferences | unrelated sensitive data |
| `TOOLS.md` | Tool conventions | local notes, safe usage patterns | secrets and tokens |
| `HEARTBEAT.md` | Periodic checks | short batched checklist | precise scheduled jobs |
| `MEMORY.md` | Curated memory | durable facts and decisions | raw transcripts |
| `BOOTSTRAP.md` | First-run ritual | one-time setup steps | recurring policy |

Starter versions are available in [`templates/basic/`](../templates/basic/).

## A useful separation of concerns

- `SOUL.md` answers: **Who are you and how do you behave?**
- `AGENTS.md` answers: **How do you work and what may you do?**
- `USER.md` answers: **Who are you helping?**
- `TOOLS.md` answers: **How are local capabilities used safely?**
- `HEARTBEAT.md` answers: **What should be checked periodically?**
- `MEMORY.md` answers: **What must survive beyond this session?**

## Writing rules

1. State boundaries as observable behavior.
2. Separate permission to analyze from permission to act.
3. Require approval before external messages, purchases, publishing, deletion, credential changes, or infrastructure mutation.
4. Define what evidence counts as done.
5. Keep transient project status out of persona files.
6. Review memory periodically and delete stale or sensitive material.

## Heartbeat versus schedule

Use `HEARTBEAT.md` for a small batch of routine checks where exact timing is unimportant. Use cron for exact timing, isolated execution, or explicit delivery. See [Automation](AUTOMATION.md).

## Backup strategy

Back up workspace files separately from runtime state. Do not publish auth profiles, session databases, logs, or the entire `~/.openclaw` directory.

## Official references

- [Agent runtime and bootstrap files](https://docs.openclaw.ai/concepts/agent)
- [Agent workspace](https://docs.openclaw.ai/concepts/agent-workspace)
- [Automation](https://docs.openclaw.ai/automation)
