# Claim Boundaries

This document defines the claim boundaries for the Yin-Yang Five-Phase Reasoning Protocol as of `v0.3.1`.

It clarifies which claims are appropriate, which claims should be avoided, and how to describe the protocol in a technically careful way.

## Purpose

The purpose of this document is to prevent overclaiming.

The Yin-Yang Five-Phase Reasoning Protocol introduces a structural model for reasoning control, but it is still an early draft specification.

This document helps distinguish between:

* structural claims
* conceptual claims
* implementation claims
* empirical claims
* unsupported claims

The protocol is strongest when it is presented as a control-layer specification, not as a proven replacement for existing AI architectures.

## Recommended Claim Level

The recommended claim level is:

```text
This protocol proposes a structural reasoning-control model.
```

A stronger but still acceptable version:

```text
This protocol defines a schema-backed draft specification for phase-based,
balance-aware reasoning control using Yin-Yang state transitions,
Five-Phase routing, dynamic control metrics, and Yin-Yang Balancer.
```

Avoid presenting the protocol as a completed system, benchmarked method, or proven architecture.

## What This Protocol May Claim

It is appropriate to claim that this protocol:

* proposes a structural model for reasoning control
* defines reasoning as phase transition rather than continuous expansion
* provides a vocabulary for activation, restraint, critique, memory, and stopping
* introduces Five-Phase routing as functional reasoning roles
* introduces dynamic control metrics such as `energy_state`, `suppression_score`, and `stop_confidence`
* introduces Yin-Yang Balancer as a dynamic equilibrium control layer
* supports conceptual modeling of sync / async reasoning behavior
* supports delayed critique and background memory return at the protocol level
* may be useful for multi-agent reasoning experiments
* may support future implementation work
* may help describe adaptive stopping, compression, and memory-aware routing
* includes schema-backed validation for specification consistency

These are structural and design-level claims.

## What This Protocol Should Not Claim

Without implementation, measurement, or peer-reviewed evaluation, the protocol should not claim that it:

* reduces hardware energy consumption
* improves benchmark performance
* replaces Transformer architecture
* replaces RNNs, diffusion models, or existing neural architectures
* guarantees safer AI behavior
* guarantees alignment
* prevents hallucination
* solves inference inefficiency
* solves AI safety
* is production-ready
* is a complete inference engine
* is a universal reasoning law
* proves Yin-Yang or Five-Phase theory scientifically
* is the first or only possible protocol of its kind
* is already an industry standard

These claims require empirical support.

## Preferred Framing

Preferred framing:

```text
A draft structural protocol for balance-aware reasoning control.
```

Also acceptable:

```text
A phase-based reasoning-control specification for describing when reasoning
should expand, compress, critique, stop, delay, or return through memory.
```

Avoid framing such as:

```text
A replacement for Transformer reasoning.
```

or:

```text
A proven energy-saving AI architecture.
```

## Structural Claims vs. Empirical Claims

### Structural Claims

Structural claims describe the design of the protocol.

Example:

```text
The protocol defines Wood, Fire, Earth, Metal, and Water as reasoning roles.
```

This is acceptable.

Another example:

```text
Yin-Yang Balancer uses dynamic control metrics to describe balance-aware routing decisions.
```

This is acceptable.

### Empirical Claims

Empirical claims describe measured performance.

Example:

```text
The protocol reduces inference cost by a fixed percentage.
```

This is not acceptable unless supported by experiments.

Another example:

```text
The protocol outperforms existing reasoning methods.
```

This is not acceptable without evaluation.

## Energy-Related Claims

The protocol may discuss energy awareness only at the control layer.

Acceptable:

```text
The protocol is designed to reduce unnecessary reasoning expansion at the control layer.
```

Acceptable:

```text
The protocol may support future experiments in energy-aware routing.
```

Not acceptable without measurement:

```text
The protocol reduces GPU power consumption.
```

Not acceptable without measurement:

```text
The protocol proves energy-efficient inference.
```

Recommended wording:

```text
This protocol does not measure electrical power directly. It defines energy awareness as a reasoning-control principle: avoid unnecessary activation, reduce redundant branching, and stop when sufficient.
```

## Safety-Related Claims

The protocol includes safety-relevant control concepts such as:

* stopping
* compression
* critique
* constraint-aware balance
* over-expansion control
* delayed critique
* memory filtering

However, these should not be described as guaranteed safety mechanisms.

Acceptable:

```text
The protocol may support safety-relevant reasoning-control experiments.
```

Acceptable:

```text
The Yin-Yang Balancer operates within existing model constraints and safety boundaries.
```

Not acceptable:

```text
The protocol guarantees safe AI.
```

Not acceptable:

```text
The protocol bypasses safety limitations.
```

Not acceptable:

```text
The protocol replaces alignment methods.
```

## Constraint Boundary

The protocol must be described as constraint-aware.

It should not be described as a method for bypassing model rules, safety boundaries, policies, or alignment layers.

Recommended statement:

```text
Yin-Yang Balancer does not override model constraints or bypass safety boundaries. It operates within existing boundaries as a reasoning-flow control layer.
```

This statement should remain visible in documentation related to v0.3.x.

## Relationship to Existing AI Architectures

The protocol should be presented as complementary to existing architectures.

Acceptable:

```text
This protocol may be implemented above existing model architectures as a control-layer specification.
```

Acceptable:

```text
The protocol may complement multi-agent orchestration, adaptive reasoning, early stopping, and memory-aware routing.
```

