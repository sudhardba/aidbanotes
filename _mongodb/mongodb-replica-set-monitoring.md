---
title: MongoDB Replica Set Monitoring
parent: Replication
layout: default
category: Replication
permalink: /mongodb/mongodb-replica-set-monitoring/
---

# MongoDB Replica Set Monitoring

## Problem Statement

Describe the MongoDB issue this guide addresses and the risk to reliability or performance.

## Scope and Assumptions

- MongoDB version: `<version>`
- Deployment: `<replica set/sharded>`
- Environment: `<prod/non-prod>`
- Required privileges: `<role>`

## Pre-Checks

- Confirm maintenance window and owner approvals
- Capture baseline metrics (ops/sec, latency, replication lag)
- Verify snapshot or backup availability

## Commands

```bash
# Add MongoDB commands for this topic
mongosh --eval 'db.serverStatus().ok'
```

Expected outcome: Current cluster health and topic-specific state are measurable.

## Validation Checklist

- Primary and secondary roles healthy
- No unacceptable replication lag
- Critical workloads pass smoke checks
- Alerts remain within normal range

## Troubleshooting

- Symptom: Slow query regression
- Check indexes, execution stats, and working set pressure
- Symptom: Lag or failover instability
- Validate network, oplog window, and election behavior

## Rollback Plan

- Define rollback trigger conditions
- Document rollback sequence and approvals
- Record restoration steps if data-impacting changes occur

## Notes

- Last reviewed: `<date>`
- Owner: `<team/name>`
- Related links: `<runbooks/tickets>`
