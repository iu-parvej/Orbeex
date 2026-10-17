# licensing/ — Legal Documentation & License Policy

All legal documentation and license usage policies for Orbeex.

The binding policy is `policies/dependency-license-policy.md` (in this folder) and is enforced by `cargo-deny` in CI.

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
