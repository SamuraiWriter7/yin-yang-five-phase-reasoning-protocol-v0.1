# Changelog

All notable changes to this project will be documented in this file.

This project follows a simple versioning style during the early draft phase.

## [0.2.0] - 2026-05-29

### Added

* Added Dynamic Control Metrics extension:

  * `spec/dynamic-control-metrics-v0.2.yaml`
  * `schemas/dynamic-control-metrics.schema.json`
  * `examples/energy-state-control.example.yaml`

* Extended validation script to support v0.2 dynamic control metrics:

  * `scripts/validate_specs.py`

* Updated `README.md` to reflect the v0.2 dynamic control metrics extension.

### Dynamic Control Metrics Introduced

This release introduces three normalized control-layer metrics:

* `energy_state`
* `suppression_score`
* `stop_confidence`

These metrics are designed to support more precise reasoning control.

### energy_state

`energy_state` represents the current activation profile of the reasoning process.

It may include:

* `activation_level`
* `compression_level`
* `routing_cost`
* `active_phase_count`
* `expansion_depth`
* `state_mode`

This metric does not represent hardware-level electrical power consumption.
It represents control-layer reasoning activation.

### suppression_score

`suppression_score` represents how strongly the system should suppress, prune, compress, reroute, or stop part of the current reasoning process.

It may be triggered by:

* excessive branching
* redundancy
* reasoning overheat
* context drift
* low confidence
* memory overload

A high `suppression_score` does not always mean final stopping.
It may indicate pruning, compression, rerouting, or memory filtering.

### stop_confidence

`stop_confidence` represents confidence that the current reasoning cycle is sufficient and should stop after any required memory retention.

High `stop_confidence` supports routing such as:

```text
Metal -> Water -> Stop
```

Low `stop_confidence` may indicate that the system should continue through Fire or Earth before final stopping.

### Validation Coverage Added

The validation script now checks:

* v0.2 dynamic control metrics specification exists
* v0.2 JSON Schema exists
* v0.2 example file exists
* `spec/dynamic-control-metrics-v0.2.yaml` validates against `schemas/dynamic-control-metrics.schema.json`
* `energy_state`, `suppression_score`, and `stop_confidence` are defined
* metric values are normalized from `0.0` to `1.0`
* threshold definitions are structurally valid
* control decisions reference valid phases
* runtime control object is structurally valid
* `examples/energy-state-control.example.yaml` is structurally valid

### Core Concepts Added

* Dynamic control metrics
* Normalized activation profile
* Suppression scoring
* Stop confidence scoring
* Metric-based routing
* Metric-guided braking
* Control-layer runtime dashboard
* Energy-aware reasoning indicators
* Runtime suppression and stopping logic

### Notes

This release extends the protocol without breaking the v0.1 core structure.

The v0.1 protocol defined the reasoning skeleton:

```text
Yin-Yang = state control
Five Phases = reasoning roles
Generating Cycle = constructive flow
Controlling Cycle = self-regulation
Brake Layer = stopping logic
Memory Layer = retained essence and return
```

The v0.2 extension adds a runtime control dashboard:

```text
energy_state = activation profile
suppression_score = braking pressure
stop_confidence = stopping readiness
```

This release does not claim measured hardware-level energy reduction.

It defines dynamic control metrics for reasoning behavior at the protocol layer.

The core principle remains:

```text
Reasoning should breathe.
```

## [0.1.1] - 2026-05-29

### Added

* Added GitHub Actions validation workflow:

  * `.github/workflows/validate-specs.yml`
* Added validation script:

  * `scripts/validate_specs.py`

### Validation Coverage

The validation workflow checks:

* Expected repository files exist
* `spec/five-phase-reasoning-protocol-v0.1.yaml` validates against `schemas/five-phase-reasoning.schema.json`
* Five-Phase agent definitions are complete
* Generating cycle references valid phases
* Controlling cycle includes expected control pairs
* Routing policy references valid phases
* Example YAML files are structurally valid
* Example reasoning cycles match their declared expected cycle order

### Fixed

* Removed Markdown code fences from machine-readable files where needed.
* Fixed JSON Schema formatting so `schemas/five-phase-reasoning.schema.json` can be parsed as valid JSON.
* Fixed YAML formatting issues in example files caused by copied Markdown code fences.
* Fixed validation script formatting issues caused by Markdown conversion of Python dunder variables and indentation.

### Notes

This release added automated validation for the repository.

No protocol-breaking changes were introduced.

The core protocol remains:

```text
Reasoning should breathe.
```

This version strengthens repository reliability by ensuring that the specification, schema, examples, and required files can be checked automatically through GitHub Actions.

## [0.1.0] - 2026-05-29

### Added

* Initial release of the Yin-Yang Five-Phase Reasoning Protocol v0.1.
* Added `README.md` with the core concept, purpose, repository structure, and start-here guide.
* Added `spec/five-phase-reasoning-protocol-v0.1.yaml`.
* Added `schemas/five-phase-reasoning.schema.json`.
* Added basic example files:

  * `examples/basic-reasoning-cycle.example.yaml`
  * `examples/critique-stopping-cycle.example.yaml`
  * `examples/memory-return-cycle.example.yaml`
* Added documentation files:

  * `docs/architecture-overview.md`
  * `docs/yin-yang-state-model.md`
  * `docs/five-phase-agent-roles.md`
  * `docs/generating-cycle-routing.md`
  * `docs/controlling-cycle-brake.md`
  * `docs/relationship-to-multi-wing.md`
  * `docs/energy-aware-reasoning-notes.md`
* Added `CHANGELOG.md`.
* Added `CITATION.cff`.
* Added `LICENSE`.

### Core Concepts Introduced

* Yin-Yang state transition model
* Five-Phase reasoning roles
* Generating cycle routing
* Controlling cycle brake behavior
* Energy-aware reasoning control
* Water-to-Wood memory return
* Relationship to Multi-Wing architecture
* Critique-driven compression
* Selective memory retention
* Stop-as-reasoning principle

### Notes

This release defines the protocol as a structural reasoning-control model.

It does not claim measured hardware-level energy reduction, replacement of Transformer architectures, or a complete inference engine implementation.

The core principle is:

```text
Reasoning should breathe.
```

