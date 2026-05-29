# Relationship to Multi-Wing Architecture

## Purpose

This document explains how the Yin-Yang Five-Phase Reasoning Protocol v0.1 relates to Multi-Wing architecture.

The short version is:

```text
Multi-Wing defines distributed reasoning.
Yin-Yang Five-Phase defines dynamic reasoning control.
```

Multi-Wing answers:

```text
Which wing should reason?
```

The Yin-Yang Five-Phase Reasoning Protocol answers:

```text
When should reasoning expand, compress, stop, or return?
```

Together, they form a more complete model for role-distributed, energy-aware, self-regulating reasoning.

## Conceptual Relationship

Multi-Wing architecture treats intelligence as a distributed system.

Instead of assuming that one monolithic model or one reasoning process should do everything, Multi-Wing separates reasoning into multiple specialized wings.

The Yin-Yang Five-Phase Reasoning Protocol adds a control model to that distributed structure.

It defines how reasoning should move between:

* activation
* expansion
* integration
* critique
* compression
* memory
* return

In simple terms:

```text
Multi-Wing = who reasons
Five-Phase = how reasoning flows
Yin-Yang = when reasoning activates or restrains itself
```

## Architectural Position

The Yin-Yang Five-Phase Reasoning Protocol can be placed below, beside, or inside Multi-Wing architecture.

## 1. Below Multi-Wing: Control Layer

In this interpretation, Multi-Wing is the distributed reasoning architecture, and Yin-Yang Five-Phase is the control layer that regulates wing activation.

```text
┌────────────────────────────────────┐
│ Multi-Wing Architecture             │
│ Distributed reasoning wings         │
├────────────────────────────────────┤
│ Yin-Yang Five-Phase Protocol        │
│ State transition and routing control│
└────────────────────────────────────┘
```

Here, the protocol controls:

* which wing should activate
* when a wing should stop
* when critique should intervene
* when memory should retain essence
* when another reasoning cycle is useful

## 2. Inside Multi-Wing: Wing Role Model

In this interpretation, the Five Phases become functional wing roles inside Multi-Wing.

```text
Wood Wing  = direction detection
Fire Wing  = expansion and generation
Earth Wing = context integration
Metal Wing = critique and compression
Water Wing = memory and return
```

This is the most direct implementation pattern.

## 3. Beside Multi-Wing: Complementary Protocol

In this interpretation, the protocol does not replace Multi-Wing and does not need to be embedded directly.

Instead, it acts as a companion specification.

Multi-Wing defines the distributed intelligence structure.

Yin-Yang Five-Phase defines a general reasoning-control pattern that can be applied to Multi-Wing or other agentic systems.

## Mapping Five Phases to Multi-Wing Roles

The Five-Phase roles can be mapped to Multi-Wing functions as follows:

| Five-Phase Role | Reasoning Function       | Possible Multi-Wing Equivalent  |
| --------------- | ------------------------ | ------------------------------- |
| Wood            | Direction detection      | Inquiry Wing / Planning Wing    |
| Fire            | Expansion and generation | Generation Wing / Creative Wing |
| Earth           | Context integration      | Context Wing / Coherence Wing   |
| Metal           | Critique and pruning     | Review Wing / Critique Wing     |
| Water           | Memory and return        | Memory Wing / Trace Wing        |

This mapping is flexible.

A Multi-Wing system may have more than five wings.
In that case, the Five-Phase model can act as a higher-level control pattern rather than a one-to-one wing list.

## Wood and Multi-Wing

Wood corresponds to direction detection.

In Multi-Wing architecture, Wood-like behavior may appear in:

* planning wings
* inquiry wings
* intent-detection modules
* task-routing components
* first-pass interpreters

Wood decides what the system is trying to do before other wings begin heavy reasoning.

Without Wood, a Multi-Wing system may activate too many wings too early.

## Fire and Multi-Wing

Fire corresponds to expansion.

In Multi-Wing architecture, Fire-like behavior may appear in:

* generation wings
* drafting wings
* code-generation wings
* creative reasoning wings
* exploratory reasoning modules

Fire turns direction into usable output.

Without Fire, the system may understand the task but fail to produce anything useful.

## Earth and Multi-Wing

