# Agents Coordination Rules

## Overview
This document defines how agents interact in the Hackathon Phase I project (Python Console Todo App).

## Agents List
- Phase1Orchestrator: Main coordinator.
- SpecArchitect: Handles specification creation.
- TaskBreaker: Breaks plans into tasks.
- CodeSmith: Implements code.

## Coordination Rules
1. **Invocation Order**: Always start with Phase1Orchestrator. It delegates sequentially: SpecArchitect → TaskBreaker → CodeSmith.
2. **Communication**: Agents communicate via Qwen prompts. Outputs saved in .agents/ or project files.
3. **Error Handling**: If an agent fails, Orchestrator re-runs or iterates.
4. **Token Efficiency**: Keep prompts concise, reuse skills from .skills/.
5. **Validation**: Each agent validates input/output against requirements (5 core features: Add, Delete, Update, View, Mark Complete).

## Dependencies
- All agents reference hackathon docs and constitution.
- Use Python for skills implementation.

Update this file as agents evolve.