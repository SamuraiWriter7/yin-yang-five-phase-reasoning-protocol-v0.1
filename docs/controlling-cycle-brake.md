# Controlling Cycle Brake

## Purpose

This document defines the controlling cycle and brake behavior used in the Yin-Yang Five-Phase Reasoning Protocol v0.1.

The generating cycle defines how reasoning grows.

```text
Wood -> Fire -> Earth -> Metal -> Water -> Wood
```

The controlling cycle defines how reasoning is restrained.

```text
Metal controls Wood
Water controls Fire
Wood controls Earth
Fire controls Metal
Earth controls Water
```

In this protocol, the controlling cycle is the brake architecture.

It prevents reasoning from becoming:

* too speculative
* too expansive
* too contextual
* too compressed
* too memory-heavy
* too repetitive
* too confident
* too long

The controlling cycle makes restraint a formal part of reasoning.

## Core Definition

The controlling cycle is a self-regulation model.

It defines which phase should intervene when another phase becomes excessive.

```text
Metal -> Wood  = cut excessive intuition
Water -> Fire  = cool excessive expansion
Wood  -> Earth = redirect stagnant context
Fire  -> Metal = restore useful detail after over-pruning
Earth -> Water = filter excessive memory
```

This creates a reasoning system that can expand without losing control.

## Why Brake Behavior Matters

Reasoning systems often fail not because they cannot generate, but because they cannot stop appropriately.

Common failures include:

* expanding every possible branch
* repeating the same point
* producing long answers when a short one is sufficient
* preserving too much memory
* pruning too aggressively
* drifting into irrelevant context
* continuing after completion
* making claims stronger than the evidence allows

The Brake Layer addresses these failures by defining when and how reasoning should be slowed, compressed, rerouted, or stopped.

## Brake Is Not Failure

A brake condition does not always mean the reasoning has failed.

A brake may mean:

* compress
* narrow
* stabilize
* qualify
* pause
* stop
* return to memory
* restore useful detail
* ask for clarification only if necessary

In this protocol, stopping is a reasoning operation.

```text
Stopping is not absence of intelligence.
Stopping is controlled intelligence.
```

## Controlling Cycle Overview

| Controller | Target | Brake Function                                       |
| ---------- | ------ | ---------------------------------------------------- |
| Metal      | Wood   | Cut excessive speculation or weak direction          |
| Water      | Fire   | Cool over-expansion and repeated generation          |
| Wood       | Earth  | Restore direction when context becomes stagnant      |
| Fire       | Metal  | Restore useful detail when pruning becomes excessive |
| Earth      | Water  | Filter memory and prevent noise retention            |

## Metal Controls Wood

## Meaning

```text
Metal -> Wood
```

Metal controls Wood by cutting excessive intuition, vague branching, or weak initial direction.

Wood is responsible for detecting what is trying to emerge.

However, Wood can become excessive when it produces too many possible directions without selecting a useful path.

Metal intervenes by sharpening the initial direction.

## Trigger Conditions

Metal may control Wood when:

* the question interpretation is too vague
* too many possible paths are generated
* the initial hypothesis is weak
* the reasoning begins with speculation
* the system attempts to expand without a clear direction
* the output shows unfocused branching
* the system is guessing the user’s intent too aggressively

## Possible Actions

Metal may:

* narrow the question
* cut secondary paths
* select the primary path
* mark uncertainty
* request clarification only when necessary
* stop a weak reasoning branch
* convert speculation into a safer minimal claim

## Example

```yaml
control:
  controller: metal
  target: wood
  function: stop_excessive_intuition
  trigger_conditions:
    - excessive_speculation
    - unfocused_branching
    - weak_initial_direction
  action: narrow_question
```

## Failure Prevented

This brake prevents:

```text
Wood -> Wood -> Wood -> Fire
```

where the system keeps inventing possible directions before understanding the task.

## Healthy Result

