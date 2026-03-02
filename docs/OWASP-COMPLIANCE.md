<div align="center">

# 🛡️ OWASP Agentic Top 10 — Compliance Mapping

**How the Agent Governance stack covers the [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)**

</div>

---

## Coverage Summary

| # | OWASP Risk | Coverage | Component |
|---|-----------|----------|-----------|
| ASI-01 | Agent Goal Hijack | ✅ Covered | Agent OS — Policy Engine |
| ASI-02 | Tool Misuse & Exploitation | ✅ Covered | Agent OS — Capability Sandboxing |
| ASI-03 | Identity & Privilege Abuse | ✅ Covered | AgentMesh — DID Identity & Trust Scoring |
| ASI-04 | Supply Chain Vulnerabilities | 🔄 Roadmap | Agent-SBOM (planned) |
| ASI-05 | Unexpected Code Execution | ✅ Covered | Agent Hypervisor — Execution Rings |
| ASI-06 | Memory & Context Poisoning | ✅ Covered | Agent OS — VFS Policies + CMVK Verification |
| ASI-07 | Insecure Inter-Agent Communication | ✅ Covered | AgentMesh — IATP + Encrypted Channels |
| ASI-08 | Cascading Failures | ✅ Covered | Agent SRE — Circuit Breakers + SLOs |
| ASI-09 | Human-Agent Trust Exploitation | ✅ Covered | Agent OS — Approval Workflows |
| ASI-10 | Rogue Agents | ✅ Covered | Agent Hypervisor — Kill Switch + Ring Isolation |

**9 of 10 risks covered today. 1 on the roadmap.**

---

## Detailed Mapping

### ASI-01: Agent Goal Hijack

> *Attackers manipulate the agent's objectives via indirect prompt injection or poisoned inputs.*

**Mitigation:** Agent OS enforces **policy-based action interception** at the kernel level. Every agent action passes through the policy engine before execution. Unauthorized goal changes are blocked before they reach the agent's tools.

- **Policy Engine** — declarative rules controlling what agents can and cannot do
- **Action Interception** — kernel-level syscall abstraction intercepts all agent actions
- **Policy Modes** — `strict` (deny by default), `permissive` (allow by default), `audit` (log only)
- **MCP Governance Proxy** — policy enforcement for MCP tool calls

```python
from agent_os import StatelessKernel, ExecutionContext

kernel = StatelessKernel()
ctx = ExecutionContext(agent_id="my-agent", policies=["read_only"])

# This action is blocked by policy — goal hijack prevented
result = await kernel.execute(
    action="delete_database",
    params={"target": "production"},
    context=ctx,
)
# result.success = False, result.error = "Policy violation: read_only"
```

