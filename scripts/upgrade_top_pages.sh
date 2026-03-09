#!/bin/zsh
set -euo pipefail

rewrite_with_template() {
  local file="$1"
  local template="$2"
  awk 'BEGIN{in_fm=0;done=0}
  {
    if (NR==1 && $0=="---") in_fm=1
    if (in_fm==1) {
      print
      if ($0=="---" && NR>1) {
        in_fm=2
        next
      }
      next
    }
    if (in_fm==2 && done==0) {
      print ""
      while ((getline line < tmpl) > 0) print line
      close(tmpl)
      done=1
      exit
    }
  }' tmpl="$template" "$file" > "$file.tmp"
  mv "$file.tmp" "$file"
}

cat > /tmp/template_oracle.md <<'EOF'
# {{TITLE}}

## Problem Statement

Define the Oracle operational problem this guide solves and the production impact if not addressed.

## Scope and Assumptions

- Oracle version: `<version>`
- Deployment: `<single instance or RAC>`
- Environment: `<prod/non-prod>`
- Required privileges: `<SYSDBA/read-only>`

## Pre-Checks

- Confirm change window and rollback owner
- Capture current database health snapshot
- Validate storage and backup availability

## Commands

```sql
-- Add Oracle-specific commands for this topic
select instance_name, status from v$instance;
```

Expected outcome: Commands validate the current state before and after changes.

## Validation Checklist

- Expected state achieved
- No new critical alerts
- Key queries/jobs complete successfully
- Evidence captured for audit/change record

## Troubleshooting

- Symptom: Unexpected wait events
- Check top SQL, AWR/ASH, and blocking sessions
- Symptom: Post-change latency increase
- Verify plan changes, stats freshness, and resource pressure

## Rollback Plan

- Define exact rollback triggers
- Document rollback commands and sequence
- Identify approver and communication channel

## Notes

- Last reviewed: `<date>`
- Owner: `<team/name>`
- Related links: `<runbooks/tickets>`
EOF

cat > /tmp/template_mongodb.md <<'EOF'
# {{TITLE}}

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
EOF

cat > /tmp/template_postgresql.md <<'EOF'
# {{TITLE}}

## Problem Statement

Explain the PostgreSQL operational challenge and expected impact on reliability or throughput.

## Scope and Assumptions

- PostgreSQL version: `<version>`
- Deployment: `<single/HA>`
- Environment: `<prod/non-prod>`
- Required privileges: `<role>`

## Pre-Checks

- Confirm backup and WAL retention for recovery needs
- Capture baseline latency, locks, and bloat indicators
- Confirm maintenance and change approvals

## Commands

```sql
-- Add PostgreSQL commands for this topic
select now(), current_setting('server_version');
```

Expected outcome: Baseline and target state are clearly measurable.

## Validation Checklist

- Replication and HA status healthy
- Query latency within threshold
- No critical lock or bloat regressions
- Monitoring and alerts stable

## Troubleshooting

- Symptom: Throughput drop
- Check plans, checkpoints, autovacuum, and IO contention
- Symptom: Replication delay
- Validate WAL generation rate and replica apply lag

## Rollback Plan

- Define rollback criteria and approval path
- Document rollback commands and restore path
- Verify post-rollback service health

## Notes

- Last reviewed: `<date>`
- Owner: `<team/name>`
- Related links: `<runbooks/tickets>`
EOF

cat > /tmp/template_redis.md <<'EOF'
# {{TITLE}}

## Problem Statement

Describe the Redis reliability or performance issue this guide is intended to solve.

## Scope and Assumptions

- Redis version: `<version>`
- Deployment: `<standalone/sentinel/cluster>`
- Environment: `<prod/non-prod>`
- Persistence mode: `<RDB/AOF>`

## Pre-Checks

- Confirm backup and restore readiness
- Capture baseline latency, memory, and keyspace stats
- Validate ownership and change approvals

## Commands

```bash
# Add Redis commands for this topic
redis-cli INFO server | head
```

Expected outcome: Topic-specific state is visible and verifiable.

## Validation Checklist

- Service availability remains stable
- Latency and memory metrics within thresholds
- Replication and failover behavior healthy
- Backup and persistence signals healthy

## Troubleshooting

- Symptom: Memory pressure increase
- Check fragmentation, eviction policy, and large keys
- Symptom: Slow operations
- Review slowlog, client behavior, and command patterns

## Rollback Plan

- Define rollback criteria and timeline
- Document rollback commands and owner approvals
- Validate service and data integrity after rollback

## Notes

- Last reviewed: `<date>`
- Owner: `<team/name>`
- Related links: `<runbooks/tickets>`
EOF

cat > /tmp/template_cassandra.md <<'EOF'
# {{TITLE}}

## Problem Statement

Describe the Cassandra cluster risk or operational issue addressed by this guide.

## Scope and Assumptions

- Cassandra version: `<version>`
- Topology: `<single DC/multi DC>`
- Environment: `<prod/non-prod>`
- Keyspaces in scope: `<list>`

## Pre-Checks

- Confirm cluster health and node status
- Capture baseline latency and compaction or repair metrics
- Validate snapshot and restore readiness

## Commands

```bash
# Add Cassandra commands for this topic
nodetool status
```

Expected outcome: Cluster baseline and target state are verifiable.

## Validation Checklist

- Node state remains healthy across ring
- Read and write latencies remain acceptable
- Repair and compaction backlog not regressed
- Monitoring alerts remain normal

## Troubleshooting

- Symptom: Uneven performance across nodes
- Check token distribution, disk usage, and compaction state
- Symptom: Repair-related instability
- Validate scheduling, concurrency, and network saturation

## Rollback Plan

- Define rollback triggers and owner
- Document rollback sequence per node or cluster
- Validate consistency and service health after rollback

## Notes

- Last reviewed: `<date>`
- Owner: `<team/name>`
- Related links: `<runbooks/tickets>`
EOF

process_files() {
  local tmpl="$1"
  shift
  for f in "$@"; do
    local title
    title=$(awk '/^# /{sub(/^# /, ""); print; exit}' "$f")
    sed "s/{{TITLE}}/${title//\//\\/}/g" "$tmpl" > /tmp/current_template.md
    rewrite_with_template "$f" /tmp/current_template.md
  done
}

process_files /tmp/template_oracle.md \
  _oracle/oracle-backup-strategy-for-production.md \
  _oracle/oracle-installation-step-by-step-guide.md \
  _oracle/oracle-query-performance-troubleshooting.md \
  _oracle/oracle-rman-restore-guide.md

process_files /tmp/template_mongodb.md \
  _mongodb/mongodb-installation-guide.md \
  _mongodb/mongodb-query-performance-tuning.md \
  _mongodb/mongodb-replica-set-monitoring.md \
  _mongodb/mongodb-security-basics.md

process_files /tmp/template_postgresql.md \
  _postgresql/postgresql-installation-guide.md \
  _postgresql/postgresql-query-performance-tuning.md \
  _postgresql/postgresql-replication-monitoring.md \
  _postgresql/postgresql-autovacuum-troubleshooting.md

process_files /tmp/template_redis.md \
  _redis/redis-installation-guide.md \
  _redis/redis-memory-optimization-guide.md \
  _redis/redis-replication-monitoring.md \
  _redis/redis-slow-log-troubleshooting.md

process_files /tmp/template_cassandra.md \
  _cassandra/cassandra-installation-guide.md \
  _cassandra/cassandra-performance-troubleshooting.md \
  _cassandra/cassandra-repair-operation-guide.md \
  _cassandra/cassandra-monitoring-basics.md

echo "Updated 20 priority pages."
