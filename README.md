# Yin-Yang Five-Phase Reasoning Protocol

A structural protocol for dynamic, energy-aware, multi-agent reasoning based on Yin-Yang state transitions, Five-Phase routing, and dynamic control metrics.

## Status

Draft specification.

Current structure:

* Core protocol: `v0.1`
* Validation release: `v0.1.1`
* Dynamic control metrics extension: `v0.2.0`

This repository defines an early conceptual and structural protocol.
It is not a benchmark result, hardware implementation, or claim of immediate energy reduction.

The purpose of this protocol is to describe a reasoning architecture that may support:

* selective inference
* role-distributed reasoning
* self-regulating generation
* critique-driven compression
* memory-aware recurrence
* dynamic stopping decisions
* reduction of unnecessary reasoning expansion
* prevention of runaway generation
* control-layer energy awareness

## Core Idea

Modern AI inference often behaves as continuous activation:

```text
generate -> expand -> attend -> continue
```

This protocol proposes a different model:

```text
reasoning = phase transition + control metrics
```

Reasoning should not always expand.
Reasoning should breathe.

The system alternates between two primary states:

* **Yang**: activation, exploration, generation, expansion
* **Yin**: compression, silence, memory, stopping

It also uses a **Balanced** state for context integration.

With the `v0.2.0` extension, the protocol adds normalized control metrics:

* `energy_state`
* `suppression_score`
* `stop_confidence`

These metrics help a reasoning system estimate:

* how active the current reasoning path is
* whether reasoning should be suppressed, pruned, or rerouted
* whether the answer is sufficient enough to stop

## Why This Matters

Large-scale AI systems often face several structural limits:

1. **Energy intensity**
   Continuous activation and wide-context computation can increase computational cost.

2. **Reasoning rigidity**
   A single model or fixed pipeline may continue generating even when compression, critique, or stopping would be more appropriate.

3. **Weak stopping behavior**
   Many systems can generate but do not have an explicit structural model for deciding when enough reasoning has occurred.

4. **Over-expansion**
   A system may continue branching, elaborating, or reviewing beyond the useful scope of the task.

The Yin-Yang Five-Phase Reasoning Protocol addresses these limits at the architectural level by introducing:

* state transitions
* agent role separation
* selective routing
* self-stopping logic
* memory return cycles
* critique-based pruning
* normalized dynamic control metrics

This protocol does not claim that philosophy directly reduces energy consumption.
Rather, it uses Yin-Yang and Five-Phase structures as an architectural model for controlling reasoning flow.

## Minimal Definition

Yin-Yang Five-Phase Reasoning Protocol is a dynamic reasoning architecture that replaces continuous model activation with phase-based, role-distributed, self-regulating inference.

## Short Definition

Reasoning should breathe.

It should expand when expansion is needed.
It should compress when compression is wiser.
It should stop when stopping is the highest form of intelligence.
And it should use control signals to decide when to move, prune, retain, or stop.

## Yin-Yang State Model

The protocol defines reasoning as an oscillation between Yang activation and Yin restraint.

### Yang

Yang represents activation.

In reasoning systems, Yang corresponds to:

* hypothesis generation
* token expansion
* broad attention
* exploration
* creative divergence
* active computation

Yang is necessary for discovery and expression.

However, uncontrolled Yang may lead to:

* excessive verbosity
* unnecessary branching
* hallucination risk
* redundant computation
* runaway generation

### Yin

Yin represents compression and restraint.

In reasoning systems, Yin corresponds to:

* pruning
* summarization
* local attention
* stopping
* memory consolidation
* reduced activation

Yin is necessary for stability.

Without Yin, reasoning cannot converge.

### Balanced State

The protocol also allows a balanced state.

Balanced state is used when reasoning requires integration rather than pure expansion or pure compression.

This is especially important for the Earth phase, where the system checks context, coherence, and alignment with the user’s actual request.

## Five-Phase Agent Roles

This protocol defines five functional reasoning agents.

These agents do not need to be separate models.
They may be implemented as modules, prompts, policies, routing states, specialized agents, or internal reasoning roles.

