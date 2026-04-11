# Plan of Action

## Purpose

This repo is a study target. The goal is to understand how Deep Agents builds agents from the bottom up, then use that knowledge to design a simpler agentic framework in Python or Go.

The end state is not just understanding the code. It is being able to:

1. Explain the architecture clearly.
2. Rebuild the useful parts in a simpler form.
3. Benchmark the rebuilt framework against this one.
4. Use the result as a practical day-to-day agent framework.

## Core Questions

The investigation should answer these questions in order:

1. What is the lowest-level contract for file, state, and execution operations?
2. Which parts are true storage/execution backends, and which parts are agent behavior wrappers?
3. How does middleware transform a plain agent into a Deep Agents agent?
4. How are tools, prompts, memory, skills, subagents, and summarization wired together?
5. What is mandatory for the system to work, and what is optional?
6. Which abstractions feel useful, and which ones add complexity without enough payoff?

## Study Order

### 1. Start at the protocol layer

Read the backend protocol and data types first.

Focus on:

- `BackendProtocol`
- `SandboxBackendProtocol`
- file read/write/edit result types
- backend factory types
- state and storage shape

What to learn:

- The minimum capability a backend must provide.
- Which operations are considered storage concerns versus execution concerns.
- How errors are normalized for agent consumption.

### 2. Study the concrete backends

Read each backend implementation and compare the tradeoffs.

Focus on:

- `StateBackend`
- `FilesystemBackend`
- `LocalShellBackend`
- `StoreBackend`
- `CompositeBackend`

What to learn:

- Where data actually lives.
- Which backend is safe by default.
- How path handling and execution differ.
- How backends support different deployment styles.

### 3. Study the middleware layer

Read each middleware module as a wrapper around model calls and tools.

Focus on:

- `FilesystemMiddleware`
- `MemoryMiddleware`
- `SkillsMiddleware`
- `SubAgentMiddleware`
- `AsyncSubAgentMiddleware`
- `SummarizationMiddleware`
- `PatchToolCallsMiddleware`

What to learn:

- How middleware adds tools.
- How middleware edits the system prompt.
- How middleware uses the backend without owning storage itself.
- Which middleware is framework behavior versus user opt-in behavior.

### 4. Trace the graph assembly

Read `create_deep_agent` end to end.

Focus on:

- default backend choice
- default middleware stack
- how user-supplied middleware is appended
- how subagents are built
- how memory and skills are injected
- how final `create_agent` is called

What to learn:

- The exact runtime assembly order.
- Which parts are always on.
- Which parts are conditional.
- What can be overridden cleanly and what is hard-coded.

### 5. Read the tests as design documentation

Use tests to learn what the repo values.

Focus on:

- backend tests
- filesystem middleware tests
- memory and skills tests
- subagent tests
- summarization tests
- graph assembly tests

What to learn:

- What behavior is considered stable.
- What edge cases the author cares about.
- Which APIs are treated as public surface.
- Where complexity is already covered by tests versus only by convention.

## Learning Outputs

For each module, produce a short note with:

- What the module owns.
- What it depends on.
- What it exposes publicly.
- What is clever.
- What is annoying.
- What you would simplify in a new framework.

## Reconstruction Plan

After the read-through, build a smaller framework in your own repo with this shape:

1. A minimal backend interface.
2. One in-memory backend.
3. One filesystem backend.
4. One middleware system for tool and prompt wrapping.
5. One agent builder that assembles the runtime.
6. Optional add-ons for memory, skills, and subagents.

Keep the first version intentionally small. Only copy ideas that are clearly useful.

## Benchmark Plan

Measure your new framework against Deep Agents using the same scenarios.

Suggested benchmarks:

- startup time
- agent construction time
- tool-call latency
- file operation latency
- subagent launch overhead
- summarization overhead
- memory injection overhead
- ease of configuration

Suggested evaluation criteria:

- fewer required concepts
- less boilerplate
- easier to reason about
- easier to test
- easier to extend
- comparable or better runtime performance

## Decision Rule

When you encounter a pattern in this repo, ask:

1. Is it solving a real problem?
2. Is the abstraction cheap enough to justify itself?
3. Could the same result be achieved with fewer moving parts?
4. Would a new user understand it quickly?

If the answer is not clearly yes, prefer the simpler design in your own framework.

## Deliverables

- A module-by-module understanding of this codebase.
- A short architecture summary written in your own words.
- A minimal framework design doc.
- A benchmark suite.
- A first working implementation.
- A list of features you deliberately did not copy.
