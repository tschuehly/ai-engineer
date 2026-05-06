# Agents

## Overview

On-device agent workflows can keep core inference local while still invoking selected tools, APIs, and structured outputs. The useful boundary is not whether an agent is purely offline, but which reasoning and data handling should stay on the device and which capabilities require external calls.

## Key Concepts

- [On-device agents can combine local reasoning with tool and API calls](../concepts/on-device-agents-can-combine-local-reasoning-with-tool-and-api-calls.md) - local inference can still support function calling, JSON output, and selected API-backed skills.

## Open Questions

- Which classes of tool calls are reliable enough for small on-device models without cloud fallback?

## Sources

- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
