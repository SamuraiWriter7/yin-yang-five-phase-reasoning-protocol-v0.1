# Generating Cycle Routing

## Purpose

This document defines the generating cycle routing model used in the Yin-Yang Five-Phase Reasoning Protocol v0.1.

The generating cycle describes the constructive flow of reasoning.

```text
Wood -> Fire -> Earth -> Metal -> Water -> Wood
```

In this protocol, the generating cycle is not a symbolic diagram only.

It is a routing model.

It defines how a reasoning system may move from direction detection, to expansion, to contextual integration, to critique, to memory, and finally back into a new direction when another cycle is useful.

## Core Definition

The generating cycle is the default constructive reasoning path:

```text
Wood  = detect direction
Fire  = expand reasoning
Earth = integrate context
Metal = prune and refine
Water = retain essence
Wood  = begin next cycle from retained essence
```

In simple terms:

```text
detect -> expand -> integrate -> prune -> retain -> return
```

This cycle prevents reasoning from becoming a flat sequence of continuous generation.

Instead of:

```text
generate -> continue -> continue -> continue
```

the protocol encourages:

```text
detect -> expand -> check -> cut -> remember -> stop or return
```

## Why Routing Matters

Reasoning systems often fail not because they cannot generate, but because they do not know where to route the reasoning next.

A system may continue expanding when it should compress.

It may critique too early when it should first develop the idea.

It may retain too much memory when it should preserve only the essence.

The generating cycle gives the system a default path for constructive reasoning.

It answers:

```text
Where should reasoning go next?
```

## Default Generating Route

The default route is:

```text
Wood -> Fire -> Earth -> Metal -> Water
```

If another cycle is needed, Water may return selected memory to Wood:

```text
Water -> Wood
```

This return should not happen automatically.

It should happen only when the retained essence, unresolved question, or next action can support a useful new reasoning cycle.

## Phase 1: Wood to Fire

## Transition

```text
Wood -> Fire
```

## Meaning

Direction becomes expansion.

Wood detects what the question is trying to become.
Fire develops that direction into usable reasoning.

## Trigger Conditions

Wood may route to Fire when:

* the core question is clear
* an initial hypothesis has been formed
* the user asks for explanation
* the task requires development
* a previous memory trace has become a new inquiry vector
* the system has enough direction to begin expansion

## Inputs from Wood

Wood may pass to Fire:

* core direction
* initial hypothesis
* inquiry vector
* possible reasoning paths
* scope warning
* next phase recommendation

## Fire Responsibilities After Receiving Wood Output

Fire should:

* expand only the selected direction
* avoid generating all possible branches by default
* produce a usable explanation, draft, example, or structure
* preserve the intent detected by Wood
* avoid losing the core question during expansion

## Example

```yaml
transition:
  from: wood
  to: fire
  meaning: direction_to_expansion
  condition: core_direction_detected
  payload:
    core_direction: "Introduce the protocol as a dynamic reasoning control model."
    initial_hypothesis: "Reasoning should alternate between expansion and compression."
```

## Failure Modes

This transition can fail when:

* Wood passes too many possible paths
* Fire expands beyond the selected direction
* the initial hypothesis is too vague
* the system begins generating before the task is understood
* scope warnings are ignored

## Corrective Actions

If failure is detected:

* route to Earth for context stabilization
* route to Metal for branch pruning
* return to Wood for direction clarification
* ask for clarification only when necessary

## Phase 2: Fire to Earth

## Transition

```text
Fire -> Earth
```

## Meaning

Expansion becomes context.

Fire generates content.
Earth checks whether that content fits the user’s request, the surrounding context, and the protocol’s constraints.

## Trigger Conditions

Fire may route to Earth when:

* an explanation has been generated
* multiple branches have appeared
* the output requires coherence checking
* the answer may be drifting from the task
* claims require contextual qualification
* the generated content needs stabilization

## Inputs from Fire

Fire may pass to Earth:

* expanded reasoning
* draft output
* generated content
* candidate branches
* examples
* logical development
* uncertainty markers
* expansion warnings

## Earth Responsibilities After Receiving Fire Output

Earth should:

* check whether the output fits the task
* identify context drift
* select relevant branches
* resolve or mark contradictions
* determine whether the output needs pruning
* decide whether the reasoning should continue, compress, or reroute

## Example

```yaml
transition:
  from: fire
  to: earth
  meaning: expansion_to_context
  condition: reasoning_requires_integration
  payload:
    expanded_reasoning: "The protocol controls reasoning through Yin-Yang states and Five-Phase roles."
    expansion_warning: "The explanation may become too broad if all implications are included."
```

## Failure Modes

This transition can fail when:

* Earth adds too much background
* context checking becomes vague
* contradiction is absorbed without resolution
* the system loses the original user request
* all generated branches are treated as equally important

## Corrective Actions

If failure is detected:

