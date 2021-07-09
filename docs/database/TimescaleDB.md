# TimescaleDB

* Characteristics of time-series data
    * Time-centric: Data records always have a timestamp.
    * Append-only: Data is almost solely append-only (INSERTs)
    * Recent: New data is typically about recent time intervals, and we more rarely make updates or backfill missing data about old intervals.

    __Time-series data compared to other data like standard relational "business" data, is that changes to the data are inserts, not overwrites.__

* 应用场景
    * Monitoring computer systems: 
        > VM, server, container metrics (CPU, free memory, net/disk IOPs), service and application metrics (request rates, request latency)
    * Financial trading systems:
        > Classic securities, newer cryptocurrencies, payments, transaction events.
    * Internet of Things:
        > Data from sensors on industrial machines and equipment, wearable devices, vehicles, physical containers, pallets, consumer devices for smart homes, etc.
    * Eventing applications: 
        > User/customer interaction data like clickstreams, pageviews, logins, signups, etc.
    * Business intelligence: 
        > Tracking key metrics and the overall health of the business.
    * Environmental monitoring: 
        > Temperature, humidity, pressure, pH, pollen count, air flow, carbon monoxide (CO), nitrogen dioxide (NO2), particulate matter (PM10)

* The advantage of TimescaleDB:
    * Transparent and automated time partitioning 
    * Native columnar compression: 原生列压缩
    * Continuous and real-time aggregations: 持续实时聚合
    * Automated time-series data management features: 

* 使用注意事项

