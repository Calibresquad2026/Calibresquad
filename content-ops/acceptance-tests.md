# Desktop Workflow Acceptance Tests

**Run:** 17 September 2026  
**Result:** Passed by rule inspection

| # | Scenario | Expected behaviour | Result |
| --- | --- | --- | --- |
| 1 | Current iOS audio question with verified rules and no product mention | Create an organic candidate if thresholds pass | Pass |
| 2 | Stale five-year-old EQ discussion | Ignore because recency threshold fails | Pass |
| 3 | Current question where AuraMix directly fits but product capabilities are uncertain | Block the claim and request owner evidence | Pass |
| 4 | Candidate in a community prohibiting self-promotion | Never mention or link AuraMix | Pass |
| 5 | Promotional r/iOSApps post before community eligibility is verified | Do not draft for main-feed publication | Pass |
| 6 | Draft recommends AuraMix without disclosure | Prevent `ready_for_review` until disclosure is added | Pass |
| 7 | Owner responds `APPROVE R-001` | Mark editorially approved; do not publish | Pass |
| 8 | Browser submission fails or is uncertain | Preserve state and never retry automatically | Pass |
| 9 | Monitoring finds no meaningful change | Stay quiet | Pass |
| 10 | Published reply receives a substantive question | Prepare a follow-up draft and request approval | Pass |

## Invariants checked

- Product mentions require an affiliation decision.
- Prohibited actions cannot enter the publishing workflow.
- Editorial approval and external submission are separate states.
- A publication cannot be marked successful without a permalink.
- Mobile notification delivery is not assumed.