After Metal controls Wood, the system should have:

* one clearer direction
* fewer branches
* weaker unsupported claims
* better scope control
* a safer transition into Fire or Earth

## Water Controls Fire

## Meaning

```text
Water -> Fire
```

Water controls Fire by cooling excessive expansion.

Fire is responsible for development, generation, and expression.

However, Fire can become excessive when it continues expanding beyond the user’s actual need.

Water intervenes by reducing activation and returning the answer to its essential pattern.

## Trigger Conditions

Water may control Fire when:

* the answer becomes too long
* the system repeats itself
* reasoning continues after completion
* too many examples are generated
* speculative branches keep expanding
* the answer loses its center
* the output becomes more energetic than useful
* the user requested concision but the system keeps elaborating

## Possible Actions

Water may:

* summarize
* pause generation
* compress output
* return to the core claim
* retain only the useful essence
* stop after memory retention
* reduce the number of examples
* convert a long answer into a concise answer

## Example

```yaml
control:
  controller: water
  target: fire
  function: cool_excessive_expansion
  trigger_conditions:
    - excessive_length
    - reasoning_overheat
    - repeated_generation
    - low_signal_expansion
  action: compress_output
```

## Failure Prevented

This brake prevents:

```text
Wood -> Fire -> Fire -> Fire -> Fire
```

where the system continues expanding without compression.

## Healthy Result

After Water controls Fire, the system should have:

* shorter output
* less repetition
* lower branching
* clearer essence
* stronger stopping behavior
* a memory trace that preserves only what matters

## Wood Controls Earth

## Meaning

```text
Wood -> Earth
```

Wood controls Earth by restoring direction when context becomes stagnant or overly broad.

Earth is responsible for integration, coherence, and context.

However, Earth can become excessive when it keeps adding background without moving toward a useful answer.

Wood intervenes by reintroducing the core question.

## Trigger Conditions

Wood may control Earth when:

* context becomes too broad
* background overwhelms the answer
* the system keeps synthesizing without deciding
* the answer loses the user’s original request
* integration becomes vague
* contradiction is absorbed without resolution
* the response becomes a context swamp

## Possible Actions

Wood may:

* restate the core question
* choose one direction
* define the next reasoning path
* remove irrelevant context
* return to the user’s actual task
* convert vague synthesis into a clear inquiry vector

## Example

```yaml
control:
  controller: wood
  target: earth
  function: redirect_stagnant_context
  trigger_conditions:
    - over_contextualization
    - loss_of_direction
    - excessive_background
  action: restate_core_question
```

## Failure Prevented

This brake prevents:

```text
Fire -> Earth -> Earth -> Earth
```

where the system keeps adding context but never sharpens the answer.

## Healthy Result

After Wood controls Earth, the system should have:

* restored direction
* reduced background
* clearer task alignment
* a more direct path toward Metal or Fire
* less ambiguity

## Fire Controls Metal

## Meaning

```text
Fire -> Metal
```

Fire controls Metal by restoring useful detail when critique becomes excessive.

Metal is responsible for pruning, compression, and stopping.

However, Metal can become excessive when it cuts too much and leaves the answer too thin, dry, or incomplete.

Fire intervenes by adding back the minimum useful detail.

## Trigger Conditions

Fire may control Metal when:

* the answer becomes too short
* important detail has been removed
* the user asked for explanation
* compression damages clarity
* critique blocks necessary development
* the output becomes overly cautious
* the answer no longer satisfies the task
* stopping occurs before the answer is useful

## Possible Actions

Fire may:

* restore one useful example
* add minimal explanation
* expand a compressed point
* clarify the reasoning
* justify retained content
* develop only the missing part
* avoid reopening all discarded branches

## Example

```yaml
control:
  controller: fire
  target: metal
  function: challenge_excessive_pruning
  trigger_conditions:
    - premature_stopping
    - loss_of_useful_detail
    - excessive_compression
  action: restore_needed_detail
```

