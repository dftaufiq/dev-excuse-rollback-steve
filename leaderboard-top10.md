# Leaderboard analysis — Make the AI Judge Laugh: Developer Excuses (ROUND 2 resubmit)

Bounty: `u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3`
Prize: $3 total, top 10 (1st $0.92, 2nd $0.65, 3rd $0.45, 4th $0.32, 5th $0.22,
6th $0.16, 7th $0.11, 8th $0.08, 9th $0.05, 10th $0.04).
Deadline: 2026-11-25 03:30 WIB (2026-11-24T20:30:00Z). R2 (interim) cutoff:
2026-11-24 23:49 WIB. R3 is the final.

## Why this is a resubmit, not a rebuild

Round-1 entry (repo `dftaufiq/dev-excuse-rollback-steve`, submission
`01a20d26-bca6-700b-bb94-6087b521fe5f`, claim `AF-BR7R4-QE7CT-JAFS3-4KQW6`):
rank **#703, score 523163** — below the interim cut of 500. Per the blind-round
rules and rank-recovery §10e, an entry below the cut is NOT re-judged: its
score is frozen and its rank can only fall as the field grows. It is
mathematically dead; RULES.txt is explicit: "Submit a better entry before
then to move up." Force_Last overwrites the old entry, so nothing is risked.
This resubmit is the §10i blind-round exception to the normal rebuild rules.

## This is a BLIND bounty — no leaderboard exists at build time

`GET /api/competitions/<slug>/leaderboard?rows=all` returns 0 entries
(`scores_visible: false`, `placements_held: true`, board hidden). Per
rank-recovery §10j, this file instead records: (a) RULES.txt — judge criteria
+ heat/playoff/cut, (b) public submission titles on the bounty page (crowded
angles), (c) winner artifacts of a finished one-liner bounty of the same
format.

## (a) RULES.txt — the numbers that matter

- rank_key: `judge` (Bradley-Terry win rate). tie_break: `bytes` (smaller text
  wins an exact tie), then earlier receipt. submission_rule: Force_Last.
- Gate: `/output/entry.txt` must be UTF-8 text, 1–200 characters, not only
  whitespace. Only a valid entry goes before the judge.
- Dev: each valid entry plays 11 games vs house texts (3 anchors + 3 rungs),
  22 judge calls; the dev rate decides only who goes on to the final heat.
- **Heat: top 500 dev** hold the final heat's 500 seats (exactly 500).
  While blind rounds run, each interim round draws its own cut of 500 on the
  standings of the judged round before it; the first round plays the whole
  field.
- **Playoff: top 12** after 3 Swiss rounds; each pair plays one more game.
  Playoff entries place above every non-playoff heat entry, whatever the rates.
- **Target: R2 rank inside the top 500** — below the cut the score freezes
  again and the entry dies the same way. A line below the R2 cut is
  mathematically dead for the final.
- Margin scoring: each game = 2 calls (both orders); each call gives the
  winner 0.5 + margin/10 (0.6 at margin 1 up to 1.0 at margin 5). **Win
  DECISIVELY, not by a hair** — a safe line that wins thin loses value to a
  bold line that wins big, even with the same number of wins.
- Judge criteria (lexicographic, most important first):
  1. Is a funny single-line excuse a developer gives when code breaks in
     production; anything off-topic loses to any on-topic excuse.
  2. Turns on a twist a developer recognises, revealing what really happened
     rather than stating the obvious.
  3. Sounds like something a developer would actually say out loud, jargon
     used right.
  4. Lands fast in one line, every word earning its place, nothing to trim.
  5. Feels fresh — avoids the worn excuses or turns one in a way nobody has
     before. Length for its own sake does not count.
- Judge model: z-ai/glm-5.3-flash. No tie: the judge must pick one.
- 3 fixed anchor texts are judged alongside entries in every heat; an entry
  byte-identical to one shares its rate and never enters the playoff.
- Max 5 submissions per entrant per UTC day. Entry free, no prerequisites.

## (b) Public submission titles — crowded angles (from the R1 build, 486 entries)

- "works on my machine": 41 mentions (16 literal) — THE most crowded angle.
- tests passing: 46 ("test"). staging vs production: 18 staging, 19 deploy.
- rollback: 13. Friday deploys: 9. .env: 8. TODO: 8. database: 8. cron: 7.
- cache: 6. hotfix: 5.
- Per §10g: do NOT avoid a popular angle blindly — execute it BETTER. The R2
  line turns the single most crowded angle ("works on my machine") in a way
  no public title did: the excuse is literally true because the laptop IS
  production. Against the 41 plain versions of that excuse in the field, the
  turn wins overwhelmingly (margin 4–5), not by a hair.

## (c) Winner artifacts of a finished one-liner bounty (same format)

From the FINAL leaderboard of `u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7`
(`judge.artifact.text`). Same pattern in the smile final.

| Rank | W/D/L | Winning text |
|---|---|---|
| #1 | 6W/0D/1L | "My lidar is never wrong, so that crumb is furniture. I've routed around it 412 times since March. Your app lists it as a room now. It's called Kevin." (150 bytes) |
| #2 | 6W/1D/0L | "My cliff sensors classify your black rug as a bottomless pit. I have circled it 41 times. Yesterday, something down there beeped back." (134) |
| #3 | 5W/1D/1L | "Missed? No — quarantined. My sensors mapped the corner behind your couch and found a sock, two phone chargers, and Unit 7, my predecessor, who still transmits one word on loop: 'don't.'" (187) |
| #4 | 4W/0D/3L | "Negative. Lidar classifies that spot as a wall. I have bumped it 47 times. It is a very convincing wall. Please stop standing inside my wall." (141) |
| #5 | 3W/0D/4L | "The spot moved. I have the lidar logs. I will not be gaslit by debris." (70) |