* route to Metal for pruning
* return to Wood to restore direction
* reduce context to the minimum needed
* mark uncertainty instead of hiding it

## Phase 3: Earth to Metal

## Transition

```text
Earth -> Metal
```

## Meaning

Context becomes critique.

Earth stabilizes the output.
Metal sharpens it.

This is where reasoning begins to move from expansion toward restraint.

## Trigger Conditions

Earth may route to Metal when:

* relevant branches have been selected
* the output needs compression
* unsupported claims have been detected
* redundancy is present
* completion may be near
* the answer should become more precise

## Inputs from Earth

Earth may pass to Metal:

* contextualized reasoning
* coherence assessment
* contradiction notes
* relevant branch list
* lower-priority branch list
* context drift signal
* claim-strength warning
* task alignment assessment

## Metal Responsibilities After Receiving Earth Output

Metal should:

* remove low-value branches
* reduce redundancy
* weaken unsupported claims
* compress the explanation
* preserve necessary detail
* evaluate whether the answer is sufficient
* decide whether to stop or continue to Water

## Example

```yaml
transition:
  from: earth
  to: metal
  meaning: context_to_critique
  condition: output_requires_refinement
  payload:
    relevant_branches:
      - energy-aware_reasoning
      - multi-agent_routing
      - self-stopping_generation
    lower_priority_branches:
      - distant_hardware_speculation
      - broad_philosophical_expansion
```

## Failure Modes

This transition can fail when:

* Metal cuts too much
* useful detail is removed
* critique becomes excessive
* output becomes too dry or unclear
* the system stops before answering the user’s real need

## Corrective Actions

If failure is detected:

* route briefly back to Fire for minimal restoration
* route to Earth for context checking
* preserve at least one useful example when clarity requires it
* distinguish compression from deletion

## Phase 4: Metal to Water

## Transition

```text
Metal -> Water
```

## Meaning

Critique becomes memory.

Metal produces the refined answer or compressed essence.
Water decides what should remain after the reasoning cycle.

## Trigger Conditions

Metal may route to Water when:

* the output has been compressed
* weak claims have been corrected
* redundancy has been removed
* a stop-or-continue decision has been made
* the answer is sufficient
* the useful essence is ready for retention

## Inputs from Metal

Metal may pass to Water:

* compressed output
* critique notes
* removed elements
* stop-or-continue decision
* corrected claim
* final answer candidate
* retained branch list
* discarded branch list

## Water Responsibilities After Receiving Metal Output

Water should:

* retain the core lesson
* preserve useful patterns
* store unresolved questions
* identify the next action
* avoid retaining discarded noise
* decide whether a Water-to-Wood return is useful
* support final stopping when appropriate

## Example

```yaml
transition:
  from: metal
  to: water
  meaning: critique_to_memory
  condition: essence_ready_for_retention
  payload:
    compressed_output: "Reasoning should breathe, not endlessly expand."
    stop_or_continue_decision: continue_to_memory_then_stop
```

## Failure Modes

This transition can fail when:

* Water stores too much
* discarded branches are retained
* critique notes are mistaken for final memory
* speculative claims are preserved
* no reusable pattern is extracted

## Corrective Actions

If failure is detected:

* route to Earth for memory filtering
* retain only the core claim, unresolved question, next action, or reusable pattern
* discard full intermediate reasoning unless required
* avoid storing noise as memory

## Phase 5: Water to Wood

## Transition

```text
Water -> Wood
```

## Meaning

Memory becomes direction.

Water does not simply end the cycle.
When another cycle is useful, selected retained memory can become the seed of a new Wood phase.

## Trigger Conditions

Water may route to Wood when:

* an unresolved question remains
* the user asks for the next step
* retained memory suggests a useful new direction
* the current answer becomes the basis for a new task
* a next action has been identified
* recursive refinement is needed

## Inputs from Water

Water may pass to Wood:

* retained essence
* unresolved question
* reusable pattern
* next action
* important constraint
* memory trace
* next cycle seed

## Wood Responsibilities After Receiving Water Output

Wood should:

* convert retained memory into a new inquiry vector
* avoid restarting from raw previous output
* detect the next direction from the retained essence
* begin a new cycle only when useful
* preserve continuity without repeating noise

## Example

```yaml
transition:
  from: water
  to: wood
  meaning: memory_to_new_direction
  condition: next_cycle_required
  payload:
    retained_essence: "Reasoning should breathe, not endlessly expand."
    unresolved_question: "How should stopping conditions be formalized?"
    next_cycle_seed: "Define brake conditions for the protocol."
```

## Failure Modes

This transition can fail when:

* Water returns too much memory
* Wood repeats the previous cycle without refinement
* discarded branches reappear
* the new direction is not actually useful
* recursion becomes endless

## Corrective Actions

If failure is detected:

* stop instead of returning
* retain only the next action
* ask whether another cycle is needed only if necessary
* route to Metal for compression before returning to Wood
* limit the next cycle to one clear inquiry vector

