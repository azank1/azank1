**Production systems engineer. I build AI agents and the systems that check them.**
I turn research questions into working software: measurable, inspectable, and useful past the demo.

[![Metaorcha](https://img.shields.io/badge/building-metaorcha.ai-2b2b2b?style=flat-square&labelColor=181818)](https://metaorcha.ai)
[![X](https://img.shields.io/badge/X-%40azankhyder-2b2b2b?style=flat-square&labelColor=181818&logo=x&logoColor=white)](https://x.com/azankhyder)

### Now

- **Production** · CRM DevOps and AI engineering (conveyancing + transport-routing real-time system scaling): the harness around live production CRMs/CMSs. [The method](https://azanhyder-port.vercel.app/research/#production)
- **Building** · [Metaorcha](https://metaorcha.ai), an open runtime where one goal becomes a verified multi-agent run. [Metabot](https://metaorcha.ai/metabot), the agent on top, is in progress.
- **Writing** · [The Harness Layer](https://dev.to/azankhyder/series/42904), field notes on agent harnesses, each with an artifact you can re-run.


### Repos, most involved first

<a href="https://github.com/solvent-labs-org/metaorcha"><img src="assets/bands/metaorcha.svg" width="100%" alt="metaorcha"></a>
<a href="https://github.com/azank1/seamkit"><img src="assets/bands/seamkit.svg" width="100%" alt="seamkit"></a>
<a href="https://github.com/azank1/agent-exposure"><img src="assets/bands/agent-check.svg" width="100%" alt="agent-check"></a>
<a href="https://github.com/azank1/guardrails-kit"><img src="assets/bands/guardrails-kit.svg" width="100%" alt="guardrails-kit"></a>
<a href="https://github.com/azank1/cdv"><img src="assets/bands/cdv.svg" width="100%" alt="conservative-dual-verify"></a>

More: [commit-city](https://github.com/azank1/commit-city) · [RP2A](https://github.com/azank1/restaurant-provider-to-agent) · [sdca-raqqr](https://github.com/azank1/sdca-raqqr)

### Measured

- **5/5** multi-protocol runs verified live, best wall clock 13 s · [Metaorcha](https://github.com/solvent-labs-org/metaorcha)
- **41%** fewer agent steps than a fixed budget, replicated to the digit, along with the case that breaks it · [field note 009](https://dev.to/azankhyder/a-stop-rule-that-trusts-one-score-is-worse-than-a-dumb-budget-428c)
- **25** typed MCP tools behind a production voice-ordering agent · [RP2A](https://github.com/azank1/restaurant-provider-to-agent)
- **290+** tests under a multi-tenant restaurant OS, built by a five-person team I led · Zayup
- **3 weeks** to a complete React Native MVP, directing a three-developer team · DeliveryOS

### Recent public activity

| date | where | what | outcome |
|---|---|---|---|
| Oct 31 | [agent-check](https://github.com/azank1/agent-exposure/releases/tag/v1.1.0) | v1.1.0: now flags comment-triggered checkouts, and documents a fix for every finding | released |
| Oct 31 | [guardrails-kit](https://github.com/azank1/guardrails-kit) | fail-closed Claude Code hooks for team repos, with tests | released |
| Oct 19 | [tmux #5775](https://github.com/tmux/tmux/pull/5775) | `^` matched again mid-string in format substitutions, since 2019 | applied upstream 10 h later, regress test credited |
| Oct 18 | [blackbox_exporter #1715](https://github.com/prometheus/blackbox_exporter/pull/1715) | target URLs percent-decoded twice since 0.29.0 | open, awaiting review |
| Oct 16 | [huggingface_hub #5180](https://github.com/huggingface/huggingface_hub/issues/5180) | `hf skills add --force` replaced a skill with a symlink to itself | fixed in-house in v2.3.0, report credited |
| Oct 15 | [ECC #3591](https://github.com/affaan-m/ECC/pull/3591) | SessionStart hook crashed in every project on plugin installs | merged Oct 29; on Windows 0/27 → 26/27 hooks passing |
| Oct 15 | [vercel-plugin #343](https://github.com/vercel/vercel-plugin/pull/343) | session-start context overran Claude Code's hook output cap | open; a Vercel engineer extended it on the branch |
| Oct 15 | [BMAD-METHOD #3094](https://github.com/bmad-code-org/BMAD-METHOD/issues/3094) | update drops the config of a module kept without a source | open issue |

What the feedback taught:

- A minimal reproduction with a regression test gets applied as written. Without one, maintainers rewrite the fix in-house, which is fine when the credit stays.
- Big projects merge in batches. ECC took two weeks; meanwhile an outside contributor verified the fix independently, which helped it land.
- When a maintainer pushes to your branch, follow their direction. The Vercel change grew from a trim into splitting the context into parts under the cap.
- Severity should follow what the job can actually do, not the pattern it matches. agent-check grades that way.

### Writing

[The Harness Layer](https://dev.to/azankhyder/series/42904): field notes on agent harnesses, each with sources, its limits and an artifact you can re-run.

- [When should an agent stop?](https://dev.to/azankhyder/a-stop-rule-that-trusts-one-score-is-worse-than-a-dumb-budget-428c) · Sep 2026
- [Web chat is not a coding environment](https://dev.to/azankhyder/web-chat-is-not-a-coding-environment-2m77) · Sep 2026
- [Pacing the frontier does not watch the agents](https://dev.to/azankhyder/pacing-the-frontier-does-not-watch-the-agents-4i5o) · Sep 2026
- [Models converged. Trust hasn't.](https://dev.to/azankhyder/models-converged-trust-hasnt-1k53) · Aug 2026
- [I turned GitHub into a 3D city, then pressed A and saw who is really writing the code](https://dev.to/azankhyder/i-turned-github-into-a-3d-city-then-pressed-a-and-saw-who-is-really-writing-the-code-4jn2) · launch post, Oct 2026

### Stack

- **Agents** · MCP, A2A, computer use, LangGraph, LLM evaluation, Claude Code, Codex, Cursor
- **Agent security** · Claude Code hooks and permissions, MCP config review, GitHub Actions agent jobs
- **Production** · FastAPI, Next.js, Postgres, Supabase, pgvector, Redis, Vercel, Cloudflare Workers
- **Stats** · OpenTelemetry, Bayesian optimization, backtesting, KMeans and PCA
- **Languages** · Python, TypeScript, SQL, Bash, Solidity

### Activity

<a href="https://github.com/azank1">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=azank1&border_radius=16&border=2f2f2f&background=181818&stroke=2f2f2f&ring=ff5f1f&fire=ff5f1f&currStreakLabel=ff8a50&currStreakNum=e4e4e4&sideNums=e4e4e4&sideLabels=a3a3a3&dates=737373">
    <img src="https://streak-stats.demolab.com?user=azank1&border_radius=16&border=e2e2e1&background=fbfbfa&stroke=e2e2e1&ring=ff5f1f&fire=ff5f1f&currStreakLabel=c2410c&currStreakNum=171717&sideNums=171717&sideLabels=525252&dates=737373" width="49%" alt="GitHub streak stats for azank1: total contributions, current streak and longest streak">
  </picture>
</a>

### On carving your own path

**Side quests used to be what you did after work. I made them the work, and made it respectable.**

The method was simple: doubt every source except my own judgment, then keep retraining how I decide
things, scoring each move by how much it widened my exposure to lucky breaks. Run that loop long enough
and your choices converge on the handful that actually pay off, while a small share of every attempt
still goes to wandering on purpose.

Where it led: companies with nobody on payroll, built one day at a time as my way out of a class that
was never meant to move.

If you want a path that's genuinely yours, my one piece of advice is to defend your mind like it's
production. Trends flip. Focus erodes. Someone will always be trying to slip their narrative past your
filters and edit your worldview for you. Don't accept the patch.

**Outlast the noise and you win.**

---

Working on agent runtimes, protocol bridges or verification? [Open an issue on Metaorcha](https://github.com/solvent-labs-org/metaorcha/issues).

<sub>[metaorcha.ai](https://metaorcha.ai) · [X](https://x.com/azankhyder) · *It's all relative.*</sub>
