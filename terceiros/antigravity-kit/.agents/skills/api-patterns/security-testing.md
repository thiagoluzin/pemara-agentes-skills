# API security review

Use this checklist during source review and in the application's local test suite. Start with one API operation and list the identity, organization, role and ownership conditions the product requires.

## Review the implementation

| Control | Evidence to locate |
| --- | --- |
| Identity | The server derives the authenticated identity from a validated session or token. Expiration and revocation are checked. |
| Resource access | The operation scopes its database query to the authorized user or organization. Object identifiers alone cannot grant access. |
| Writable fields | The service accepts a defined set of fields. Roles, ownership and server-managed state are controlled by server logic. |
| Limits | Server-side quotas protect the operation, bound expensive requests and return a documented error when exhausted. |
| Responses and logs | Users receive only the data and error detail appropriate to their role. Logs record decisions without including secrets or private records. |

For GraphQL, check authorization on the resolver that supplies each protected field. Verify configured depth and work limits against ordinary, representative queries.

## Test the documented boundary

Build fixtures for an anonymous actor, the resource owner and a member of a different test organization. For the same operation, assert the expected result for each identity. When access is denied, verify that protected fields and stored state remain unchanged. Add tests for expired sessions and a configured quota boundary where applicable. Use the project's test client and synthetic data.

Record the operation, policy, local tests, code version and any unresolved risk. Tie each finding to the smallest change that enforces the documented policy.