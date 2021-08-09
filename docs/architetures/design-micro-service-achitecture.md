Design Micro Service Architectures
==================================

* Great Architecture
    - Scales Development Teams
    - Delivers Quality
    - Enables High Performance / Low Cost
    - Supports Future Features Naturally

* Misconception
```
    #1: Micro Service enable our teams to choose the best programming languages and frameworks for their tasks
    Reality: We'll demonstrate just how expensive this is. Team size and investement are critical inputes

    #2: Code Generation is Evil
    Reality: Wha's important is creating a defined schema that is 100% trusted.

    #3. The Event Log Must be the Source of Truth
    Reality: Events are critical parts of an interface. But it's okay for servies to be the system of record for their resources.

    #4. Developers can maintain no more than 3 services each
    Reality: Wrong metrics; we'll demonstrate where automation shines.
```

* API Definition
```
GDPR - General Data Protection Regulation 一般数据保护条例
```

* Resouce Oriented
```

```

* Definitions in Git, with Continuous Integration
```

```

* Tests Enforce Consistency
```

```

* Tests Prevent Errors:
```

```

* API Implementation Supported by Code Generation
```

```

* Code Generation: Routes
```
Guarantee that API operations are actually defined
User friendly paths
Consistent naming
```

* Code Generation: Mock Client
```
Mock and Client from Same Source
Enables High Fidelity, Fast Testing
```

* Database Architecture
```
1. Each micro service application owns its database
2. No other service is allowed to connect to the database
3. Other services use only the service interface (API + Events)
```

* Continuous Delivery
```
Continuous Delivery is a prerequisite to managing micro service architectures
Deploy triggered by a git tag
Git tags created automatically by a change on master
100% automated, 100% reliable
Auto Deploy on New Commit on Master
```

* Event
```
Principles of an Event Interface
    First class schema for all events
        1 model / event
        N events in one union type
        1 union type / stream
        Stream owned by 1 service
        Most services define exactly 1 stream

    Producers guarantee at least once delivery
    Consumers implement idempotency [幂等]

Producers:
    Create a journal of ALL operations on table
    Record operation (insert, update, delete)
    On creation, queue the journal record to be published
    Real time, async, we publish 1 event per journal record
    Enable replay by simply requeuing journal record

Consumers:
    Store new events in local database, partitioned for fast removal
    On event arrival, queue record to be consumed
    Process incoming events in micro batches
    Record failures locally
```

* Dependencies
```
Keeping things up to date

Goal: Automatically update all service to latest dependencies
    Critical for security patches/bug fixes in core libraries
    Takes hours (not weeks or months)
    Same process for internally developed libraries and open source
    Flow: we upgrade all services every week to latest dependencies
```

* Summary: Critical Decisions
```
Design schema first for all APIs and Events
    - consume events (not API) by default

Invest in automation
    - deployment, code generation, dependency management

Enable teams to write amazing and simple tests
    - drivers quality, streamling maintenance, enables continuous delivery
```

