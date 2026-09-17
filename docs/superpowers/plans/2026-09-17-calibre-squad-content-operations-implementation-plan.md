# Calibre Squad Content Operations Implementation Plan

**Design:** `docs/superpowers/specs/2026-09-16-calibre-squad-reddit-content-operations-design.md`  
**Mode:** Desktop-only, supervised publishing  
**Status:** Desktop pilot implemented

## Phase 1: Operating foundation

1. Create a reusable Calibre Squad content-operations skill.
2. Create the product knowledge base, Reddit playbook, community watchlist, structured approval queue, and activity log.
3. Validate the skill and data files.

## Phase 2: Draft-only pilot

1. Run an initial public-web opportunity scan without accessing the Reddit account.
2. Add only high-relevance, rule-compatible candidates to the local queue.
3. Prepare drafts for desktop review; do not publish.
4. Record approval, edit, skip, and publication decisions in the queue.

## Phase 3: Desktop monitoring

1. Create a quiet weekday desktop heartbeat at 9:00 AM Australia/Perth.
2. The heartbeat checks for meaningful opportunities and replies, updates the queue, and notifies only when a review decision is needed.
3. No mobile delivery is assumed or promised.

## Phase 4: Supervised publication

1. Present each final draft with its source, rule check, disclosure status, and risk classification.
2. Obtain explicit approval for the exact text.
3. Recheck the live thread and community rules.
4. Obtain action-time confirmation before submitting through the authenticated browser.
5. Record the resulting link and monitoring date.

## Deferred items

- Reddit profile edits, Reddit Pro enrolment, handle reservation, and public posting require separate action-time authorization.
- Airtable remains an optional storage upgrade; the first pilot uses a local structured queue.
- Additional channels begin only after the Reddit pilot is calibrated.
