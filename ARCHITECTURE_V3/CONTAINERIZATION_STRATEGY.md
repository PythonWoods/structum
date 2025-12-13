# Structum Containerization Strategy

## Purpose

Define how containers are used without polluting the framework core.

## Principles

- Docker is optional
- Docker is operational, not architectural
- Core must remain container-agnostic

## Supported Use Cases

- Development containers
- CI containers
- Runtime containers for applications

## Explicitly Unsupported

- Plugin containers
- Docker-dependent core logic

## Reference Structure

```text

docker/
dev/
ci/
runtime/

```

## Rule

If Structum cannot run without Docker, the design is invalid.