```text
Wood  = direction
Fire  = expansion
Earth = integration
Metal = critique
Water = memory
```

## Wood: Direction Agent

Wood represents the beginning of direction.

Primary functions:

* detect the core question
* form the initial hypothesis
* identify possible reasoning paths
* sense the direction of inquiry

Wood asks:

```text
What is trying to emerge?
```

## Fire: Expansion Agent

Fire represents active development.

Primary functions:

* expand the hypothesis
* generate explanation
* produce code, text, or structured output
* explore implications
* develop logical paths

Fire asks:

```text
How can this be expressed or developed?
```

## Earth: Context Agent

Earth represents integration.

Primary functions:

* align reasoning with context
* check coherence
* absorb contradiction
* connect local reasoning with broader knowledge
* stabilize meaning

Earth asks:

```text
Does this fit the whole context?
```

## Metal: Critique Agent

Metal represents pruning and refinement.

Primary functions:

* remove noise
* reduce redundancy
* detect weak claims
* compress output
* decide whether to stop
* enforce precision

Metal asks:

```text
What should be cut, corrected, or stopped?
```

## Water: Memory Agent

Water represents retention and return.

Primary functions:

* store essential patterns
* extract reusable lessons
* preserve minimal traces
* support future reasoning cycles
* return refined knowledge to Wood

Water asks:

```text
What should remain after the reasoning ends?
```

## Generating Cycle

The generating cycle describes constructive reasoning flow.

```text
Wood -> Fire -> Earth -> Metal -> Water -> Wood
```

Meaning:

1. Wood initiates direction.
2. Fire expands the idea.
3. Earth integrates the result.
4. Metal prunes and refines it.
5. Water stores the essence.
6. The next Wood cycle begins from a more refined ground.

This cycle enables reasoning to grow without becoming uncontrolled.

## Controlling Cycle

The controlling cycle describes self-regulation.

```text
Metal controls Wood
Water controls Fire
Wood controls Earth
Fire controls Metal
Earth controls Water
```

In reasoning terms:

* Metal stops excessive intuition.
* Water cools excessive expansion.
* Wood redirects stagnant context.
* Fire challenges excessive pruning.
* Earth stabilizes excessive memory accumulation.

The controlling cycle prevents reasoning from becoming one-sided.

## Dynamic Control Metrics v0.2.0

The `v0.2.0` extension adds normalized dynamic control metrics to the protocol.

These metrics are defined in:

```text
spec/dynamic-control-metrics-v0.2.yaml
schemas/dynamic-control-metrics.schema.json
examples/energy-state-control.example.yaml
```

The purpose of this extension is to make reasoning control more explicit and measurable at the protocol layer.

It introduces:

```text
energy_state
suppression_score
stop_confidence
```

These are control-layer indicators, not direct hardware measurements.

## energy_state

`energy_state` represents the current activation profile of the reasoning process.

It may include:

* `activation_level`
* `compression_level`
* `routing_cost`
* `active_phase_count`
* `expansion_depth`
* `state_mode`

Example:

```yaml
energy_state:
  activation_level: 0.76
  compression_level: 0.22
  routing_cost: 0.61
  active_phase_count: 3
  expansion_depth: 4
  state_mode: yang
```

Interpretation:

* High activation may be appropriate for difficult tasks.
* Low activation may be appropriate for concise or completed tasks.
* High routing cost may indicate unnecessary complexity.
* High compression may indicate strong Yin behavior.

`energy_state` does not measure electrical power directly.

It represents control-layer activation intensity.

## suppression_score

`suppression_score` represents how strongly the system should suppress, prune, compress, reroute, or stop part of the current reasoning process.

Example:

```yaml
suppression_score:
  value: 0.82
  triggered_by: excessive_branching_detected
  controller: water
  target: fire
```

A high `suppression_score` may indicate:

* excessive branching
* repeated generation
* reasoning overheat
* context drift
* weak claims
* memory overload

A high suppression score does not always mean final stopping.
It may mean pruning, rerouting, compression, or memory filtering.

## stop_confidence

`stop_confidence` represents confidence that the current reasoning cycle is sufficient and should stop after any required memory retention.

