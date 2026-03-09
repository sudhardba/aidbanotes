---
title: Redis Backup Automation
parent: Backup
layout: default
category: Backup
permalink: /redis/redis-backup-automation/
---

# Redis Backup Automation

Use this template to define automated backup workflow for Redis persistence and disaster recovery readiness.

## Problem Statement

Describe what failure scenario this backup automation protects against.

Example: "Accidental key deletion and node loss require recoverable snapshots with minimal operator intervention."

## Scope and Assumptions

- Redis version: `<version>`
- Deployment type: `<standalone/cluster/sentinel>`
- Persistence mode: `<RDB/AOF/both>`
- Backup target: `<object storage/NFS>`
- RPO target: `<value>`

## Strategy Design

- Snapshot frequency: `<value>`
- AOF rewrite policy: `<value>`
- Retention policy: `<value>`
- Integrity checks: `<checksum policy>`
- Restore drills: `<cadence>`

## Commands

### 1. Trigger and Collect Snapshot

```bash
redis-cli -h <host> -p <port> BGSAVE
```

Expected outcome: `dump.rdb` is generated without blocking workload.

### 2. Verify Last Save Timestamp

```bash
redis-cli -h <host> -p <port> LASTSAVE
```

Expected outcome: Timestamp updates after backup run window.

### 3. Store Backup with Checksum

```bash
cp /var/lib/redis/dump.rdb /backup/redis/dump-$(date +%F).rdb
sha256sum /backup/redis/dump-$(date +%F).rdb
```

Expected outcome: Snapshot copy and checksum are recorded for audit.

## Validation Checklist

- Scheduled backup jobs complete successfully
- Backup artifacts exist in primary and remote storage
- Checksum records are preserved
- Recovery test completed in non-production
- Alerting enabled for backup failures

## Troubleshooting

- Symptom: Snapshot not updated
Cause to check: Redis persistence disabled or permission issue on data directory.
- Symptom: Backup copy fails intermittently
Cause to check: Storage mount availability and cron/task execution environment.
- Symptom: Restore starts but data mismatch appears
Cause to check: Wrong backup version or missed AOF replay requirements.

## Notes

- Last reviewed: `<date>`
- Owner: `<team or name>`
- Linked runbooks: `<links>`
