from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(**file**).resolve().parents[1]

V01_SPEC_PATH = ROOT / "spec" / "five-phase-reasoning-protocol-v0.1.yaml"
V01_SCHEMA_PATH = ROOT / "schemas" / "five-phase-reasoning.schema.json"

V02_SPEC_PATH = ROOT / "spec" / "dynamic-control-metrics-v0.2.yaml"
V02_SCHEMA_PATH = ROOT / "schemas" / "dynamic-control-metrics.schema.json"
V02_EXAMPLE_PATH = ROOT / "examples" / "energy-state-control.example.yaml"

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
"spec/dynamic-control-metrics-v0.2.yaml",
"schemas/dynamic-control-metrics.schema.json",
"examples/energy-state-control.example.yaml",
]

V01_EXPECTED_EXAMPLES = [
ROOT / "examples" / "basic-reasoning-cycle.example.yaml",
ROOT / "examples" / "critique-stopping-cycle.example.yaml",
ROOT / "examples" / "memory-return-cycle.example.yaml",
]

EXPECTED_PHASES = {"wood", "fire", "earth", "metal", "water"}
EXPECTED_PHASES_WITH_STOP = {"wood", "fire", "earth", "metal", "water", "stop"}

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

EXPECTED_V02_METRICS = {
"energy_state",
"suppression_score",
"stop_confidence",
}

def fail(message: str) -> None:
print(f"ERROR: {message}", file=sys.stderr)
raise SystemExit(1)

def load_yaml(path: Path) -> Any:
if not path.exists():
fail(f"Missing file: {path.relative_to(ROOT)}")

```
try:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)
except yaml.YAMLError as exc:
    fail(f"Invalid YAML in {path.relative_to(ROOT)}: {exc}")
```

def load_json(path: Path) -> Any:
if not path.exists():
fail(f"Missing file: {path.relative_to(ROOT)}")

```
try:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)
except json.JSONDecodeError as exc:
    fail(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
```

def assert_expected_files_exist() -> None:
for relative_path in EXPECTED_FILES:
path = ROOT / relative_path
if not path.exists():
fail(f"Expected file does not exist: {relative_path}")
if path.is_file() and path.stat().st_size == 0:
fail(f"Expected file is empty: {relative_path}")

```
print("OK: expected repository files exist")
```

def validate_against_schema(
data_path: Path,
schema_path: Path,
label: str,
) -> dict[str, Any]:
data = load_yaml(data_path)
schema = load_json(schema_path)

```
validator = Draft202012Validator(schema)
errors = sorted(validator.iter_errors(data), key=lambda error: list(error.path))

if errors:
    print(f"{label} schema validation failed:", file=sys.stderr)
    for error in errors:
        location = ".".join(str(part) for part in error.path) or "<root>"
        print(f"- {location}: {error.message}", file=sys.stderr)
    raise SystemExit(1)

print(f"OK: {label} validates against JSON Schema")
return data
```

def validate_v01_spec_against_schema() -> dict[str, Any]:
return validate_against_schema(
data_path=V01_SPEC_PATH,
schema_path=V01_SCHEMA_PATH,
label="v0.1 protocol spec",
)

def validate_v02_spec_against_schema() -> dict[str, Any]:
return validate_against_schema(
data_path=V02_SPEC_PATH,
schema_path=V02_SCHEMA_PATH,
label="v0.2 dynamic control metrics spec",
)

def validate_v01_generating_cycle(spec: dict[str, Any]) -> None:
generating_cycle = spec.get("generating_cycle", {})
sequence = generating_cycle.get("sequence", [])

```
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

print("OK: v0.1 generating cycle is structurally valid")
```

def validate_v01_controlling_cycle(spec: dict[str, Any]) -> None:
controlling_cycle = spec.get("controlling_cycle", {})
controls = controlling_cycle.get("controls", [])

```
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

print("OK: v0.1 controlling cycle is structurally valid")
```

def validate_v01_routing_policy(spec: dict[str, Any]) -> None:
routing_policy = spec.get("routing_policy", {})

```
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

print("OK: v0.1 routing policy references valid phases")
```

def validate_v01_phase_agents(spec: dict[str, Any]) -> None:
agents = spec.get("five_phase_agents", {})

```
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

print("OK: v0.1 five-phase agent definitions are complete")
```

