# Architecture Overview

## Purpose

This document provides an architectural overview of the Yin-Yang Five-Phase Reasoning Protocol v0.1.

The protocol defines a dynamic reasoning-control model based on two structural principles:

1. **Yin-Yang state transition**
2. **Five-Phase functional routing**

It is designed to support reasoning systems that do not remain in continuous expansion, but instead move through activation, integration, critique, compression, memory, and return.

In simple terms:

```text
Reasoning should breathe.
```

It should expand when expansion is useful.
It should compress when compression is wiser.
It should stop when the answer is sufficient.
It should retain only what can improve the next cycle.

## Architectural Summary

The protocol can be understood as a five-layer reasoning architecture:

```text
┌────────────────────────────────────┐
│ Layer 5: Memory Layer              │
│ Retain essence and prepare return  │
├────────────────────────────────────┤
│ Layer 4: Brake Layer               │
│ Compress, prune, slow, or stop     │
├────────────────────────────────────┤
│ Layer 3: Routing Layer             │
│ Move between reasoning phases      │
├────────────────────────────────────┤
│ Layer 2: Phase Layer               │
│ Activate Wood / Fire / Earth /     │
│ Metal / Water roles                │
├────────────────────────────────────┤
│ Layer 1: State Layer               │
│ Yin / Yang / Balanced state        │
└────────────────────────────────────┘
```

Each layer controls a different aspect of reasoning.

* The **State Layer** decides whether the system should expand, compress, or stabilize.
* The **Phase Layer** decides which reasoning role should be active.
* The **Routing Layer** decides where the reasoning should go next.
* The **Brake Layer** decides when reasoning should be reduced or stopped.
* The **Memory Layer** decides what should remain after the cycle ends.

## Core Architectural Model

The protocol replaces a simple linear generation model:

```text
input -> generate -> continue -> output
```

with a cyclical reasoning-control model:

```text
Wood -> Fire -> Earth -> Metal -> Water -> Wood
```

This means reasoning is not treated as endless continuation.

Instead, reasoning becomes a controlled cycle:

1. detect direction
2. expand only as needed
3. integrate with context
4. prune and evaluate stopping
5. retain the useful essence
6. return to a refined next direction when needed

## Yin-Yang State Layer

The State Layer defines whether the reasoning system is operating in an active, restrained, or balanced mode.

## Yang State

Yang represents activation.

Typical Yang operations include:

* generating hypotheses
* expanding explanations
* exploring possible paths
* using broader attention
* producing structured output
* developing logical branches

Yang is necessary for discovery, creativity, and expression.

However, uncontrolled Yang can cause:

* excessive verbosity
* unnecessary branching
* weak or unsupported claims
* hallucination risk
* redundant computation
* runaway generation

## Yin State

Yin represents compression and restraint.

Typical Yin operations include:

* pruning
* summarizing
* stopping
* localizing attention
* consolidating memory
* reducing activation

Yin is necessary for convergence, stability, and completion.

Without Yin, a reasoning system may continue generating even after the useful answer has already emerged.

## Balanced State

The balanced state is used when reasoning requires integration rather than pure expansion or pure compression.

This state is especially important for the Earth phase, where the system checks context, coherence, and alignment with the user’s actual request.

## Five-Phase Reasoning Roles

The protocol defines five functional reasoning roles.

These roles may be implemented as:

* separate agents
* model routes
* prompt modes
* internal policies
* orchestration states
* reasoning modules
* Multi-Wing components

They do not require five separate models.

## Wood: Direction

Wood detects the beginning of reasoning.

It asks:

```text
What is trying to emerge?
```

Wood is responsible for:

* detecting the core question
* forming the initial hypothesis
* identifying possible paths
* sensing the direction of inquiry

Wood prevents reasoning from beginning blindly.

## Fire: Expansion

Fire develops the reasoning.

It asks:

```text
How can this be expressed or developed?
```

Fire is responsible for:

* expanding hypotheses
* generating explanations
* producing drafts
* developing logical paths
* exploring implications

Fire gives reasoning its expressive force.

However, Fire must eventually be checked.
Without restraint, Fire becomes over-expansion.

## Earth: Integration

Earth stabilizes the reasoning in context.

It asks:

```text
Does this fit the whole context?
```

Earth is responsible for:

* checking coherence
* aligning reasoning with the task
* absorbing contradictions
* connecting local reasoning to broader context
* stabilizing meaning

Earth prevents the output from drifting away from the original request.

## Metal: Critique

Metal prunes and refines the reasoning.

It asks:

```text
What should be cut, corrected, or stopped?
```

Metal is responsible for:

* removing noise
* reducing redundancy
* detecting weak claims
* compressing output
* enforcing precision
* deciding whether to stop

Metal turns critique into a structural part of reasoning rather than an afterthought.

## Water: Memory

Water retains what matters.

It asks:

```text
What should remain after the reasoning ends?
```

Water is responsible for:

* retaining essential patterns
* extracting reusable lessons
* preserving minimal traces
* supporting future cycles
* returning refined knowledge to Wood

Water prevents reasoning from becoming either forgetful or overloaded.

It does not store everything.
It stores what can improve future reasoning.

## Generating Cycle

The generating cycle describes constructive reasoning flow.

```text
Wood -> Fire -> Earth -> Metal -> Water -> Wood
```

This cycle means:

1. **Wood** detects direction.
2. **Fire** expands the idea.
3. **Earth** integrates the reasoning with context.
4. **Metal** critiques and prunes.
5. **Water** retains the essence.
6. **Wood** receives the refined seed for a new cycle if needed.