**Component:** [Agent OS](https://github.com/imran-siddique/agent-os) — `src/agent_os/policy/`, `extensions/mcp-server/src/services/policy-engine.ts`

---

### ASI-02: Tool Misuse & Exploitation

> *An agent's authorized tools are abused in unintended ways, such as exfiltrating data via read operations.*

**Mitigation:** Agent OS provides **capability-based security** inspired by POSIX. Agents are granted specific, scoped capabilities — not blanket tool access. Tool inputs are sanitized for injection patterns.

- **Capability Sandboxing** — agents receive explicit capability grants (read, write, execute, network)
- **Tool Allowlists/Denylists** — built-in strict mode blocks `run_shell`, `execute_command`, `eval`
- **Input Sanitization** — command injection detection, shell metacharacter blocking
- **`verify_code_safety`** MCP tool — checks generated code before execution

**Component:** [Agent OS](https://github.com/imran-siddique/agent-os) — capability model, MCP proxy policy rules

---

### ASI-03: Identity & Privilege Abuse

> *Agents escalate privileges by abusing identities or inheriting excessive credentials.*

**Mitigation:** AgentMesh implements **zero-trust identity** using Decentralized Identifiers (DIDs). Every agent has a cryptographic identity with scoped capabilities. Trust is earned, not assumed.

- **DID Identity** — `did:agentmesh:{agentId}:{fingerprint}` with Ed25519 key pairs
- **Trust Scoring** — tiered model: `Untrusted → Provisional → Trusted → Verified`
- **Delegation Chains** — track trust inheritance with verifiable credentials
- **Challenge-Response Handshake** — cryptographic authentication at connection time
- **Trust Decay** — scores degrade over time without positive signals

```python
from agentmesh import AgentIdentity

identity = AgentIdentity.create(
    name="data-analyst",
    sponsor="admin@company.com",
    capabilities=["read:data"],  # Scoped — cannot write or delete
)
```

**Component:** [AgentMesh](https://github.com/imran-siddique/agent-mesh) — `sdks/typescript/src/identity.ts`, `sdks/typescript/src/trust.ts`

---

### ASI-04: Agentic Supply Chain Vulnerabilities

> *Vulnerabilities in third-party tools, plugins, or APIs cascade to agent behavior.*

**Status:** 🔄 **On roadmap** — Agent-SBOM (Software Bill of Materials for agent tool chains) is planned.

**Current partial coverage:**
- PyPI packages with pinned dependencies
- CI security scanning (Bandit) on all repos
- MIT-licensed, auditable source code

**Planned:**
- Agent dependency provenance tracking
- Tool chain integrity verification
- Runtime dependency scanning

---

### ASI-05: Unexpected Code Execution

> *Agents trigger remote code execution through tools, interpreters, or APIs.*

**Mitigation:** Agent Hypervisor implements **CPU ring-inspired execution isolation**. Agents run in restricted rings with resource limits and can be terminated instantly.

- **Execution Rings (Ring 0–3)** — privilege tiers from kernel (0) to untrusted (3)
- **Resource Limits** — CPU, memory, time bounds per agent execution
- **Kill Switch** — instant termination of runaway agents
- **Saga Compensation** — automatic rollback when execution fails
- **Sandboxed Execution** — code runs in isolated contexts

**Component:** [Agent Hypervisor](https://github.com/imran-siddique/agent-hypervisor) — execution rings, resource management, saga orchestration

---

### ASI-06: Memory & Context Poisoning

> *Persistent memory or long-running context is poisoned with malicious instructions.*

**Mitigation:** Agent OS provides **policy-controlled virtual filesystem (VFS)** for agent memory with read-only policy enforcement and multi-model claim verification.

- **VFS Memory Policies** — `vfs://{agent_id}/mem/*` with per-agent access control
- **Policy-Protected Context** — `vfs://{agent_id}/policy/*` is read-only
- **CMVK (Cross-Model Verification Kernel)** — verifies claims across multiple AI models to detect poisoned context
- **Prompt Injection Detection** — sanitizer blocks `ignore previous instructions`, `disregard prior` patterns
- **PII Protection** — detects and redacts sensitive data in agent context

**Component:** [Agent OS](https://github.com/imran-siddique/agent-os) — VFS, CMVK verification, MCP proxy sanitizer

---

### ASI-07: Insecure Inter-Agent Communication

> *Agents collaborate without adequate authentication, confidentiality, or validation.*

**Mitigation:** AgentMesh provides **IATP (Inter-Agent Trust Protocol)** — a purpose-built secure communication layer for multi-agent systems.

- **IATP Sign/Verify** — cryptographic trust attestations for every message
- **Encrypted Channels** — all inter-agent communication is encrypted
- **Trust Scoring at Connection** — agents evaluated before communication is established
- **Reputation System** — ongoing trust tracking with decay and penalty
- **Mutual Authentication** — both sides must prove identity via challenge-response

```python
# Sign a trust attestation
attestation = iatp_sign(agent_id="sender", claim="data_verified", evidence={...})

# Verify before acting on inter-agent message
is_valid = iatp_verify(attestation, expected_signer="sender")
```

**Component:** [AgentMesh](https://github.com/imran-siddique/agent-mesh) — IATP protocol, trust scoring, handshake service

---

### ASI-08: Cascading Failures

> *An initial error or compromise triggers multi-step compound failures across chained agents.*

**Mitigation:** Agent SRE provides **production-grade reliability engineering** specifically designed for agent fleets.

- **Circuit Breakers** — automatic isolation of failing agents before failures cascade
- **Cascading Failure Detection** — monitors dependency chains for propagation patterns
- **SLO Enforcement** — Service Level Objectives with error budgets per agent
- **Error Budgets** — quantified failure tolerance that triggers automatic intervention
- **Canary Deploys** — gradual rollout of agent changes to detect issues early
- **OpenTelemetry Integration** — distributed tracing across multi-agent workflows

**Component:** [Agent SRE](https://github.com/imran-siddique/agent-sre) — circuit breakers, SLO engine, cascading failure detection, chaos testing

---

### ASI-09: Human-Agent Trust Exploitation

> *Attackers leverage misplaced user trust in agents' autonomy to authorize dangerous actions.*

**Mitigation:** Agent OS implements **approval workflows** that require explicit human confirmation for high-risk agent actions.

- **Approval Workflows** — configurable human-in-the-loop for sensitive operations
- **Risk Assessment** — automatic classification: `critical`, `high`, `medium`, `low`
- **Quorum Logic** — critical actions require multiple approvals
- **Expiration Tracking** — approval requests time out to prevent stale authorizations
- **`require_approval` Policy Action** — built-in policy rule for human review gates

**Component:** [Agent OS](https://github.com/imran-siddique/agent-os) — `extensions/mcp-server/src/services/approval-workflow.ts`

---

### ASI-10: Rogue Agents

> *Agents operating outside their defined scope by configuration drift, reprogramming, or emergent misbehavior.*

**Mitigation:** Agent Hypervisor provides **runtime behavioral monitoring** with instant kill capability, combined with AgentMesh trust decay.

- **Ring Isolation** — rogue agents are confined to their execution ring and cannot escalate
- **Kill Switch** — immediate termination of agents exhibiting rogue behavior
- **Behavioral Monitoring** — trust score decay on failures, anomaly tracking
- **Immutable Audit Trail** — hash-chain audit logs detect tampering
- **Shapley-Value Fault Attribution** — identify which agent in a multi-agent system is responsible for failures
- **Merkle Audit Trails** — cryptographic proof of agent action history

**Component:** [Agent Hypervisor](https://github.com/imran-siddique/agent-hypervisor) + [AgentMesh](https://github.com/imran-siddique/agent-mesh) trust decay

---

## One Install, Nine Protections

```bash
pip install ai-agent-governance[full]
```

This single command installs the complete governance stack:

| Layer | Package | OWASP Risks Covered |
|-------|---------|-------------------|
| **Kernel** | `agent-os-kernel` | ASI-01, ASI-02, ASI-06, ASI-09 |
| **Trust Mesh** | `agentmesh-platform` | ASI-03, ASI-07, ASI-10 |
| **Hypervisor** | `agent-hypervisor` | ASI-05, ASI-10 |
| **SRE** | `agent-sre` | ASI-08 |

---

## Alignment with Other Frameworks

| Framework | Status |
|-----------|--------|
| [OWASP Agentic Top 10 (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | 9/10 covered |
| [NIST AI RMF](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework) | Govern, Map, Measure, Manage functions addressed |
| [NIST AI Agent Standards Initiative](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure) | Agent identity (IATP), authentication, audit trails |
| [Singapore MGF for Agentic AI](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) | Zero-trust, accountability, oversight layers |
| [EU AI Act (Aug 2026)](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | Risk classification, audit trails, human oversight |

---

<div align="center">

*Last updated: March 2026*

**[⬅ Back to README](../README.md)** · **[📈 Traction](TRACTION.md)**

</div>
