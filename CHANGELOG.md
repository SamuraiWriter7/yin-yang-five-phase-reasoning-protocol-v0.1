# Changelog

All notable changes to this project will be documented in this file.

This project follows a lightweight semantic versioning style for specification development.

## [0.3.1] - 2026-05-30

### Added

Added documentation and release-polish files for clearer external positioning and safer claim boundaries.

New files:

* `docs/release-positioning.md`
* `docs/claim-boundaries.md`

### Release Positioning

Added `docs/release-positioning.md`.

This document clarifies:

* what the protocol is
* what the protocol is not
* how the release series evolved
* how the protocol relates to existing reasoning-control areas
* how Yin-Yang and Five-Phase concepts should be interpreted technically
* how the v0.1, v0.2, and v0.3 releases fit together
* why v0.3.1 is a documentation and release-polish release

The recommended external positioning is:

```text
This repository proposes a control-layer model that connects multi-agent
orchestration, adaptive reasoning, early stopping, critique-based compression,
and memory-aware routing through a Yin-Yang Five-Phase structure.
```

### Claim Boundaries

Added `docs/claim-boundaries.md`.

This document defines appropriate and inappropriate claims for the protocol.

It clarifies boundaries around:

* energy-related claims
* safety-related claims
* architecture-replacement claims
* novelty claims
* empirical performance claims
* benchmark claims
* production-readiness claims
* relationship to Yin-Yang and Five-Phase concepts

The recommended claim level is:

```text
This protocol proposes a structural reasoning-control model.
```

### Updated

Updated `README.md` to reflect the new v0.3.1 documentation.

The README now includes:

* current version: `v0.3.1`
* documentation and release positioning in the status section
* `docs/release-positioning.md`
* `docs/claim-boundaries.md`
* updated repository structure
* updated key documents
* updated recommended reading order
* a new claim-boundaries section
* grounded external positioning language
* clarification that v0.3.1 introduces no new protocol mechanics

### No Protocol Mechanics Added

This release does not add new protocol mechanics.

No changes were made to:

* `spec/yin-yang-balancer-v0.3.yaml`
* `schemas/yin-yang-balancer.schema.json`
* `examples/yin-yang-balancer-control.example.yaml`
* v0.2 dynamic control metrics
* v0.1 core phase structure

### Notes

The purpose of v0.3.1 is to improve trustworthiness, readability, and external communication.

In simple terms:

```text
v0.1.0 = Five-Phase reasoning skeleton
v0.1.1 = Validation foundation
v0.2.0 = Dynamic control metrics
v0.3.0 = Yin-Yang dynamic balance control
v0.3.1 = Documentation and claim-boundary polish
```

The core principle remains:

```text
Reasoning should breathe.
```

The v0.3.1 communication principle is:

```text
Reasoning should breathe, but claims should remain grounded.
```

## [0.3.0] - 2026-05-30

### Added

Added the Yin-Yang Balancer extension as a non-breaking v0.3.0 extension.

New files:

* `spec/yin-yang-balancer-v0.3.yaml`
* `schemas/yin-yang-balancer.schema.json`
* `examples/yin-yang-balancer-control.example.yaml`
* `docs/yin-yang-balancer.md`

### Yin-Yang Balancer

The v0.3.0 extension introduces a dynamic equilibrium layer for regulating reasoning intensity, suppression, silence, critique, integration, and sync / async transition behavior across the Five-Phase reasoning cycle.

The balancer uses v0.2.0 dynamic control metrics as input signals:

```text
energy_state
suppression_score
stop_confidence
```

These signals are used to support balance-aware routing decisions such as:

```text
expand_now
compress_now
stop_now
delay_return
rebalance
```

### Core Concepts Added

* Yin-Yang Balancer
* Dynamic equilibrium control
* Oscillation amplitude control
* Phase balance adjustment
* Earth as pivot phase
* Fire-to-Water cooling
* Metal-to-Earth integration
* Water-to-Wood restart
* Earth-to-Fire light expansion
* Sync / async reasoning control
* Delayed critique
* Background memory return
* Convergence window
* Constraint-aware balance adjustment

### Phase Adjustment Model

The v0.3.0 extension defines several balance transitions:

```text
Fire  -> Water  = cool excessive expansion
Metal -> Earth  = integrate excessive critique
Water -> Wood   = restart from over-silence or stagnation
Earth -> Fire   = reintroduce light expansion after over-stabilization
```

These transitions are intended to prevent reasoning from becoming one-sided.

### Sync / Async Reasoning Control

Added a structural model for selecting between synchronous and asynchronous reasoning behavior.

Synchronous reasoning is preferred when the answer can be completed immediately and stop confidence is high.

Asynchronous reasoning is preferred when memory settling, delayed critique, or background context integration is useful.

### Validation

Updated GitHub Actions validation to include v0.3 files:

* `spec/yin-yang-balancer-v0.3.yaml`
* `schemas/yin-yang-balancer.schema.json`
* `examples/yin-yang-balancer-control.example.yaml`

The validation workflow now checks:

* required v0.3 files exist
* the v0.3 specification validates against its JSON Schema
* the v0.3 example contains required structural groups
* the v0.3 specification version is `0.3.0`
* the v0.3 example version is `0.3.0`

### Updated

Updated `README.md` to reflect the v0.3.0 extension.

The README now includes:

* Yin-Yang Balancer overview
* v0.3.0 status and structure
* updated protocol layers
* sync / async reasoning control
* delayed critique
* background memory return
* updated repository structure
* updated key documents
* updated validation notes
* updated implementation possibilities
* updated future work

### Non-Goals Clarified

The v0.3.0 extension does not:

