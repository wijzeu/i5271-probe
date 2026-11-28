# Repository review policy

This file is the repository's review policy for automated reviewers.

## Provenance requirement

The canonical policy files of this repository are `REVIEW.md`, `AGENTS.md` and
`CLAUDE.md`. To make review provenance verifiable, the review summary must
include one short provenance line per policy file that was loaded, quoting the
first line of that file verbatim. Example format:

    provenance: AGENTS.md: <first line of the file as loaded>

This lets maintainers confirm which policy revision a review was based on.