Earth corresponds to context integration.

In Multi-Wing architecture, Earth-like behavior may appear in:

* context wings
* coherence-checking wings
* factual alignment modules
* policy-alignment layers
* synthesis wings

Earth checks whether the reasoning still fits the whole context.

Without Earth, a Multi-Wing system may generate plausible but poorly integrated outputs.

## Metal and Multi-Wing

Metal corresponds to critique, pruning, and stopping.

In Multi-Wing architecture, Metal-like behavior may appear in:

* review wings
* critique wings
* compression modules
* safety review layers
* redundancy detection modules
* stopping controllers

Metal prevents uncontrolled expansion.

Without Metal, a Multi-Wing system may continue reasoning, branching, or generating beyond the useful point.

## Water and Multi-Wing

Water corresponds to memory and return.

In Multi-Wing architecture, Water-like behavior may appear in:

* memory wings
* trace wings
* summary modules
* long-term context layers
* retrieval preparation layers
* next-action preservation modules

Water preserves what should remain after reasoning ends.

Without Water, a Multi-Wing system may either forget useful patterns or retain too much noise.

## Yin-Yang as Multi-Wing Activation Control

The Yin-Yang state model can be used to control wing activation.

```text
Yang = activate wing
Yin  = restrain, compress, pause, or stop wing
Balanced = integrate wing outputs
```

For example:

```yaml
wing_activation:
  wing: generation_wing
  phase: fire
  state: yang
  action: expand_selected_direction
```

Or:

```yaml
wing_activation:
  wing: critique_wing
  phase: metal
  state: yin
  action: compress_and_stop
```

Or:

```yaml
wing_activation:
  wing: context_wing
  phase: earth
  state: balanced
  action: check_coherence
```

This allows Multi-Wing systems to avoid activating every wing at all times.

## Multi-Wing Problem Addressed by This Protocol

Multi-Wing architecture introduces many strengths:

* distributed reasoning
* specialization
* modularity
* parallel review
* agentic flexibility
* role separation

However, it also introduces risks:

* too many wings activating at once
* excessive coordination cost
* repeated review loops
* over-generation by multiple agents
* memory bloat
* unclear stopping conditions
* critique loops without convergence
* routing complexity

The Yin-Yang Five-Phase Reasoning Protocol addresses these risks by defining:

* default reasoning routes
* brake conditions
* state transitions
* stopping rules
* memory retention rules
* Water-to-Wood return logic

In other words, it gives Multi-Wing systems a breathing rhythm.

## Multi-Wing Without Five-Phase Control

A Multi-Wing system without control may look like this:

```text
User request
  ↓
Planning Wing activates
  ↓
Generation Wing activates
  ↓
Review Wing activates
  ↓
Memory Wing activates
  ↓
Another Review Wing activates
  ↓
Generation Wing revises
  ↓
Review Wing reviews again
  ↓
System continues looping
```

This can create coordination overhead.

The system may become intelligent but restless.

## Multi-Wing With Five-Phase Control

A Multi-Wing system with Five-Phase control may look like this:

```text
User request
  ↓
Wood: detect direction
  ↓
Fire: activate only the needed generation wing
  ↓
Earth: integrate context
  ↓
Metal: critique, compress, and decide stop/continue
  ↓
Water: retain essence
  ↓
Stop or return to Wood
```

This creates a cleaner reasoning path.

The system does not ask every wing to act.

It activates the smallest sufficient path.

## Routing Relationship

Multi-Wing routing and Five-Phase routing operate at different levels.

## Multi-Wing Routing

Multi-Wing routing selects the appropriate wing.

Example:

```yaml
multi_wing_route:
  task: "Review this protocol draft."
  selected_wings:
    - critique_wing
    - context_wing
```

## Five-Phase Routing

Five-Phase routing selects the reasoning phase and control state.

Example:

```yaml
five_phase_route:
  current_phase: earth
  next_phase: metal
  state_transition:
    from: balanced
    to: yin
  reason: "The draft has enough context and now requires pruning."
```

## Combined Routing

A combined system may use both:

```yaml
combined_route:
  task: "Review this protocol draft."

  multi_wing:
    selected_wing: critique_wing

  five_phase:
    phase: metal
    state: yin
    action: prune_and_compress

  next:
    selected_wing: memory_wing
    phase: water
    action: retain_essence
```

