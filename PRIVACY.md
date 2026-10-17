# Privacy Policy

**Last updated: 2026-10-17**

This policy describes how Orbeex handles data. Orbeex is desktop software that runs on your
machine. The project operates no servers and collects no user data by default.

## Summary

| Question | Answer |
|---|---|
| Does Orbeex collect telemetry? | No, not by default. |
| Is geospatial data sent to any server? | No. Processing is local. |
| Is data sent to AI providers? | Only when you enable AI features, and only the task intent or dataset schema — never raw data by default. |
| Are API keys stored anywhere remote? | No. Keys are stored locally in the operating system keychain. |
| Does the project have access to your data? | No. The maintainers cannot access your machine or files. |

## 1. Data Orbeex processes

Orbeex processes geospatial datasets that you open or create, and project files that store
your work. This data remains on your device.

## 2. AI features and third-party providers

The AI features are optional and disabled until you configure a provider and supply an API
key. When you use them:

- The software sends the **task description** and, where needed, the **dataset schema**
  (field names, types, coordinate reference system, extent) to the language model provider
  you selected.
- **Raw geometry and attribute values are not sent** unless you explicitly enable that
  option for a specific task.
- The provider's own privacy policy governs that provider's handling of the request. You
  choose the provider and hold the account with it.

If you require complete isolation, use a local model. In that mode, no data leaves the
machine.

## 3. Data we do not collect

The Orbeex project and its maintainers do not collect, receive, or store:

- your datasets or project files;
- your API keys;
- your usage, location, or device information;
- crash reports, unless you explicitly choose to submit one.

## 4. Optional telemetry

Any future telemetry will be opt-in, documented in `DATA-USAGE.md`, off by default, and
reviewable before transmission. No telemetry is present in the current version.

## 5. Your controls

- Enable or disable AI features entirely.
- Choose the model provider, or use a local model.
- Restrict what context is sent per task.
- Delete all local data by removing the application and its data directory.

## 6. Regulatory position

Orbeex is designed to support compliance with data-protection regulations (for example
GDPR) by keeping data local. Because the project does not collect personal data, it does not
act as a data controller for your content. Where you send data to a third-party model
provider, that provider and you determine the applicable terms.

## 7. Changes to this policy

Material changes to this policy are recorded in the changelog and, for structural changes,
in an Architecture Decision Record under `brain/decisions/`.

## 8. Contact

Open an issue in the repository for privacy questions.
