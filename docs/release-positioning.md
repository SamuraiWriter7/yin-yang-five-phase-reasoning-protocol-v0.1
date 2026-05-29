# Release Positioning

This document explains the positioning of the Yin-Yang Five-Phase Reasoning Protocol as of `v0.3.1`.

It clarifies what the protocol is, what it is not, how the release series evolved, and how it connects to existing reasoning-control concepts.

## Purpose of This Document

The purpose of this document is to provide a clear release-level interpretation of the protocol.

It is intended for:

* readers evaluating the repository for the first time
* researchers comparing the protocol with existing reasoning-control approaches
* developers considering implementation experiments
* reviewers checking the scope of the claims
* future maintainers of the specification

This document does not introduce new protocol features.

It only clarifies positioning, scope, and interpretation.

## Summary

The Yin-Yang Five-Phase Reasoning Protocol is a structural protocol for describing dynamic reasoning control.

It models reasoning as a cycle of:

```text
activation -> integration -> critique -> compression -> memory -> return
```

rather than as continuous expansion.

The protocol uses three main layers:

```text
Yin-Yang State Model      = activation / restraint / balance
Five-Phase Routing        = functional reasoning roles
Dynamic Control Metrics   = runtime control signals
Yin-Yang Balancer         = dynamic equilibrium controller
```

In simple terms:

```text
v0.1 = reasoning cycle
v0.2 = runtime control metrics
v0.3 = balance controller
v0.3.1 = documentation and release positioning
```

## Release Series

### v0.1.0: Core Protocol

The initial release defined the core reasoning structure:

* Yin-Yang state model
* Five-Phase agent roles
* generating cycle
* controlling cycle
* brake layer
* memory layer
* relationship to Multi-Wing architecture
* energy-aware reasoning notes

This version established the core idea:

```text
Reasoning should breathe.
```

### v0.1.1: Validation Foundation

The `v0.1.1` release added validation infrastructure.

It introduced automated checks for:

* required repository files
* YAML specification structure
* JSON Schema validation
* phase consistency
* generating cycle references
* controlling cycle references
* example validity

This release made the repository easier to maintain and extend.

### v0.2.0: Dynamic Control Metrics

The `v0.2.0` release introduced runtime control metrics:

```text
energy_state
suppression_score
stop_confidence
```

These metrics are control-layer indicators.

They do not measure hardware power directly.

They are used to describe reasoning activation, suppression pressure, and stopping readiness.

### v0.3.0: Yin-Yang Balancer

The `v0.3.0` release introduced Yin-Yang Balancer as a dynamic equilibrium control layer.

It added a structural model for:

* over-expansion detection
* over-suppression detection
* phase balance adjustment
* sync / async reasoning selection
* delayed critique
* background memory return
* constraint-aware balance control

This release connected the v0.2 metrics to balance-aware routing decisions.

### v0.3.1: Documentation and Release Polish

The `v0.3.1` release does not introduce new protocol mechanics.

Its purpose is to clarify:

* release positioning
* claim boundaries
* relationship to existing fields
* appropriate interpretation of Yin-Yang and Five-Phase concepts
* external communication style

This release improves readability and reduces ambiguity.

## What This Protocol Is

This protocol is:

* a structural reasoning-control specification
* a conceptual architecture for phase-based reasoning
* a schema-backed draft protocol
* a model for self-regulating reasoning flow
* a way to describe activation, compression, critique, memory, and stopping
* a possible interface layer for multi-agent reasoning systems
* a foundation for future implementation experiments

It is best understood as a control model, not as a model architecture.

## What This Protocol Is Not

This protocol is not:

* a benchmark result
* a hardware implementation
* a replacement for Transformer architecture
* a claim of measured energy reduction
* a complete inference engine
* a safety bypass mechanism
* a guaranteed alignment method
* a scientific proof of Yin-Yang or Five-Phase theory
* a claim that philosophy directly improves model performance

The protocol should be evaluated through implementation, testing, and comparison before any strong empirical claims are made.

## Relationship to Existing Areas

This protocol may be understood as complementary to several existing areas.

### Multi-Agent Orchestration

Multi-agent orchestration focuses on how multiple agents, roles, or tools are coordinated.

This protocol contributes a phase-based control model for deciding:

```text
which reasoning role should activate,
when it should compress,
when it should critique,
when it should stop,
and what should return to memory.
```

### Adaptive Reasoning

Adaptive reasoning systems adjust reasoning depth according to task requirements.

This protocol contributes a structured vocabulary for describing that adjustment:

```text
Yang = expansion
Yin = restraint
Balanced = integration
```

### Early Stopping

Early stopping concerns when computation or generation should stop.

