# Approval Queue Schema

## Queue envelope

- `schema_version`: integer, currently `1`.
- `last_updated`: ISO 8601 timestamp with timezone.
- `next_id`: next numeric suffix for an ID formatted as `R-001`.
- `items`: array of queue items.

## Queue item

Every item must contain:

- `id`: stable ID such as `R-001`.
- `status`: one of `candidate`, `ready_for_review`, `needs_edit`, `approved`, `ready_to_publish`, `published`, `skipped`, `blocked`, or `removed`.
- `created_at` and `updated_at`: ISO 8601 timestamps with timezone.
- `source_url`: canonical Reddit discussion URL.
- `community`: subreddit name including `r/`.
- `thread_title`: title as observed.
- `opportunity_summary`: what the person is asking or discussing.
- `value_add`: the distinct help Calibre Squad can provide.
- `category`: `organic`, `experience`, or `promotion`.
- `scores`: integers from 1 to 5 for `relevance`, `value`, `recency`, `confidence`, and `promotion_risk`.
- `risk`: `low`, `medium`, or `high`.
- `rule_check`: object with `checked_at`, `summary`, and `source_urls`.
- `evidence_notes`: verified facts supporting the reply.
- `disclosure_required`: boolean.
- `link_recommended`: boolean.
- `draft`: the proposed final text, or an empty string while status is `candidate`.
- `owner_decision`: `null`, `approved`, `edit`, or `skipped`.
- `approved_at`: ISO 8601 timestamp or `null`.
- `publication`: object with `status`, `permalink`, `published_at`, and `follow_up_at`; values are `null` until applicable.
- `notes`: short operational notes.

## State safeguards

- Only the owner can cause `owner_decision` to become `approved`.
- Editorial approval moves an item to `approved`, never directly to `published`.
- `ready_to_publish` requires a fresh live-thread and rule check.
- `published` requires a verified permalink and timestamp.
- A failed or uncertain submission never creates another automatic attempt.

