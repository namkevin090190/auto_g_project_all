# Performance

## How to run
1. With UI

```
locust -f path/to/locustfile.py -H localhost
```
e.g `locust -f platforms/perf/bench_login/locustfile.py -H localhost`

2. Headless mode

```
locust -f path/to/locustfile.py -config path/to/config.conf --headless --users <no_of_user> --spawn-rate <spawn_rate> -t <run_time_in_seconds> -H http://localhost:5000`
```

e.g. `locust -f platforms/perf/bench_login/locustfile.py -H localhost --headless --users 10 --spawn-rate 2 -t 10 -H http://localhost:5000`