---
name: duckflow-api-wireframe
description: Maintain DuckFlow API targets, tests, suites, and page wireframe plans. Use when the task is to set up UI-linked API testing, align page components with tests, or keep suite and page-plan state coherent with the project map.
---

# DuckFlow API and Wireframes

Use this skill for the API tester and page-wireframe surfaces.

## Read Order

1. `docs/duckflow-agent-system-guide.md`
2. `docs/api-tester-v1-implementation-plan.md`
3. `references/planning-checklist.md`
4. Read `docs/project-template.yaml` if YAML must be produced or normalized.

## Use This Skill For

- defining API targets
- creating or updating saved tests
- grouping tests into suites
- building page wireframe plans
- placing components and assigning load behavior
- linking tests to API nodes, contract nodes, and page/wireframe nodes
- planning UI checks against existing map/runtime structure

## Workflow

1. Identify the user-facing page or API surface under test.
2. Define or reuse the correct target.
3. Create the smallest useful tests.
4. Group them into suites that match page flows or smoke checks.
5. Define page-plan components with load behavior:
   - `initial`
   - `lazy`
   - `background`
   - `manual`
6. Link tests to page components and relevant map nodes.

## Modeling Rules

- One test should represent one request definition.
- Use suites, not multi-request tests, for grouped flows.
- Page plans are planning/testing surfaces, not full UI implementations.
- Component timing should map to page load behavior, not invent new runtime semantics.

## Good Outputs

- coherent API target catalog
- small, readable tests
- suites that match page/user flows
- page plans whose components and linked tests line up with map/runtime structure

## Do Not

- overload one test with many unrelated calls
- create page plans without linked tests when checks are known
- treat wireframe plans as visual design files rather than test/planning artifacts

## Dogfood Note

When validating this skill in this repo, use `mock-project/`:

- browser-local target on port `3001`
- page route `/dashboard`
- health, orders summary, and customers endpoints
