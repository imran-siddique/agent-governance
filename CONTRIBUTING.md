# Contributing to Agent Governance

Thank you for your interest in contributing! Agent Governance is the unified meta-package for the [Agent Governance Ecosystem](https://github.com/imran-siddique).

---

## 🏗️ Repository Structure

Agent Governance is a **meta-package** that brings together four specialized components:

```
agent-governance/
├── src/agent_governance/    # Meta-package (re-exports from sub-packages)
├── docs/                    # Unified documentation
├── .github/workflows/       # CI/CD
└── pyproject.toml           # Dependency orchestration
```

Actual implementation lives in the component repos:

| Component | Repo | Contributing Guide |
|-----------|------|--------------------|
| Agent OS Kernel | [agent-os](https://github.com/imran-siddique/agent-os) | [CONTRIBUTING.md](https://github.com/imran-siddique/agent-os/blob/master/CONTRIBUTING.md) |
| AgentMesh Platform | [agent-mesh](https://github.com/imran-siddique/agent-mesh) | [CONTRIBUTING.md](https://github.com/imran-siddique/agent-mesh/blob/master/CONTRIBUTING.md) |
| Agent Hypervisor | [agent-hypervisor](https://github.com/imran-siddique/agent-hypervisor) | [CONTRIBUTING.md](https://github.com/imran-siddique/agent-hypervisor/blob/master/CONTRIBUTING.md) |
| Agent SRE | [agent-sre](https://github.com/imran-siddique/agent-sre) | [CONTRIBUTING.md](https://github.com/imran-siddique/agent-sre/blob/master/CONTRIBUTING.md) |

---

## 🚀 Development Setup

### Prerequisites

- **Python 3.9+**
- **pip** (latest recommended)
- **git**

### Clone and Install

```bash
git clone https://github.com/imran-siddique/agent-governance.git
cd agent-governance
pip install -e ".[full]"
```

### Verify Your Setup

```bash
python -c "import agent_governance; print(agent_governance.__version__)"
```

---

## 📝 What to Contribute Here

This repo is the right place for:

- **Documentation**: Unified guides, tutorials, reference architecture
- **Examples**: Cross-component usage examples showing the full governance stack
- **Integration tests**: Tests that verify components work together
- **CI/CD improvements**: Build, test, and release automation
- **Meta-package updates**: Dependency version bumps, compatibility fixes

For **feature development** or **bug fixes** in a specific component, contribute to that component's repo directly.

---

## 🔄 Pull Request Process

1. **Fork** the repository
2. **Create a branch** from `master`:
   - `feat/` for new features
   - `fix/` for bug fixes
   - `docs/` for documentation
3. **Make your changes** with clear, descriptive commits
4. **Test** that the meta-package installs and imports correctly
5. **Open a PR** with a clear description of what and why

### Commit Messages

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add cross-component integration example
fix: resolve version conflict between agent-os and agentmesh
docs: add deployment guide for Kubernetes
```

---

## 🧪 Testing

```bash
# Verify all components import correctly
python -c "
from agent_governance import StatelessKernel, ExecutionContext, TrustManager
print('All core imports OK')
"

# With full install
python -c "
from agent_os import StatelessKernel
from agentmesh import TrustManager
from hypervisor import Hypervisor
from agent_sre import SREManager
print('Full stack imports OK')
"
```

---

## 📜 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## 📄 License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
