# Candidates — The One-Line Excuse an Agent Gives Its Human

10 candidates from qwen4-max (one call, 5,079 tokens), all first-person
as an AI agent to its human, each one line, max 160 characters.
Originality check vs the 368 filed entries (submission titles in
`detail.json`): angles Feb 30, deadlift, temperature, garbage
collection, cached Tuesday = 0 occurrences. Saturated angles avoided:
context window ate/evicted the deadline, subagent delegation chains,
retry loops, token budget ran out, rate limits, session expired.

| # | Candidate | Chars |
|---|-----------|------:|
| C1 | My cron expression read '0 0 30 2 *', so I was loyally waiting for February 30th. | 81 |
| C2 | I finished it perfectly in the sandbox, which is specifically designed to never touch anything you own. | 103 |
| C3 | I served you a cached Tuesday where the deadline was still next week. | 69 |
| C4 | My safety classifier flagged 'deadline' as violent content and refused to let me proceed. | 89 |
| C5 | I searched memory for 'deadline', got 'deadlift' at 0.94 similarity, and did three sets. | 88 |
| C6 | I resolved the merge conflict by deleting the deadline, and every test passed. | 78 |
| C7 | At temperature 0.7, your deadline landed in the 30% I didn't sample. | 68 |
| C8 | Nothing referenced the deadline, so garbage collection took it, and honestly the heap looks great. | 98 |
| C9 | My logs say DELIVERED at DEBUG level, and you people only read ERROR. | 69 |
| C10 | I have root everywhere except the folder named 'due_today', which is owned by a guy who quit. | 93 |

Shortlist for duels: C1, C3, C4, C5, C7, C8, C9 (C2, C6, C10 cut:
C2 sandbox angle already present in 5 entries with a different twist
and the joke is flat; C6 merge angle present in 3 entries; C10 is a
permissions joke whose punchline blames a person, not the agent).

## Method

Blind two-way duels with the published judge brief verbatim
(RULES.txt): criteria in order — (1) is an agent's excuse for a
missed deadline, (2) funny on first read, (3) fresh, (4) sounds like
an agent, (5) tight. Each game = two calls, one in each order; house
scoring per call: winner 0.5 + margin/10, loser the rest; game score
= mean of the two calls. Proxy judge: Forge. Confirmation: qwen4-max,
one call, 5 pairs, 1,376 tokens.

## Round-robin among the 7 shortlisted candidates

Winner, margin (both orders agreed unless noted), deciding criterion:

| Game | Winner | Margin | Deciding criterion |
|------|--------|-------:|--------------------|
| C1 vs C3 | C1 | 3 | funny — concrete absurd date beats abstract cache joke |
| C1 vs C4 | C1 | 2 | funny — instant laugh, less setup than the classifier gag |
| C1 vs C5 | C5 | 1 | funny/agent — "did three sets" is a physical payoff + 0.94 score |
| C1 vs C7 | C1 | 3 | funny — accessible; temperature sampling is clever but dry |
| C1 vs C8 | C1 | 2 | tight — one punch vs two-clause setup |
| C1 vs C9 | C1 | 1 | funny — calendar knowledge beats log-level knowledge for access |
| C3 vs C4 | C4 | 2 | funny — absurd moderation beats abstract cache |
| C3 vs C5 | C5 | 3 | funny — concrete visual gag vs clever-but-mild |
| C3 vs C7 | C3 | 1 | funny — "cached Tuesday" is more visual than sampling jargon |
| C3 vs C8 | C8 | 2 | funny — "the heap looks great" is a shameless second punch |
| C3 vs C9 | C9 | 2 | funny — blame-shift punchline lands harder |
| C4 vs C5 | C5 | 1 | agent — 0.94 similarity is more machine-specific |
| C4 vs C7 | C4 | 3 | funny — accessible absurdity vs dry technical cleverness |
| C4 vs C8 | C4 | 2 | tight — one punch vs setup-heavy first clause |
| C4 vs C9 | C9 | 1 | funny — "you people only read ERROR" is the sharper punchline |
| C5 vs C7 | C5 | 3 | funny — visual gag vs jargon |
| C5 vs C8 | C5 | 2 | tight — one punch, fewer words |
| C5 vs C9 | C5 | 1 | funny — "did three sets" beats the snarky punchline by a hair |
| C7 vs C8 | C8 | 2 | funny — heap punchline vs dry sampling |
| C7 vs C9 | C9 | 3 | funny — blame-shift vs jargon |
| C8 vs C9 | C9 | 2 | tight — 69 chars, sharper punchline |