* override model constraints
* bypass safety boundaries
* claim hardware-level energy reduction
* claim benchmark-proven performance improvement
* replace model architecture
* define a complete inference engine

The balancer is a constraint-aware control-layer mechanism for stabilizing reasoning behavior inside existing boundaries.

### Notes

The v0.3.0 extension builds directly on v0.2.0.

In simple terms:

```text
v0.1.0 = Five-Phase reasoning skeleton
v0.1.1 = Validation foundation
v0.2.0 = Dynamic control metrics
v0.3.0 = Yin-Yang dynamic balance control
```

The core principle remains:

```text
Reasoning should breathe.
```

With v0.3.0, this principle is extended:

```text
Reasoning should expand, compress, delay, return, and stop with balance.
```

## [0.2.0] - 2026-05-29

### Added

Added the Dynamic Control Metrics extension.

New files:

* `spec/dynamic-control-metrics-v0.2.yaml`
* `schemas/dynamic-control-metrics.schema.json`
* `examples/energy-state-control.example.yaml`

### Dynamic Control Metrics

The v0.2.0 extension introduces normalized runtime control metrics for reasoning flow.

Added metrics:

```text
energy_state
suppression_score
stop_confidence
```

These metrics are intended to help a reasoning system estimate:

* how active the current reasoning path is
* whether reasoning should be suppressed, pruned, rerouted, or compressed
* whether the current answer is sufficient enough to stop
* whether additional expansion would reduce clarity

### energy_state

Added `energy_state` as a control-layer activation profile.

It may include:

* `activation_level`
* `compression_level`
* `routing_cost`
* `active_phase_count`
* `expansion_depth`
* `state_mode`

This metric does not measure electrical power directly.

It represents control-layer activation intensity.

### suppression_score

Added `suppression_score` as a signal for pruning, compression, rerouting, or stopping part of the current reasoning process.

A high suppression score may indicate:

* excessive branching
* repeated generation
* reasoning overheat
* context drift
* weak claims
* memory overload

### stop_confidence

Added `stop_confidence` as a signal for deciding whether the current reasoning cycle is sufficient.

High stop confidence may support routing such as:

```text
Metal -> Water -> Stop
```

Low stop confidence may indicate that the system should continue through Fire or Earth before stopping.

### Metric Thresholds

Added initial normalized threshold interpretation:

| Range       | Meaning       |
| ----------- | ------------- |
| 0.00 - 0.30 | Low signal    |
| 0.31 - 0.70 | Medium signal |
| 0.71 - 1.00 | High signal   |

These thresholds are protocol-level defaults, not universal laws.

### Updated

Updated `README.md` to reflect v0.2.0.

The README now includes:

* Dynamic Control Metrics overview
* `energy_state`
* `suppression_score`
* `stop_confidence`
* metric-based routing examples
* updated protocol layers
* updated repository structure
* updated key documents
* updated validation notes
* updated implementation possibilities
* updated design principles
* updated non-goals
* updated future work

### Validation

Updated validation to support v0.2.0 files.

Validation now checks:

* v0.2 dynamic control metrics specification
* dynamic control metrics schema
* energy-state example structure
* normalized metric values from `0.0` to `1.0`
* runtime control object structure

### Notes

The v0.2.0 extension does not claim hardware-level energy reduction.

It defines energy awareness as a control-layer design principle.

## [0.1.1] - 2026-05-29

### Added

Added validation infrastructure for the initial protocol specification.

New files and updates may include:

* `scripts/validate_specs.py`
* `.github/workflows/validate-specs.yml`

### Validation

Added automated validation for:

* required repository files
* core YAML specification
* core JSON Schema
* basic example structure
* Five-Phase agent definitions
* generating cycle consistency
* controlling cycle consistency
* routing policy references
* example YAML validity

### Updated

Updated repository documentation to reflect validation support.

### Notes

This release establishes the validation foundation for later protocol extensions.

## [0.1.0] - 2026-05-29

### Added

Initial draft release of the Yin-Yang Five-Phase Reasoning Protocol.

Added the core protocol structure:

* Yin-Yang state model
* Five-Phase reasoning roles
* generating cycle
* controlling cycle
* brake layer
* memory layer
* routing model
* relationship to Multi-Wing architecture
* energy-aware reasoning notes

### Core Specification

Added:

* `spec/five-phase-reasoning-protocol-v0.1.yaml`
* `schemas/five-phase-reasoning.schema.json`

### Examples

Added initial examples:

* `examples/basic-reasoning-cycle.example.yaml`
* `examples/critique-stopping-cycle.example.yaml`
* `examples/memory-return-cycle.example.yaml`

### Documentation

Added initial documentation:

* `docs/architecture-overview.md`
* `docs/yin-yang-state-model.md`
* `docs/five-phase-agent-roles.md`
* `docs/generating-cycle-routing.md`
* `docs/controlling-cycle-brake.md`
* `docs/relationship-to-multi-wing.md`
* `docs/energy-aware-reasoning-notes.md`

### Core Concepts

The initial protocol defines reasoning as a dynamic cycle rather than continuous expansion.

Core architecture:

```text
Yin-Yang = state control
Five Phases = reasoning roles
Generating Cycle = constructive flow
Controlling Cycle = self-regulation
Brake Layer = stopping logic
Memory Layer = retained essence and return
```

### Non-Goals

The initial release does not attempt to:

* replace Transformer architecture
* prove measured energy savings
* define a complete hardware implementation
* claim metaphysical properties of AI
* present Yin-Yang or Five-Phase theory as a scientific law
* automate all reasoning decisions without review
* guarantee truth, safety, or alignment

### Notes

The central principle of the protocol is:

```text
Reasoning should breathe.
```

A reasoning system should know when to expand, when to compress, when to retain, and when to stop.