def validate_v01_examples() -> None:
for example_path in V01_EXPECTED_EXAMPLES:
example = load_yaml(example_path)
relative_path = example_path.relative_to(ROOT)

```
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

print("OK: v0.1 examples are structurally valid")
```

def validate_normalized_number(value: Any, label: str) -> None:
if not isinstance(value, (int, float)):
fail(f"{label} must be a number, got {type(value).**name**}")

```
if value < 0.0 or value > 1.0:
    fail(f"{label} must be between 0.0 and 1.0, got {value}")
```

def validate_v02_metric_definitions(spec: dict[str, Any]) -> None:
metric_definitions = spec.get("metric_definitions", {})

```
missing = EXPECTED_V02_METRICS - set(metric_definitions.keys())
if missing:
    fail(f"Missing v0.2 metric definitions: {sorted(missing)}")

energy_state = metric_definitions.get("energy_state", {})
components = set(energy_state.get("components", []))
required_components = {
    "activation_level",
    "compression_level",
    "routing_cost",
    "active_phase_count",
    "expansion_depth",
    "state_mode",
}

missing_components = required_components - components
if missing_components:
    fail(f"Missing energy_state components: {sorted(missing_components)}")

for metric_name in ["suppression_score", "stop_confidence"]:
    metric = metric_definitions.get(metric_name, {})
    metric_range = metric.get("range", {})
    minimum = metric_range.get("minimum")
    maximum = metric_range.get("maximum")

    if minimum != 0.0 or maximum != 1.0:
        fail(
            f"{metric_name}.range must be 0.0 to 1.0, "
            f"got {minimum} to {maximum}"
        )

print("OK: v0.2 metric definitions are structurally valid")
```

def validate_v02_thresholds(spec: dict[str, Any]) -> None:
thresholds = spec.get("thresholds", {})

```
expected_thresholds = ["low", "medium", "high"]
for threshold_name in expected_thresholds:
    if threshold_name not in thresholds:
        fail(f"Missing v0.2 threshold: {threshold_name}")

    threshold = thresholds[threshold_name]
    minimum = threshold.get("minimum")
    maximum = threshold.get("maximum")

    validate_normalized_number(minimum, f"thresholds.{threshold_name}.minimum")
    validate_normalized_number(maximum, f"thresholds.{threshold_name}.maximum")

    if minimum > maximum:
        fail(
            f"thresholds.{threshold_name}.minimum must not exceed maximum"
        )

print("OK: v0.2 thresholds are structurally valid")
```

def validate_v02_control_decisions(spec: dict[str, Any]) -> None:
decisions = spec.get("control_decisions", [])

```
if not decisions:
    fail("v0.2 control_decisions must not be empty")

for decision in decisions:
    route = decision.get("recommended_route", [])
    for phase in route:
        if phase not in EXPECTED_PHASES_WITH_STOP:
            fail(f"Invalid phase in v0.2 recommended_route: {phase}")

    action = decision.get("recommended_action")
    if not action:
        fail("v0.2 control_decision missing recommended_action")

print("OK: v0.2 control decisions are structurally valid")
```

def validate_v02_runtime_control_object(spec: dict[str, Any]) -> None:
runtime_object = spec.get("runtime_control_object", {})
example = runtime_object.get("example", {})

```
energy_state = example.get("energy_state", {})
validate_normalized_number(
    energy_state.get("activation_level"),
    "runtime_control_object.example.energy_state.activation_level",
)
validate_normalized_number(
    energy_state.get("compression_level"),
    "runtime_control_object.example.energy_state.compression_level",
)
validate_normalized_number(
    energy_state.get("routing_cost"),
    "runtime_control_object.example.energy_state.routing_cost",
)

state_mode = energy_state.get("state_mode")
if state_mode not in {"yang", "yin", "balanced"}:
    fail(
        "runtime_control_object.example.energy_state.state_mode "
        f"must be yang, yin, or balanced, got {state_mode}"
    )

suppression_score = example.get("suppression_score", {})
validate_normalized_number(
    suppression_score.get("value"),
    "runtime_control_object.example.suppression_score.value",
)

stop_confidence = example.get("stop_confidence", {})
validate_normalized_number(
    stop_confidence.get("value"),
    "runtime_control_object.example.stop_confidence.value",
)

next_phase = example.get("next_phase")
if next_phase not in EXPECTED_PHASES_WITH_STOP:
    fail(f"Invalid runtime_control_object.example.next_phase: {next_phase}")

print("OK: v0.2 runtime control object is structurally valid")
```

