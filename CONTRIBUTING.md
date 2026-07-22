# Contributing

Contributions should make the guide more accurate, reproducible, navigable, or secure.

## Good contributions

- Fix a command that changed upstream.
- Add a tested deployment or recovery recipe.
- Improve a security boundary or approval pattern.
- Replace a conceptual step with a reproducible integration.
- Add sources and verification notes.
- Repair navigation, accessibility, or broken links.

## Content labels

Use one of these labels near the beginning of a guide:

- **Verified path** — commands or configuration checked against official documentation.
- **Blueprint** — an architecture or workflow that requires custom integrations.
- **Experimental** — behavior that may change or is not recommended for production.

Every file in `use-cases/` must include the standard blueprint notice.

## Pull request checklist

- [ ] Technical claims link to primary documentation.
- [ ] Every command was checked on a current supported release or is clearly conceptual.
- [ ] No secrets, private endpoints, or signed temporary asset URLs are included.
- [ ] Sensitive actions include an approval boundary.
- [ ] Internal links are relative and valid.
- [ ] `python scripts/check_docs.py` passes.
- [ ] The pull request explains what was verified and how.

## Style

- Prefer plain language and short sections.
- Use sentence-case headings.
- Put warnings before the risky instruction.
- Avoid unverified superlatives, fixed ecosystem counts, and promises of compliance.
- Distinguish product capabilities from third-party or hypothetical integrations.
