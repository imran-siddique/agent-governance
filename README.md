<div align="center">

# Agent Governance

**The safety, trust, and reliability platform for production AI agents**

*One install for the complete governance stack — kernel · trust mesh · runtime supervisor · reliability engineering*

[![PyPI](https://img.shields.io/badge/pypi-ai--agent--governance-blue.svg)](https://pypi.org/project/ai-agent-governance/)
[![CI](https://github.com/imran-siddique/agent-governance/actions/workflows/ci.yml/badge.svg)](https://github.com/imran-siddique/agent-governance/actions/workflows/ci.yml)
[![GitHub Stars](https://img.shields.io/github/stars/imran-siddique/agent-governance?style=social)](https://github.com/imran-siddique/agent-governance/stargazers)
[![Sponsor](https://img.shields.io/badge/sponsor-❤️-ff69b4)](https://github.com/sponsors/imran-siddique)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

```
pip install ai-agent-governance[full]
```

[Architecture](#architecture) • [Quick Start](#quick-start) • [Components](#components) • [Why Unified?](#why-a-unified-governance-stack) • [Ecosystem](#the-agent-governance-ecosystem) • [OWASP Compliance](docs/OWASP-COMPLIANCE.md) • [Traction](docs/TRACTION.md)

</div>

> ⭐ **If this project helps you, please star it!** It helps others discover the agent governance stack.

> 🔗 **Part of the Agent Governance Ecosystem** — Installs [Agent OS](https://github.com/imran-siddique/agent-os) · [AgentMesh](https://github.com/imran-siddique/agent-mesh) · [Agent Hypervisor](https://github.com/imran-siddique/agent-hypervisor) · [Agent SRE](https://github.com/imran-siddique/agent-sre)

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      agent-governance                           │
│                  pip install ai-agent-governance[full]           │
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
import asyncio
from agent_os import StatelessKernel, ExecutionContext
from agentmesh import AgentIdentity

# Boot the governance kernel
kernel = StatelessKernel()
ctx = ExecutionContext(agent_id="my-agent", policies=["read_only"])

# Establish zero-trust agent identity
identity = AgentIdentity.create(
    name="my-agent",
    sponsor="alice@company.com",
    capabilities=["read:data", "write:reports"],
)

# Execute a governed action
async def main():
    result = await kernel.execute(
        action="database_query",
        params={"query": "SELECT * FROM users"},
        context=ctx,
    )
    print(f"Success: {result.success}, Data: {result.data}")

asyncio.run(main())
```

Install only what you need:

```bash
# Core: kernel + trust mesh
pip install ai-agent-governance

# Full stack: adds hypervisor + SRE
pip install ai-agent-governance[full]

# À la carte
pip install ai-agent-governance[hypervisor]
pip install ai-agent-governance[sre]
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

## Examples

See the [`examples/`](examples/) directory for runnable demos:

```bash
# Quick start — boot the governance stack in 30 lines
python examples/quickstart.py

# Full stack — all 4 layers working together
python examples/governed_agent.py
```

---

## Framework Integration

```bash
# LangChain
pip install langchain ai-agent-governance

# CrewAI
pip install crewai ai-agent-governance

# AutoGen
pip install pyautogen ai-agent-governance
```

---

## 🗺️ Roadmap

| Quarter | Milestone |
|---------|-----------|
| **Q1 2026** | ✅ Unified meta-package, 4 components integrated, PyPI published |
| **Q2 2026** | Cross-component integration tests, unified CLI, dashboard UI |
| **Q3 2026** | Helm chart for Kubernetes, managed cloud preview |
| **Q4 2026** | SOC2 Type II certification, enterprise support tier |

---

## 🛡️ OWASP Agentic Top 10 Coverage

The agent governance stack covers **9 of 10** risks from the [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/):

| OWASP Risk | Coverage | Component |
|-----------|----------|-----------|
| Agent Goal Hijack | ✅ | Agent OS — Policy Engine |
| Tool Misuse | ✅ | Agent OS — Capability Sandboxing |
| Identity & Privilege Abuse | ✅ | AgentMesh — DID Identity |
| Supply Chain Vulnerabilities | 🔄 Roadmap | Agent-SBOM (planned) |
| Unexpected Code Execution | ✅ | Agent Hypervisor — Execution Rings |
| Memory & Context Poisoning | ✅ | Agent OS — VFS + CMVK |
| Insecure Inter-Agent Communication | ✅ | AgentMesh — IATP Protocol |
| Cascading Failures | ✅ | Agent SRE — Circuit Breakers |
| Human-Agent Trust Exploitation | ✅ | Agent OS — Approval Workflows |
| Rogue Agents | ✅ | Agent Hypervisor — Kill Switch |

**[→ Full OWASP compliance mapping with code examples](docs/OWASP-COMPLIANCE.md)**

---

## 📈 Traction

The ecosystem is growing — **3,000+ views, 9,400+ clones, and 1,278 unique developers** in the last 14 days alone. Traffic from Medium, Reddit, LinkedIn, Google, and even ChatGPT.

**[→ See full traction report](docs/TRACTION.md)**

---

## Contributing

We welcome contributions! See our [Contributing Guide](CONTRIBUTING.md) for details.

For component-specific contributions, see:
- [Agent OS](https://github.com/imran-siddique/agent-os/blob/master/CONTRIBUTING.md)
- [AgentMesh](https://github.com/imran-siddique/agent-mesh/blob/master/CONTRIBUTING.md)
- [Agent Hypervisor](https://github.com/imran-siddique/agent-hypervisor/blob/master/CONTRIBUTING.md)
- [Agent SRE](https://github.com/imran-siddique/agent-sre/blob/master/CONTRIBUTING.md)

## License

MIT — see [LICENSE](LICENSE) for details.

---

<div align="center">

**[imransiddique.com](https://imransiddique.com)** · **[Documentation](https://imransiddique.com/agent-os-docs/)** · **[GitHub](https://github.com/imran-siddique)**

*Building the governance layer for the agentic era*

</div>
