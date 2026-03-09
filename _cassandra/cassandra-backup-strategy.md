---
title: Cassandra Backup Strategy
parent: Backup
layout: default
category: Backup
permalink: /cassandra/cassandra-backup-strategy/
---

# Cassandra Backup Strategy

Use this template to define Cassandra backup design and recovery process for production clusters.

## Problem Statement

Describe the risk and recovery requirement the strategy addresses.

Example: "Cluster-level failures or operator mistakes require predictable recovery using snapshots and commit log strategy."

## Scope and Assumptions

- Cassandra version: `<version>`
- Topology: `<single DC/multi DC>`
- Backup scope: `<keyspaces/tables>`
- Backup storage: `<object storage/NFS>`
- RPO target: `<value>`

## Strategy Design

- Snapshot schedule: `<daily/weekly>`
- Incremental backup policy: `<enabled/disabled>`
- Retention period: `<value>`
- Verification cadence: `<value>`
- Restore drill frequency: `<value>`

## Commands

### 1. Trigger Snapshot

```bash
nodetool snapshot --tag daily_backup
```

Expected outcome: Snapshot directories are created for targeted keyspaces.

### 2. Validate Snapshot Artifacts

```bash
find /var/lib/cassandra/data -type d -name snapshots | head
```

Expected outcome: Snapshot paths are present and align with backup timestamp.

### 3. Clear Old Snapshots (After Offload)

```bash
nodetool clearsnapshot --tag daily_backup
```

Expected outcome: Local snapshot cleanup succeeds only after remote backup confirmation.

## Validation Checklist

- Snapshot process completed on all nodes
- Backup data copied to remote storage
- Retention policy enforced
- Restore drill executed and documented
- Monitoring alerts for backup failures are active

## Troubleshooting

- Symptom: Snapshot size unexpectedly large
Cause to check: Compaction state and duplicate snapshot retention.
- Symptom: Incomplete backup on some nodes
Cause to check: Orchestration timeout and node-specific disk constraints.
- Symptom: Restore inconsistency between nodes
Cause to check: Partial snapshot sets or schema mismatch during restore.

## Notes

- Last reviewed: `<date>`
- Owner: `<team or name>`
- Linked runbooks: `<links>`