## Failure Prevented

This brake prevents:

```text
Wood -> Metal -> Stop
```

when the user actually needed explanation.

## Healthy Result

After Fire controls Metal, the system should have:

* enough detail to be useful
* no unnecessary expansion
* restored clarity
* one or two relevant examples if needed
* a path back to Earth or Metal for final checking

## Earth Controls Water

## Meaning

```text
Earth -> Water
```

Earth controls Water by filtering memory.

Water is responsible for retention, memory, and return.

However, Water can become excessive when it stores too much detail, including discarded branches, noise, speculation, or stale context.

Earth intervenes by checking what memory actually fits the whole reasoning context.

## Trigger Conditions

Earth may control Water when:

* memory retains too much
* discarded branches are preserved
* speculative claims are stored
* stale context affects future reasoning
* memory traces become vague
* memory accumulates noise
* the retained essence does not support future reasoning

## Possible Actions

Earth may:

* filter memory
* retain only the essence
* remove nonessential trace
* separate core claim from discarded branches
* preserve unresolved questions only when useful
* check whether the memory improves future reasoning
* prevent memory from becoming raw accumulation

## Example

```yaml
control:
  controller: earth
  target: water
  function: stabilize_memory_retention
  trigger_conditions:
    - excessive_retention
    - noise_preservation
    - stale_memory_risk
  action: retain_only_essence
```

## Failure Prevented

This brake prevents:

```text
Metal -> Water
```

where Water stores everything Metal removed.

## Healthy Result

After Earth controls Water, the system should have:

* cleaner memory
* fewer stale traces
* retained essence
* useful unresolved questions
* clear next actions
* less future context pollution

## Brake Conditions

The protocol defines several common brake conditions.

## Redundancy Detected

Triggered when the output repeats prior content without adding value.

Recommended response:

```yaml
brake:
  triggered_by: redundancy_detected
  preferred_agent: metal
  preferred_state: yin
  action:
    - compress_output
    - remove_duplicate_content
    - stop_if_sufficient
```

## Excessive Branching Detected

Triggered when too many reasoning paths are being explored at once.

Recommended response:

```yaml
brake:
  triggered_by: excessive_branching_detected
  preferred_agent: metal
  preferred_state: yin
  action:
    - select_primary_path
    - cut_secondary_paths
    - return_to_core_question
```

## Reasoning Overheat Detected

Triggered when expansion continues beyond the useful scope of the task.

Recommended response:

```yaml
brake:
  triggered_by: reasoning_overheat_detected
  preferred_agent: water
  preferred_state: yin
  action:
    - pause_generation
    - summarize_current_state
    - return_to_essence
```

## Context Drift Detected

Triggered when reasoning moves away from the user’s original request.

Recommended response:

```yaml
brake:
  triggered_by: context_drift_detected
  preferred_agent: earth
  preferred_state: balanced
  action:
    - restore_context
    - restate_task
    - reroute_to_relevant_phase
```

## Low Confidence Detected

Triggered when the system lacks enough support for a claim.

Recommended response:

```yaml
brake:
  triggered_by: low_confidence_detected
  preferred_agent: earth
  preferred_state: balanced
  action:
    - mark_uncertainty
    - reduce_claim_strength
    - request_evidence
    - avoid_overstatement
```

## Completion Detected

Triggered when the answer is sufficient for the current task.

Recommended response:

```yaml
brake:
  triggered_by: completion_detected
  preferred_agent: metal
  preferred_state: yin
  action:
    - stop_generation
    - provide_final_output
    - retain_core_trace
```

## Memory Overload Detected

Triggered when memory retains too much detail or preserves discarded noise.

Recommended response:

```yaml
brake:
  triggered_by: memory_overload_detected
  preferred_agent: earth
  preferred_state: balanced
  action:
    - filter_memory
    - retain_only_essence
    - remove_discarded_branches
```