This protocol extends the idea of stopping into a broader control cycle:

```text
expand -> integrate -> critique -> compress -> retain -> stop
```

Stopping is not treated as failure.

It is treated as a valid reasoning operation.

### Memory-Aware Routing

Memory-aware routing concerns what information should be retained or reused.

This protocol treats Water as the memory and return phase.

Water does not retain everything.

It preserves only useful essence, unresolved direction, or reusable structure.

### Critique and Compression

Critique and compression are often added as post-processing steps.

This protocol treats them as structural phases.

Metal critique and Water compression are built into the reasoning cycle.

## Technical Interpretation of Yin-Yang

In this protocol, Yin-Yang is not used as a metaphysical claim.

It is used as a state-control metaphor and structural model.

```text
Yang = activation, exploration, expansion
Yin = restraint, compression, silence
Balanced = integration and phase stabilization
```

This allows the protocol to describe reasoning as controlled oscillation rather than continuous generation.

## Technical Interpretation of Five Phases

In this protocol, the Five Phases are not treated as scientific laws.

They are used as functional reasoning roles.

```text
Wood  = direction
Fire  = expansion
Earth = integration
Metal = critique
Water = memory
```

The value of the model is not that it proves Five-Phase theory.

The value is that it provides a compact structure for organizing reasoning behavior.

## Technical Interpretation of Yin-Yang Balancer

Yin-Yang Balancer is the v0.3 dynamic equilibrium layer.

It uses v0.2 control metrics as input signals:

```text
energy_state
suppression_score
stop_confidence
```

It then supports routing decisions such as:

```text
expand_now
compress_now
stop_now
delay_return
rebalance
```

The balancer does not override constraints.

It operates within existing model constraints and safety boundaries.

## Claim Boundaries

The protocol makes structural claims, not empirical performance claims.

It may claim:

* this is a proposed reasoning-control structure
* this is a schema-backed draft protocol
* this models reasoning as phase transition and balance control
* this connects Yin-Yang / Five-Phase concepts to reasoning-control vocabulary
* this may support experiments in adaptive reasoning, stopping, compression, and memory routing

It should not claim without evidence:

* measured energy reduction
* benchmark improvement
* replacement of model architecture
* guaranteed safety improvement
* superiority over existing architectures
* complete novelty across all prior research
* production readiness

## Recommended External Description

A concise external description:

```text
Yin-Yang Five-Phase Reasoning Protocol is a draft structural protocol for
dynamic, energy-aware, multi-agent reasoning control. It uses Yin-Yang
state transitions, Five-Phase routing, dynamic control metrics, and
Yin-Yang Balancer equilibrium control to describe when reasoning should
expand, compress, critique, stop, delay, or return through memory.
```

A shorter description:

```text
A phase-based reasoning-control protocol for balancing expansion,
compression, critique, memory, stopping, and return.
```

A very short description:

```text
Reasoning should breathe.
```

## Recommended Positioning

The safest and clearest positioning is:

```text
This repository proposes a control-layer model that connects multi-agent
orchestration, adaptive reasoning, early stopping, critique-based compression,
and memory-aware routing through a Yin-Yang Five-Phase structure.
```

This avoids overclaiming while still showing the protocol’s distinctive contribution.

## Suggested Use Cases

Potential use cases include:

* prompt-level reasoning control
* lightweight reasoning assistants
* multi-agent routing experiments
* critique and compression pipelines
* memory-aware reasoning workflows
* early-stopping policy experiments
* documentation of reasoning-state transitions
* conceptual modeling for energy-aware reasoning

These use cases remain implementation-dependent.

## Current Maturity Level

The protocol is currently an early draft specification.

Current maturity:

```text
Conceptual structure: strong
Documentation: improving
Schema validation: available
Examples: available
Reference implementation: not yet included
Benchmark evaluation: not yet included
Production readiness: not claimed
```

This repository should be treated as a specification and research-oriented design artifact.

## Future Direction

Future releases may explore:

* oscillation tuning
* convergence window optimization
* phase stability scoring
* additional Multi-Wing examples
* prompt-level implementation profiles
* agent-framework implementation profiles
* test vectors for stopping and delayed return
* lightweight reference implementations
* comparison with existing adaptive reasoning approaches

A natural next major extension after v0.3.x is:

```text
v0.4.0 = Oscillation Tuning and Convergence Control
```

## Closing Principle

The protocol’s central principle remains:

```text
Reasoning should breathe.
```

With v0.3.0 and v0.3.1, this becomes more precise:

```text
Reasoning should expand, compress, critique, delay, return, and stop
through controlled balance rather than continuous activation.
```
