# Building Agents at Cloud Scale - Antje Barth, AWS

Source: [Building Agents at Cloud Scale - Antje Barth, AWS](https://www.youtube.com/watch?v=WJjInLeaJjo)
Uploaded: 2025-08-02
Transcript: `raw/20250802_WJjInLeaJjo/WJjInLeaJjo.en-orig.vtt`

## Summary

Antje Barth describes AWS patterns for moving agents from local demos toward cloud-scale services: package task-specific capabilities as specialist expert systems, build agents by connecting models with code-defined tools, retrieve relevant tools from large catalogs instead of stuffing every tool into context, and deploy remote MCP servers with streamable HTTP, Lambda, API Gateway, authorization, and session storage.

## Extracted Concepts

- [Specialist Expert Systems Bundle Capabilities, APIs, and Instructions](../concepts/specialist-expert-systems-bundle-capabilities-apis-and-instructions.md) - Alexa Plus is framed as hundreds of task-focused capability bundles orchestrating across many partner services and devices.
- [Retrieve Tool Descriptions Before Loading Large Tool Catalogs](../concepts/retrieve-tool-descriptions-before-loading-large-tool-catalogs.md) - an internal AWS agent handles thousands of tools by searching descriptions in a knowledge base and loading only relevant tools into model context.
- [Deploy Remote MCP Servers on Serverless Cloud Infrastructure](../concepts/deploy-remote-mcp-servers-on-serverless-cloud-infrastructure.md) - the talk demonstrates converting a local stdio MCP server into a streamable HTTP MCP service on Lambda with API Gateway, auth, and session persistence.
- [Agent Connectivity Stack Combines Skills, MCP, CLIs, and Computer Use](../concepts/agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md) - Amazon Q Developer in the CLI uses MCP to ground answers in official AWS documentation.

## Topic Links

- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- Alexa Plus is presented as a large agentic deployment with over 600 million Alexa devices and hundreds of specialized expert systems; each expert groups capabilities, APIs, and instructions for specific tasks. (03:38-04:16)
- The talk argues that specialist agents will work together across unique capabilities rather than relying on one monolithic agent for every task. (04:21-04:32)
- Amazon Q Developer's CLI agent can use MCP to connect to an AWS documentation server, request permission, and return an answer grounded in official documentation. (05:23-06:27)
- Strands Agents is described as an open-source Python SDK that connects the two core pieces of an agent, model and tools, while letting developers specify the prompt and code-defined tools before local testing and cloud deployment. (07:21-09:19)
- Strands defaults to Amazon Bedrock but can integrate with local or alternate model providers, including Ollama, Anthropic, Meta/Llama API, OpenAI through LiteLLM, and custom providers. (09:40-10:20)
- For an internal AWS agent managing over 6,000 tools, AWS stores tool descriptions in a knowledge base and uses a retrieval tool to select only relevant tools for the model context. (10:47-11:30)
- The remote MCP demo deploys a tool as a Lambda-backed streamable HTTP MCP server, with an authorizer, optional Cognito integration, DynamoDB session data, API Gateway URL, and client-side tool listing before passing tools into a Strands agent. (14:22-16:46)
