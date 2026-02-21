<div align="center">

# Agent Governance

**The safety, trust, and reliability platform for production AI agents**

*One install for the complete governance stack — kernel · trust mesh · runtime supervisor · reliability engineering*

[![PyPI](https://img.shields.io/badge/pypi-agent--governance-blue.svg)](https://pypi.org/project/agent-governance/)
[![GitHub Stars](https://img.shields.io/github/stars/imran-siddique/agent-governance?style=social)](https://github.com/imran-siddique/agent-governance/stargazers)
[![Sponsor](https://img.shields.io/badge/sponsor-❤️-ff69b4)](https://github.com/sponsors/imran-siddique)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

```
pip install agent-governance[full]
```

[Architecture](#architecture) • [Quick Start](#quick-start) • [Components](#components) • [Why Unified?](#why-a-unified-governance-stack) • [Ecosystem](#the-agent-governance-ecosystem)

</div>

> ⭐ **If this project helps you, please star it!** It helps others discover the agent governance stack.

> 🔗 **Part of the Agent Governance Ecosystem** — Installs [Agent OS](https://github.com/imran-siddique/agent-os) · [AgentMesh](https://github.com/imran-siddique/agent-mesh) · [Agent Hypervisor](https://github.com/imran-siddique/agent-hypervisor) · [Agent SRE](https://github.com/imran-siddique/agent-sre)

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      agent-governance                           │
│                  pip install agent-governance[full]              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌───────────────────┐      ┌───────────────────────────┐     │
│   │   Agent OS Kernel │◄────►│   AgentMesh Platform      │     │
│   │                   │      │                           │     │
│   │  Policy Engine    │      │  Zero-Trust Identity      │     │
│   │  Capability Model │      │  Mutual TLS for Agents    │     │
│   │  Audit Logging    │      │  Encrypted Channels       │     │
│   │  Syscall Layer    │      │  Trust Scoring             │     │
│   └────────┬──────────┘      └─────────────┬─────────────┘     │
│            │                               │                   │
│            ▼                               ▼                   │
│   ┌───────────────────┐      ┌───────────────────────────┐     │
│   │ Agent Hypervisor  │      │   Agent SRE               │     │
│   │                   │      │                           │     │
│   │  Execution Rings  │      │  Health Monitoring        │     │
│   │  Resource Limits  │      │  SLO Enforcement          │     │
│   │  Runtime Sandboxing│     │  Incident Response        │     │
│   │  Kill Switch      │      │  Chaos Engineering        │     │
│   └───────────────────┘      └───────────────────────────┘     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Quick Start

```python
from agent_os import StatelessKernel, ExecutionContext
from agentmesh import TrustManager

# Boot the governance kernel
kernel = StatelessKernel()
ctx = ExecutionContext(agent_id="my-agent", capabilities=["read", "write"])

# Establish zero-trust agent identity
trust = TrustManager()
trust.register_agent(ctx)
```

Install only what you need:

```bash
# Core: kernel + trust mesh
pip install agent-governance

# Full stack: adds hypervisor + SRE
pip install agent-governance[full]

# À la carte
pip install agent-governance[hypervisor]
pip install agent-governance[sre]
```

---

## Components

| Component | Package | What It Does |
|-----------|---------|--------------|
| **[Agent OS](https://github.com/imran-siddique/agent-os)** | `agent-os-kernel` | Governance kernel — policy enforcement, capability-based security, audit trails, and the syscall abstraction layer for AI agents |
| **[AgentMesh](https://github.com/imran-siddique/agent-mesh)** | `agentmesh-platform` | Zero-trust communication — mutual TLS for agents, encrypted channels, trust scoring, and secure multi-agent orchestration ("SSL for AI Agents") |
| **[Agent Hypervisor](https://github.com/imran-siddique/agent-hypervisor)** | `agent-hypervisor` | Runtime supervisor — execution rings, resource limits, sandboxed execution, kill switches, and real-time intervention for autonomous agents |
| **[Agent SRE](https://github.com/imran-siddique/agent-sre)** | `agent-sre` | Reliability engineering — health monitoring, SLO enforcement, incident response automation, and chaos engineering for agent fleets |

### Star the ecosystem

<p align="center">

[![Agent OS Stars](https://img.shields.io/github/stars/imran-siddique/agent-os?label=Agent%20OS&style=social)](https://github.com/imran-siddique/agent-os)&nbsp;&nbsp;
[![AgentMesh Stars](https://img.shields.io/github/stars/imran-siddique/agent-mesh?label=AgentMesh&style=social)](https://github.com/imran-siddique/agent-mesh)&nbsp;&nbsp;
[![Agent Hypervisor Stars](https://img.shields.io/github/stars/imran-siddique/agent-hypervisor?label=Agent%20Hypervisor&style=social)](https://github.com/imran-siddique/agent-hypervisor)&nbsp;&nbsp;
[![Agent SRE Stars](https://img.shields.io/github/stars/imran-siddique/agent-sre?label=Agent%20SRE&style=social)](https://github.com/imran-siddique/agent-sre)

</p>

---

## Why a Unified Governance Stack?

Running AI agents in production without governance is like deploying microservices without TLS, RBAC, or monitoring. Each layer solves a different problem:

| Concern | Without Governance | With Agent Governance |
|---------|-------------------|----------------------|
| **Security** | Agents call any tool, access any resource | Capability-based permissions, policy enforcement |
| **Trust** | No identity verification between agents | Mutual TLS, trust scores, encrypted channels |
| **Control** | Runaway agents consume unbounded resources | Execution rings, resource limits, kill switches |
| **Reliability** | Silent failures, no observability | SLO enforcement, health checks, incident automation |
| **Compliance** | No audit trail for agent decisions | Immutable audit logs, decision lineage tracking |

**One install. Four layers of protection.**

The meta-package ensures all components are version-compatible and properly integrated. No dependency conflicts, no version mismatches — just a single `pip install` to go from zero to production-grade agent governance.

---

## The Agent Governance Ecosystem

```
agent-governance ─── The meta-package (you are here)
├── agent-os-kernel ─── Governance kernel
├── agentmesh-platform ─── Zero-trust mesh
├── agent-hypervisor ─── Runtime supervisor (optional)
└── agent-sre ─── Reliability engineering (optional)
```

Each component works standalone, but they're designed to work together. The kernel enforces policy, the mesh secures communication, the hypervisor controls execution, and SRE keeps everything running.

---

## Contributing

Contributions are welcome! Please see the individual component repos for contribution guidelines:

- [Agent OS](https://github.com/imran-siddique/agent-os)
- [AgentMesh](https://github.com/imran-siddique/agent-mesh)
- [Agent Hypervisor](https://github.com/imran-siddique/agent-hypervisor)
- [Agent SRE](https://github.com/imran-siddique/agent-sre)

## License

MIT — see [LICENSE](LICENSE) for details.

---

<div align="center">

**[imransiddique.com](https://imransiddique.com)** · **[Documentation](https://imransiddique.com/agent-os-docs/)** · **[GitHub](https://github.com/imran-siddique)**

*Building the governance layer for the agentic era*

</div>
