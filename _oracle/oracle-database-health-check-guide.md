---
title: Oracle Database Health Check Guide
parent: Operations
nav_order: 1
layout: default
category: General
permalink: /oracle/oracle-database-health-check-guide/
---


# Oracle Database Health Check Guide

Use this page as a reusable template for operational runbooks and DBA-focused blog articles.

## Problem Statement

Describe the operational problem in 2-3 lines.

Example: "Database response time increased after a patch window, and on-call needs a fast health validation checklist."

## When to Use This Guide

- Planned maintenance validation
- Incident triage (high CPU, sessions waiting, slow SQL)
- Daily or weekly production health checks

## Scope and Assumptions

- Oracle version: `<version>`
- Environment: `<single instance or RAC>`
- Privileges required: `<SYSDBA or read-only views>`
- Change window: `<yes/no>`

## Commands

### 1. Instance and Database Status

```sql
select instance_name, status, database_status from v$instance;
select name, open_mode, log_mode from v$database;
```

Expected outcome: Instance should be `OPEN` and database mode should match target state.

### 2. Tablespace Usage Snapshot

```sql
select tablespace_name,
			 round(used_percent, 2) as used_percent
from dba_tablespace_usage_metrics
order by used_percent desc;
```

Expected outcome: No critical tablespace near threshold (define your own alert limits).

### 3. Blocking Sessions

```sql
select sid, serial#, blocking_session, event, wait_class
from v$session
where blocking_session is not null;
```

Expected outcome: No long-lived blocking chains without a known business reason.

### 4. Top SQL by Elapsed Time

```sql
select *
from (
	select sql_id,
				 elapsed_time/1000000 as elapsed_sec,
				 executions,
				 substr(sql_text, 1, 120) as sql_text
	from v$sql
	where executions > 0
	order by elapsed_time desc
)
where rownum <= 10;
```

Expected outcome: Top SQL should be known workloads. Unknown statements require investigation.

## Validation Checklist

- Instance and listener are healthy
- Tablespaces have safe free capacity
- No abnormal lock/blocking patterns
- No unexplained spike in top SQL elapsed time
- Backup and archive log activity are normal

## Rollback or Mitigation

If checks fail after a recent change, document rollback plan here:

- Revert parameter/configuration: `<steps>`
- Stop risky batch jobs: `<steps>`
- Escalate to app owner/on-call DBA: `<contact path>`

## Troubleshooting

- Symptom: High CPU but low user throughput
	- Check AWR/ASH for top waits and SQL plan changes
- Symptom: Frequent `log file sync`
	- Check redo sizing and commit behavior
- Symptom: Sudden session growth
	- Check connection pooling and failed app retries

## Monitoring and Alert Thresholds

- CPU warning: `<value>`
- Sessions warning: `<value>`
- Tablespace warning/critical: `<value>/<value>`
- Backup duration threshold: `<value>`

## Notes

- Last tested on: `<date>`
- Author: `<name>`
- Review cadence: `<monthly/quarterly>`
- Related guides: `<links>`
