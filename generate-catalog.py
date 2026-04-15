#!/usr/bin/env python3
"""
Generate Backstage catalog entities for performance testing.
Target: 50,000 entities across 14 files
Structure: 100 systems per file, 36 entities per system
"""

import os

SYSTEMS_PER_FILE = 100
TOTAL_FILES = 14
OUTPUT_DIR = "/Users/abarbaro/code/perf-catalog"

# Template for a single system with 36 entities
def generate_system(system_idx):
    """Generate one complete system with all its entities (36 total)"""

    return f"""---
# System Definition
apiVersion: backstage.io/v1alpha1
kind: System
metadata:
  name: janus-idp-{system_idx}
  title: Janus-IDP-{system_idx}
spec:
  owner: group-{system_idx % 100}

---
# Resource 1: PostgreSQL Database
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: pgdb-{system_idx}
  title: PostgreSQL cluster {system_idx}
  description: PostgreSQL database for application data storage
spec:
  type: database
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 2: Keycloak Identity Provider
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: keycloak-{system_idx}
  title: Keycloak {system_idx}
  description: Single sign-on and identity management
spec:
  type: identity-provider
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 3: ArgoCD
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: argocd-{system_idx}
  title: ArgoCD {system_idx}
  description: GitOps continuous delivery for Kubernetes
spec:
  type: deployment-tool
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 4: S3 Object Storage
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: obc-{system_idx}
  title: S3 Object Storage {system_idx}
  description: Object storage for techdocs and artifacts
spec:
  type: s3-bucket
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 5: GitHub Repository
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: github-{system_idx}
  title: GitHub Repository {system_idx}
  description: Source code repository
spec:
  type: repository
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 6: Redis Cache
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: redis-{system_idx}
  title: Redis Cache {system_idx}
  description: In-memory data store for caching
spec:
  type: cache
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 7: MongoDB
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: mongodb-{system_idx}
  title: MongoDB {system_idx}
  description: NoSQL document database
spec:
  type: database
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 8: Kafka
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: kafka-{system_idx}
  title: Kafka {system_idx}
  description: Distributed event streaming platform
spec:
  type: message-queue
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 9: Prometheus
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: prometheus-{system_idx}
  title: Prometheus {system_idx}
  description: Monitoring and alerting system
spec:
  type: monitoring
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 10: Grafana
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: grafana-{system_idx}
  title: Grafana {system_idx}
  description: Metrics dashboards and visualization
spec:
  type: monitoring
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 11: Jenkins
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: jenkins-{system_idx}
  title: Jenkins {system_idx}
  description: Continuous integration server
spec:
  type: ci-tool
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 12: Nexus
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: nexus-{system_idx}
  title: Nexus Repository {system_idx}
  description: Artifact repository manager
spec:
  type: artifact-repository
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 13: Vault
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: vault-{system_idx}
  title: HashiCorp Vault {system_idx}
  description: Secrets management system
spec:
  type: secrets-manager
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 14: Elasticsearch
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: elasticsearch-{system_idx}
  title: Elasticsearch {system_idx}
  description: Search and analytics engine
spec:
  type: search-engine
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 15: RabbitMQ
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: rabbitmq-{system_idx}
  title: RabbitMQ {system_idx}
  description: Message broker for async communication
spec:
  type: message-queue
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 16: MySQL
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: mysql-{system_idx}
  title: MySQL Database {system_idx}
  description: Relational database for structured data
spec:
  type: database
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 17: GitLab
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: gitlab-{system_idx}
  title: GitLab {system_idx}
  description: DevOps platform and repository
spec:
  type: repository
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 18: SonarQube
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: sonarqube-{system_idx}
  title: SonarQube {system_idx}
  description: Code quality and security analysis
spec:
  type: code-quality
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 19: Artifactory
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: artifactory-{system_idx}
  title: JFrog Artifactory {system_idx}
  description: Universal artifact repository
spec:
  type: artifact-repository
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# Resource 20: Datadog
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: datadog-{system_idx}
  title: Datadog {system_idx}
  description: Monitoring and observability platform
spec:
  type: monitoring
  lifecycle: production
  owner: group-{system_idx % 100}
  system: janus-idp-{system_idx}

---
# API 1: Petstore API
apiVersion: backstage.io/v1alpha1
kind: API
metadata:
  name: petstore-{system_idx}
  title: Petstore API {system_idx}
  description: Sample Pet Store Server based on OpenAPI 3.0
spec:
  type: openapi
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production

---
# API 2: User Management API
apiVersion: backstage.io/v1alpha1
kind: API
metadata:
  name: user-api-{system_idx}
  title: User Management API {system_idx}
  description: User registration, authentication, and profile management
spec:
  type: openapi
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production

---
# API 3: Authentication API
apiVersion: backstage.io/v1alpha1
kind: API
metadata:
  name: auth-api-{system_idx}
  title: Authentication API {system_idx}
  description: OAuth2 and SSO authentication endpoints
spec:
  type: openapi
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production

---
# API 4: Catalog API
apiVersion: backstage.io/v1alpha1
kind: API
metadata:
  name: catalog-api-{system_idx}
  title: Catalog API {system_idx}
  description: Software catalog management endpoints
spec:
  type: openapi
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production

---
# API 5: Notification API
apiVersion: backstage.io/v1alpha1
kind: API
metadata:
  name: notification-api-{system_idx}
  title: Notification API {system_idx}
  description: Email, Slack, and webhook notifications
spec:
  type: openapi
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production

---
# API 6: Metrics API
apiVersion: backstage.io/v1alpha1
kind: API
metadata:
  name: metrics-api-{system_idx}
  title: Metrics API {system_idx}
  description: Application and infrastructure metrics
spec:
  type: openapi
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production

---
# API 7: Workflow API
apiVersion: backstage.io/v1alpha1
kind: API
metadata:
  name: workflow-api-{system_idx}
  title: Workflow API {system_idx}
  description: CI/CD workflow orchestration
spec:
  type: openapi
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production

---
# API 8: Search API
apiVersion: backstage.io/v1alpha1
kind: API
metadata:
  name: search-api-{system_idx}
  title: Search API {system_idx}
  description: Full-text search across entities
spec:
  type: openapi
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production

---
# API 9: Reporting API
apiVersion: backstage.io/v1alpha1
kind: API
metadata:
  name: reporting-api-{system_idx}
  title: Reporting API {system_idx}
  description: Analytics and reporting data
spec:
  type: openapi
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production

---
# API 10: Deployment API
apiVersion: backstage.io/v1alpha1
kind: API
metadata:
  name: deployment-api-{system_idx}
  title: Deployment API {system_idx}
  description: Application deployment and release management
spec:
  type: openapi
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production

---
# Component 1: Red Hat Developer Hub
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: red-hat-developer-hub-{system_idx}
  title: Red Hat Developer Hub {system_idx}
  description: Internal developer portal platform
  annotations:
    argocd/app-name: 'janus-idp-{system_idx}'
    backstage.io/kubernetes-id: 'janus-idp-{system_idx}'
    github.com/project-slug: redhat-developer/rhdh
spec:
  type: website
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production
  dependsOn:
    - resource:pgdb-{system_idx}
    - resource:keycloak-{system_idx}
    - resource:redis-{system_idx}

---
# Component 2: Frontend Application
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: frontend-app-{system_idx}
  title: Frontend Application {system_idx}
  description: React-based user interface
spec:
  type: website
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production
  consumesApis:
    - catalog-api-{system_idx}
    - user-api-{system_idx}
    - auth-api-{system_idx}

---
# Component 3: Backend Service
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: backend-service-{system_idx}
  title: Backend Service {system_idx}
  description: Core API backend service
spec:
  type: service
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production
  providesApis:
    - catalog-api-{system_idx}
    - user-api-{system_idx}
  dependsOn:
    - resource:pgdb-{system_idx}
    - resource:mongodb-{system_idx}
    - resource:kafka-{system_idx}

---
# Component 4: API Gateway
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: api-gateway-{system_idx}
  title: API Gateway {system_idx}
  description: Central API gateway and routing
spec:
  type: service
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production
  dependsOn:
    - resource:redis-{system_idx}
    - resource:vault-{system_idx}

---
# Component 5: Worker Service
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: worker-service-{system_idx}
  title: Worker Service {system_idx}
  description: Background job processing service
spec:
  type: service
  system: janus-idp-{system_idx}
  owner: group-{system_idx % 100}
  lifecycle: production
  dependsOn:
    - resource:kafka-{system_idx}
    - resource:rabbitmq-{system_idx}
    - resource:redis-{system_idx}
"""


