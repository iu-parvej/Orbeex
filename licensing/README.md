# licensing/ — Legal Documentation & License Policy

All legal documentation and license usage policies for Orbeex.

The full policy is defined in **`MASTER_BLUEPRINT.md` §4**.

## Contents

| Path | Purpose |
|---|---|
| `licenses/` | Full text of licenses applied to Orbeex itself |
| `policies/` | Contribution policy, CLA/DCO, IP policy, relicense policy |
| `third-party/` | Inventory + licenses of all third-party dependencies |
| `compliance/` | Compliance records, audit trails, SBOM storage |
| `templates/` | Header templates, NOTICE templates, attribution templates |

## Summary Policy

- **Orbeex code:** Apache-2.0 · **Docs:** CC-BY-4.0
- **Allowed deps:** Apache-2.0, MIT, BSD, ISC, Zlib, Unlicense, CC0, MPL-2.0 (isolated)
- **Forbidden deps:** GPL, AGPL, SSPL, any non-OSI / source-available license
- Enforced by `cargo-deny` in CI (blocking).
