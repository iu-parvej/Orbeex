# F-NNNN — Test Plan Template

**Feature:** F-NNNN
**Owner:** 
**Requirements under test:** FR-XX-NN

## Scope

What is tested; what is explicitly out of scope.

## Test Matrix

| Layer | Test(s) | Location | Pass Criterion |
|---|---|---|---|
| Unit | | `software/.../tests` | |
| Integration | | `tests/` | |
| Property | | | |
| AI golden-plan | | `tests/qa/ai/` | |
| Performance | | `tests/reports/` | budget from `plan/metrics/` |
| E2E | | `tests/` | |

## Edge Cases

- Empty / null geometry
- Invalid CRS
- Very large datasets
- Malformed input files

## Exit Criteria

- [ ] All layers green
- [ ] Performance within budget
- [ ] No new error codes without documentation
- [ ] Coverage target met
