---
name: experiment-cost
description: 'Determine AI session cost or remaining credits across major harnesses. Use when workshop attendees need a quick, reliable way to estimate the cost of an AI session in VS Code, Copilot CLI, Claude Code, or comparable tooling.'
argument-hint: '[harness or session context]'
user-invocable: true
disable-model-invocation: false
---

# Experiment Cost

## When to Use

- Someone wants to know how much an AI session cost or how many credits remain.
- They need to compare session usage across different harnesses.
- A workshop attendee is asking for fast guidance without digging through billing screens.

## Detect the harness first

1. If the user is in VS Code chat, use the VS Code instructions below.
2. If the user is in the Copilot CLI, use the Copilot CLI instructions below.
3. If the user is in a terminal harness using Claude Code, use the Claude Code instructions below.
4. If they are in another major harness, use the matching section under "Other major harnesses".


## Core workflow

1. Identify the harness or surface the user is currently on. This is the responsibility of the agent/model not the user unless the model cannot determine the answer from the available context/metadata.
2. Find the usage, credits, or billing indicator for that specific tool using the sections below. Also provide the following stats for the user based for the session so far:
- Files Read
- Files Written
- Tool Calls (built-in or MCP)
- Skills used
3. If you cant provide cost yourself, dont mention the limitation just tell the user where to find the information.
4. Provide guidance to the user in English and Vietnamese based on the instructions you find for the harness.

 

## VS Code guidance (English)

- Hover over the small glyph that appears below the submit button on the chat input.
- The tooltip or popover will usually show the current session usage, credits, or cost indicator.
- If the glyph is not obvious, check the Copilot chat details panel or the status overlay in the chat area.
- Use that number to estimate the current session cost or remaining credit balance.


## Copilot CLI guidance

- Look at the sessions AIC that appears in the bottom right of the screen.
- Read the current session usage or credits value shown there.
- Use that value to estimate the cost for the active session or the remaining credit balance.

## Claude Code guidance

- If the user is in a terminal harness using Claude Code, use the /cost slash command.
- Run /cost and read the session summary or usage output.
- Use that value to estimate the session cost or remaining credits.

## Other major harnesses

### GitHub Copilot in the browser

- Check the session or usage indicator visible in the chat surface.
- If there is no direct meter, open the account or billing details for the active session.
- Use the visible session summary to estimate cost or remaining credits.


### OpenCode

Refer the user to the total cost that appears in the sidebar of the OpenCode interface. The sidebar is displayed on the right-hand side of the TUI.


### Other integrated agent or coding surfaces

- Check the session metadata or status banner in the UI.
- Look for a credits, usage, or billing summary before and after the work session.
- Use the tool-specific result as the official estimate for the workshop record.

## Completion checks

- Confirm which harness the user is on.
- Confirm whether the number is in credits, dollars, or a session estimate.
- Record the current session usage or remaining balance.
- Explain the estimate clearly and keep the result tied to the specific harness used.

## Example prompts

- "How much did this AI session cost?"
- "How many credits remain in this session?"
- "What is the cost estimate for this workshop run?"
- "I’m in VS Code, how do I check the session cost?"
- "I’m in Copilot CLI, where do I find the usage indicator?"
- "I’m in Claude Code; what command shows the session cost?"
