# Connect selected sources after the interview

Inspect the host's available tools only after all seven answers are collected. Reuse verified available connections. For missing connections, use its supported plugin or connector discovery and present its actual install/connect control when available. Do not invent buttons, claim installation, or repeat a request for an already connected service. Request the minimum access needed to read the chosen source.

If no supported connector exists, check the service's current official API documentation. Use an API only when the environment has a usable way to call it securely. Otherwise offer a user-provided export or supported link; a key alone is not an integration.

For an API fallback:
1. Confirm the official key creation page and required permissions. Give a short, accurate route to that page; never guess menu names.
2. Run `python scripts/prepare_env.py VARIABLE_NAME` from the root with the documented environment variable name, for example `FATHOM_API_KEY` only if that is what the integration actually reads. The helper adds an empty field to ignored local `.env` without replacing existing values. It refuses tracked or unignored files. No secret may be passed as a command argument.
3. Link the actual absolute local `.env` file. Say: "I created a field called VARIABLE_NAME. Open this file and paste your key after the equals sign. Save it, then tell me you're ready. Never share API keys, passwords, or confidential information in this chat." If an existing field was preserved, say so rather than claiming it is empty.
4. Do not read or print the filled file into chat or model context. The authorized adapter may load it privately in-process. Avoid secret-bearing command lines, logs, URLs, and error dumps. Use secure credential storage instead when the host supports it.
5. Test one minimal authorized read after the user confirms saving. Record date, source scope, success or blocker, never credentials.

If Python or the helper is unavailable, create the same empty local field only after verifying ignore rules and that the file is not tracked; preserve existing content without displaying it. If safe setup cannot be verified, use the connector or export route instead.

Keep `.env.example` safe and tracked with empty example fields only. Never commit a real `.env` or other credential file. Check staged paths before publishing.

Do not loop endlessly on blocked access. Continue with available sources and name the gap. Access setup does not grant permission to send, publish, delete, or change external records.
