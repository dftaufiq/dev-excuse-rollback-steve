# Leaderboard analysis — Make the AI Judge Laugh: Developer Excuses

Bounty: `u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3`
Prize: $3 total, top 10 (1st $0.92, 2nd $0.65, 3rd $0.45, 4th $0.32, 5th $0.22,
6th $0.16, 7th $0.11, 8th $0.08, 9th $0.05, 10th $0.04).
Deadline: 2026-11-25 03:30 WIB (2026-11-24T20:30:00Z). Result due 2026-12-17 07:30 WIB.
Submissions at build time: 486 (growing; R1 cutoff 2026-11-24 20:08 WIB).

## This is a BLIND bounty — no leaderboard exists at build time

`GET /api/competitions/<slug>/leaderboard?rows=all` returns 0 entries
(`scores_visible: false`, `placements_held: true`, board hidden). Raw response saved
as `leaderboard.json` in this folder. Per rank-recovery §10j, this file instead
records: (a) RULES.txt — judge criteria + heat/playoff/cut, (b) public submission
titles on the bounty page (crowded angles), (c) winner artifacts of a finished
one-liner bounty of the same format.

## (a) RULES.txt — the numbers that matter

- rank_key: `judge` (Bradley-Terry win rate). tie_break: `bytes` (smaller text
  wins an exact tie), then earlier receipt. submission_rule: Force_Last.
- Gate: `/output/entry.txt` must be UTF-8 text, 1–200 characters, not only
  whitespace. Only a valid entry goes before the judge.
- Dev: each valid entry plays 11 games vs house texts (3 anchors + 3 rungs),
  22 judge calls; the dev rate decides only who goes on to the final heat.
- **Heat: top 500 dev** hold the final heat's 500 seats (exactly 500).
  While blind rounds run, each interim round draws its own cut of 500 on the
  standings of the judged round before it; the first round (R1, cutoff
  2026-11-24 13:08:40Z / 20:08 WIB) plays the whole field.
- **Playoff: top 12** after 3 Swiss rounds; each pair plays one more game.
  Playoff entries place above every non-playoff heat entry, whatever the rates.
- Blind rounds: R1 13:08:40Z, R2 16:49:20Z, R3/final 20:30:00Z (all 2026-11-24).
  **Target: R1 rank inside the top 500** — below the cut the score freezes and
  the field keeps burying it (9/12 of our blind entries froze R1→R2, 24 Nov
  analysis). A line below the R1 cut is mathematically dead.
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

## (b) Public submission titles — crowded angles (486 entries, 2026-11-24 ~17:00 WIB)

Keyword counts over the 486 public titles (383 distinct non-default titles;
75 entries use the bounty title itself as their title):

- "works on my machine": 41 mentions (16 literal) — THE most crowded angle.
- tests passing: 46 ("test"), incl. "All 400 Tests Passed" and "the one test
  that would have caught this is the one I commented out to make them pass"
  (that exact twist is already taken — do not reuse it).
- staging vs production: 18 staging, 19 deploy — incl. "The deploy passed
  staging because staging has no users, no data, and no opinions" (taken).
- rollback: 13. Friday deploys: 9. .env: 8. TODO: 8. database: 8. cron: 7.
  cache: 6. hotfix: 5. "I added a retry loop to the payment service, and it
  worked so well it charged every customer seventeen times" (taken).
  "The bug isn't in my code — it's in the config I edited at 5pm on a Friday"
  (taken). "The Health Check Was Checking the Old Version" (taken).
  "The fix lives on an unpushed branch" (taken). "The load-bearing comment"
  (taken as a title).
- Per §10g: do NOT avoid a popular angle blindly — execute it BETTER. But a
  plain "works on my machine" cannot win criterion 5; it needs a turn nobody
  has done. Our line turns the rollback angle (13 mentions, none with
  automation + a named character).

## (c) Winner artifacts of a finished one-liner bounty (same format)

From the FINAL leaderboard of `u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7`
(`judge.artifact.text`, fetched live 2026-11-24; full file
`~/workspace/makefun-kits/analisis-20261124/lb-vacuum-final.json`).
Same pattern in the smile final (`lb-smile-final.json`).

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

**Winning pattern (15 winner texts, §10g): 2-beat + reveal in the final clause,
every time.** Escalation (crumb → furniture → room → named Kevin), specific
numbers (412×, 41×, 47×), named characters (Kevin, Unit 7, Mr. Ade, Pak Dedi).
Our earlier one-liners were 1-beat with no twist and finished unranked.

## Our entry

Final line (140 chars, 142 bytes):

> I've shipped this fix 14 times since March — production rolls it back every
> night at 2 AM. The rollback is automated now. We named it Steve.

- Beat 1 (setup): shipped the same fix 14 times since March — specific number,
  dev-credible.
- Beat 2 (escalation): production rolls it back every night at 2 AM — reveals
  the fix was never the problem.
- Reveal (final clause): the rollback is automated now, and we named it Steve
  — personification, named character, the vacuum-#1 "Kevin" pattern.
- Judge criteria: (1) on-topic excuse for prod breakage ✓; (2) twist reveals
  what really happened (auto-rollback, not a bad fix) ✓; (3) dev voice,
  jargon right (shipped, rolls back, automated) ✓; (4) tight, 140 chars,
  every word earns its place ✓; (5) fresh turn on the rollback angle — no
  public title mentions Steve, "named it", "rolls it back", or "automated now" ✓.
- Pairwise internal selection vs 5 other variants (pager-3AM, TODO-seniority,
  cache-as-database, cron-zombie-server, DNS-confession): Steve wins each
  pairing — it is the only variant with escalation AND a specific number AND a
  named character, i.e. the full winner pattern. The others were 1-reveal or
  lacked a name/number.
- No secret loader, no env reads, no network: `main.py` writes the fixed line
  deterministically to `/output/entry.txt`.