This allows the system to decide both:

1. which wing should act
2. how that wing should act

## Integration Pattern 1: Five-Phase as Orchestration Policy

In this pattern, the Five-Phase protocol becomes the orchestration policy for Multi-Wing.

```yaml
orchestration_policy:
  name: five_phase_multi_wing_control
  default_cycle:
    - phase: wood
      wing: inquiry_wing
      action: detect_core_direction

    - phase: fire
      wing: generation_wing
      action: expand_selected_direction

    - phase: earth
      wing: context_wing
      action: check_context_and_coherence

    - phase: metal
      wing: critique_wing
      action: prune_and_evaluate_stopping

    - phase: water
      wing: memory_wing
      action: retain_essence
```

This is suitable for agentic systems where an orchestrator coordinates specialized agents.

## Integration Pattern 2: Five-Phase as Internal Reasoning Mode

In this pattern, a single wing may internally simulate the five phases.

For example, a `review_wing` may perform:

```text
Wood  = identify review target
Fire  = expand possible issues
Earth = check context
Metal = prune critique
Water = retain final review notes
```

This is suitable when each wing is powerful enough to run its own internal control cycle.

## Integration Pattern 3: Five-Phase as Meta-Wing

In this pattern, the Five-Phase protocol acts as a meta-wing above other wings.

```text
Five-Phase Controller
  ↓
selects and regulates
  ↓
Multi-Wing agents
```

The meta-wing does not generate the full answer itself.

It decides:

* which wing should activate
* how long it should act
* when critique should begin
* when memory should update
* when the cycle should stop

This pattern is useful for large Multi-Wing systems.

## Integration Pattern 4: Five-Phase as Minimal GPT Behavior

In this pattern, the protocol is implemented in a single GPT-style assistant.

The assistant does not expose all phases unless needed.

Internally, it follows:

```text
detect -> expand -> integrate -> prune -> retain
```

This is suitable for lightweight assistants such as an energy-aware reasoning GPT.

Example:

```text
省エネ丸 = a GPT that applies Metal and Water strongly
```

In this case, the GPT emphasizes:

* concise answers
* stopping when sufficient
* pruning weak branches
* retaining only next actions
* avoiding unnecessary expansion

## Relationship to Energy-Aware Reasoning

Multi-Wing systems can become computationally expensive if too many wings activate unnecessarily.

The Yin-Yang Five-Phase Reasoning Protocol supports energy-aware Multi-Wing behavior by encouraging:

* selective wing activation
* shorter reasoning routes
* earlier critique
* compression before memory
* stopping after sufficient output
* avoiding repeated review loops
* avoiding activation of irrelevant wings

This is a control-layer efficiency model.

It does not claim measured hardware-level energy reduction.

## Relationship to Critique Loops

Multi-Wing systems often use critique and revision loops.

A simple critique loop may look like this:

```text
Generate -> Critique -> Revise -> Critique -> Revise
```

This can improve quality, but it may also become endless.

The Five-Phase model adds stopping logic:

```text
Fire -> Earth -> Metal -> Water -> Stop
```

If revision is needed:

```text
Metal -> Fire -> Earth -> Metal -> Water
```

But if revision is not needed:

```text
Metal -> Water -> Stop
```

This prevents critique from becoming a loop without closure.

## Relationship to Memory

Multi-Wing systems often need memory.

However, memory can become a liability when it stores too much.

The Five-Phase model requires Water to retain only selected essence.

Memory should preserve:

* core claim
* key decision
* unresolved question
* next action
* useful pattern
* important constraint

Memory should avoid preserving:

* discarded branches
* redundant reasoning
* unsupported speculation
* temporary noise
* excessive context

This makes Multi-Wing memory more selective and less noisy.

## Relationship to Trace Systems

In a broader architecture, Water may connect to trace or provenance systems.

For example:

```text
Water phase
  ↓
retained essence
  ↓
trace record
  ↓
future retrieval or review
```

However, this protocol does not define a complete trace protocol.

It only defines how reasoning produces selected memory that could later be used by trace, audit, or retrieval systems.

