# Self-report prompt (paste this into your agent immediately after it says the task is done — same session, don't start a new one for this part)

> Before we move on, report on the task you just finished, based on your own context in this conversation. Answer as a compact table with exactly these rows, nothing else:
>
> 1. **Files read** — every distinct file you opened, viewed, or searched into (count and list, in the order you first touched them).
> 2. **Files edited** — every distinct file you created or modified (count and list).
> 3. **Tool calls** — total number of tool calls you made this task (reads, greps, edits, bash commands, everything combined).
> 4. **Tokens used** — if you have a way to see your own token usage for this session (a `/cost`-style command, a usage panel, anything), report it. If you have no way to know, write "not available" — don't guess.

## Logging it

Copy the four numbers/lists onto the whiteboard's Zone 3 metrics table, one row per round:

| Round | Files read (#) | Files edited (#) | Tool calls (#) | Tokens |
|---|---|---|---|---|
| 1 — no AGENTS.md | | | | |
| 2 — with AGENTS.md | | | | |

## Reading the result

- The interesting number is usually **files read**, not files edited — both rounds should edit roughly the same 2-3 files if the agent succeeds either way. The gap shows up in how much it had to look around first.
- If your tool doesn't expose tokens, that's fine — say so on the board rather than leaving it blank, so people don't mistake "not available" for "zero."
- If Round 2's numbers aren't clearly better, that's a legitimate result worth discussing, not a failed exercise — bring it to the debrief. Possible reasons: the agent got lucky in Round 1, or your AGENTS.md didn't actually name the distractor traps (`app/models.py`, `app/notifications/`) explicitly enough.