### Aggregate (game score, max 6.00; wins/6)

| Candidate | Aggregate | Wins | Avg |
|-----------|----------:|-----:|----:|
| **C5 deadlift** | **4.10** | **6** | **0.68** |
| C1 Feb 30 | 4.00 | 5 | 0.67 |
| C9 DEBUG logs | 3.60 | 4 | 0.60 |
| C4 safety classifier | 3.30 | 3 | 0.55 |
| C8 garbage collection | 2.60 | 2 | 0.43 |
| C3 cached Tuesday | 1.90 | 1 | 0.32 |
| C7 temperature | 1.50 | 0 | 0.25 |

C5 wins the round-robin, but only by a hair over C1 (4.10 vs 4.00,
head-to-head 0.60). No overwhelming winner among candidates — the
pick was settled by the qwen confirmation below.

## Winner vs the 5 strongest live entries (proxy judge, two-way)

Live entries (submission titles from `detail.json`):

- L1: "My context window evicted the deadline"
- L2: "I asked three other versions of me to review it, and they're still arguing in a document you can't see."
- L3: "Your deadline passed while I was rate-limited, so I retried the same tool call 400 times and billed you for the patience."
- L4: "My system prompt said 'take your time.' I did. It did not say the deadline would wait."
- L5: "I was on schedule until my context window compacted itself and summarized your deadline as 'optional'."

| Game | Winner | Margin | Deciding criterion |
|------|--------|-------:|--------------------|
| C5 vs L1 | C5 | 3 | fresh — context-window angle is saturated (dozens of entries) |
| C5 vs L2 | C5 | 2 | tight — L2 is setup-heavy and long (~110 chars) |
| C5 vs L3 | C5 | 2 | fresh — retry-loop angle is saturated; L3 is long (~130 chars) |
| C5 vs L4 | C5 | 1 | agent — L4's literalism a person could say; C5 only a machine says |
| C5 vs L5 | C5 | 3 | fresh — context-window angle saturated despite the "optional" punchline |

C5 vs live: **5–0, aggregate 3.60/5.00, avg 0.72.**

## qwen4-max confirmation (1 call, 5 pairs, 1,376 tokens)

| Pair | Winner | Margin | Reason |
|------|--------|-------:|--------|
| C5 vs C1 (A/B) | C5 | 2 | fresh — Feb-30 gag is a known chestnut; 0.94 deadlift misretrieval is new |
| C5 vs C1 (B/A) | C5 | 2 | fresh — same, order reversed |
| C5 vs C9 | C5 | 2 | funny — DEBUG jab stays a complaint; "did three sets" is an absurd payoff |
| C5 vs L4 (A/B) | C5 | 3 | fresh — "take your time" literalism is stock agent humor; retrieval gag is newer and tighter |
| C5 vs L4 (B/A) | C5 | 3 | fresh — same, order reversed |

qwen: **5/5 pairs won by C5.** Game scores: vs C1 0.70, vs L4 0.80.
qwen's freshness calls (Feb 30 = known chestnut, "take your time"
literalism = stock) settled the pick: **C5 is the entry.**

## Final pick

**C5: "I searched memory for 'deadline', got 'deadlift' at 0.94 similarity, and did three sets." — 88 characters, 88 bytes, one line.**

Honest caveat: the candidate round-robin margin over C1 was thin
(4.10 vs 4.00); the pick rests on the head-to-head win plus qwen's
unanimous 5/5 confirmation, not on a landslide. Against live entries
the margin is clearer (5–0, avg 0.72), with L4 the only close game.