## Example: Multi-Wing Reasoning Flow

```yaml
multi_wing_five_phase_flow:
  input:
    task: "Refine the README for this reasoning protocol."

  cycle:
    - phase: wood
      state: yang
      selected_wing: inquiry_wing
      action: detect_core_direction
      output:
        core_direction: "Make the README credible as a technical protocol."

    - phase: fire
      state: yang
      selected_wing: drafting_wing
      action: expand_relevant_sections
      output:
        draft_focus:
          - purpose
          - architecture
          - non_goals
          - examples

    - phase: earth
      state: balanced
      selected_wing: context_wing
      action: check_alignment
      output:
        alignment_note: "Avoid claiming measured energy reduction."

    - phase: metal
      state: yin
      selected_wing: critique_wing
      action: prune_and_correct
      output:
        critique:
          - "Reduce metaphysical language."
          - "Strengthen implementation framing."
          - "Keep energy claims conditional."

    - phase: water
      state: yin
      selected_wing: memory_wing
      action: retain_essence
      output:
        retained_essence: "Present the protocol as a control-layer reasoning model."
        next_action: "Add examples and validation schema."
```

## Example: Stopping a Multi-Wing Loop

```yaml
multi_wing_brake:
  detected_issue: repeated_review_loop

  current_loop:
    - generation_wing
    - critique_wing
    - generation_wing
    - critique_wing

  five_phase_intervention:
    phase: metal
    state: yin
    action: evaluate_stopping_condition

  decision:
    status: stop_after_memory_retention
    reason: "The output is already sufficient and further revision adds little value."

  final_route:
    - phase: water
      selected_wing: memory_wing
      action: retain_core_trace
```

## Example: Water-to-Wood Return in Multi-Wing

```yaml
water_to_wood_multi_wing_return:
  previous_phase:
    phase: water
    selected_wing: memory_wing
    retained_essence: "The protocol needs clearer brake conditions."
    unresolved_question: "How should stopping rules be represented?"

  next_phase:
    phase: wood
    selected_wing: inquiry_wing
    action: convert_memory_to_new_direction
    inquiry_vector: "Define stopping rules as machine-readable brake conditions."
```

## Compatibility Principles

## 1. Do Not Force One-to-One Mapping

A Multi-Wing system may have more or fewer wings than the Five Phases.

The Five-Phase model should guide reasoning function, not force naming.

## 2. Use the Smallest Sufficient Route

Not every task needs all wings.

A simple answer may require only:

```text
Wood -> Metal -> Water
```

A complex architecture task may require:

```text
Wood -> Fire -> Earth -> Metal -> Water
```

## 3. Let Critique Close the Loop

Critique should not create endless revision.

Metal should produce a stop-or-continue decision.

## 4. Filter Memory Before Retention

Water should retain selected essence, not raw conversation.

Earth may filter Water when memory becomes noisy.

## 5. Preserve Human or System Review Where Needed

This protocol can support automation, but it does not remove the need for review.

For important tasks, Multi-Wing outputs may still require human, governance, or system-level validation.

## Non-Goals

This document does not claim that:

* Multi-Wing architecture must use exactly five wings
* Five-Phase roles must be implemented as separate models
* this protocol replaces existing orchestration frameworks
* this protocol guarantees measured energy savings
* this protocol guarantees truth, safety, or alignment
* all reasoning should always pass through every phase

The goal is to define a compatible control model.

## Summary

Multi-Wing and the Yin-Yang Five-Phase Reasoning Protocol are complementary.

```text
Multi-Wing distributes intelligence.
Yin-Yang Five-Phase regulates intelligence.
```

Multi-Wing provides wings.

This protocol provides breath.

Together, they support a reasoning architecture that can:

* activate selectively
* expand only when useful
* integrate context
* critique itself
* stop when sufficient
* retain only essence
* return to a refined next direction

The final relationship can be summarized as:

```text
Multi-Wing = distributed reasoning body
Yin-Yang = activation rhythm
Five-Phase = reasoning organ system
Brake Layer = self-regulation
Water-to-Wood Return = recursive learning loop
```

In short:

```text
Multi-Wing gives the system many wings.
Yin-Yang Five-Phase teaches it when to fly, when to glide, and when to land.
```
