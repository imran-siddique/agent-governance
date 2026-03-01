"""
Agent Governance — Quick Start

Boot the full governance stack in under 30 lines.
Shows: kernel init, trust registration, policy check, audit trail.

Usage:
    pip install ai-agent-governance
    python examples/quickstart.py
"""

from agent_os import StatelessKernel, ExecutionContext
from agentmesh import TrustManager

# 1. Boot the governance kernel
kernel = StatelessKernel()
print("✅ Governance kernel booted")

# 2. Create an execution context for our agent
ctx = ExecutionContext(
    agent_id="quickstart-agent",
    capabilities=["read", "write"],
)

# 3. Register with the trust mesh
trust = TrustManager()
trust.register_agent(ctx)
print(f"✅ Agent registered with trust score: {trust.get_trust_score(ctx.agent_id)}")

# 4. Check a policy before executing an action
result = kernel.check_policy(ctx, action="file_read", resource="/data/reports.csv")
print(f"✅ Policy check: {'ALLOWED' if result.allowed else 'DENIED'} — {result.reason}")

# 5. Log the action for audit
kernel.audit_log(ctx, action="file_read", resource="/data/reports.csv", outcome=result)
print("✅ Action logged to audit trail")

print("\n🎉 Governance stack is running! Your agent is now governed.")
