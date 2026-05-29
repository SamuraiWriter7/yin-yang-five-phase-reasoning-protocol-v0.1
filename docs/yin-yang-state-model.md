# Yin-Yang State Model

## Purpose

This document defines the Yin-Yang state model used in the Yin-Yang Five-Phase Reasoning Protocol v0.1.

In this protocol, Yin-Yang is not treated as a mystical claim or metaphysical doctrine.

It is used as a structural model for reasoning-state control.

The core idea is simple:

```text
Reasoning should not remain in continuous activation.
Reasoning should alternate between expansion and restraint.
```

In other words:

```text
Reasoning should breathe.
```

## Core Definition

The Yin-Yang state model defines two primary reasoning states:

```text
Yang = activation, expansion, exploration
Yin  = restraint, compression, stopping
```

A reasoning system should be able to move between these states depending on the task, context, uncertainty, redundancy, and completion level.

This protocol treats reasoning as a dynamic state transition:

```text
Yang -> Yin -> Yang -> Yin ...
```

rather than a continuous generation process:

```text
generate -> continue -> continue -> continue
```

## Why State Control Matters

Many reasoning systems tend to continue generating once activated.

This can create several problems:

* unnecessary length
* excessive branching
* repeated explanations
* unsupported claims
* context drift
* hallucination risk
* wasted computation
* weak stopping behavior

The Yin-Yang state model addresses this by making restraint a formal part of reasoning.

A system should not only know how to begin reasoning.

It should also know how to:

* slow down
* compress
* pause
* stop
* retain only what matters
* return only when another cycle is useful

## Yang State

## Definition

Yang is the active state of reasoning.

It represents:

* activation
* generation
* expansion
* exploration
* divergence
* broad attention
* hypothesis creation

Yang is required when the system must produce, discover, explore, or develop an idea.

## Typical Yang Operations

Yang operations include:

* generating hypotheses
* expanding explanations
* creating drafts
* writing code
* exploring alternatives
* developing logical paths
* producing structured output
* searching for possible interpretations
* broadening the reasoning context

## Yang Is Useful When

Yang is appropriate when:

* the question is open-ended
* an idea needs development
* multiple options should be considered
* the user asks for creativity
* the system needs to explore possible paths
* the reasoning direction is still forming
* the answer requires explanation rather than conclusion only

## Yang Failure Modes

Uncontrolled Yang can become excessive.

Common failure modes include:

* over-expansion
* excessive verbosity
* unnecessary speculation
* too many branches
* repeated claims
* drifting away from the user’s request
* continuing after the answer is already sufficient
* presenting weak claims with too much confidence

In this protocol, Yang should eventually be checked by Earth, Metal, or Water.

## Yin State

## Definition

Yin is the restrained state of reasoning.

It represents:

* compression
* pruning
* silence
* stopping
* consolidation
* local attention
* reduced activation
* memory filtering

Yin is required when the system must refine, reduce, stabilize, or end reasoning.

## Typical Yin Operations

Yin operations include:

* summarizing
* pruning
* removing redundancy
* detecting weak claims
* narrowing scope
* stopping generation
* retaining core lessons
* compressing long output
* consolidating memory
* refusing unnecessary expansion

## Yin Is Useful When

Yin is appropriate when:

* the answer is already sufficient
* the output is becoming too long
* the reasoning has too many branches
* uncertainty is high
* the system is repeating itself
* the user asked for a concise answer
* the task requires judgment rather than exploration
* memory should retain only the useful essence

## Yin Failure Modes

Excessive Yin can also become harmful.

Common failure modes include:

* premature stopping
* under-exploration
* excessive compression
* loss of useful detail
* overly dry output
* insufficient explanation
* failure to consider alternatives
* refusal to develop a useful idea

In this protocol, Yin can be challenged by Fire when useful detail has been removed too aggressively.

## Balanced State

The protocol also allows a balanced state.

Balanced state is not a third metaphysical force.

It is a practical reasoning state used when the system must integrate expansion and restraint.

Balanced state is especially important for the Earth phase.

## Balanced State Functions

Balanced state supports:

* coherence checking
* context alignment
* contradiction absorption
* factual caution
* task relevance checking
* scope stabilization
* transition between Yang and Yin

Balanced state is useful when the system must decide whether to continue expanding or begin compressing.

## State Transition Model

The protocol defines reasoning as state transition.

A typical flow looks like this:

```text
Yang -> Yang -> Balanced -> Yin -> Yin
```

For example:

```text
Wood  = Yang
Fire  = Yang
Earth = Balanced
Metal = Yin
Water = Yin
```

This pattern means:

1. Wood detects a direction.
2. Fire expands it.
3. Earth checks context.
4. Metal prunes and evaluates stopping.
5. Water retains the useful essence.

## Basic State Pattern

```text
Question
  ↓
Yang: detect and expand
  ↓
Balanced: integrate and check
  ↓
Yin: prune, compress, stop, retain
```

This state pattern prevents reasoning from remaining in endless activation.

## Oscillation

The Yin-Yang state model is not static.

A reasoning cycle may move repeatedly between expansion and restraint.

Example:

```text
Yang: generate possible answer
Yin: remove weak parts
Yang: restore one necessary detail
Balanced: check coherence
Yin: compress and stop
```

This oscillation allows reasoning to become flexible.

The goal is not to maximize Yang or maximize Yin.

The goal is appropriate transition.

## State Transition Triggers

A system should shift from Yang to Yin when it detects:

* redundancy
* excessive length
* low-value expansion
* unsupported claims
* context drift
* completion
* high uncertainty
* user preference for brevity
* repeated reasoning loops

A system should shift from Yin to Yang when it detects:

