# Structum Architecture V3

Enterprise Plugin Framework — Definitive Architecture Specification

## 1. Purpose

Structum V3 defines a foundational meta-framework for building plugin-oriented systems, domain frameworks, and extensible applications. This document is authoritative.

## 2. Architectural Vision

Structum is not an application and not a toolbox.  
It is a **foundation layer** enabling:

- plugin-driven systems
- domain-specific frameworks
- enterprise-grade extensibility
- operational readiness

Structum V3 establishes **clear boundaries** between core runtime, extensions, applications, and deployment.

---

## 3. Layered Architecture Model

### L1 — Core Runtime (structum)

Mandatory, minimal, long-lived API.

Responsibilities:

- Plugin Engine (discovery, lifecycle, registry)
- Plugin Management (built-in feature, not a plugin)
- Configuration Engine
- Observability primitives
- Security validation
- Dependency Injection container
- CLI bootstrap

### L2 — Official Extensions (structum_*)

Optional, modular, replaceable.

Examples:

- structum_tree
- structum_archive
- structum_clean
- structum_docs

### L3 — Domain Frameworks

User-owned frameworks built on Structum.

Examples:

- camera framework
- motion detection pipeline
- automation platforms

### L4 — Community Plugins

Third-party plugins following public contracts.

---

## 4. Core vs Extension Boundary (Critical Decision)

| Capability | Location |
|----------|---------|
| Plugin discovery | Core |
| Plugin enable/disable | Core |
| Plugin metadata | Core |
| CLI injection | Core |
| FS utilities | Extension |
| Logging implementation | Extension |
| Docs tooling | Extension |

> Plugin management is **core**, otherwise the framework is incomplete.

---

## 5. Monorepo & Distribution Strategy

### Development

- Single GitHub monorepo
- Unified CI/CD
- Cross-package integration tests

### Distribution

- Separate PyPI packages
- Modular installation
- Explicit version compatibility

This model is final and non-negotiable.

---

## 6. Dependency Injection Strategy

DI is mandatory for:

- testability
- isolation
- plugin orchestration

The DI container lives in core and supports:

- singleton
- scoped
- transient lifetimes

---

## 7. Observability

Core provides:

- metrics hooks
- tracing hooks
- structured logging interface

No hard dependency on vendors.

---

## 8. Security Model

Core enforces:

- plugin metadata validation
- policy-based enable/disable
- future sandboxing readiness

---

## 9. Containerization Strategy

Docker is **not part of the core**.

Docker is supported for:

- development environments
- CI pipelines
- deployment of applications (L3)

Rules:

- Core must run without containers
- Plugins are Python packages, not images
- Containers package applications, not the framework

---

## 10. Roadmap Summary

- V3.0 — Stable contracts
- V3.1 — Health checks
- V3.2 — DI v1
- V3.3 — Security policies
- V3.4 — Hot reload (dev)
- V4.0 — Advanced isolation (optional)

---

## 11. Architectural Rule

Any new feature must declare:

- target layer (L1–L4)
- justification
- impact on stability