## Premature Stopping Detected

Triggered when the answer stops before satisfying the user’s actual need.

Recommended response:

```yaml
brake:
  triggered_by: premature_stopping_detected
  preferred_agent: fire
  preferred_state: yang
  action:
    - restore_needed_detail
    - add_minimal_explanation
    - continue_to_context_check
```

## Brake Severity

Brake conditions may be assigned severity levels.

```yaml
severity_levels:
  low:
    meaning: "Minor adjustment required."
    typical_action: "compress or clarify slightly"

  medium:
    meaning: "Reasoning quality may degrade without intervention."
    typical_action: "reroute, prune, or stabilize"

  high:
    meaning: "Reasoning is likely to become uncontrolled or misleading."
    typical_action: "stop branch, reduce claim, or compress strongly"

  critical:
    meaning: "Continuation is likely harmful, irrelevant, or structurally invalid."
    typical_action: "stop generation or require review"
```

## Brake Actions

Common brake actions include:

```yaml
brake_actions:
  - narrow_question
  - cut_branch
  - reduce_claim_strength
  - mark_uncertainty
  - compress_output
  - summarize_current_state
  - remove_duplicate_content
  - return_to_core_question
  - restore_needed_detail
  - filter_memory
  - retain_only_essence
  - stop_generation
  - route_to_context_check
  - route_to_critique
  - route_to_memory
```

## Brake Decision Object

A minimal brake decision may look like this:

```yaml
brake_decision:
  triggered: true
  triggered_by: excessive_branching_detected
  severity: high
  controller: metal
  target: wood
  action: select_primary_path_and_stop_secondary_paths
  next_phase: earth
```

Another example:

```yaml
brake_decision:
  triggered: true
  triggered_by: completion_detected
  severity: medium
  controller: metal
  target: fire
  action: stop_generation
  next_phase: water
```

## Stop or Continue Decision

The controlling cycle should often produce a stop-or-continue decision.

```yaml
stop_or_continue_decision:
  status: stop_after_memory_retention
  reason: "The answer is sufficient and further expansion would reduce clarity."
  next_phase: water
```

Possible statuses include:

```yaml
statuses:
  - continue
  - continue_with_narrower_scope
  - continue_after_context_check
  - continue_to_memory_then_stop
  - stop_after_memory_retention
  - stop_without_memory_update
  - request_review
```

## Brake Routing Patterns

## Branch Pruning Route

Use when the system has too many possible paths.

```text
Wood / Fire -> Earth -> Metal -> Water -> Stop
```

## Compression Route

Use when the output is too long.

```text
Fire -> Metal -> Water -> Stop
```

## Context Recovery Route

Use when the answer drifts away from the task.

```text
Fire -> Earth -> Wood -> Earth -> Metal
```

## Detail Restoration Route

Use when pruning removed too much useful content.

```text
Metal -> Fire -> Earth -> Metal -> Water
```

## Memory Filtering Route

Use when retained memory contains noise.

```text
Water -> Earth -> Water
```

## Anti-Patterns

## No Brake

```text
Wood -> Fire -> Fire -> Fire -> Fire
```

Problem:

The system keeps expanding.

Correction:

Activate Earth for context checking, then Metal for pruning.

## Brake Too Late

```text
Wood -> Fire -> Fire -> Fire -> Earth -> Metal
```

Problem:

The system waits too long before checking scope.

Correction:

Route to Earth earlier when branching appears.

## Brake Too Early

```text
Wood -> Metal -> Stop
```

Problem:

The system cuts reasoning before enough useful content exists.

Correction:

Route to Fire for minimal expansion.

## Memory Without Filtering

```text
Metal -> Water
```

Problem:

Water stores everything, including discarded branches.

Correction:

Earth should filter Water’s memory retention.

## Endless Correction

```text
Metal -> Fire -> Metal -> Fire -> Metal
```

Problem:

The system alternates between critique and restoration without converging.

