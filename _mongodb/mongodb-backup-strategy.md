---
title: MongoDB Backup Strategy
parent: Backup
layout: default
category: Backup
permalink: /mongodb/mongodb-backup-strategy/
---

# MongoDB Backup Strategy

Use this template to document your production backup policy and execution workflow.

## Problem Statement

Document why this backup strategy exists and what business risk it mitigates.

Example: "The team needs point-in-time recovery for critical clusters while keeping backup cost predictable."

## Scope and Assumptions

- MongoDB version: `<version>`
- Deployment: `<replica set or sharded>`
- Backup target: `<S3/NFS/object storage>`
- RPO target: `<value>`
- RTO target: `<value>`

## Strategy Design

- Full backup frequency: `<daily/weekly>`
- Incremental or oplog capture: `<enabled/disabled>`
- Retention policy: `<days/weeks/months>`
- Encryption: `<at rest and in transit>`
- Restore drill cadence: `<monthly/quarterly>`

## Commands

### 1. Full Backup Example

```bash
mongodump --uri "<connection-string>" --archive=/backup/mongo/full-$(date +%F).archive --gzip
```

Expected outcome: Backup archive is created and uploaded to long-term storage.

### 2. Backup Integrity Check

```bash
ls -lh /backup/mongo/
sha256sum /backup/mongo/full-$(date +%F).archive
```

Expected outcome: File exists with expected size and checksum recorded.

### 3. Restore Validation (Non-Production)

```bash
mongorestore --uri "<restore-cluster-connection-string>" --archive=/backup/mongo/full-<date>.archive --gzip --drop
```

Expected outcome: Restore completes and application smoke tests pass.

## Validation Checklist

- Backup jobs finished on schedule
- Backup file size aligns with historical baseline
- Checksums are logged and retrievable
- Restore test completed in target RTO window
- Alerts configured for backup failures

## Troubleshooting

- Symptom: Backup job duration increased significantly
Cause to check: Storage throughput, compression overhead, network saturation.
- Symptom: Restore fails with namespace or index errors
Cause to check: Version mismatch and incompatible restore target settings.
- Symptom: Missing recent oplog history
Cause to check: Oplog window too small for planned recovery objective.

## Notes

- Last reviewed: `<date>`
- Owner: `<team or name>`
- Linked runbooks: `<links>`