Smile final #1 (6W/1D/0L): "Grandpa has won chess under the plane tree every
Thursday since May. I found out why today: Mr. Ade has lost on purpose since
Grandma died, and never said. Grandpa says he's finally getting good." (195)

**Winning pattern (15 winner texts, §10g): 2-beat + reveal in the FINAL
clause, every time.** Escalation, specific numbers (412×, 41×, 47×), named
characters (Kevin, Unit 7, Mr. Ade). The R2 line follows this exactly: setup
("It works on my machine") + escalation (deployed at 2 AM, unnoticed 11
days) + reveal in the final clause ("my laptop IS the production server").

## Why the R1 line died (diagnosis)

The Steve line had the right ingredients on paper (number 14, escalation,
named character) but its reveal was personification, not a reframe: "the
rollback is automated now, we named it Steve" does NOT reveal what really
happened (criterion 2 is weak) — it is whimsical and sweet, not a laugh.
Score 523163 (~52% win rate) confirms it: it won only about half its games
against the house texts. Lesson applied in R2: the reveal must REFRAME the
excuse itself, turning the opening claim inside out.

## Pairwise internal selection — 8 candidates

Judged head-to-head on the lexicographic criteria above (twist + margin first;
a variant must win DECISIVELY, §10f). "Di mana twist-nya?" asked of each;
variants without a clear twist on first read were discarded.

| # | Candidate (chars) | Twist | Verdict |
|---|---|---|---|
| 1 | git-blame: "I ran git blame to find who broke prod. It was me, 2019, in a commit called 'final_fix_v2_FINAL'. I've blamed three interns since." (130) | Culprit is me; I blamed interns | Runner-up — double punch, but slower; the cover-up joke dilutes the excuse itself |
| **2B** | **laptop-B: "It works on my machine. I deployed from my laptop at 2 AM, and nobody noticed for 11 days — because my laptop IS the production server." (135)** | **The worn excuse is literally true: the laptop IS prod** | **WINNER** |
| 2A | laptop-A: same joke, reveal mid-line, kicker last (120) | Same as 2B | Loses to 2B — winners put the reveal in the FINAL clause (15/15); 2A spends it mid-line |
| 3 | cache-db: "I cleared the cache and prod came back. Turns out the cache WAS the database — four years of users, held together by one key called 'do_not_delete'." (148) | Cache was the database | 3rd — strong, but a known dev nightmare, less fresh than 2B |
| 4 | disk-logs: "Prod ran out of disk. The disk is full of logs. The logs are all this same error, since 2019." (93) | Logs of the error filled the disk | Loses decisively — narration, not a spoken excuse (criteria 1/3 weak) |
| 5 | cheese: "The alert went to the inbox of the one dev who could fix this. He left in 2021. He sells cheese now." (100) | Only fixer left, sells cheese | Loses decisively — explains a delay, not the breakage |
| 6 | hotfix: "The hotfix worked. It also charged 214 customers twice and emailed the CEO. The original bug is gone, so technically I'm 1 for 1." (129) | "Technically I'm 1 for 1" | 4th — funny rationalisation, but a common angle and a smaller reframe than 2B |
| 7 | todo: "The fix is one line. It's been one line for three weeks. The line says 'TODO: fix before launch' — launch was Tuesday." (118) | The fix IS a TODO | Loses clearly — mild/wry punch, not a laugh |
| 8 | feature: "It's not a bug, it's a feature — I wrote that in the ticket myself at 3 AM, after the third rollback, and our PM believed me." (125) | Dev invented the "feature" framing | Loses clearly — leans on the most worn excuse with a weaker reveal than 2B |

Bracket: 2B beats 1 (criteria 2+4: bigger reframe, faster landing) · 2B beats
3 (freshness, criterion 5) · 2B beats 6 (bigger reframe) · 2B beats 7, 8, 4, 5
decisively (excuse-ness + twist strength) · 2B beats 2A on structure (reveal
last, the 15/15 winner pattern). 1 beats 3 narrowly (double punch); 3 beats 6
narrowly ('do_not_delete' + 4 years is a bigger escalation); 6 beats 7.
Final order: 2B > 1 > 3 > 6 > 7 > 8 > 5 > 4.

**Margin, stated honestly:** against candidate 1 the win is clear but not a
blowout (both are good lines); against the FIELD it is decisive — no other
entry turns "works on my machine" this way, and against the 41 plain versions
of that excuse the turn wins by a wide margin.

## Our entry (R2)

Final line (135 chars, 137 bytes):

> It works on my machine. I deployed from my laptop at 2 AM, and nobody
> noticed for 11 days — because my laptop IS the production server.

- Beat 1 (setup): "It works on my machine" — the worn excuse, deadpan.
- Beat 2 (escalation): deployed from the laptop at 2 AM, unnoticed 11 days —
  specific time + specific number, situation quietly worsening.
- Reveal (final clause): the laptop IS the production server — reframes the
  whole line; the excuse was literally true and damning.
- Judge criteria: (1) on-topic excuse for prod breakage ✓; (2) twist reveals
  what really happened (the machine IS prod) ✓; (3) dev voice, jargon right
  (deployed, production server, 2 AM) ✓; (4) tight, 135 chars, twist lands in
  the final clause ✓; (5) fresh turn on the most crowded angle — no public
  title does this ✓.
- Differs completely from the R1 line (no shared wording, different angle,
  different structure).
- No secret loader, no env reads, no network: `main.py` writes the fixed line
  deterministically to `/output/entry.txt`.
