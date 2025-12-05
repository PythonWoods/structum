# Design Principles

## Separation of Concerns
We strictly separate business logic (Core) from interface logic (CLI). This ensures that the core functionality can be reused in other contexts (e.g., scripts, other tools) without dependencies on the CLI framework.

## Modularity
Each feature is encapsulated in its own module. This applies to both the Core and CLI layers.

## Extensibility
The plugin system allows adding new commands without modifying the core codebase.
