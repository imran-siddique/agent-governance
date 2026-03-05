from __future__ import annotations

import importlib
import sys
import types
from pathlib import Path

import pytest

try:
    import tomllib  # py3.11+
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore


ROOT = Path(__file__).resolve().parents[1]
PYPROJECT = ROOT / "pyproject.toml"


def _load_pyproject() -> dict:
    return tomllib.loads(PYPROJECT.read_text(encoding="utf-8"))


def test_base_dependencies_include_kernel_and_mesh() -> None:
    project = _load_pyproject()["project"]
    deps = set(project["dependencies"])

    assert "agent-os-kernel>=1.0.0" in deps
    assert "agentmesh-platform>=1.0.0" in deps


@pytest.mark.parametrize(
    ("extra", "expected_dep"),
    [
        ("hypervisor", "agent-hypervisor>=2.0.0"),
        ("sre", "agent-sre>=1.0.0"),
        ("full", "agent-hypervisor>=2.0.0"),
        ("full", "agent-sre>=1.0.0"),
    ],
)
def test_optional_dependency_groups_are_wired(extra: str, expected_dep: str) -> None:
    optional = _load_pyproject()["project"]["optional-dependencies"]
    assert expected_dep in optional[extra]


def test_re_exports_work_when_optional_packages_exist(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_agent_os = types.ModuleType("agent_os")

    class StatelessKernel: ...

    class ExecutionContext: ...

    fake_agent_os.StatelessKernel = StatelessKernel
    fake_agent_os.ExecutionContext = ExecutionContext

    fake_agentmesh = types.ModuleType("agentmesh")

    class TrustManager: ...

    fake_agentmesh.TrustManager = TrustManager

    monkeypatch.setitem(sys.modules, "agent_os", fake_agent_os)
    monkeypatch.setitem(sys.modules, "agentmesh", fake_agentmesh)

    sys.modules.pop("agent_governance", None)
    pkg = importlib.import_module("agent_governance")

    assert pkg.StatelessKernel is StatelessKernel
    assert pkg.ExecutionContext is ExecutionContext
    assert pkg.TrustManager is TrustManager


def test_import_still_works_when_optional_packages_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delitem(sys.modules, "agent_os", raising=False)
    monkeypatch.delitem(sys.modules, "agentmesh", raising=False)

    sys.modules.pop("agent_governance", None)
    pkg = importlib.import_module("agent_governance")

    assert pkg.__version__ == "1.0.1"