Example:

```yaml
stop_confidence:
  value: 0.88
  evidence:
    - "The answer is sufficient."
    - "Further expansion would reduce clarity."
  decision: stop_after_memory_retention
```

High `stop_confidence` supports routing such as:

```text
Metal -> Water -> Stop
```

Low `stop_confidence` may indicate that the system should continue through Fire or Earth before final stopping.

## Metric Thresholds

The `v0.2.0` extension uses a normalized range:

```text
0.0 -> 1.0
```

Suggested interpretation:

| Range       | Meaning       |
| ----------- | ------------- |
| 0.00 - 0.30 | Low signal    |
| 0.31 - 0.70 | Medium signal |
| 0.71 - 1.00 | High signal   |

These thresholds are not universal laws.

They are initial protocol-level defaults for control decisions.

## Metric-Based Routing

The metrics may guide routing decisions.

### High suppression, low stop confidence

Meaning:

```text
The current path is excessive, but the answer is not complete.
```

Recommended route:

```text
Earth -> Metal -> Fire
```

Typical action:

```text
Prune branch, then restore minimal needed detail.
```

### High suppression, high stop confidence

Meaning:

```text
Further reasoning is likely unnecessary.
```

Recommended route:

```text
Metal -> Water -> Stop
```

Typical action:

```text
Compress, retain essence, and stop.
```

### Low suppression, low stop confidence

Meaning:

```text
The reasoning is not excessive, but the answer is not complete.
```

Recommended route:

```text
Fire -> Earth
```

Typical action:

```text
Continue expansion with context checking.
```

### Low suppression, high stop confidence

Meaning:

```text
The answer is sufficient and does not require strong pruning.
```

Recommended route:

```text
Water -> Stop
```

Typical action:

```text
Retain minimal trace and stop.
```

## Protocol Layers

This protocol can be understood through six layers.

### Layer 1: State Layer

Defines whether the system is in a Yang, Yin, or Balanced state.

Example:

```yaml
state:
  mode: yang
  function: expansion
```

or:

```yaml
state:
  mode: yin
  function: compression
```

### Layer 2: Phase Layer

Defines which Five-Phase agent is currently active.

Example:

```yaml
phase:
  active_agent: metal
  role: critique
```

### Layer 3: Routing Layer

Defines the next transition.

Example:

```yaml
routing:
  from: fire
  to: earth
  reason: context_integration_required
```

### Layer 4: Brake Layer

Defines when reasoning should slow, compress, reroute, or stop.

Example:

```yaml
brake:
  triggered_by: redundancy_detected
  action: compress_output
```

### Layer 5: Memory Layer

Defines what should be retained after the reasoning cycle.

Example:

```yaml
memory:
  retain:
    - core_claim
    - unresolved_question
    - next_action
```

### Layer 6: Dynamic Control Metrics Layer

Defines runtime control signals for activation, suppression, and stopping.

Example:

```yaml
dynamic_control:
  energy_state:
    activation_level: 0.52
    compression_level: 0.61
    routing_cost: 0.38
    active_phase_count: 2
    expansion_depth: 2
    state_mode: yin

  suppression_score:
    value: 0.44
    triggered_by: scope_reduced
    controller: metal
    target: fire

  stop_confidence:
    value: 0.68
    evidence:
      - "The scope has been narrowed."
      - "The answer still needs a concise comparison."
    decision: compress_then_continue
```

## Example Reasoning Cycle

```yaml
reasoning_cycle:
  question: "How should this protocol be introduced?"

  wood:
    function: "detect core direction"
    output: "Introduce it as an energy-aware reasoning protocol."

  fire:
    function: "expand explanation"
    output: "Explain Yin-Yang as state transition and Five-Phase as agent routing."

  earth:
    function: "context integration"
    output: "Connect the protocol to Multi-Wing architecture and AI inference control."

  metal:
    function: "critique and compression"
    output: "Avoid unsupported claims about actual energy reduction."

  water:
    function: "memory and return"
    output: "Retain the principle: reasoning should breathe, not endlessly expand."
```

## Example Dynamic Control Cycle