Not acceptable:

```text
This protocol replaces Transformer architecture.
```

Not acceptable:

```text
This protocol makes existing architectures obsolete.
```

Recommended framing:

```text
The protocol is architecture-adjacent rather than architecture-replacing.
```

## Relationship to Multi-Agent Systems

The protocol may be connected to multi-agent reasoning.

Acceptable:

```text
The protocol can describe how different reasoning roles activate, critique, compress, and return information in a multi-agent system.
```

Acceptable:

```text
The protocol may serve as a control vocabulary for Multi-Wing or other distributed reasoning architectures.
```

Not acceptable without implementation:

```text
The protocol is a complete multi-agent runtime.
```

## Relationship to Early Stopping

The protocol may be connected to early stopping.

Acceptable:

```text
The protocol provides a structural model for deciding when reasoning should stop, compress, or continue.
```

Acceptable:

```text
The `stop_confidence` metric is a protocol-level signal for stopping readiness.
```

Not acceptable without evaluation:

```text
The protocol optimizes stopping better than existing methods.
```

## Relationship to Memory-Aware Routing

The protocol may be connected to memory-aware routing.

Acceptable:

```text
Water represents selective memory retention and return.
```

Acceptable:

```text
The protocol distinguishes between retaining useful essence and preserving unnecessary detail.
```

Not acceptable without implementation:

```text
The protocol provides a complete long-term memory system.
```

## Relationship to Yin-Yang and Five-Phase Concepts

Yin-Yang and Five-Phase concepts are used as structural models.

They should not be presented as scientific proof.

Acceptable:

```text
The protocol uses Yin-Yang and Five-Phase concepts as a compact structural vocabulary for reasoning control.
```

Acceptable:

```text
Yang represents activation, Yin represents restraint, and Balanced represents integration.
```

Not acceptable:

```text
Yin-Yang proves how AI reasoning works.
```

Not acceptable:

```text
Five-Phase theory is a physical law of inference.
```

## Novelty Claims

Novelty claims should be cautious.

Acceptable:

```text
This repository proposes a distinctive integration of Yin-Yang state control, Five-Phase routing, dynamic control metrics, and balance-aware reasoning control.
```

Acceptable:

```text
The protocol may be useful as an exploratory specification for reasoning-control research.
```

Avoid:

```text
This is the world’s first reasoning OS.
```

Avoid:

```text
No existing research has anything similar.
```

Avoid:

```text
This is the future standard of AI reasoning.
```

Such statements may be suitable for personal essays or speculative commentary, but not for technical documentation.

## Recommended External Language

Use:

```text
proposes
defines
models
describes
may support
is intended to
is designed as
can be interpreted as
```

Avoid:

```text
proves
solves
guarantees
replaces
surpasses
is the first
is the only
will become the standard
```

## Safe Short Descriptions

### One-Sentence Description

```text
Yin-Yang Five-Phase Reasoning Protocol is a draft structural protocol for balance-aware reasoning control across activation, critique, compression, memory, stopping, and return.
```

### Technical Description

```text
The protocol combines Yin-Yang state transitions, Five-Phase routing, dynamic control metrics, and Yin-Yang Balancer to describe when reasoning should expand, compress, critique, stop, delay, or return through memory.
```

### Repository Description

```text
A schema-backed draft specification for phase-based, balance-aware reasoning control in multi-agent and adaptive reasoning systems.
```

## Unsafe Short Descriptions

Avoid:

```text
A new AI architecture that replaces Transformers.
```

Avoid:

```text
A proven energy-saving inference protocol.
```

Avoid:

```text
The first complete reasoning OS for artificial intelligence.
```

Avoid:

```text
A guaranteed AI safety solution.
```

## Maturity Statement

Recommended maturity statement:

```text
This repository is an early draft specification and research-oriented design artifact. It provides structural definitions, examples, and validation files, but it does not yet include a reference implementation, benchmark evaluation, or production deployment.
```

## Release-Specific Claim Boundaries

### v0.1.x

Appropriate claim:

```text
The v0.1.x releases define the core phase-based reasoning structure and validation foundation.
```

### v0.2.0

Appropriate claim:

```text
The v0.2.0 release adds dynamic control metrics for describing activation, suppression, and stopping readiness.
```

### v0.3.0

Appropriate claim:

```text
The v0.3.0 release adds Yin-Yang Balancer as a dynamic equilibrium layer for balance-aware reasoning control.
```

### v0.3.1

Appropriate claim:

```text
The v0.3.1 release clarifies documentation, positioning, and claim boundaries without adding new protocol mechanics.
```

## Review Checklist

Before publishing documentation, release notes, or external articles, check:

* Does the text distinguish structural claims from empirical claims?
* Does it avoid claiming measured energy savings?
* Does it avoid claiming benchmark improvement?
* Does it avoid claiming architecture replacement?
* Does it avoid claiming guaranteed safety or alignment?
* Does it describe Yin-Yang and Five-Phase as structural models?
* Does it mention that the protocol is an early draft specification?
* Does it preserve the safety boundary?
* Does it avoid unsupported novelty claims?
* Does it use cautious terms such as "proposes", "models", and "may support"?

## Closing Principle

The safest external position is:

```text
This protocol is a draft structural specification for reasoning control.
```

The strongest internal design principle remains:

```text
Reasoning should breathe.
```

Together:

```text
Reasoning should breathe, but claims should remain grounded.
```
