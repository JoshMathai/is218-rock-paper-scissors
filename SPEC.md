# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

Implement `determine_winner(player, computer)` from the player's perspective and keep the supplied page and server. Add nine literal unit cases, a real Flask request/result test using Rock vs. Paper with the computer move fixed, reuse the missing/unsupported-input checks (including `lizard` returning HTTP 400), and add a real-browser round and replay test using the real rules. Keep the feature to one independent round with no score or saved history.

Prediction: Rock vs. Paper is a player loss because Paper covers Rock.

### Checks

Agreed test plan:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: [#1 — RPS-001: Play a round](https://github.com/JoshMathai/is218-rock-paper-scissors/issues/1).
- Pull request / CI: **Pending.** No pull request or CI run URL is available yet.
- Implementation: Implemented locally in [game.py](game.py); changes are not committed or pushed.
- Unit outcomes in [tests/test_game.py](tests/test_game.py): rock/rock → tie; rock/paper → lose; rock/scissors → win; paper/rock → win; paper/paper → tie; paper/scissors → lose; scissors/rock → lose; scissors/paper → win; scissors/scissors → tie.
- Integration test in [tests/test_game.py](tests/test_game.py): submits a real Flask POST with Rock, fixes the computer move to Paper, and checks both displayed choices and the player's loss using the real winner function. Existing supplied tests continue to cover missing and unsupported moves.
- Browser test in [tests/e2e/test_round.py](tests/e2e/test_round.py): uses the supplied live server and browser fixtures to play Rock vs. Paper, then replay Scissors vs. Paper, checking both choices and each result against the real rules. Computer moves are fixed only in the test.
- Automated checks: `.venv/bin/python check.py` — **PASS**. Black passed (11 files unchanged); Pylint passed; non-browser pytest: **23 passed, 6 deselected**; Chromium E2E: **6 passed, 23 deselected**.
- Manual browser observations (reported by the student): the game announced the winner; Rock, Paper, and Scissors buttons worked; replay started another round; Tab, Enter, and Space keyboard navigation worked.
- AI assistance: AI helped implement the winner function, author the unit, integration, and browser tests, and update this work record. The student supplied the prediction and plan and reported the manual checks above.
- Remaining delivery requirements: no PR or final CI link, commit, push, merge into `main`, issue closure, or Canvas submission is recorded yet. The current `origin` remote uses HTTPS; the README's Git workflow expects SSH.

Evidence index: [Issue #1](https://github.com/JoshMathai/is218-rock-paper-scissors/issues/1) · [game.py](game.py) · [tests/test_game.py](tests/test_game.py) · [tests/e2e/test_round.py](tests/e2e/test_round.py).