def validate_v02_example() -> None:
example = load_yaml(V02_EXAMPLE_PATH)
relative_path = V02_EXAMPLE_PATH.relative_to(ROOT)

```
required_keys = [
    "example_id",
    "protocol_ref",
    "extension_ref",
    "version",
    "status",
    "description",
    "input",
    "initial_control_state",
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

if example["extension_ref"] != "dynamic-control-metrics-v0.2":
    fail(
        f"Invalid extension_ref in {relative_path}: "
        f"{example['extension_ref']}"
    )

initial_control_state = example.get("initial_control_state", {})
validate_control_metric_bundle(
    initial_control_state,
    f"{relative_path}.initial_control_state",
)

reasoning_cycle = example.get("reasoning_cycle", [])
if not isinstance(reasoning_cycle, list) or not reasoning_cycle:
    fail(f"reasoning_cycle must be a non-empty list in {relative_path}")

for index, step in enumerate(reasoning_cycle):
    phase = step.get("phase")
    state = step.get("state")

    if phase not in EXPECTED_PHASES:
        fail(f"Invalid phase in {relative_path} step {index}: {phase}")

    if state not in {"yang", "yin", "balanced"}:
        fail(f"Invalid state in {relative_path} step {index}: {state}")

    input_metrics = step.get("input_metrics")
    if input_metrics is not None:
        validate_partial_metric_bundle(
            input_metrics,
            f"{relative_path}.reasoning_cycle[{index}].input_metrics",
        )

expected_metrics = set(
    example.get("validation_notes", {}).get("expected_metrics", [])
)

missing_metrics = EXPECTED_V02_METRICS - expected_metrics
if missing_metrics:
    fail(
        f"Missing expected_metrics in {relative_path}: "
        f"{sorted(missing_metrics)}"
    )

print("OK: v0.2 energy-state example is structurally valid")
```

def validate_control_metric_bundle(bundle: dict[str, Any], label: str) -> None:
for required_key in EXPECTED_V02_METRICS:
if required_key not in bundle:
fail(f"Missing {label}.{required_key}")

```
validate_partial_metric_bundle(bundle, label)
```

def validate_partial_metric_bundle(bundle: dict[str, Any], label: str) -> None:
energy_state = bundle.get("energy_state")
if energy_state is not None:
for key in ["activation_level", "compression_level", "routing_cost"]:
if key in energy_state:
validate_normalized_number(
energy_state[key],
f"{label}.energy_state.{key}",
)

```
    state_mode = energy_state.get("state_mode")
    if state_mode is not None and state_mode not in {"yang", "yin", "balanced"}:
        fail(f"Invalid {label}.energy_state.state_mode: {state_mode}")

suppression_score = bundle.get("suppression_score")
if suppression_score is not None:
    if "value" in suppression_score:
        validate_normalized_number(
            suppression_score["value"],
            f"{label}.suppression_score.value",
        )

    controller = suppression_score.get("controller")
    if controller is not None and controller not in EXPECTED_PHASES:
        fail(f"Invalid {label}.suppression_score.controller: {controller}")

    target = suppression_score.get("target")
    if target is not None and target not in EXPECTED_PHASES:
        fail(f"Invalid {label}.suppression_score.target: {target}")

stop_confidence = bundle.get("stop_confidence")
if stop_confidence is not None:
    if "value" in stop_confidence:
        validate_normalized_number(
            stop_confidence["value"],
            f"{label}.stop_confidence.value",
        )
```

def main() -> None:
assert_expected_files_exist()

```
v01_spec = validate_v01_spec_against_schema()
validate_v01_phase_agents(v01_spec)
validate_v01_generating_cycle(v01_spec)
validate_v01_controlling_cycle(v01_spec)
validate_v01_routing_policy(v01_spec)
validate_v01_examples()

v02_spec = validate_v02_spec_against_schema()
validate_v02_metric_definitions(v02_spec)
validate_v02_thresholds(v02_spec)
validate_v02_control_decisions(v02_spec)
validate_v02_runtime_control_object(v02_spec)
validate_v02_example()

print("All validations passed.")
```

if __name__ == "__main__":
    main()

