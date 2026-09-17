# Calibre Squad Reddit and Content Operations Design

**Date:** 16 September 2026  
**Status:** Approved, desktop-only implementation underway  
**Primary account:** `u/Calibresquad`  
**Parent brand:** Calibre Squad  
**Initial featured product:** AuraMix

## 1. Objective

Build a transparent, useful, and repeatable community-marketing system for Calibre Squad. The system will help the company participate on Reddit, develop reputation through useful contributions, publish product content across selected channels, respond to relevant discussions, and learn from results without manipulating karma or creating spam.

The first goal is not maximum posting volume. It is to establish `u/Calibresquad` as a credible founder-led company account that can discuss all Calibre Squad products while clearly disclosing commercial relationships.

## 2. Success criteria

The initial 30-day pilot succeeds when all of the following are true:

- At least 20 useful, non-promotional Reddit contributions are published.
- At least 90% of published contributions remain live after seven days.
- No account-level or community-level warnings are received.
- Every product-related contribution contains appropriate affiliation disclosure.
- At least five substantive conversations are generated, defined as a reply, follow-up question, beta enquiry, or direct product-feedback exchange.
- Direct promotional contributions remain at or below 10% of activity in each community unless that community explicitly allows more.
- The workflow records the source discussion, draft, approval, publication link, outcome, and learning for every managed contribution.

Karma is recorded as a secondary signal. It is never used as the system's primary objective or as a trigger for automated engagement.

## 3. Account architecture

### 3.1 Primary account: `u/Calibresquad`

This is the only active publishing identity during the pilot. It represents Calibre Squad and uses a human, founder-led voice.

It may discuss:

- Building apps and websites
- Product-development lessons
- Audio, equalisation, music libraries, and Apple-platform development
- AuraMix development and feedback
- Operational software and HVA Comply
- Calibre Squad consultancy experience when directly relevant

The profile must identify the account as representing Calibre Squad. Product references must not imply independence from Calibre Squad.

Recommended profile description:

> Calibre Squad is a Perth product studio and consultancy. We build practical software including AuraMix, our precision audio and EQ toolkit for iPhone, iPad and Mac. Here to share what we learn, answer questions and get honest feedback.

Recommended product disclosure:

> I am building AuraMix through Calibre Squad, so I am connected to the product. Here is what we found...

The wording may be shortened when context makes the relationship obvious, but the relationship must not be concealed.

### 3.2 Reserved AuraMix identity

Reserve one clear handle, preferably `u/AuraMixApp`, `u/AuraMixAudio`, or `u/AuraMixByCalibre`, if available. The reserved account remains inactive during the pilot and does not vote, comment, or reinforce `u/Calibresquad` activity.

Activate a separate AuraMix account only when at least two of these conditions are met:

- AuraMix is publicly available or has a substantial external beta.
- Product-specific support appears weekly.
- A dedicated AuraMix community is active.
- At least 30% of Calibre Squad's Reddit workload concerns AuraMix support.
- Official release notes and service notices need a dedicated identity.

### 3.3 AuraMix community

Create an official AuraMix subreddit only after recurring user demand exists. Its purpose will be support, feedback, release notes, feature requests, and transparent product discussion. It will not be created merely to host advertisements.

### 3.4 Account separation rules

- Calibre Squad and AuraMix accounts never vote on the same material.
- They never simulate independent agreement or praise.
- They do not post duplicate or substantially similar content.
- Each account has a distinct stated role.
- Automation never attempts to evade removals, restrictions, bans, or platform safeguards.

## 4. Content strategy

### 4.1 Reddit participation mix

Target mix for `u/Calibresquad`:

- 70% useful participation with no product mention
- 20% relevant experience with transparent Calibre Squad or AuraMix disclosure
- 10% direct announcements, links, beta recruitment, or promotion

Community-specific rules override this target. If a community prohibits promotion, the system will not introduce or link to a Calibre Squad product there.

### 4.2 Initial content pillars

