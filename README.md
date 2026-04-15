# Backstage Performance Testing Catalog

This directory contains catalog entities for performance testing RHDH/Backstage instances.

## 📊 Statistics

- **Total Entities**: 50,400
- **Total Systems**: 1,400
- **Entities per System**: 36
  - 1 System
  - 20 Resources
  - 10 APIs
  - 5 Components
- **Files**: 14
- **Systems per File**: 100
- **Entities per File**: 3,600

## 📁 Files

```
bulk-test-systems-000.yaml  # Systems 0-99
bulk-test-systems-001.yaml  # Systems 100-199
bulk-test-systems-002.yaml  # Systems 200-299
...
bulk-test-systems-013.yaml  # Systems 1300-1399
```

## 🚀 Usage

### Option 1: Load All Systems (Full Performance Test)

Add to your `app-config.yaml`:

```yaml
catalog:
  locations:
    - type: file
      target: /Users/abarbaro/code/perf-catalog/all-systems.yaml
```

This will load all **50,400 entities**.

### Option 2: Load Subset (Partial Test)

Load individual files for smaller tests:

```yaml
catalog:
  locations:
    # Load just one file (3,600 entities)
    - type: file
      target: /Users/abarbaro/code/perf-catalog/bulk-test-systems-000.yaml
    
    # Or load a few files (7,200 entities)
    - type: file
      target: /Users/abarbaro/code/perf-catalog/bulk-test-systems-000.yaml
    - type: file
      target: /Users/abarbaro/code/perf-catalog/bulk-test-systems-001.yaml
```

### Option 3: Load from GitHub

If you push this to GitHub:

```yaml
catalog:
  locations:
    - type: url
      target: https://github.com/YOUR_ORG/perf-catalog/blob/main/all-systems.yaml
```

## 🔄 Regenerating

To regenerate all files:

```bash
cd /Users/abarbaro/code/perf-catalog
python3 generate-catalog.py
```

## 📝 Entity Structure

Each system follows this pattern:

```
System (janus-idp-N)
├── Resources (20)
│   ├── PostgreSQL, MongoDB, MySQL, Elasticsearch
│   ├── Redis, Kafka, RabbitMQ
│   ├── ArgoCD, Jenkins
│   ├── Prometheus, Grafana, Datadog
│   ├── GitHub, GitLab, Nexus, Artifactory
│   ├── Keycloak, Vault, SonarQube
│   └── S3
├── APIs (10)
│   ├── Petstore, User, Auth, Catalog
│   ├── Notification, Metrics, Workflow
│   └── Search, Reporting, Deployment
└── Components (5)
    ├── Red Hat Developer Hub
    ├── Frontend Application
    ├── Backend Service
    ├── API Gateway
    └── Worker Service
```

## 🎯 Group Assignment

Entities are distributed across 100 groups (group-0 through group-99) using modulo:
- System 0-99 → group-0 to group-99
- System 100-199 → group-0 to group-99
- etc.

Make sure you have these groups in your LDAP/catalog before loading.

## ⚠️ Performance Notes

Loading 50,400 entities will:
- Take significant time on first import
- Require adequate database resources (PostgreSQL)
- Use considerable memory during processing

Monitor:
- Catalog processing time
- Database query performance
- Memory usage
- Search index build time
