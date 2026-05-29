from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]

SPEC_PATH = ROOT / "spec" / "five-phase-reasoning-protocol-v0.1.yaml"
SCHEMA_PATH = ROOT / "schemas" / "five-phase-reasoning.schema.json"

EXPECTED_FILES = [
    "README.md",
    "spec/five-phase-reasoning-protocol-v0.1.yaml",
    "schemas/five-phase-reasoning.schema.json",
    "examples/basic-reasoning-cycle.example.yaml",
    "examples/critique-stopping-cycle.example.yaml",
    "examples/memory-return-cycle.example.yaml",
    "docs/architecture-overview.md",
    "docs/yin-yang-state-model.md",
    "docs/five-phase-agent-roles.md",
    "docs/generating-cycle-routing.md",
    "docs/controlling-cycle-brake.md",
    "docs/relationship-to-multi-wing.md",
    "docs/energy-aware-reasoning-notes.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "LICENSE",
]

EXPECTED_PHASES = {"wood", "fire", "earth", "metal", "water"}

EXPECTED_GENERATING_SEQUENCE = [
    "wood",
    "fire",
    "earth",
    "metal",
    "water",
    "wood",
]

EXPECTED_CONTROLLING_PAIRS = {
    ("metal", "wood"),
    ("water", "fire"),
    ("wood", "earth"),
    ("fire", "metal"),
    ("earth", "water"),
}

EXPECTED_EXAMPLES = [
    ROOT / "examples" / "basic-reasoning-cycle.example.yaml",
    ROOT / "examples" / "critique-stopping-cycle.example.yaml",
    ROOT / "examples" / "memory-return-cycle.example.yaml",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_yaml(path: Path) -> Any:
    if not path.exists():
        fail(f"Missing file: {path.relative_to(ROOT)}")

    try:
        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as exc:
        fail(f"Invalid YAML in {path.relative_to(ROOT)}: {exc}")


def load_json(path: Path) -> Any:
    if not path.exists():
        fail(f"Missing file: {path.relative_to(ROOT)}")

    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")


def assert_expected_files_exist() -> None:
    for relative_path in EXPECTED_FILES:
        path = ROOT / relative_path
        if not path.exists():
            fail(f"Expected file does not exist: {relative_path}")
        if path.is_file() and path.stat().st_size == 0:
            fail(f"Expected file is empty: {relative_path}")

    print("OK: expected repository files exist")


def validate_spec_against_schema() -> dict[str, Any]:
    spec = load_yaml(SPEC_PATH)
    schema = load_json(SCHEMA_PATH)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(spec), key=lambda error: list(error.path))

    if errors:
        print("Schema validation failed:", file=sys.stderr)
        for error in errors:
            location = ".".join(str(part) for part in error.path) or "<root>"
            print(f"- {location}: {error.message}", file=sys.stderr)
        raise SystemExit(1)

    print("OK: spec validates against JSON Schema")
    return spec


def validate_generating_cycle(spec: dict[str, Any]) -> None:
    generating_cycle = spec.get("generating_cycle", {})
    sequence = generating_cycle.get("sequence", [])

    if sequence != EXPECTED_GENERATING_SEQUENCE:
        fail(
            "generating_cycle.sequence must be "
            f"{EXPECTED_GENERATING_SEQUENCE}, got {sequence}"
        )

    transitions = generating_cycle.get("transitions", [])
    for transition in transitions:
        from_phase = transition.get("from")
        to_phase = transition.get("to")

        if from_phase not in EXPECTED_PHASES:
            fail(f"Invalid generating transition source: {from_phase}")
        if to_phase not in EXPECTED_PHASES:
            fail(f"Invalid generating transition target: {to_phase}")

    print("OK: generating cycle is structurally valid")


def validate_controlling_cycle(spec: dict[str, Any]) -> None:
    controlling_cycle = spec.get("controlling_cycle", {})
    controls = controlling_cycle.get("controls", [])

    observed_pairs = {
        (control.get("controller"), control.get("target"))
        for control in controls
    }

    missing = EXPECTED_CONTROLLING_PAIRS - observed_pairs
    if missing:
        fail(f"Missing controlling-cycle pairs: {sorted(missing)}")

    for controller, target in observed_pairs:
        if controller not in EXPECTED_PHASES:
            fail(f"Invalid controlling-cycle controller: {controller}")
        if target not in EXPECTED_PHASES:
            fail(f"Invalid controlling-cycle target: {target}")

    print("OK: controlling cycle is structurally valid")


def validate_routing_policy(spec: dict[str, Any]) -> None:
    routing_policy = spec.get("routing_policy", {})

    default_route = routing_policy.get("default_route", [])
    for phase in default_route:
        if phase not in EXPECTED_PHASES:
            fail(f"Invalid phase in routing_policy.default_route: {phase}")

    conditional_routes = routing_policy.get("conditional_routes", [])
    for route_entry in conditional_routes:
        route = route_entry.get("route", [])
        for phase in route:
            if phase not in EXPECTED_PHASES:
                fail(
                    "Invalid phase in routing_policy.conditional_routes: "
                    f"{phase}"
                )

    print("OK: routing policy references valid phases")


def validate_phase_agents(spec: dict[str, Any]) -> None:
    agents = spec.get("five_phase_agents", {})

    for phase in EXPECTED_PHASES:
        if phase not in agents:
            fail(f"Missing five-phase agent definition: {phase}")

        agent = agents[phase]
        required_keys = [
            "label",
            "role",
            "primary_function",
            "yin_yang_bias",
            "description",
            "asks",
            "operations",
            "outputs",
            "failure_modes",
        ]

        for key in required_keys:
            if key not in agent:
                fail(f"Missing key in five_phase_agents.{phase}: {key}")

    print("OK: five-phase agent definitions are complete")


def validate_examples() -> None:
    for example_path in EXPECTED_EXAMPLES:
        example = load_yaml(example_path)
        relative_path = example_path.relative_to(ROOT)

        required_keys = [
            "example_id",
            "protocol_ref",
            "version",
            "status",
            "description",
            "input",
            "initial_state",
            "reasoning_cycle",
            "final_output",
            "memory_trace",
            "validation_notes",
        ]

        for key in required_keys:
            if key not in example:
                fail(f"Missing key in {relative_path}: {key}")

        if example["protocol_ref"] != "five-phase-reasoning-protocol-v0.1":
            fail(
                f"Invalid protocol_ref in {relative_path}: "
                f"{example['protocol_ref']}"
            )

        reasoning_cycle = example.get("reasoning_cycle", [])
        if not isinstance(reasoning_cycle, list) or not reasoning_cycle:
            fail(f"reasoning_cycle must be a non-empty list in {relative_path}")

        phases = [step.get("phase") for step in reasoning_cycle]
        for phase in phases:
            if phase not in EXPECTED_PHASES:
                fail(f"Invalid phase in {relative_path}: {phase}")

        expected_order = (
            example.get("validation_notes", {})
            .get("expected_cycle_order", [])
        )

        if expected_order and phases != expected_order:
            fail(
                f"Cycle order mismatch in {relative_path}: "
                f"expected {expected_order}, got {phases}"
            )

    print("OK: examples are structurally valid")


def main() -> None:
    assert_expected_files_exist()

    spec = validate_spec_against_schema()

    validate_phase_agents(spec)
    validate_generating_cycle(spec)
    validate_controlling_cycle(spec)
    validate_routing_policy(spec)
    validate_examples()

    print("All validations passed.")


if __name__ == "__main__":
    main()