1. **Audio education:** EQ concepts, listening workflows, spectrum interpretation, library management, and practical audio questions.
2. **Building AuraMix:** Product decisions, technical lessons, accessibility, testing, and honest development trade-offs.
3. **Independent app development:** Product validation, beta feedback, shipping lessons, and small-team development.
4. **Useful product feedback:** Thoughtful responses to requests, frustrations, and feature discussions without forcing an AuraMix mention.
5. **Calibre Squad field notes:** Broader lessons from building practical software and operational systems.

### 4.3 Reply quality standard

A managed reply must:

- Address the actual question or discussion.
- Add a concrete idea, example, clarification, or useful experience.
- Match the community's tone without imitating a specific person.
- Avoid generic praise and low-information comments.
- Avoid claims that cannot be supported.
- Disclose affiliation before recommending a Calibre Squad product.
- Avoid a link unless the link materially helps the reader.
- Be distinct from other replies and adapted to the full thread context.

## 5. Operating workflow

### 5.1 Opportunity intake

Candidate opportunities come from:

- Approved subreddit feeds and searches
- Replies to Calibre Squad posts or comments
- Product mentions and relevant keyword discussions
- Questions surfaced by the owner
- Planned product milestones and releases

Each candidate receives:

- Community and discussion link
- Discussion summary
- Relevance score
- Value-add opportunity
- Promotion risk
- Community-rule status
- Recommended action: ignore, reply, create post, or escalate

### 5.2 Drafting

The assistant reads the relevant discussion context and prepares a channel-native draft. Drafts contain:

- Proposed response or post
- Reason it is useful
- Disclosure, if required
- Supporting evidence or source when relevant
- Risk note when the subject is sensitive or rules are unclear

### 5.3 Approval

During the pilot, every Reddit post, comment, direct message, and edit requires explicit human approval at the point of publication. Approval of a general strategy is not approval of an unseen message.

After the pilot, low-risk scheduled content may be approved in batches. Replies to individuals, direct messages, controversial discussions, and material claims remain individually approved.

### 5.4 Publication

Publication uses the user's authenticated browser or an official, approved platform integration. Credentials are not stored in content documents. Captchas, one-time codes, and other human-verification challenges are completed by the owner.

The system records:

- Final published text
- Account used
- Channel and community
- Publication time
- Permanent link
- Approval record
- Required follow-up date

### 5.5 Monitoring and follow-up

Published material is checked for:

- Replies and questions
- Removal or moderation
- Positive and negative reception
- Useful product insight
- Support needs
- Opportunities requiring a new approved response

The assistant may prepare follow-up drafts automatically. It may not publish them without the approval required for their risk category.

## 6. Multi-channel content system

One approved source idea becomes separate channel-specific adaptations rather than identical cross-posts.

The content record contains:

- Core idea and business objective
- Intended audience
- Evidence and approved claims
- Master narrative
- Reddit version
- Other selected channel versions
- Required media
- Approval and scheduling state
- Published links
- Results and lessons

Each channel receives its own hook, length, tone, call to action, and media treatment. Reddit versions prioritize discussion and usefulness. Product announcements are adapted to the rules and expectations of the chosen community.

## 7. System components

### 7.1 AuraMix and Calibre Squad knowledge base

The knowledge base holds:

- Product descriptions and current availability
- Target audiences and use cases
- Approved feature claims
- Claims requiring evidence
- Known limitations
- Frequently asked questions
- Brand voice and examples
- Disclosure rules
- Links and assets
- Community-specific constraints

### 7.2 Content control centre

A structured database will manage opportunities, drafts, approvals, schedules, publications, conversations, and results. Airtable is the preferred first option because it can provide a visible approval queue without requiring a custom admin application. A database inside an existing Calibre Squad application remains a later option if the workflow outgrows Airtable.

### 7.3 Calibre Squad content skill

A reusable Codex skill will encode the approved positioning, writing standards, disclosure requirements, scoring model, and channel rules. It assists research and drafting but does not grant publication authority.

### 7.4 Monitoring automation

Scheduled tasks may:

- Prepare a daily opportunity digest
- Surface replies requiring attention
- Prepare a weekly performance review
- Flag removed content or rule changes
- Generate drafts for approval

