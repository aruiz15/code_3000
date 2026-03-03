# security overview

## intended users
this repository is intended only for:
- student (repo owner)
- course instructor and TAs

## risk assessment 
repository contains coursework assignments and educational datasets. while the data looks to be low-risk some potential concerns could include:

- exposure of personal identifying information if accidentally committed
- academic integrity risks if others copy coursework solutions
- misuse of code in unintended contexts

if this repository were to fall into the wrong hands the most realistic risks would involve academic dishonesty or minor privacy concerns.

## security measures
steps that can be taken to secure this repository include:

- avoiding committing sensitive information (API keys, passwords, etc.)
- using a CODEOWNERS file to define code ownership
- applying GitHub branch protection rules or rulesets to prevent force pushes and accidental deletion
- requiring pull request review before merging changes

given that this repository is primarily for coursework and does not contain sensitive production systems additional security hardening is not strictly necessary.