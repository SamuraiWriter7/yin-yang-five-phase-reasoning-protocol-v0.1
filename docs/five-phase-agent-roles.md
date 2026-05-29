# Five-Phase Agent Roles

## Purpose

This document defines the five functional reasoning roles used in the Yin-Yang Five-Phase Reasoning Protocol v0.1.

The Five Phases are used here as an architectural model for reasoning roles.

They are not treated as metaphysical entities.

They are used to describe five recurring functions that appear in effective reasoning systems:

```text
Wood  = direction
Fire  = expansion
Earth = integration
Metal = critique
Water = memory
```

Together, these roles allow a reasoning system to move through a complete cycle:

```text
detect -> expand -> integrate -> prune -> retain
```

In the protocol, these roles may be implemented as:

* separate agents
* internal model modes
* prompt stages
* routing states
* orchestration policies
* Multi-Wing components
* software modules

They do not require five separate AI models.

## Overview

The five roles form a complete reasoning ecology.

```text
Wood  asks: What is trying to emerge?
Fire  asks: How can this be expressed or developed?
Earth asks: Does this fit the whole context?
Metal asks: What should be cut, corrected, or stopped?
Water asks: What should remain after reasoning ends?
```

Each role has:

* a primary function
* a state tendency
* a set of operations
* expected outputs
* failure modes
* routing behavior

## Role Summary

| Phase | Role                    | State Tendency | Primary Function                         |
| ----- | ----------------------- | -------------- | ---------------------------------------- |
| Wood  | Intuition / Direction   | Yang           | Detect the core direction                |
| Fire  | Expansion / Development | Yang           | Develop the reasoning                    |
| Earth | Context / Integration   | Balanced       | Stabilize reasoning in context           |
| Metal | Critique / Pruning      | Yin            | Remove noise and evaluate stopping       |
| Water | Memory / Return         | Yin            | Retain essence and prepare future cycles |

## Wood: Direction Agent

## Definition

Wood is the direction-detection role.

It identifies the beginning of reasoning.

Wood does not need to produce a complete answer.
Its purpose is to determine what kind of answer should begin.

Wood asks:

```text
What is trying to emerge?
```

## State Tendency

Wood usually leans toward Yang because it initiates movement.

However, Wood may also become restrained when the first task is to narrow an unclear question.

## Primary Functions

Wood is responsible for:

* detecting the core question
* identifying the user’s actual intent
* forming the initial hypothesis
* selecting possible reasoning paths
* sensing the direction of inquiry
* preparing the first transition into expansion or clarification

## Typical Inputs

Wood may receive:

* a user question
* a previous memory trace
* an unresolved question from Water
* a task instruction
* a broad or ambiguous request
* a new inquiry vector

## Typical Outputs

Wood produces:

* core direction
* initial hypothesis
* inquiry vector
* possible paths
* scope warning
* next phase recommendation

Example:

```yaml
wood:
  role: direction
  state: yang
  input: "How should this protocol be introduced?"
  output:
    core_direction: "Introduce it as a dynamic reasoning control model."
    initial_hypothesis: "The protocol should be explained through state transition and agent routing."
    next_phase: fire
```

## Wood Failure Modes

Wood can fail when it produces:

* vague direction
* excessive speculation
* too many starting paths
* poor scope detection
* weak initial hypothesis
* misunderstanding of the user’s actual request

## Wood Brake Conditions

Wood should be checked when:

* the system begins exploring too many paths
* the core question remains unclear
* the reasoning direction becomes speculative
* the initial hypothesis is weak
* the system is about to expand without sufficient direction

Metal may control Wood by cutting excessive intuition.

## Fire: Expansion Agent

## Definition

Fire is the expansion role.

It develops the direction identified by Wood.

Fire gives reasoning its expressive force.

Fire asks:

```text
How can this be expressed or developed?
```

## State Tendency

Fire strongly leans toward Yang.

It is the most active and generative phase.

## Primary Functions

Fire is responsible for:

* expanding hypotheses
* generating explanations
* producing structured output
* drafting text
* writing code
* exploring implications
* developing logical paths
* turning direction into usable form

## Typical Inputs

Fire may receive:

* initial hypothesis from Wood
* inquiry vector
* user request for elaboration
* selected memory from Water
* refined direction from Earth
* restored detail after excessive pruning

## Typical Outputs

Fire produces:

* expanded reasoning
* draft output
* candidate branches
* examples
* logical development
* structured explanation
* generated content

Example:

```yaml
fire:
  role: expansion
  state: yang
  input: "Introduce the protocol as a dynamic reasoning control model."
  output:
    expanded_reasoning: >
      The protocol uses Yin-Yang as a state model and Five-Phase agents
      as functional reasoning roles.
    next_phase: earth
```

## Fire Failure Modes

Fire can fail when it produces:

* over-expansion
* excessive length
* unsupported claims
* speculative branches
* reasoning overheat
* low-value continuation
* repetition
* output that drifts away from the task

## Fire Brake Conditions

Fire should be checked when:

* the answer becomes too long
* the system repeats itself
* too many branches appear
* the output exceeds the user’s need
* claims become stronger than the evidence
* the reasoning continues after completion

Water may control Fire by cooling excessive expansion.

Metal may also prune Fire’s output when precision is needed.

## Earth: Context Agent

## Definition

Earth is the integration role.

It checks whether reasoning fits the whole context.

Earth prevents the system from becoming either too scattered or too narrow.

Earth asks:

```text
Does this fit the whole context?
```

## State Tendency

Earth usually operates in a Balanced state.

It mediates between Yang expansion and Yin compression.

## Primary Functions

Earth is responsible for:

* checking coherence
* aligning reasoning with the user’s request
* identifying context drift
* absorbing contradiction
* stabilizing meaning
* connecting local reasoning to broader knowledge
* determining whether the answer should expand, compress, or reroute

## Typical Inputs

Earth may receive:

* expanded reasoning from Fire
* candidate branches
* draft output
* context from the user
* memory trace from Water
* critique notes from Metal

## Typical Outputs

Earth produces:

* contextualized reasoning
* coherence assessment
* contradiction notes
* relevant branch selection
* scope stabilization
* rerouting recommendation

Example:

```yaml
earth:
  role: context
  state: balanced
  input: "Multiple possible implications have been generated."
  output:
    contextual_assessment: >
      The user likely needs the strongest implications, not every possible branch.
    relevant_branches:
      - energy-aware_reasoning
      - multi-agent_routing
      - self-stopping_generation
    next_phase: metal
```

## Earth Failure Modes

Earth can fail when it produces:

* excessive generalization
* over-contextualization
* vague synthesis
* ambiguity without resolution
* delayed decision-making
* too much background
* context expansion that buries the answer

## Earth Brake Conditions

Earth should be checked when:

* the answer becomes too broad
* integration becomes vague
* context overwhelms the core task
* the system keeps adding background
* contradiction is absorbed without being resolved

Wood may control Earth by restoring direction.

Metal may prune Earth’s over-contextualization.

## Metal: Critique Agent

## Definition

Metal is the critique and pruning role.

It removes noise, sharpens claims, and evaluates whether reasoning should stop.

Metal asks:

```text
What should be cut, corrected, or stopped?
```

## State Tendency

Metal usually leans toward Yin.

It reduces rather than expands.

## Primary Functions

Metal is responsible for:

* removing redundancy
* cutting unnecessary branches
* detecting weak claims
* reducing overstatement
* compressing output
* enforcing precision
* identifying unsupported claims
* evaluating stopping conditions

## Typical Inputs

Metal may receive:

* expanded reasoning from Fire
* contextualized output from Earth
* excessive branching warning
* low-confidence claim
* long draft
* user request for concision

## Typical Outputs

Metal produces:

* critique notes
* compressed output
* removed elements
* claim-strength adjustment
* stop-or-continue decision
* final refinement

Example:

```yaml
metal:
  role: critique
  state: yin
  input: "The reasoning has generated too many branches."
  brake_check:
    triggered: true
    triggered_by: excessive_branching_detected
    action: select_primary_path_and_stop_secondary_paths
  output:
    compressed_output: >
      The protocol defines a phase-based reasoning control model that
      alternates between activation and restraint.
    next_phase: water
```

## Metal Failure Modes

Metal can fail when it produces:

* excessive pruning
* premature stopping
* loss of useful detail
* overly dry output
* excessive skepticism
* refusal to develop necessary reasoning
* over-correction

## Metal Brake Conditions

Metal should be checked when:

* the answer becomes too thin
* useful detail has been removed
* critique blocks necessary explanation
* the user asked for development
* compression damages clarity

Fire may control Metal by restoring useful detail.

Earth may stabilize Metal by checking context before final pruning.

## Water: Memory Agent

## Definition

Water is the memory and return role.

It retains what matters after reasoning ends.

Water does not preserve everything.
It preserves essence.

Water asks:

```text
What should remain after the reasoning ends?
```

## State Tendency

Water usually leans toward Yin.

It is quiet, selective, and retentive.

## Primary Functions

Water is responsible for:

* retaining core claims
* extracting reusable patterns
* preserving minimal traces
* identifying unresolved questions
* storing next actions
* preparing future reasoning cycles
* returning selected memory to Wood

## Typical Inputs

Water may receive:

* compressed output from Metal
* final answer
* unresolved question
* next action
* useful pattern
* memory update request

## Typical Outputs

Water produces:

* retained essence
* reusable pattern
* memory trace
* next cycle seed
* unresolved question
* Water-to-Wood return signal

Example:

```yaml
water:
  role: memory
  state: yin
  input: "The answer has been refined and compressed."
  output:
    retained_essence: "Reasoning should breathe, not endlessly expand."
    reusable_pattern: "Wood detects, Fire expands, Earth integrates, Metal prunes, Water retains."
    next_cycle_seed: "Apply this pattern to the next protocol example."
```

## Water Failure Modes

Water can fail when it produces:

* excessive retention
* stale memory
* noise preservation
* loss of important essence
* vague memory traces
* unnecessary accumulation
* failure to return useful memory to Wood

## Water Brake Conditions

Water should be checked when:

* memory stores too much detail
* discarded branches are retained
* speculative claims are preserved
* memory becomes stale
* the retained trace does not help future reasoning

Earth may control Water by filtering memory.

Wood may receive Water’s retained essence as a new inquiry vector.

## Role Interaction

The five roles are not isolated.

They form a reasoning ecology.

## Constructive Flow

```text
Wood -> Fire -> Earth -> Metal -> Water -> Wood
```

Meaning:

1. Wood detects direction.
2. Fire expands the idea.
3. Earth integrates it with context.
4. Metal prunes and sharpens it.
5. Water retains the essence.
6. Wood receives the retained essence if another cycle is needed.

## Control Flow

```text
Metal controls Wood
Water controls Fire
Wood controls Earth
Fire controls Metal
Earth controls Water
```

Meaning:

* Metal cuts excessive intuition.
* Water cools excessive expansion.
* Wood redirects stagnant context.
* Fire restores useful detail when critique is too severe.
* Earth filters memory and prevents noise retention.

## Minimal Agent Object

A minimal phase agent object may look like this:

```yaml
phase_agent:
  phase: wood
  role: direction
  state_tendency: yang
  primary_function: detect_core_direction
  asks: "What is trying to emerge?"
  outputs:
    - core_direction
    - initial_hypothesis
    - inquiry_vector
```

Another example:

```yaml
phase_agent:
  phase: metal
  role: critique
  state_tendency: yin
  primary_function: prune_and_stop
  asks: "What should be cut, corrected, or stopped?"
  outputs:
    - critique_notes
    - compressed_output
    - stop_or_continue_decision
```

## Implementation Patterns

## Prompt-Level Implementation

A single GPT-style assistant can simulate the five roles by following a structured internal sequence:

```text
1. Wood: identify the core question.
2. Fire: expand only what is needed.
3. Earth: check context and coherence.
4. Metal: remove excess and correct overclaims.
5. Water: retain the essential result and stop.
```

This is suitable for lightweight reasoning assistants such as an energy-aware GPT.

## Agent-Level Implementation

A multi-agent system may implement each phase as a separate agent:

```text
Wood Agent  -> direction detection
Fire Agent  -> generation
Earth Agent -> context verification
Metal Agent -> critique and compression
Water Agent -> memory and return
```

An orchestrator routes tasks between agents.

## Multi-Wing Implementation

In a Multi-Wing architecture, the Five-Phase roles can operate as control functions across wings.

For example:

* a creative wing may perform Fire-like expansion
* a review wing may perform Metal-like critique
* a memory wing may perform Water-like retention
* a context wing may perform Earth-like integration
* a direction wing may perform Wood-like inquiry detection

This protocol does not replace Multi-Wing architecture.

It provides a control model for it.

## Policy-Level Implementation

A production reasoning system may implement the roles as policies:

```yaml
policies:
  direction_policy:
    phase: wood
    trigger: new_question_received
    action: detect_core_direction

  expansion_policy:
    phase: fire
    trigger: explanation_required
    action: expand_minimally

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
```

## Role Selection Rules

A system may select a phase according to the current reasoning condition.

| Condition                                     | Recommended Phase |
| --------------------------------------------- | ----------------- |
| New question received                         | Wood              |
| Initial direction is clear but underdeveloped | Fire              |
| Output may be drifting from context           | Earth             |
| Output is too long or repetitive              | Metal             |
| Reasoning is complete                         | Water             |
| User asks for more detail                     | Fire              |
| User asks for concise answer                  | Metal             |
| Previous answer should inform next cycle      | Water -> Wood     |

## Design Principle

The Five-Phase agent model is based on one principle:

```text
Reasoning quality improves when different reasoning functions are separated.
```

A system should not generate, critique, contextualize, and remember in the same undifferentiated motion.

It should know which function is currently needed.

## Summary

The Five-Phase agent roles define a functional reasoning cycle:

```text
Wood  = detect direction
Fire  = expand reasoning
Earth = integrate context
Metal = prune and stop
Water = retain essence
```

Together, they create a reasoning system that can:

* begin with direction
* expand without losing control
* integrate with context
* critique itself structurally
* stop when sufficient
* retain only what matters
* return to a refined next cycle

The result is not merely a symbolic model.

It is a practical architecture for controlled, role-distributed, energy-aware reasoning.
