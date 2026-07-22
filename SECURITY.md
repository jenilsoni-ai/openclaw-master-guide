# Security policy

This repository contains independent documentation and design blueprints. It does not ship the OpenClaw runtime.

## Reporting an issue in this guide

Open a private security advisory in this repository when a documented command, configuration, or workflow could expose credentials, weaken access controls, or cause unsafe execution. Include the affected file, expected safe behavior, and a minimal reproduction. Do not include live credentials or private logs.

For ordinary documentation corrections, open an issue or pull request.

## Reporting an upstream vulnerability

Runtime vulnerabilities belong to the upstream project. Follow the reporting instructions in the [official security documentation](https://docs.openclaw.ai/gateway/security) and avoid publishing exploit details before maintainers can respond.

## Scope

In scope here:

- unsafe instructions in this repository;
- leaked secrets or temporary signed URLs;
- examples that unintentionally disable a security boundary;
- misleading claims that could lead to unsafe deployment.

Out of scope here:

- vulnerabilities in the OpenClaw runtime;
- third-party services, skills, or plugins;
- social engineering unrelated to this repository's content.
