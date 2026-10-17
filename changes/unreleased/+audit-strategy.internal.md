---
area: infra
breaking: false
---

RustSec advisories checked via cargo-deny (every commit); removed the fragile cargo-audit job that rebuilt from source on each run. Python deps keep daily pip-audit.