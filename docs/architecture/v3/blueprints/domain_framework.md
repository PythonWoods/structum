# Domain Framework Blueprint

## Purpose

Standard template for frameworks built on Structum.

## Characteristics

- Plugin-driven
- Configurable
- Observable
- Secure by default

## Recommended Structure

```text

framework/
src/
app.py
config.py
di.py
pipeline/
plugins/
docker/

```

## Plugin Contract

Plugins must:

- declare metadata
- expose clear domain hooks
- support health checks

## Example Domains

- video processing
- motion detection
- automation
- AI pipelines
