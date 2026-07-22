# Security hardening

OpenClaw can read untrusted content and invoke powerful tools. Prompts are guidance; enforceable security comes from sender restrictions, tool policy, sandboxing, approvals, filesystem scope, and credential isolation.

## Threat model

Assume an attacker can place instructions inside:

- chat messages and quoted replies;
- web pages and search results;
- emails and documents;
- repository files and issue content;
- images, attachments, and pasted logs;
- tool output returned to the model.

Private access does not remove prompt-injection risk. Untrusted content remains untrusted even when the operator requested that it be read.

## Minimum secure baseline

### 1. Restrict senders

- Pair private users explicitly.
- Use channel and room allowlists.
- Require mentions in group rooms.
- Avoid exposing high-capability agents in public channels.

### 2. Minimize tools

- Deny tools an agent does not need.
- Separate research-only agents from agents allowed to act.
- Keep elevated execution disabled unless the workflow proves it is necessary.
- Do not treat general interpreters or shells as safe commands.

### 3. Use sandboxing

Sandbox untrusted or code-executing workloads. Restrict workspace access and network reach. Remember that a container with the host Docker socket can control the host through Docker.

### 4. Keep approvals meaningful

Require explicit approval for:

- shell execution outside a narrow allowlist;
- publishing or sending messages;
- purchases, transfers, or account changes;
- deletion or destructive modification;
- production deployment or infrastructure mutation;
- access-control and credential changes;
- medical, legal, hiring, safety, or enforcement decisions.

Approval prompts should show the exact action, destination, affected resource, and relevant diff or payload.

### 5. Isolate credentials

- Never place secrets in workspace Markdown.
- Do not expose auth-profile files to tools.
- Prefer scoped, revocable credentials.
- Use separate credentials for separate agents and environments.
- Keep logs and transcripts redacted and retain them only as long as needed.

## Audit commands

```bash
openclaw security audit
openclaw security audit --deep
openclaw doctor --deep
openclaw status --all
```

Use the regular audit for cold, read-only configuration checks. Deep mode adds live Gateway probes and applicable runtime collectors.

## Deployment checklist

- [ ] Gateway binds to loopback or a trusted private network.
- [ ] Remote access uses a secure overlay or authenticated reverse proxy.
- [ ] No raw Gateway port is exposed publicly.
- [ ] DM, group, and room policies are explicit.
- [ ] Each agent has the minimum required tools.
- [ ] Sandboxing is enabled for untrusted execution.
- [ ] Exec approvals are tested with both allowed and denied commands.
- [ ] Secrets are outside reachable workspaces.
- [ ] Logs redact tokens, internal URLs, and sensitive identifiers.
- [ ] Backups exclude live credentials unless encrypted and access-controlled.
- [ ] A human approval gate exists before irreversible external actions.
- [ ] `openclaw security audit --deep` has no unexplained critical finding.

## Incident response

If compromise is suspected:

1. Stop or isolate the Gateway.
2. Revoke provider, channel, plugin, and external-service credentials.
3. Preserve relevant redacted logs and task evidence.
4. Inspect recently installed or updated skills and plugins.
5. Review tool calls, approvals, session routes, and filesystem changes.
6. Restore from a known-good configuration and rotate credentials again.
7. Re-run the deep audit before reconnecting channels.

## Official references

- [Gateway security](https://docs.openclaw.ai/gateway/security)
- [Security audit checks](https://docs.openclaw.ai/gateway/security/audit-checks)
- [Sandboxing](https://docs.openclaw.ai/gateway/sandboxing)
- [Exec approvals](https://docs.openclaw.ai/tools/exec-approvals)
- [Advanced exec approvals](https://docs.openclaw.ai/tools/exec-approvals-advanced)
