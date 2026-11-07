---
title: "Messages"
source: "https://modelcontextprotocol.io/specification/2024-11-05/basic/messages.md"
scraped_at: "2026-11-07T19:29:32.107136+00:00"
doc_id: "specification/2024-11-05/basic/messages"
content_hash: "a66f1bf05d3561ee"
corpus_source: "mcp"
---

# Messages

All messages in MCP **MUST** follow the
[JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification. The protocol defines
three types of messages:

## Requests

Requests are sent from the client to the server or vice versa.

```typescript theme={null}
{
  jsonrpc: "2.0";
  id: string | number;
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

* Requests **MUST** include a string or integer ID.
* Unlike base JSON-RPC, the ID **MUST NOT** be `null`.
* The request ID **MUST NOT** have been previously used by the requestor within the same
  session.

## Responses

Responses are sent in reply to requests.

```typescript theme={null}
{
  jsonrpc: "2.0";
  id: string | number;
  result?: {
    [key: string]: unknown;
  }
  error?: {
    code: number;
    message: string;
    data?: unknown;
  }
}
```

* Responses **MUST** include the same ID as the request they correspond to.
* Either a `result` or an `error` **MUST** be set. A response **MUST NOT** set both.
* Error codes **MUST** be integers.

## Notifications

Notifications are sent from the client to the server or vice versa. They do not expect a
response.

```typescript theme={null}
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

* Notifications **MUST NOT** include an ID.
