# Metrics Microservice

[![CI](https://github.com/Ubademy-G3/metrics.service/actions/workflows/default.yml/badge.svg)](https://github.com/Ubademy-G3/metrics.service/actions/workflows/default.yml)
[![codecov](https://codecov.io/gh/Ubademy-G3/metrics.service/branch/main/graph/badge.svg?token=P5PT97QTE2)](https://codecov.io/gh/Ubademy-G3/metrics.service)

# File Structure:
```tree
├── main.py
├── src
│   ├── infrastructure
│   │   ├── db
│   │   │   ├──  metrics_courses_schema.py 
│   │   │   └──  database.py 
│   │   ├── routes
│   │   │   └──  metrics_courses.py
│   ├── persistence
│   │   └── repositories
│   │       └── metrics_course_repository_postgres.py
│   ├── application
│   │   ├── controllers
│   │   │   └── 
│   │   ├──serializers
│   │   │   └── 
│   │   └── useCases
│   │       └── 
│   └── domain
│       ├── metrics_course_model.py
│       └── metrics_course_repository.py
├── monitoring
├── deploy
└── tests
```

# Local Environment 

## Requirements 

* Docker
* Docker-compose

## Build and Deploy Services

```docker-compose up -d --build```

This command deploys the service:

* `metricsservice_web`: Web Service
* `metricsservice_db`: Data base
* `pgadmin`: Data base admin

## Stop services

```docker-compose stop```
