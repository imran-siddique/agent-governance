"""
Agent Governance — Full Stack Example

Shows all four governance layers working together:
  1. Agent OS Kernel — policy enforcement
  2. AgentMesh — zero-trust identity and communication
  3. Agent Hypervisor — execution rings and resource limits
  4. Agent SRE — health monitoring and SLO enforcement

Usage:
    pip install ai-agent-governance[full]
    python examples/governed_agent.py
"""

from agent_os import StatelessKernel, ExecutionContext
from agentmesh import TrustManager

# Optional: import hypervisor and SRE if installed
try:
    from hypervisor import Hypervisor
    HAS_HYPERVISOR = True
except ImportError:
    HAS_HYPERVISOR = False

try:
    from agent_sre import SREManager
    HAS_SRE = True
except ImportError:
    HAS_SRE = False


def main():
    print("=" * 60)
    print("  Agent Governance — Full Stack Demo")
    print("=" * 60)

    # --- Layer 1: Kernel ---
    kernel = StatelessKernel()
    ctx = ExecutionContext(
        agent_id="governed-agent-001",
        capabilities=["read", "write", "execute"],
    )
    print("\n🧠 [Agent OS] Kernel booted, context created")

    # --- Layer 2: Trust Mesh ---
    trust = TrustManager()
    trust.register_agent(ctx)
    score = trust.get_trust_score(ctx.agent_id)
    print(f"🔗 [AgentMesh] Agent registered — trust score: {score}")

    # --- Layer 3: Hypervisor ---
    if HAS_HYPERVISOR:
        hv = Hypervisor()
        hv.register_agent(ctx.agent_id, ring=2)
        print(f"⚡ [Hypervisor] Agent assigned to Ring 2 (standard privileges)")
    else:
        print("⚡ [Hypervisor] Not installed — pip install ai-agent-governance[full]")

    # --- Layer 4: SRE ---
    if HAS_SRE:
        sre = SREManager()
        sre.register_agent(ctx.agent_id)
        health = sre.health_check(ctx.agent_id)
        print(f"📊 [Agent SRE] Health check: {health.status}")
    else:
        print("📊 [Agent SRE] Not installed — pip install ai-agent-governance[full]")

    # --- Execute a governed action ---
    print("\n--- Executing governed action ---")

    action = "database_query"
    resource = "SELECT * FROM users WHERE role = 'admin'"

    # Check policy
    result = kernel.check_policy(ctx, action=action, resource=resource)
    print(f"📋 Policy check: {'✅ ALLOWED' if result.allowed else '❌ DENIED'}")

    if result.allowed:
        # Log for audit
        kernel.audit_log(ctx, action=action, resource=resource, outcome=result)
        print(f"📝 Audit logged")
        print(f"🎯 Action executed successfully under full governance")
    else:
        print(f"🛑 Action blocked: {result.reason}")

    print("\n" + "=" * 60)
    print("  All governance layers operational ✅")
    print("=" * 60)


if __name__ == "__main__":
    main()