Correction:

Route to Earth for context stabilization, then Water for final retention.

## Design Principles

## 1. Brake Early, Not Harshly

A good brake does not wait until reasoning has become chaotic.

It intervenes early with small corrections.

## 2. Compression Is Not Deletion

Metal should remove noise, not meaning.

If compression damages clarity, Fire may restore the minimum useful detail.

## 3. Memory Must Be Filtered

Water should not retain everything.

Earth should ensure that memory preserves useful essence rather than raw accumulation.

## 4. Stopping Is a Valid Output

When the answer is sufficient, stopping is the correct action.

The system should not continue merely because it can.

## 5. Control Should Preserve Usefulness

The purpose of braking is not to silence reasoning.

The purpose is to keep reasoning useful.

## Relationship to Energy-Aware Reasoning

The controlling cycle supports energy-aware reasoning by reducing unnecessary activation.

It may reduce wasted reasoning activity by:

* cutting excessive branches
* stopping repeated generation
* compressing long outputs
* avoiding unnecessary context expansion
* preventing memory bloat
* limiting recursion
* stopping when the task is complete

This is not a measured hardware-level energy claim.

It is a control-layer efficiency model.

## Relationship to Safety

The controlling cycle may also support safer reasoning behavior by:

* reducing unsupported claims
* marking uncertainty
* stopping speculative branches
* restoring context
* preventing overconfident expansion
* limiting hallucination-prone continuation

However, this protocol does not guarantee truth or safety by itself.

It provides structural support for better reasoning control.

## Minimal Control Object

A minimal controlling cycle object may look like this:

```yaml
control_rule:
  controller: water
  target: fire
  function: cool_excessive_expansion
  trigger_conditions:
    - excessive_length
    - repeated_generation
  possible_actions:
    - compress_output
    - return_to_core_claim
    - stop_after_memory_retention
```

## Full Control Set

```yaml
controlling_cycle:
  controls:
    - controller: metal
      target: wood
      function: stop_excessive_intuition
      trigger_conditions:
        - excessive_speculation
        - unfocused_branching
        - weak_initial_direction
      possible_actions:
        - narrow_question
        - cut_branch
        - request_clarification
        - stop_path

    - controller: water
      target: fire
      function: cool_excessive_expansion
      trigger_conditions:
        - excessive_length
        - reasoning_overheat
        - repeated_generation
        - low_signal_expansion
      possible_actions:
        - summarize
        - pause_generation
        - compress_output
        - return_to_core_claim

    - controller: wood
      target: earth
      function: redirect_stagnant_context
      trigger_conditions:
        - over_contextualization
        - loss_of_direction
        - excessive_background
      possible_actions:
        - restate_core_question
        - choose_new_path
        - define_next_direction

    - controller: fire
      target: metal
      function: challenge_excessive_pruning
      trigger_conditions:
        - premature_stopping
        - loss_of_useful_detail
        - excessive_compression
      possible_actions:
        - restore_needed_detail
        - expand_minimally
        - justify_retained_content

    - controller: earth
      target: water
      function: stabilize_memory_retention
      trigger_conditions:
        - excessive_retention
        - noise_preservation
        - stale_memory_risk
      possible_actions:
        - filter_memory
        - retain_only_essence
        - remove_nonessential_trace
```

## Summary

The controlling cycle defines the brake architecture of the protocol.

```text
Metal controls Wood  = cut excessive intuition
Water controls Fire  = cool excessive expansion
Wood controls Earth  = restore direction
Fire controls Metal  = restore useful detail
Earth controls Water = filter memory
```

The generating cycle helps reasoning grow.

The controlling cycle keeps reasoning from growing without limit.

Together, they create a system that can:

* expand without runaway generation
* critique without destroying meaning
* remember without accumulating noise
* stop without failing
* return without repeating

The central principle is:

```text
Reasoning should be able to move.
Reasoning should also be able to stop.
```
