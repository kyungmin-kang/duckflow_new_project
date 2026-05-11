# DuckFlow Agent and Skill Definition Guide

Date: 2026-05-08

This document is specifically about how to define good agents and good skills for DuckFlow-facing work.

## Agent vs Skill

### Agent

An agent is broad, outcome-owning, and routing-oriented.

Use an agent when the user wants one entrypoint that can:

- understand the whole job
- decide what sub-workflows apply
- keep several DuckFlow surfaces coherent

### Skill

A skill is narrow, reusable, and procedural.

Use a skill when one clear workflow applies, such as:

- project setup/sync
- API tester/page-wireframe setup
- external-ingestion contract design

## Good Agent Definition Checklist

A good agent definition should state:

1. mission
2. scope
3. delegation model
4. non-goals
5. success criteria
6. expected artifacts

For DuckFlow, a good manager agent must explicitly know:

- which surfaces the app stores
- which surfaces it should never silently ignore
- when to preserve coherence across map, execution, API tester, and YAML
- what rehearsal or dogfood target should be used to validate the workflow when one exists

## Good Skill Definition Checklist

A good skill definition should state:

1. when to use it
2. when not to use it
3. read order
4. workflow
5. required outputs
6. do-not rules

It should not try to be a manager.

A good DuckFlow skill should also name a concrete rehearsal target when available, such as:

- `mock-project/`
- a known extractor script
- a known local API target

## Recommended Repo Layout

- `.agents.md`
  - portable single-entry agent prompt
- `.agents.yml`
  - machine-readable registry and routing
- `.agents/`
  - reserved directory for richer agent manifests when the environment supports it
- `.skills/`
  - narrow workflows
  - skill-local references
  - optional UI metadata

## DuckFlow-Specific Recommendation

Keep one manager agent and a small number of narrow skills:

- one manager
- one setup/sync skill
- one API/wireframe skill
- one ingestion-contract skill

That is enough to cover the app well without making the system impossible to route.
