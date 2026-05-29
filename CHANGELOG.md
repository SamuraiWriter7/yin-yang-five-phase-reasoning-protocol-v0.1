# Changelog

All notable changes to this project will be documented in this file.

This project follows a simple versioning style during the early draft phase.

## [0.1.1-candidate] - 2026-05-29

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

### Notes

This candidate release prepares the repository for automated validation.

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