def main():
    print("🚀 Generating Backstage catalog for performance testing...")
    print(f"📊 Target: {TOTAL_FILES} files × {SYSTEMS_PER_FILE} systems × 36 entities = {TOTAL_FILES * SYSTEMS_PER_FILE * 36:,} entities")
    print()

    # Generate the bulk test files
    for file_idx in range(TOTAL_FILES):
        start_system = file_idx * SYSTEMS_PER_FILE
        end_system = start_system + SYSTEMS_PER_FILE - 1

        filename = f"bulk-test-systems-{file_idx:03d}.yaml"
        filepath = os.path.join(OUTPUT_DIR, filename)

        print(f"📝 Generating {filename} (systems {start_system}-{end_system})...", end=" ")

        with open(filepath, 'w') as f:
            f.write(f"# Backstage Catalog - Performance Testing\n")
            f.write(f"# File {file_idx + 1}/{TOTAL_FILES}: Systems {start_system}-{end_system}\n")
            f.write(f"# {SYSTEMS_PER_FILE} systems × 36 entities = {SYSTEMS_PER_FILE * 36} entities in this file\n")

            for system_idx in range(start_system, end_system + 1):
                f.write(generate_system(system_idx))

        file_size = os.path.getsize(filepath) / 1024 / 1024  # Size in MB
        print(f"✅ {file_size:.2f} MB")

    print()
    print("✨ Generation complete!")
    print(f"📂 Files location: {OUTPUT_DIR}")
    print(f"📈 Total entities: {TOTAL_FILES * SYSTEMS_PER_FILE * 36:,}")
    print()
    print("Next: Create location file to import all systems")


if __name__ == "__main__":
    main()
