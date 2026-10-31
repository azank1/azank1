**Production systems engineer. I build AI agents and the systems that check them.**
I turn research questions into working software: measurable, inspectable, and useful past the demo.

[![Portfolio](https://img.shields.io/badge/portfolio-azanhyder--port.vercel.app-ff5f1f?style=flat-square&labelColor=181818)](https://azanhyder-port.vercel.app)
[![Metaorcha](https://img.shields.io/badge/building-metaorcha.ai-2b2b2b?style=flat-square&labelColor=181818)](https://metaorcha.ai)
[![dev.to](https://img.shields.io/badge/dev.to-%40azankhyder-2b2b2b?style=flat-square&labelColor=181818&logo=devdotto&logoColor=white)](https://dev.to/azankhyder)
[![Fixed-price work](https://img.shields.io/badge/fixed--price%20work-agent%20security%20%C2%B7%20Claude%20Code%20setup-2b2b2b?style=flat-square&labelColor=181818)](https://azank1.github.io/offer-site/)
[![X](https://img.shields.io/badge/X-%40azankhyder-2b2b2b?style=flat-square&labelColor=181818&logo=x&logoColor=white)](https://x.com/azankhyder)
[![Email](https://img.shields.io/badge/email-azanhyder49%40gmail.com-2b2b2b?style=flat-square&labelColor=181818&logo=gmail&logoColor=white)](mailto:azanhyder49@gmail.com)

### Now

- **Production** · CRM DevOps and AI engineering (conveyancing + transport-routing real-time system scaling): the harness around live production CRMs/CMSs. [The method](https://azanhyder-port.vercel.app/research/#production)
- **Shipped** · [agent-check v1.0.0](https://github.com/azank1/agent-exposure), one workflow line that flags risky agent setup in a repo, and [guardrails-kit](https://github.com/azank1/guardrails-kit), fail-closed Claude Code hooks for team repos.
- **Building** · [Metaorcha](https://metaorcha.ai), an open runtime where one goal becomes a verified multi-agent run. [Metabot](https://metaorcha.ai/metabot), the agent on top, is in progress.
- **Writing** · [The Harness Layer](https://dev.to/azankhyder/series/42904), field notes on agent harnesses, each with an artifact you can re-run.


### Work, most involved first

<p>
<a href="https://metaorcha.ai/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/metaorcha-dark.svg"><img src="assets/cards/metaorcha-light.svg" width="49%" alt="01 Metaorcha. Live, open source, Apache 2.0. One goal in, a verified multi-agent run out, across MCP, A2A and computer use. Every run leaves a signed receipt that verifies offline."></picture></a>
<a href="https://azanhyder-port.vercel.app/research/#production"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/production-dark.svg"><img src="assets/cards/production-light.svg" width="49%" alt="02 Production harness. In production, private. Around three live production CRMs: every change classified by what it can break, rehearsed off production, done only when production shows it. Links to the method."></picture></a>
<a href="https://github.com/azank1/seamkit"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/seamkit-dark.svg"><img src="assets/cards/seamkit-light.svg" width="49%" alt="03 seamkit. On npm, open source, Apache 2.0. Deterministic production checks for code mostly written by agents: verdicts read back from what is live, with no model inside. Proven on real deploys."></picture></a>
<a href="https://github.com/azank1/agent-exposure"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/agent-check-dark.svg"><img src="assets/cards/agent-check-light.svg" width="49%" alt="04 agent-check. v1.0.0, open source, MIT. Flags the risky agent setup a repo ships to every clone, and the CI agents that issue or PR text from outsiders can drive. One line in a workflow."></picture></a>
<a href="https://github.com/azank1/cdv"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/cdv-dark.svg"><img src="assets/cards/cdv-light.svg" width="49%" alt="05 CDV. Open source research preview. An agent never grades its own work: a deterministic floor and an LLM critic score each step, the stricter wins, and a Bayesian loop decides when to stop."></picture></a>
<a href="https://github.com/azank1/code-desk-cli"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/code-desks-dark.svg"><img src="assets/cards/code-desks-light.svg" width="49%" alt="06 Code Desks. Open source, MIT. Run an office of AI coding sessions from your terminal: named desks, gated handoffs, and a meter that reads what each desk really used."></picture></a>
</p>

Code behind Metaorcha: [solvent-labs-org/metaorcha](https://github.com/solvent-labs-org/metaorcha)<br>
More: [guardrails-kit](https://github.com/azank1/guardrails-kit) · [commit.city](https://commit.city) · [bizopsmap](https://bizopsmap-preview-nu.vercel.app/) · [RP2A](https://github.com/azank1/restaurant-provider-to-agent) · [ML Trend Probability](https://github.com/azank1/ML-ProbabalisticTrend) · [sdca-raqqr](https://github.com/azank1/sdca-raqqr) · [strategy-builder-ai](https://github.com/azank1/strategy-builder-ai) · [notion-mcp](https://github.com/azank1/notion-mcp) · [claude-agent](https://github.com/azank1/claude-agent) · [all 16 builds](https://azanhyder-port.vercel.app/catalog/)

### Measured

- **5/5** multi-protocol runs verified live, best wall clock 13 s · [Metaorcha](https://github.com/solvent-labs-org/metaorcha)
- **41%** fewer agent steps than a fixed budget, replicated to the digit, along with the case that breaks it · [field note 009](https://dev.to/azankhyder/a-stop-rule-that-trusts-one-score-is-worse-than-a-dumb-budget-428c)
- **5.4B** tokens metered over 30 days and 31k turns, 97% of them from cache · [Code Desks](https://github.com/azank1/code-desk-cli)
- **25** typed MCP tools behind a production voice-ordering agent · [RP2A](https://github.com/azank1/restaurant-provider-to-agent)
- **290+** tests under a multi-tenant restaurant OS, built by a five-person team I led · Zayup
- **3 weeks** to a complete React Native MVP, directing a three-developer team · DeliveryOS

### Merged upstream

- **[ECC](https://github.com/affaan-m/ECC/pull/3591)** · a SessionStart hook crash that broke every project for plugin installs. Merged 2026-10-29; a Windows user measured 0/27 hooks passing before the fix and 26/27 after.
- **[tmux](https://github.com/tmux/tmux/pull/5775)** · a regex anchoring bug in format substitutions, present since 2019. Applied upstream with credit.
- **[huggingface_hub](https://github.com/huggingface/huggingface_hub/issues/5180)** · reported `hf skills add --force` replacing an installed skill with a symlink to itself. Fixed in v2.3.0.

### Writing

[The Harness Layer](https://dev.to/azankhyder/series/42904): field notes on agent harnesses, each with sources, its limits and an artifact you can re-run.

- [When should an agent stop?](https://dev.to/azankhyder/a-stop-rule-that-trusts-one-score-is-worse-than-a-dumb-budget-428c) · Sep 2026 · [artifact](https://github.com/azank1/code-desk-cli/tree/main/research/009-stop-rule)
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

Working on agent runtimes, protocol bridges or verification? [Open an issue on Metaorcha](https://github.com/solvent-labs-org/metaorcha/issues) or [email me](mailto:azanhyder49@gmail.com).
Want your agents' reach checked, or Claude Code set up for a team with guardrails? [Fixed-price work](https://azank1.github.io/offer-site/).

<sub>[azanhyder-port.vercel.app](https://azanhyder-port.vercel.app) · [metaorcha.ai](https://metaorcha.ai) · [dev.to](https://dev.to/azankhyder) · [X](https://x.com/azankhyder) · [LinkedIn](https://www.linkedin.com/in/azan-hyder-8aa58b408/) · [azanhyder49@gmail.com](mailto:azanhyder49@gmail.com) · *It's all relative.*</sub>
