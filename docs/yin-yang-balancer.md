# Yin-Yang Balancer

Yin-Yang Balancer is a v0.3.0 extension of the Yin-Yang Five-Phase Reasoning Protocol.

It introduces a dynamic equilibrium layer for regulating reasoning intensity, suppression, silence, critique, integration, and sync/async transition behavior across the Five-Phase reasoning cycle.

## Purpose

The purpose of Yin-Yang Balancer is to prevent reasoning from becoming one-sided.

A reasoning system may over-expand, over-compress, over-criticize, stop too early, or continue too long. Yin-Yang Balancer provides a structural control layer for detecting these tendencies and returning the system toward a stable reasoning flow.

## Non-Goals

Yin-Yang Balancer does not:

- override model constraints
- bypass safety boundaries
- replace model architecture
- claim measured hardware-level energy reduction
- define a complete inference engine

It operates within existing model constraints and safety boundaries.

## Core Idea

The v0.1 protocol defined the basic reasoning cycle:

```text
Wood -> Fire -> Earth -> Metal -> Water -> Wood

The v0.2 extension added dynamic control metrics:

energy_state
suppression_score
stop_confidence

The v0.3 extension adds a balance controller:

Yin-Yang Balancer

Together:

Five Phases = reasoning roles
Dynamic Control Metrics = runtime signals
Yin-Yang Balancer = equilibrium controller
Why Balance Is Needed

Reasoning does not fail only by being wrong.

It can also fail by becoming structurally unbalanced.

Examples:

too much Fire: excessive expansion
too much Metal: excessive critique
too much Water: stagnation or over-silence
too much Earth: over-stabilization
too much Wood: unstable direction shifting

Yin-Yang Balancer detects these tendencies and adjusts routing.

Pivot Phase

Earth is the default pivot phase.

Earth checks:

context fit
coherence
phase conflict
integration pressure
convergence readiness
sync/async suitability

Earth does not simply average all signals. It stabilizes the whole reasoning flow.

Yin and Yang Signals

Yang signals include:

expansion pressure
generation momentum
exploratory reasoning
active phase count
parallel activation
low stop confidence

Yin signals include:

suppression score
stop confidence
uncertainty level
memory settling required
redundancy detected
high routing cost

The balancer does not eliminate either side. It regulates the oscillation.

Phase Adjustments
Fire to Water

Used when expansion becomes excessive.

Fire -> Water

Typical action:

cool down, compress, delay, or retain memory
Metal to Earth

Used when critique becomes excessive.

Metal -> Earth

Typical action:

integrate useful critique and simplify
Water to Wood

Used when silence or memory settling becomes stagnant.

Water -> Wood

Typical action:

restart with minimal direction
Earth to Fire

Used when integration becomes too heavy or premature.

Earth -> Fire

Typical action:

reintroduce light expansion
Sync / Async Bridge

Yin-Yang Balancer also supports sync/async reasoning control.

Synchronous reasoning is preferred when:

the answer can be completed immediately
context drift is low
memory settling is not required
stop confidence is high

Asynchronous reasoning is preferred when:

memory settling is required
delayed critique is useful
context integration needs more space
immediate expansion may reduce clarity
Delayed Critique

Metal critique does not always need to occur immediately.

In some cases, immediate critique may interrupt useful exploration. The v0.3 balancer allows critique to be delayed and returned through Earth after context integration.

Background Memory Return

Water may retain essential patterns and return them to Wood in a later cycle.

This supports:

delayed insight
reduced over-generation
memory-aware recurrence
future reasoning refinement
Safety Boundary

Yin-Yang Balancer is constraint-aware.

It does not override alignment, policy, or model constraints.

Its purpose is to regulate reasoning flow inside existing boundaries.

Core Principle

Reasoning should not remain fixed in expansion or suppression.

It should oscillate within a controlled range, return to balance, and stop when further activation would reduce clarity.


---

## README.md への追記方針

既存 README は `v0.2.0` まで Current structure に入っているので、そこへ以下を追加します。現在 README は v0.2 の `energy_state`、`suppression_score`、`stop_confidence` を説明しているため、v0.3 はその後に置くのが自然です。:contentReference[oaicite:2]{index=2}

```markdown
* Dynamic balance extension: `v0.3.0`

Core Idea 付近にはこれを追加。

With the `v0.3.0` extension, the protocol adds Yin-Yang Balancer:

* dynamic equilibrium control
* oscillation amplitude control
* sync / async phase selection
* delayed critique
* background memory return
* constraint-aware balance adjustment

Repository Structure にはこれを追加。

spec/
├── five-phase-reasoning-protocol-v0.1.yaml
├── dynamic-control-metrics-v0.2.yaml
└── yin-yang-balancer-v0.3.yaml

schemas/
├── five-phase-reasoning.schema.json
├── dynamic-control-metrics.schema.json
└── yin-yang-balancer.schema.json

examples/
├── basic-reasoning-cycle.example.yaml
├── critique-stopping-cycle.example.yaml
├── memory-return-cycle.example.yaml
├── energy-state-control.example.yaml
└── yin-yang-balancer-control.example.yaml

docs/
├── architecture-overview.md
├── yin-yang-state-model.md
├── five-phase-agent-roles.md
├── generating-cycle-routing.md
├── controlling-cycle-brake.md
├── relationship-to-multi-wing.md
├── energy-aware-reasoning-notes.md
└── yin-yang-balancer.md
CHANGELOG.md 追記
## [0.3.0] - 2026-05-30

### Added

* Added Yin-Yang Balancer extension:

  * `spec/yin-yang-balancer-v0.3.yaml`
  * `schemas/yin-yang-balancer.schema.json`
  * `examples/yin-yang-balancer-control.example.yaml`
  * `docs/yin-yang-balancer.md`

### Yin-Yang Balancer Introduced

This release introduces a dynamic equilibrium layer for regulating reasoning intensity, suppression, silence, critique, integration, and sync/async transition behavior across the Five-Phase reasoning cycle.

The balancer operates within existing model constraints and safety boundaries.

It does not override constraints, bypass alignment, or claim hardware-level energy reduction.

### Core Concepts Added

* Yin-Yang Balancer
* Dynamic equilibrium control
* Oscillation amplitude control
* Earth as pivot phase
* Fire-to-Water cooling
* Metal-to-Earth integration
* Water-to-Wood restart
* Earth-to-Fire light expansion
* Sync / async phase selection
* Delayed critique
* Background memory return
* Constraint-aware balance adjustment

### Notes

The v0.3.0 extension builds on v0.2.0 dynamic control metrics.

The v0.2.0 release introduced:

```text
energy_state
suppression_score
stop_confidence

The v0.3.0 release uses these metrics as input signals for balance control.

In simple terms:

v0.1.0 = Five-Phase reasoning skeleton
v0.1.1 = Validation foundation
v0.2.0 = Dynamic control metrics
v0.3.0 = Yin-Yang dynamic balance control

The core principle remains:

Reasoning should breathe.
