# Life Betterment Simulation

[![CI](https://github.com/organvm-ii-poiesis/life-betterment-simulation/actions/workflows/ci.yml/badge.svg)](https://github.com/organvm-ii-poiesis/life-betterment-simulation/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-pending-lightgrey)](https://github.com/organvm-ii-poiesis/life-betterment-simulation)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/organvm-ii-poiesis/life-betterment-simulation/blob/main/LICENSE)
[![Organ II](https://img.shields.io/badge/Organ-II%20Poiesis-EC4899)](https://github.com/organvm-ii-poiesis)
[![Status](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/organvm-ii-poiesis/life-betterment-simulation)
[![Python](https://img.shields.io/badge/lang-Python-informational)](https://github.com/organvm-ii-poiesis/life-betterment-simulation)


[![CI](https://github.com/organvm-ii-poiesis/life-betterment-simulation/actions/workflows/ci-minimal.yml/badge.svg)](https://github.com/organvm-ii-poiesis/life-betterment-simulation/actions)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![ORGAN-II: Art](https://img.shields.io/badge/ORGAN--II-Art-6a1b9a?style=flat-square)](https://github.com/organvm-ii-poiesis)
[![Status: DESIGN_ONLY](https://img.shields.io/badge/status-DESIGN__ONLY-lightgrey?style=flat-square)]()
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

**An interactive simulation exploring social influence theory, dating dynamics, and personal growth through experiential narrative design -- combining dating sim mechanics with behavioral science to create a reflective tool for understanding social dynamics and self-improvement.**

---

## Table of Contents

1. [Conceptual Framework](#1-conceptual-framework)
2. [Solution Overview](#2-solution-overview)
3. [Technical Architecture](#3-technical-architecture)
4. [Installation and Setup](#4-installation-and-setup)
5. [Usage](#5-usage)
6. [Working Examples](#6-working-examples)
7. [Research Foundation](#7-research-foundation)
8. [Testing and Quality](#8-testing-and-quality)
9. [Cross-References](#9-cross-references)
10. [Contributing](#10-contributing)
11. [License and Author](#11-license-and-author)

---

## 1. Conceptual Framework

### Why a Dating Sim for Self-Improvement?

Most self-improvement tools operate on a broadcast model: they tell you what to do, present frameworks as inert diagrams, and measure progress through checklists. Life Betterment Simulation inverts this relationship. Instead of reading about social influence theory, you inhabit it. Instead of studying relationship dynamics from the outside, you make choices inside a narrative system and observe the downstream consequences of those choices across an interconnected social network.

The dating sim genre is one of the oldest forms of interactive narrative. Its core mechanic -- make a choice, observe a consequence, adjust your strategy -- maps precisely onto the experiential learning cycle that Kolb formalized in 1984. What the genre lacks is intellectual rigor. What behavioral science lacks is emotional engagement. This project occupies the space between those two deficiencies.

### Social Influence Theory: "Beyond the Five"

Robert Cialdini's six principles of influence (reciprocity, commitment/consistency, social proof, authority, liking, and scarcity) remain the canonical framework taught in every psychology and marketing curriculum. They were formulated through decades of field research and laboratory experiments. They are also incomplete for the world we now inhabit.

Life Betterment Simulation extends Cialdini's framework with what we call "Beyond the Five" -- three additional influence dynamics that emerge specifically in digital-age social environments:

1. **Social Contagion.** Behaviors, emotions, and attitudes spread through social networks in patterns that resemble epidemiological transmission. The Christakis-Fowler "three degrees of influence" finding -- that your friend's friend's friend affects your behavior -- becomes a first-class mechanic in the simulation. Your choices ripple outward through the simulated social graph, and choices made by distant nodes ripple back to you.

2. **Parasocial Relationships.** One-directional emotional bonds with media figures, influencers, and online personalities shape real-world decision-making in ways Cialdini's framework does not capture. The simulation includes parasocial characters -- figures you observe but cannot directly interact with -- whose influence on your network operates through different channels than direct relationships.

3. **Algorithmic Influence.** Recommendation systems, feed curation, and attention-capture mechanics create influence patterns that have no analog in face-to-face social environments. The simulation's narrative engine itself acts as a kind of algorithm, surfacing certain storylines and suppressing others based on your prior choices, making the medium itself part of the message.

### The Friend Zone as Social Dynamics Laboratory

The "friend zone" is a culturally loaded term that typically obscures more than it reveals. In this simulation, we reclaim it as a precise social dynamics concept: the boundary condition where one party's relational expectations diverge from the other's, and both parties must negotiate the resulting asymmetry. This is not a trivial problem. It is one of the most common interpersonal challenges humans face, and it involves every major influence principle simultaneously: reciprocity (what do I owe?), commitment (what did I signal?), social proof (what does my network expect?), and scarcity (is this my only chance?).

The Friend Zone Contagion Model -- one of the core interactive components -- visualizes how relationship-pattern templates propagate through social networks. When one person in a friend group adopts a particular relational stance (avoidance, pursuit, boundary-setting, radical honesty), that stance influences adjacent relationships through observation, conversation, and social proof. The simulation makes this contagion visible and manipulable.

---

## 2. Solution Overview

### Simulation Architecture

Life Betterment Simulation is not a single application but a constellation of interconnected components, each addressing a different facet of the self-improvement-through-narrative thesis:

```
+-----------------------------------------+
|       Interactive Narrative Engine       |
|  (dating sim mechanics, choice trees,   |
|   branching storylines, stat tracking)  |
+---+---------+---------+--------+--------+
    |         |         |        |
    v         v         v        v
+-------+ +-------+ +-------+ +--------+
|Social | |Human  | |Eastern| |Guided  |
|Influ. | |Design | |Cosmos | |Journal |
|Theory | |Sched. | |Integr.| |System  |
|Engine | |Mapper | |Module | |        |
+-------+ +-------+ +-------+ +--------+
    |         |         |        |
    v         v         v        v
+-----------------------------------------+
|         Visualization Layer             |
|  (Friend Zone Contagion, Spiral Anim., |
|   network graphs, stat dashboards)     |
+-----------------------------------------+
```

**Interactive Narrative Engine** sits at the center. It manages story state, processes player choices, and coordinates with the four satellite modules:

- **Social Influence Theory Engine** evaluates each choice against Cialdini's principles plus the three digital-age extensions, computing influence scores and propagating effects through the social graph.
- **Human Design Schedule Mapper** takes the player's Human Design profile (type, strategy, authority, defined/undefined centers, active gates) and generates personalized scheduling recommendations that integrate with the narrative timeline.
- **Eastern Cosmos Integration Module** provides philosophical context for narrative events, drawing from Buddhist impermanence, Taoist wu-wei, Vedantic self-inquiry, and Confucian relational ethics.
- **Guided Journal System** produces daily prompts informed by the player's simulation choices, loosely structured after Hesse's Siddhartha -- a 30-day progression from seeking, through disillusionment, toward integration.

### Narrative Engine Design

The narrative engine uses a graph-based story structure rather than a tree. Traditional dating sims present binary or ternary choices that branch into independent paths. This simulation allows paths to reconverge, creating situations where two players who made very different early choices can arrive at the same narrative moment with different internal states (different influence scores, different relationship histories, different growth stats). The consequence is that the same scene reads differently depending on how you arrived there.

Story nodes carry metadata beyond their text content: required influence thresholds, relationship prerequisites, growth-stat gates, and philosophical alignment tags. A player who has been making choices aligned with wu-wei (non-forcing, yielding, following natural flow) will encounter different framing text than a player who has been making assertive, boundary-setting choices -- even in the same scene.

### Personal Growth Statistics

The simulation tracks five core growth dimensions:

| Dimension | Description | Influenced By |
|-----------|-------------|---------------|
| **Authenticity** | Alignment between expressed and internal values | Consistency of choices across contexts |
| **Resilience** | Recovery speed from negative social outcomes | Exposure to and navigation of rejection/conflict |
| **Empathy** | Accuracy of social perception and emotional attunement | Listening choices, perspective-taking actions |
| **Boundaries** | Clarity and maintenance of personal limits | Frequency and consistency of boundary assertions |
| **Agency** | Sense of authorship over one's social trajectory | Proactive vs. reactive choice patterns |

These are not gamified metrics with obvious "good" directions. High Agency combined with low Empathy produces a different character archetype than low Agency with high Empathy. The simulation does not judge; it reveals patterns.

---

## 3. Technical Architecture

### Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Interactive Simulations** | HTML5 + Vanilla JavaScript (ES6+) | Core narrative engine, choice processing, stat tracking |
| **Visualizations** | HTML5 Canvas + CSS3 Animations | Friend Zone Contagion model, spiral growth animation |
| **Styling** | CSS3 (custom properties, grid, flexbox) | Responsive layouts, animation keyframes, theme system |
| **Design Documents** | DOCX | Research papers, social influence theory framework, design specs |
| **Data Format** | JSON | Story graph nodes, influence parameters, schedule mappings |

### Component Inventory

```
life-betterment-simulation/
  src/
    narrative/
      engine.js            # Story graph traversal, state management
      nodes.json           # Story node definitions with metadata
      influence.js         # Cialdini + "Beyond the Five" computations
      contagion.js         # Social graph propagation algorithms
    schedule/
      human-design.js      # Energy type / center / gate mapping
      optimizer.js         # Schedule generation from HD profile
    cosmos/
      eastern-wisdom.js    # Philosophy module (Buddhist/Taoist/Vedantic/Confucian)
      alignment.js         # Choice-to-philosophy alignment scoring
    journal/
      prompts.js           # 30-day Siddhartha-inspired prompt generator
      reflection.js        # Outcome-to-reflection integration
  viz/
    friend-zone-contagion/
      index.html           # Standalone HTML visualization
      contagion.js         # D3-style force-directed social graph
      styles.css           # Visualization theming
    spiral-animation/
      index.html           # Growth trajectory spiral
      spiral.js            # Canvas-based animated spiral renderer
      styles.css           # Animation CSS
  docs/
    beyond-the-five.docx   # Social influence theory framework paper
    human-design-mapping.docx  # HD schedule methodology
    eastern-cosmos.docx    # Eastern philosophy integration rationale
    research-bibliography.docx # Annotated bibliography
  assets/
    portraits/             # Character portrait assets
    audio/                 # Ambient audio for narrative scenes
  index.html               # Main simulation entry point
  styles.css               # Global stylesheet
  package.json             # Dependencies (dev server, linting)
```

### Social Graph Data Model

The social graph uses an adjacency list representation with weighted, typed edges:

```javascript
const socialGraph = {
  nodes: [
    { id: "player", type: "protagonist", stats: { auth: 0, res: 0, emp: 0, bnd: 0, agn: 0 } },
    { id: "alex", type: "romantic_interest", affinity: 0.3, archetype: "challenger" },
    { id: "jordan", type: "friend", affinity: 0.7, archetype: "mirror" },
    { id: "influence_figure", type: "parasocial", reach: 0.9, visibility: "public" }
  ],
  edges: [
    { source: "player", target: "alex", weight: 0.5, type: "attraction", reciprocated: false },
    { source: "player", target: "jordan", weight: 0.8, type: "friendship", reciprocated: true },
    { source: "jordan", target: "alex", weight: 0.4, type: "acquaintance", reciprocated: true }
  ]
};
```

Edges carry a `type` (friendship, attraction, rivalry, mentorship, parasocial), a `weight` (0.0-1.0 closeness), and a `reciprocated` flag. The contagion model propagates influence along edges with decay proportional to inverse weight, consistent with Granovetter's weak-ties theory: low-weight connections often transmit novel information more effectively than high-weight bonds.

---

## 4. Installation and Setup

### Prerequisites

- A modern web browser (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- For local development: Node.js 18+ and npm (optional, for dev server and linting)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/organvm-ii-poiesis/life-betterment-simulation.git
cd life-betterment-simulation

# Option A: Open directly in browser (no build step)
open index.html

# Option B: Use a local dev server
npx serve .
# → Open http://localhost:3000
```

### Development Setup

```bash
# Install development dependencies (linting, formatting, local server)
npm install

# Start development server with live reload
npm run dev

# Run linter
npm run lint

# Format code
npm run format
```

### Human Design Profile Configuration

To use the schedule mapping feature, create a profile file:

```bash
cp assets/templates/hd-profile.example.json my-profile.json
```

Edit `my-profile.json` with your Human Design chart data:

```json
{
  "type": "Generator",
  "strategy": "respond",
  "authority": "sacral",
  "defined_centers": ["sacral", "root", "solar_plexus"],
  "undefined_centers": ["head", "ajna", "throat", "g_center", "heart", "spleen"],
  "active_gates": [34, 20, 57, 10, 25]
}
```

---

## 5. Usage

### Interaction Patterns

**Narrative Mode.** The primary interaction is reading narrative text and making choices. Each scene presents a social situation -- a conversation, a group gathering, a one-on-one encounter, a moment of internal reflection -- and offers 2-4 response options. Options are not labeled "good" or "bad." They represent different relational strategies, each with distinct downstream consequences.

```
Scene: Coffee shop. Alex sits across from you, phone face-down on the table.
"I keep thinking about what you said last week," Alex says. "About patterns."

  [A] "Which pattern specifically?" (Empathy probe — seek understanding)
  [B] "I say a lot of things. Remind me." (Boundary assertion — protect emotional labor)
  [C] Stay quiet. Let the silence do the work. (Wu-wei alignment — non-forcing)
  [D] "Patterns repeat until you see them." (Authenticity expression — share belief)
```

**Journal Mode.** After each narrative session, the journal system generates a reflection prompt tied to your recent choices. Day 1 prompts are concrete and situation-specific. By Day 15, prompts become increasingly abstract. By Day 30, prompts dissolve into open-ended contemplation, mirroring Siddhartha's progression from seeking to being.

Example Day 7 prompt (generated from a player who chose boundary-assertion options frequently):

> You have been drawing lines. Walls protect, but walls also isolate. Write about a boundary you hold that costs you something you want. Is the cost justified? How would you know?

**Schedule Mode.** Access your personalized daily schedule by loading your Human Design profile. The optimizer maps your energy type to activity blocks:

- **Generators** receive schedules front-loaded with responsive, high-energy work
- **Projectors** receive schedules with rest-recognition-rest rhythms
- **Manifestors** receive schedules with initiation bursts and recovery valleys
- **Reflectors** receive schedules that vary with the lunar cycle

### Workflow: A Typical Session

1. Open the simulation (5 minutes to orient)
2. Play 2-3 narrative scenes, making choices (15-20 minutes)
3. Review your influence dashboard and growth stats (5 minutes)
4. Complete the daily journal prompt (10-15 minutes)
5. Optionally review your schedule map for tomorrow (5 minutes)

Total: approximately 40 minutes per session, designed for a 30-day arc.

---

## 6. Working Examples

### Friend Zone Contagion Visualization

Open `viz/friend-zone-contagion/index.html` in any modern browser to see the social contagion model in action. The visualization renders a force-directed graph of 15-20 social nodes. Click any node to "infect" it with a relational pattern (friend-zoning, pursuit escalation, healthy boundary-setting, or avoidance). Watch the pattern propagate through the network over simulated time steps.

Key behaviors to observe:

- **Cluster effects.** Tightly connected subgroups adopt patterns faster than loosely connected ones.
- **Bridge nodes.** Individuals connecting two clusters act as transmission bottlenecks. A single bridge node with high resistance can prevent pattern spread entirely.
- **Weak-tie transmission.** Counterintuitively, novel patterns sometimes spread faster through weak connections (acquaintances) than strong ones (close friends), because close friends have already converged on shared norms.

Controls:

| Control | Effect |
|---------|--------|
| Click node | Infect with selected pattern |
| Dropdown | Select pattern type (friend-zone, pursuit, boundary, avoidance) |
| Slider | Adjust transmission probability (0.1 - 0.9) |
| Play/Pause | Start/stop simulation clock |
| Reset | Return all nodes to neutral state |

### Spiral Growth Animation

Open `viz/spiral-animation/index.html` to see a canvas-rendered spiral that represents personal growth trajectories. The spiral is not a simple outward expansion. It loops back through familiar territory at higher altitudes -- the visual metaphor for the insight that growth means encountering the same problems from a more developed vantage point.

The spiral renders dynamically based on a growth-stat array. Feed it different stat profiles to see how different growth patterns produce different spiral geometries:

- Balanced growth produces a symmetrical, gradually expanding spiral
- Lopsided growth (high Agency, low Empathy) produces an eccentric, wobbling spiral
- Stagnation produces a tightening spiral that collapses inward

### Schedule Mapping Output

With a Generator-type Human Design profile loaded, the schedule mapper produces output like:

```
06:00 - 07:00  [SACRAL REST]     Morning stillness. Wait for response.
07:00 - 09:00  [RESPOND BLOCK]   High-energy work responding to requests/tasks
09:00 - 09:30  [INTEGRATION]     Reflect on morning energy expenditure
09:30 - 12:00  [RESPOND BLOCK]   Deep work on projects that "light up" sacral
12:00 - 13:00  [NOURISH]         Meal + social connection (recharge)
13:00 - 15:00  [RESPOND BLOCK]   Afternoon responsive work
15:00 - 15:30  [SACRAL CHECK]    Is the sacral still engaged? Honest body scan.
15:30 - 17:00  [FLEXIBLE]        Continue or shift based on sacral response
17:00 - 21:00  [WIND DOWN]       Decreasing intensity, social, creative play
21:00 - 22:00  [DISCHARGE]       Physical movement to burn remaining sacral energy
```

---

## 7. Research Foundation

### Academic Grounding

This project draws from peer-reviewed research across social psychology, network science, behavioral economics, and contemplative traditions. It does not claim to be a clinical tool. It is an experiential narrative system designed to make abstract social science concepts tangible through interactive storytelling.

### Core Theoretical Frameworks

**Social Influence.** Cialdini's six principles (1984, 2001, 2021) provide the backbone. The "Beyond the Five" extensions draw from Christakis and Fowler's network influence research (2007, 2009), Horton and Wohl's parasocial interaction theory (1956), and Pariser's filter bubble work (2011).

**Social Contagion.** The Friend Zone Contagion Model is grounded in Centola's complex contagion research (2010, 2018), which demonstrates that behavior adoption in social networks follows different rules than disease transmission -- requiring reinforcement from multiple network neighbors rather than single exposure.

**Narrative as Cognition.** The use of interactive narrative as a psychological tool draws from Bruner's narrative cognition framework (1986, 1990), Murray's work on procedural authorship in digital environments (1997), and Bogost's concept of procedural rhetoric (2007).

**Human Design.** The schedule mapping component adapts Ra Uru Hu's Human Design system (1992) as a heuristic for energy management. We do not endorse Human Design as empirically validated science. We use it as a structured self-reflection framework with sufficient specificity to generate actionable schedule recommendations.

**Eastern Philosophy.** The journal system's Siddhartha-inspired arc draws from Hesse (1922), but the philosophical integration module references primary sources: the Tao Te Ching (Laozi), the Dhammapada (Theravada Buddhism), the Bhagavad Gita (Vedantic tradition), and the Analects (Confucius).

### Theory Bibliography

| Source | Year | Contribution to This Project |
|--------|------|------------------------------|
| Cialdini, R. *Influence: Science and Practice* | 1984 | Six principles of persuasion as core mechanic |
| Cialdini, R. *Influence, New and Expanded* | 2021 | Unity principle; updated digital-age examples |
| Christakis, N. & Fowler, J. *Connected* | 2009 | Three degrees of influence rule; network effects |
| Centola, D. *How Behavior Spreads* | 2018 | Complex contagion; reinforcement thresholds |
| Granovetter, M. "The Strength of Weak Ties" | 1973 | Weak-tie transmission mechanics |
| Horton, D. & Wohl, R. "Mass Communication and Para-Social Interaction" | 1956 | Parasocial relationship theory |
| Pariser, E. *The Filter Bubble* | 2011 | Algorithmic influence on perception |
| Bruner, J. *Actual Minds, Possible Worlds* | 1986 | Narrative as cognitive mode |
| Murray, J. *Hamlet on the Holodeck* | 1997 | Procedural authorship; agency in digital narrative |
| Bogost, I. *Persuasive Games* | 2007 | Procedural rhetoric; games as argument |
| Hesse, H. *Siddhartha* | 1922 | 30-day journal arc structure |
| Kolb, D. *Experiential Learning* | 1984 | Experience-reflection-conceptualization-experimentation cycle |
| Ra Uru Hu. *The Human Design System* | 1992 | Energy type and center-based scheduling heuristic |

---

## 8. Testing and Quality

### Current Status

This repository has a `DESIGN_ONLY` implementation status. The design documents, research framework, and visualization prototypes exist. The full narrative engine and integration layer are specified but not yet implemented. Testing infrastructure is planned for the implementation phase.

### Planned Testing Strategy

**Visualization Tests.** The Friend Zone Contagion and Spiral Animation components will use browser-based testing with headless Chrome:

```bash
# Run visualization tests (planned)
npm test -- --filter=viz

# Test contagion propagation math
npm test -- --filter=contagion

# Test schedule optimizer output
npm test -- --filter=schedule
```

**Narrative Graph Validation.** Story nodes will be validated for:
- Reachability (no orphan nodes)
- Completeness (all branches terminate)
- Stat consistency (no negative stats, no overflow)
- Philosophical alignment coherence (tags match content)

**Manual Playtesting Protocol.** Given the experiential nature of the project, automated tests supplement but do not replace human playtesting. A structured playtesting protocol will assess:
- Choice meaningfulness (do players feel their choices matter?)
- Narrative coherence (do story transitions feel natural?)
- Journal prompt relevance (do prompts connect to recent gameplay?)
- Schedule utility (do generated schedules feel actionable?)

### Linting and Code Quality

```bash
# ESLint with standard configuration
npm run lint

# Prettier for consistent formatting
npm run format
```

---

## 9. Cross-References

### Within ORGAN II (Art)

Life Betterment Simulation connects to several other repositories in the `organvm-ii-poiesis` organization:

| Repository | Relationship |
|-----------|--------------|
| [`metasystem-master`](https://github.com/organvm-ii-poiesis/metasystem-master) | The canonical ORGAN-II monorepo; provides the performance engine patterns that influence the narrative engine design |
| [`example-interactive-installation`](https://github.com/organvm-ii-poiesis/example-interactive-installation) | Shares interaction design patterns for sensor-driven narrative experiences |
| [`example-ai-collaboration`](https://github.com/organvm-ii-poiesis/example-ai-collaboration) | The AI-conductor model used for generating narrative content and journal prompts |
| [`showcase-portfolio`](https://github.com/organvm-ii-poiesis/showcase-portfolio) | Aggregates this project's visualizations into the ORGAN-II portfolio |
| [`example-theatre-dialogue`](https://github.com/organvm-ii-poiesis/example-theatre-dialogue) | Interactive dialogue patterns that inform the narrative engine's conversation scenes |

### Across the Eight-Organ System

| Organ | Connection |
|-------|-----------|
| **ORGAN I** (Theory) | The social influence framework extends ontological modeling patterns from [`narratological-algorithmic-lenses`](https://github.com/organvm-i-theoria/narratological-algorithmic-lenses) |
| **ORGAN III** (Commerce) | Potential productization path as a self-improvement SaaS tool via [`commerce--meta`](https://github.com/organvm-iii-ergon/commerce--meta) |
| **ORGAN IV** (Orchestration) | Governance and state management patterns from [`orchestration-start-here`](https://github.com/organvm-iv-taxis/orchestration-start-here) |
| **ORGAN V** (Public Process) | Building-in-public essays documenting the design process at [`public-process`](https://github.com/organvm-v-logos/public-process) |

### System Documentation

For the complete architecture of the eight-organ system, see the [meta-system corpus](https://github.com/meta-organvm/organvm-corpvs-testamentvm).

---

## 10. Contributing

Contributions are welcome. This project is currently in the design phase (`DESIGN_ONLY`), which means the most valuable contributions right now are:

1. **Design feedback.** Open an issue with the `design` label to discuss the social influence framework, narrative structure, or philosophical integration approach.
2. **Research references.** If you know of relevant peer-reviewed work on social contagion, serious games, or interactive narrative for self-improvement, open a PR adding it to the bibliography.
3. **Visualization improvements.** The Friend Zone Contagion and Spiral Animation components are functional prototypes. CSS, Canvas rendering, and interaction design improvements are welcome.
4. **Playtesting.** Once narrative content is drafted, structured playtesting feedback will be the most valuable input.

### Development Workflow

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/life-betterment-simulation.git
cd life-betterment-simulation

# Create a feature branch
git checkout -b feature/your-contribution

# Make changes, test locally
npx serve .

# Commit with descriptive message
git commit -m "add: contagion decay rate slider to visualization"

# Push and open PR
git push origin feature/your-contribution
```

### Code Conventions

- Vanilla JavaScript (ES6+), no framework dependencies for core simulation
- Semantic HTML5 for all interactive components
- CSS custom properties for theming (no preprocessors)
- JSDoc comments for all public functions
- Descriptive variable names over terse abbreviations

---

## 11. License and Author

**License:** [MIT](LICENSE)

**Author:** [@4444j99](https://github.com/4444j99)

**Organization:** [organvm-ii-poiesis](https://github.com/organvm-ii-poiesis) -- ORGAN II: Art (Poiesis)

This repository is part of the eight-organ creative-institutional system coordinating 81 repositories across 8 GitHub organizations:

| Organ | Domain | Organization |
|-------|--------|-------------|
| I | Theory | [organvm-i-theoria](https://github.com/organvm-i-theoria) |
| **II** | **Art** | [**organvm-ii-poiesis**](https://github.com/organvm-ii-poiesis) |
| III | Commerce | [organvm-iii-ergon](https://github.com/organvm-iii-ergon) |
| IV | Orchestration | [organvm-iv-taxis](https://github.com/organvm-iv-taxis) |
| V | Public Process | [organvm-v-logos](https://github.com/organvm-v-logos) |
| VI | Community | [organvm-vi-koinonia](https://github.com/organvm-vi-koinonia) |
| VII | Marketing | [organvm-vii-kerygma](https://github.com/organvm-vii-kerygma) |
| Meta | Governance | [meta-organvm](https://github.com/meta-organvm) |

---

<sub>Part of the [organvm](https://github.com/meta-organvm/organvm-corpvs-testamentvm) system. ORGAN II: Art -- where theory becomes experience.</sub>