* missing detail
* insufficient explanation
* premature stopping
* unresolved question
* user request for expansion
* necessary example not yet provided
* useful branch not yet explored

A system should shift into Balanced state when it detects:

* conflicting context
* unclear user intent
* need for coherence checking
* need for scope stabilization
* tension between expansion and compression

## State-Aware Routing

The Yin-Yang state model affects Five-Phase routing.

```text
Wood  tends toward Yang.
Fire  tends toward Yang.
Earth tends toward Balanced.
Metal tends toward Yin.
Water tends toward Yin.
```

However, these are tendencies, not rigid rules.

For example:

* Wood may become Yin when narrowing an unclear question.
* Fire may become restrained when producing a minimal explanation.
* Earth may lean Yang when adding necessary context.
* Metal may briefly activate Yang when restoring useful detail.
* Water may return to Yang when selected memory becomes a new inquiry seed.

The protocol allows flexible state transitions.

## Example: Broad Request

Input:

```text
Explain every possible implication of this protocol.
```

Possible state flow:

```text
Wood  / Yang      = detect scope risk
Fire  / Yang      = list candidate branches
Earth / Balanced  = identify relevant branches
Metal / Yin       = cut unnecessary branches
Water / Yin       = retain the useful essence
```

Result:

```text
The system gives a focused answer instead of expanding endlessly.
```

## Example: Concise Request

Input:

```text
Explain this in one sentence.
```

Possible state flow:

```text
Wood  / Yang      = detect core direction
Metal / Yin       = compress immediately
Water / Yin       = retain the core definition
```

Result:

```text
The system avoids unnecessary expansion.
```

## Example: Under-Explained Answer

Input:

```text
This is too short. Give me one example.
```

Possible state flow:

```text
Water / Yin       = retrieve retained essence
Wood  / Yang      = detect needed direction
Fire  / Yang      = add one example
Earth / Balanced  = check fit
Metal / Yin       = stop before over-expansion
```

Result:

```text
The system expands only where needed.
```

## Brake Behavior

The Yin state is closely related to the Brake Layer.

The Brake Layer may activate Yin when it detects:

* redundancy
* over-expansion
* excessive branching
* completion
* unsupported certainty
* low-value continuation

A brake does not always mean final stopping.

It may mean:

* compress
* summarize
* narrow
* reroute
* pause
* ask for clarification
* retain memory
* stop generation

The key point is that restraint becomes part of the reasoning architecture.

## State Model and Energy Awareness

This protocol does not claim measured hardware-level energy savings.

Instead, it defines energy awareness at the reasoning-control level.

A state-aware reasoning system may reduce unnecessary work by:

* avoiding needless expansion
* stopping when sufficient
* pruning weak branches
* limiting redundant generation
* retaining only useful memory
* routing to the smallest sufficient reasoning path

Energy awareness begins with the ability to not activate everything all the time.

In this sense, Yin is not merely “less output.”

Yin is controlled non-activation.

## State Model and Hallucination Risk

Uncontrolled Yang can increase hallucination risk when the system continues expanding beyond available support.

The Yin state helps reduce this risk by:

* weakening unsupported claims
* marking uncertainty
* stopping speculative branches
* compressing to supported points
* returning to context before continuing

However, Yin does not guarantee truth.

It only supports safer reasoning behavior by reducing uncontrolled expansion.

## State Model and Memory

The Water phase uses Yin to determine what should remain.

Memory should not preserve full reasoning noise.

It should retain:

* core claim
* useful pattern
* unresolved question
* next action
* important constraint
* reusable lesson

Memory should avoid retaining:

* discarded branches
* unsupported speculation
* redundant explanation
* temporary noise
* excessive context

This allows future reasoning cycles to begin from refined essence rather than raw accumulation.

## Implementation Notes

## Prompt-Level Implementation

A prompt-level implementation may instruct a model to:

1. identify whether the task requires expansion or compression
2. answer in the smallest sufficient form
3. expand only when needed
4. prune weak claims
5. stop when the answer is sufficient

## Agent-Level Implementation

An agent-level implementation may route tasks through:

* a Yang-oriented generator
* a Balanced context checker
* a Yin-oriented critic
* a memory filter

## Policy-Level Implementation

A policy-level implementation may define state transitions such as:

```yaml
state_transition:
  from: yang
  to: yin
  trigger: redundancy_detected
  action: compress_output
```

or:

```yaml
state_transition:
  from: yin
  to: yang
  trigger: insufficient_explanation
  action: add_minimal_example
```

## Minimal State Object

A minimal state object may look like this:

```yaml
state:
  mode: yang
  function: expansion
  active_phase: fire
  transition_reason: explanation_required
```

A Yin state object may look like this:

```yaml
state:
  mode: yin
  function: compression
  active_phase: metal
  transition_reason: redundancy_detected
```

A balanced state object may look like this:

```yaml
state:
  mode: balanced
  function: context_integration
  active_phase: earth
  transition_reason: coherence_check_required
```

## Design Principle

The central design principle of the Yin-Yang state model is:

```text
Do not reward endless continuation.
Reward appropriate transition.
```

A reasoning system should not be judged only by how much it can produce.

It should also be judged by whether it knows:

* when to expand
* when to narrow
* when to compress
* when to stop
* when to remember
* when to return

## Summary

The Yin-Yang state model defines the dynamic control layer of the protocol.

```text
Yang     = activation and expansion
Yin      = restraint and compression
Balanced = context integration
```

Together, these states allow reasoning to move through controlled cycles instead of endless generation.

The goal is not silence alone.

The goal is intelligent timing.

Reasoning should activate when needed.
It should compress when wiser.
It should stop when sufficient.
And when the next cycle begins, it should return from retained essence rather than accumulated noise.
