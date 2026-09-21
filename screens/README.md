# Market Screens

Screens define reproducible candidate searches. A screen definition contains its universe, inputs, filters, ranking factors, warning flags, source hierarchy, refresh policy, and output contract.

Definitions are registered in [`registry.yaml`](registry.yaml). Each successful or diagnostically useful execution must create a new append-only run; prior results are never overwritten. Screen candidates require human research and are not recommendations.

## Active definitions

For feature overview, usage commands, limitations, and resume tasks, read the [Search Strategy Guide](../docs/SearchStrategyGuide.md).

- [`forward-dividend-yield/`](forward-dividend-yield/README.md) — estimates whether normalized earnings and cash capacity may support a forward cash yield of at least 7%.