This structure allows reasoning to develop without becoming uncontrolled.

## Controlling Cycle

The controlling cycle defines self-regulation.

```text
Metal controls Wood
Water controls Fire
Wood controls Earth
Fire controls Metal
Earth controls Water
```

In architectural terms:

* **Metal controls Wood** by cutting excessive speculation.
* **Water controls Fire** by cooling over-expansion.
* **Wood controls Earth** by redirecting stagnant context.
* **Fire controls Metal** by restoring useful detail when pruning becomes excessive.
* **Earth controls Water** by filtering memory and preventing noise retention.

The controlling cycle prevents any single reasoning mode from dominating the system.

## Brake Architecture

The Brake Layer is one of the most important parts of the protocol.

It defines when reasoning should:

* slow down
* compress
* change phase
* stop
* return to memory
* avoid further expansion

Typical brake conditions include:

* redundancy detected
* excessive branching detected
* unsupported claim risk
* context drift detected
* reasoning overheat detected
* completion detected

The Brake Layer makes stopping a first-class reasoning operation.

Stopping is not failure.
Stopping is a valid form of intelligence.

## Memory Return Architecture

The Memory Layer does not simply store the final answer.

It retains selected essence.

A memory trace may include:

* core claim
* key decision
* unresolved question
* next action
* reusable pattern
* important constraint

The Water-to-Wood return process converts selected memory into a new reasoning direction.

```text
Water -> Wood
retained essence -> new inquiry vector
```

This allows recursive reasoning without preserving unnecessary noise.

The system does not restart from zero.
It begins the next cycle from refined memory.

## Relationship to Multi-Wing Architecture

This protocol is designed to complement Multi-Wing architecture.

Multi-Wing defines distributed reasoning through multiple wings or agents.

The Yin-Yang Five-Phase Reasoning Protocol defines how those wings should activate, restrain, route, critique, stop, and return.

In simple terms:

```text
Multi-Wing = distributed reasoning structure
Yin-Yang Five-Phase = dynamic reasoning control model
```

Multi-Wing answers:

```text
Which reasoning wing should act?
```

This protocol answers:

```text
When should reasoning expand, compress, stop, or return?
```

Together, they form a more complete architecture:

```text
Distributed intelligence + dynamic control
```

## Energy-Aware Reasoning

This protocol does not claim measured hardware-level energy reduction.

Instead, it defines an energy-aware reasoning model at the control layer.

Energy awareness begins by reducing unnecessary reasoning activity, such as:

* unnecessary branching
* unnecessary expansion
* unnecessary repetition
* excessive context use
* continued generation after completion
* retention of irrelevant memory

The protocol aims to improve reasoning efficiency by controlling activation.

A system that can stop, compress, and route selectively may reduce wasted reasoning steps compared with a system that continues expanding by default.

This should be understood as an architectural direction, not a measured performance claim.

## Example Architecture Flow

A basic reasoning cycle may look like this:

```text
User question
   ↓
Wood detects the core direction
   ↓
Fire expands the explanation
   ↓
Earth checks context and coherence
   ↓
Metal removes weak or unnecessary parts
   ↓
Water retains the useful essence
   ↓
Final answer or next Wood cycle
```

A stopping-focused cycle may look like this:

```text
Broad request
   ↓
Wood detects scope risk
   ↓
Fire expands candidate branches
   ↓
Earth detects context drift
   ↓
Metal prunes excessive branches
   ↓
Water stores the essential pattern
   ↓
Stop
```

A memory-return cycle may look like this:

```text
Previous retained essence
   ↓
Water retrieves selected memory
   ↓
Wood converts memory into new direction
   ↓
Fire expands minimally
   ↓
Earth integrates
   ↓
Metal refines
   ↓
Water updates memory
```

## Implementation Possibilities

This protocol may be implemented in several ways.

## Prompt-Level Implementation

A single model can simulate the five phases through instruction design.

Example:

* first identify direction
* then expand
* then check context
* then critique
* then summarize and stop

This is suitable for GPT-style assistants.

## Agent-Level Implementation

Each phase can be implemented as a separate agent.

Example:

* Wood Agent
* Fire Agent
* Earth Agent
* Metal Agent
* Water Agent

An orchestrator routes the task between agents.

This is suitable for Multi-Wing systems.

## Policy-Level Implementation

The phases can be implemented as policies inside a larger reasoning system.

Example:

* expansion policy
* context policy
* critique policy
* stopping policy
* memory policy

This is suitable for production AI systems.

## Hardware-Aware Implementation

In future work, the protocol may inspire systems where different reasoning phases correspond to different activation levels or computational pathways.

However, this repository does not define a hardware implementation.

## Architectural Non-Goals

This protocol does not attempt to:

* replace Transformer architecture directly
* prove measured energy savings
* define a complete neuromorphic system
* claim metaphysical properties of AI
* treat Yin-Yang or Five-Phase theory as scientific law
* automate all reasoning decisions without review
* remove the need for evaluation, validation, or governance

It is a structural reasoning-control protocol.

## Summary

The Yin-Yang Five-Phase Reasoning Protocol defines reasoning as a dynamic cycle rather than continuous expansion.

Its core architecture is:

```text
Yin-Yang = state control
Five Phases = reasoning roles
Generating Cycle = constructive flow
Controlling Cycle = self-regulation
Brake Layer = stopping logic
Memory Layer = retained essence and return
```

The central principle is simple:

```text
Reasoning should breathe.
```

A reasoning system should know when to expand.
It should know when to compress.
It should know when to stop.
And when another cycle is needed, it should begin not from noise, but from retained essence.