```yaml
dynamic_control_cycle:
  input:
    question: "Explain all possible implications of this protocol."

  initial_metrics:
    energy_state:
      activation_level: 0.84
      compression_level: 0.10
      routing_cost: 0.72
      active_phase_count: 4
      expansion_depth: 5
      state_mode: yang

    suppression_score:
      value: 0.78
      triggered_by: excessive_branching_detected
      controller: water
      target: fire

    stop_confidence:
      value: 0.32
      decision: continue_after_context_check

  route:
    - wood
    - earth
    - metal
    - fire
    - earth
    - metal
    - water
    - stop

  final_metrics:
    energy_state:
      activation_level: 0.39
      compression_level: 0.72
      routing_cost: 0.24
      active_phase_count: 2
      expansion_depth: 1
      state_mode: yin

    suppression_score:
      value: 0.31
      triggered_by: residual_redundancy
      controller: metal
      target: fire

    stop_confidence:
      value: 0.88
      decision: stop_after_memory_retention
```

## Relationship to Multi-Wing Architecture

This protocol is designed to complement Multi-Wing reasoning systems.

Multi-Wing defines distributed intelligence through multiple reasoning wings or agents.

The Yin-Yang Five-Phase Reasoning Protocol provides a deeper control model for how those wings should activate, interact, restrain, and return information.

In simple terms:

```text
Multi-Wing = distributed reasoning architecture
Yin-Yang Five-Phase = dynamic reasoning control protocol
Dynamic Control Metrics = runtime control dashboard
```

Multi-Wing answers:

```text
Which wing should reason?
```

This protocol answers:

```text
When should reasoning expand, compress, stop, or return?
```

The dynamic control metrics answer:

```text
How strongly should the system activate, suppress, or stop?
```

Together, they form a more complete architecture:

```text
Distributed intelligence + dynamic control + runtime metrics
```

## Energy-Aware Reasoning

This protocol does not claim measured hardware-level energy reduction.

Instead, it defines energy awareness as a reasoning-control principle:

```text
Reduce unnecessary reasoning activation.
Route only what is needed.
Stop when the answer is sufficient.
Retain only what improves future cycles.
```

Energy awareness begins at the control layer.

It may reduce unnecessary reasoning activity by:

* avoiding needless expansion
* stopping when sufficient
* pruning weak branches
* limiting redundant generation
* retaining only useful memory
* routing to the smallest sufficient reasoning path
* using `energy_state`, `suppression_score`, and `stop_confidence` to guide control decisions

This should be understood as an architectural direction, not a measured performance claim.

## Repository Structure

```text
yin-yang-five-phase-reasoning-protocol-v0.1/
├── README.md
├── spec/
│   ├── five-phase-reasoning-protocol-v0.1.yaml
│   └── dynamic-control-metrics-v0.2.yaml
├── schemas/
│   ├── five-phase-reasoning.schema.json
│   └── dynamic-control-metrics.schema.json
├── examples/
│   ├── basic-reasoning-cycle.example.yaml
│   ├── critique-stopping-cycle.example.yaml
│   ├── memory-return-cycle.example.yaml
│   └── energy-state-control.example.yaml
├── docs/
│   ├── architecture-overview.md
│   ├── yin-yang-state-model.md
│   ├── five-phase-agent-roles.md
│   ├── generating-cycle-routing.md
│   ├── controlling-cycle-brake.md
│   ├── relationship-to-multi-wing.md
│   └── energy-aware-reasoning-notes.md
├── scripts/
│   └── validate_specs.py
├── .github/
│   └── workflows/
│       └── validate-specs.yml
├── CHANGELOG.md
├── CITATION.cff
└── LICENSE
```

## Key Documents

### Core Specification

* `spec/five-phase-reasoning-protocol-v0.1.yaml`
  Machine-readable draft specification for the core protocol.

* `schemas/five-phase-reasoning.schema.json`
  JSON Schema for validating the core protocol specification.

### Dynamic Control Metrics v0.2.0

* `spec/dynamic-control-metrics-v0.2.yaml`
  Extension specification defining `energy_state`, `suppression_score`, and `stop_confidence`.