Monitoring remains quiet when there is no meaningful change.

### 7.5 Publishing adapters

Use official connectors or approved APIs when available. Browser-based publication is the fallback for supervised actions. The system must not use browser automation to bypass platform restrictions or disguise automated activity.

## 8. Risk controls

The system will not:

- Automate voting or karma manipulation
- Coordinate votes across accounts
- Mass-comment or reuse substantially similar replies
- Scrape Reddit outside approved access
- Send unsolicited promotional direct messages
- Conceal a commercial relationship
- Invent customer experiences, reviews, or product claims
- Evade a subreddit ban, account restriction, or removal decision
- Publish in a community before checking its rules

High-risk topics include legal, medical, financial, safety-critical, regulatory, hostile, or personally sensitive discussions. The assistant may draft factual material for review but will not autonomously publish it.

## 9. Failure handling

- **Unclear community rule:** Do not publish. Flag the rule and request a decision.
- **Human-verification challenge:** Hand control to the owner.
- **Post or comment removal:** Record the removal, stop similar activity, and review the likely cause before retrying elsewhere.
- **Moderator warning:** Pause publishing in that community until the owner reviews it.
- **Factual uncertainty:** Remove the claim or attach a reliable source before approval.
- **Negative reply:** Prepare a calm response or recommend no reply. Do not escalate automatically.
- **Connector failure:** Preserve the approved draft and publication state; do not create duplicate submissions.
- **Platform-policy change:** Pause affected automation until the workflow is reviewed.

## 10. Measurement

### Primary measures

- Contribution survival rate after seven days
- Substantive conversation rate
- Helpful follow-up question count
- Product-feedback insights captured
- Beta or qualified-interest conversations
- Moderator warnings or removals

### Secondary measures

- Comment and post karma
- Profile visits, when available
- Website visits attributable to approved links
- Followers and community membership

Raw posting volume is not a success measure.

## 11. Rollout

### Stage 1: Identity and playbook

- Complete the `u/Calibresquad` profile.
- Verify the email and keep the profile safe-for-work.
- Evaluate Reddit Pro eligibility.
- Reserve a clearly qualified AuraMix handle.
- Finalize the product knowledge base and disclosure language.
- Select the first five to eight communities.

### Stage 2: Draft-only calibration

- Collect opportunities for one week.
- Draft responses without publishing automatically.
- Review approximately 20 candidates.
- Refine tone, relevance scoring, and community rules.

### Stage 3: Supervised publication

- Publish individually approved contributions.
- Track every outcome for 30 days.
- Review removals and negative signals immediately.

### Stage 4: Multi-channel operation

- Add the approved external channels.
- Create channel-native adaptations from source ideas.
- Introduce batch approval for planned, low-risk content.

### Stage 5: Limited automation

- Automate monitoring, triage, drafting, and reporting.
- Allow scheduled publication only where the platform permits it and the content was approved in advance.
- Keep Reddit conversational activity supervised unless a separate transparent app account receives the required platform approval.

## 12. Testing and acceptance

Before live publication:

- Test the opportunity and approval flow with ten historical or mock discussions.
- Confirm every product mention triggers an affiliation check.
- Confirm prohibited actions cannot enter the publishing queue.
- Confirm a failed publication cannot produce a duplicate.
- Confirm each published item has a traceable approval record.
- Confirm monitoring can distinguish an actionable reply from unchanged activity.

The pilot moves to broader automation only after the success criteria in Section 2 are met and the owner approves the 30-day review.

## 13. Implementation boundary

This document approves the system design, not account mutations or representational communications. Creating accounts, changing public profiles, enrolling in Reddit Pro, and publishing content will be performed only with the user's specific authorization at the appropriate action point.

## 14. Approved notification mode

The pilot is desktop-only. Local Codex task messages and approval requests are not assumed to sync to ChatGPT iOS or produce mobile push notifications. The workflow surfaces review items in the desktop task when the owner opens or returns to it. SMS, email, and a separate mobile approval application are outside the pilot.
