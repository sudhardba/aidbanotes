# Oracle RMAN Backup Strategy

## Overview
This article explains RMAN backup strategy.

## Commands

```bash
rman target /

backup database plus archivelog;
```

## Verification

```sql
list backup summary;
```

## Troubleshooting

Common issues:
- Archive log missing
- Backup storage full