## Full Generating Cycle Example

```yaml
generating_cycle:
  sequence:
    - wood
    - fire
    - earth
    - metal
    - water
    - wood

  transitions:
    - from: wood
      to: fire
      meaning: direction_to_expansion
      condition: core_direction_detected

    - from: fire
      to: earth
      meaning: expansion_to_context
      condition: reasoning_requires_integration

    - from: earth
      to: metal
      meaning: context_to_critique
      condition: output_requires_refinement

    - from: metal
      to: water
      meaning: critique_to_memory
      condition: essence_ready_for_retention

    - from: water
      to: wood
      meaning: memory_to_new_direction
      condition: next_cycle_required
```

## Routing Conditions

The generating cycle should not always run in full.

A system may use a shortened route when the task is simple.

## Minimal Answer Route

For a simple question:

```text
Wood -> Metal -> Water
```

Use when:

* the answer is obvious
* the user wants brevity
* expansion is unnecessary
* the response should be minimal

## Explanation Route

For ordinary explanation:

```text
Wood -> Fire -> Earth -> Metal -> Water
```

Use when:

* the user needs a useful explanation
* some expansion is needed
* the output should still be checked and compressed

## Broad Request Route

For broad or risky requests:

```text
Wood -> Fire -> Earth -> Metal -> Water
```

with stronger Earth and Metal checks.

Use when:

* the task may expand too far
* the user asks for many implications
* scope drift is likely
* branches must be selected carefully

## Iterative Refinement Route

For follow-up refinement:

```text
Water -> Wood -> Fire -> Earth -> Metal -> Water
```

Use when:

* previous memory should guide the next answer
* a retained pattern becomes a new question
* the user asks how to improve the prior output
* the system must avoid repeating the previous answer

## Compression Route

For overly long output:

```text
Earth -> Metal -> Water
```

Use when:

* context has already been established
* the main task is pruning
* the output needs to be shortened
* a memory trace should remain after compression

## Route Selection Table

| Condition                                | Recommended Route                                |
| ---------------------------------------- | ------------------------------------------------ |
| New open-ended question                  | Wood -> Fire -> Earth -> Metal -> Water          |
| Simple factual or direct answer          | Wood -> Metal -> Water                           |
| User asks for concise answer             | Wood -> Metal -> Water                           |
| User asks for deep explanation           | Wood -> Fire -> Earth -> Metal -> Water          |
| Output is too long                       | Earth -> Metal -> Water                          |
| Reasoning has too many branches          | Earth -> Metal -> Water                          |
| Previous memory should guide next answer | Water -> Wood -> Fire -> Earth -> Metal -> Water |
| Need to restore useful detail            | Metal -> Fire -> Earth -> Metal                  |
| Answer is complete                       | Metal -> Water -> Stop                           |

## Stop Conditions

The generating cycle should stop when:

* the answer is sufficient
* the user’s task has been satisfied
* further expansion would reduce clarity
* remaining branches are low value
* the output has been compressed and retained
* no unresolved question requires another cycle

A complete cycle does not always require returning to Wood.

Often, the correct endpoint is:

```text
Metal -> Water -> Stop
```

## Anti-Patterns

## Endless Fire

```text
Wood -> Fire -> Fire -> Fire -> Fire
```

Problem:

The system continues expanding without context checking or critique.

Correction:

Route to Earth, then Metal.

## Memory Overload

```text
Metal -> Water
```

but Water retains everything.

Problem:

Memory stores noise, discarded branches, and redundant explanation.

Correction:

Water should retain only essence, unresolved questions, next actions, and reusable patterns.

## Premature Metal

```text
Wood -> Metal
```

when explanation is actually needed.

Problem:

The answer becomes too thin.

Correction:

Route to Fire for minimal expansion.

## Context Swamp

```text
Fire -> Earth -> Earth -> Earth
```

Problem:

The system keeps adding background and loses the answer.

Correction:

Route to Metal to prune and finalize.

## Empty Return

```text
Water -> Wood
```

without a useful next cycle seed.

Problem:

The system restarts unnecessarily.

Correction:

Stop instead of returning.

## Design Principle

The generating cycle is governed by one principle:

```text
Each phase should prepare the next phase, not replace it.
```

Wood should not do all expansion.

Fire should not decide final memory.

Earth should not become endless context.

Metal should not erase useful meaning.

Water should not store everything.

Each role contributes one necessary movement in the reasoning cycle.

## Summary

Generating cycle routing defines the constructive flow of the protocol:

```text
Wood -> Fire -> Earth -> Metal -> Water -> Wood
```

This route allows reasoning to:

* begin with direction
* expand with purpose
* integrate with context
* prune with precision
* retain useful essence
* return only when another cycle is valuable

The goal is not to force every answer through every phase.

The goal is to route reasoning through the smallest sufficient cycle.

In short:

```text
Reasoning should move.
But it should not wander.
```
