# Security review checklist

Establish the expected authorization for each operation. Locate the server-side decision, its data scope and the tests that cover allowed and denied outcomes. Use fictitious identities for review.

Review the storage and lifecycle of credentials, redaction of logs, dependency versions, validation of data sent to external systems, and defaults for new deployments. For a public release, review the exact files selected for publication.

Record the version examined, material findings, remediation, and regression evidence. A reviewer with an independent role can confirm the artifact corresponds to the version tested.