* `schemas/dynamic-control-metrics.schema.json`
  JSON Schema for validating the dynamic control metrics extension.

* `examples/energy-state-control.example.yaml`
  Demonstrates metric-guided routing, suppression, compression, and stopping behavior.

### Examples

* `examples/basic-reasoning-cycle.example.yaml`
  Demonstrates a standard Wood -> Fire -> Earth -> Metal -> Water reasoning cycle.

* `examples/critique-stopping-cycle.example.yaml`
  Demonstrates how Metal and Water prevent over-expansion and stop runaway reasoning.

* `examples/memory-return-cycle.example.yaml`
  Demonstrates how Water returns selected memory to Wood as a new inquiry vector.

* `examples/energy-state-control.example.yaml`
  Demonstrates how v0.2 dynamic control metrics guide routing and stopping.

### Architecture Notes

* `docs/architecture-overview.md`
  Explains the full architecture and how the protocol layers fit together.

* `docs/yin-yang-state-model.md`
  Defines Yin, Yang, and Balanced states as reasoning-state control modes.

* `docs/five-phase-agent-roles.md`
  Defines Wood, Fire, Earth, Metal, and Water as functional reasoning roles.

* `docs/generating-cycle-routing.md`
  Defines the constructive routing cycle.

* `docs/controlling-cycle-brake.md`
  Defines brake behavior, self-regulation, and stopping conditions.

* `docs/relationship-to-multi-wing.md`
  Explains how this protocol connects to Multi-Wing architecture.

* `docs/energy-aware-reasoning-notes.md`
  Explains energy-aware reasoning as a control-layer efficiency model.

### Validation

* `scripts/validate_specs.py`
  Validates core specification files, v0.2 dynamic control metrics, examples, phase consistency, routing consistency, and metric ranges.

* `.github/workflows/validate-specs.yml`
  GitHub Actions workflow for automated validation.

## Start Here

Recommended reading order:

1. `README.md`
2. `docs/architecture-overview.md`
3. `docs/yin-yang-state-model.md`
4. `docs/five-phase-agent-roles.md`
5. `docs/generating-cycle-routing.md`
6. `docs/controlling-cycle-brake.md`
7. `docs/relationship-to-multi-wing.md`
8. `docs/energy-aware-reasoning-notes.md`
9. `spec/five-phase-reasoning-protocol-v0.1.yaml`
10. `schemas/five-phase-reasoning.schema.json`
11. `examples/basic-reasoning-cycle.example.yaml`
12. `examples/critique-stopping-cycle.example.yaml`
13. `examples/memory-return-cycle.example.yaml`
14. `spec/dynamic-control-metrics-v0.2.yaml`
15. `schemas/dynamic-control-metrics.schema.json`
16. `examples/energy-state-control.example.yaml`
17. `scripts/validate_specs.py`

## Validation

This repository includes automated validation.

The validation checks:

* expected repository files exist
* the core YAML specification validates against the JSON Schema
* the v0.2 dynamic control metrics specification validates against its JSON Schema
* Five-Phase agent definitions are complete
* generating cycle references valid phases
* controlling cycle includes expected control pairs
* routing policy references valid phases
* example YAML files are structurally valid
* example reasoning cycles match their declared expected cycle order
* dynamic control metrics use normalized values from `0.0` to `1.0`
* runtime control objects are structurally valid

Run locally:

```bash
python scripts/validate_specs.py
```

GitHub Actions runs the same validation automatically.

## Implementation Possibilities

This protocol may be implemented in several ways.

### Prompt-Level Implementation

A single model can simulate the five phases through instruction design.

Example:

```text
1. Wood: identify the core question.
2. Fire: expand only what is needed.
3. Earth: check context and coherence.
4. Metal: remove excess and correct overclaims.
5. Water: retain the essential result and stop.
```

With `v0.2.0`, the assistant may also estimate:

```text
energy_state
suppression_score
stop_confidence
```

This is suitable for GPT-style assistants.

### Agent-Level Implementation

Each phase can be implemented as a separate agent.

Example:

```text
Wood Agent  -> direction detection
Fire Agent  -> generation
Earth Agent -> context verification
Metal Agent -> critique and compression
Water Agent -> memory and return
```

An orchestrator routes tasks between agents.

This is suitable for Multi-Wing systems.

### Policy-Level Implementation

The phases and metrics can be implemented as policies inside a larger reasoning system.

Example:

```yaml
policies:
  direction_policy:
    phase: wood
    trigger: new_question_received
    action: detect_core_direction

  expansion_policy:
    phase: fire
    trigger: explanation_required
    action: expand_selected_direction

  context_policy:
    phase: earth
    trigger: coherence_check_required
    action: align_with_context

  critique_policy:
    phase: metal
    trigger: redundancy_detected
    action: compress_output

  memory_policy:
    phase: water
    trigger: reasoning_complete
    action: retain_essence

  dynamic_control_policy:
    metrics:
      - energy_state
      - suppression_score
      - stop_confidence
    action: select_smallest_sufficient_route
```

### GPT-Level Implementation

A lightweight GPT-style implementation may emphasize:

* concise answers
* stopping when sufficient
* pruning weak branches
* avoiding unnecessary expansion
* retaining only the next useful action
* estimating when suppression or stopping is appropriate

A practical implementation may be called:

```text
省エネ丸
Energy-Aware Reasoning Assistant
```

This assistant would not reduce GPU power directly.
It would reduce unnecessary reasoning behavior at the interaction and control level.

## Design Principles

## 1. Reasoning Should Not Always Expand

More output does not always mean better reasoning.

A mature reasoning system must know when to stop.

## 2. Silence Is Part of Intelligence

Stopping, waiting, compressing, and refusing unnecessary expansion are valid reasoning operations.

## 3. Critique Must Be Structural

Critique should not be an afterthought.
It should be built into the reasoning cycle.

## 4. Memory Should Be Selective

Not everything should be retained.
Memory should preserve essence, not noise.

## 5. Energy Awareness Begins With Routing

Energy-aware reasoning begins by reducing unnecessary activation, unnecessary branching, and unnecessary context expansion.

## 6. Use the Smallest Sufficient Route

Not every task needs every phase.

A simple task may use:

```text
Wood -> Metal -> Water
```

A complex task may use:

```text
Wood -> Fire -> Earth -> Metal -> Water
```

A refinement task may use:

```text
Water -> Wood -> Fire -> Earth -> Metal -> Water
```

## 7. Metrics Guide Control, But Do Not Replace Judgment

`energy_state`, `suppression_score`, and `stop_confidence` are control-layer indicators.

They should guide routing and stopping decisions, but they do not guarantee correctness, safety, or truth by themselves.

## Non-Goals

This protocol does not attempt to:

* replace Transformer architecture directly
* prove measured energy savings
* define a complete hardware implementation
* claim metaphysical properties of AI
* present Yin-Yang or Five-Phase theory as a scientific law
* automate all reasoning decisions without review
* guarantee truth, safety, or alignment
* require every reasoning task to pass through every phase
* claim that `energy_state` is a hardware-level power measurement

This is a structural protocol, not a completed inference engine.

## Future Work

Planned extensions may include:

* semantic validation rules
* additional examples for Multi-Wing routing
* stopping-condition test vectors
* prompt-level implementation profile
* agent-level implementation profile
* relationship to trace and memory systems
* neuromorphic implementation notes
* routing policy examples
* self-stopping condition models
* sync / async reasoning control
* delayed critique and background memory return
* convergence window models

## Citation

If you use this specification, please cite:

```text
Yin-Yang Five-Phase Reasoning Protocol
SamuraiWriter7
2026
```

See `CITATION.cff` for citation metadata.

## License

This project is licensed under the MIT License.
See `LICENSE` for details.

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
Dynamic Control Metrics = runtime control dashboard
```

The central principle is simple:

```text
Reasoning should breathe.
```

A reasoning system should know when to expand.
It should know when to compress.
It should know when to stop.
And with `v0.2.0`, it should also begin to measure how strongly it should activate, suppress, and conclude.

Reasoning should not merely continue.

It should move with timing, restraint, memory, and return.

