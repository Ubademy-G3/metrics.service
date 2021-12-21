# Metrics Microservice

[![CI](https://github.com/Ubademy-G3/metrics.service/actions/workflows/default.yml/badge.svg)](https://github.com/Ubademy-G3/metrics.service/actions/workflows/default.yml)
[![codecov](https://codecov.io/gh/Ubademy-G3/metrics.service/branch/main/graph/badge.svg?token=5YTWOVJWEY)](https://codecov.io/gh/Ubademy-G3/metrics.service)

Service for obtain metrics of Courses (with their exams), Users and Payments microservices.

# Directory structure:

```tree
├── application
│   ├── controllers
│   │   ├── courses_controller.py
│   │   ├── __init__.py
│   │   ├── payments_controller.py
│   │   └── users_controller.py
│   ├── __init__.py
│   ├── services
│   │   ├── auth.py
│   │   └── __init__.py
│   └── use_cases
│       ├── courses
│       │   └── get.py
│       ├── __init__.py
│       ├── payments
│       │   └── get.py
│       └── users
│           └── get.py
├── deploy
│   └── heroku-entrypoint.sh
├── docker-compose.yml
├── Dockerfile
├── exceptions
│   ├── auth_error.py
│   └── __init__.py
├── heroku.yml
├── infrastructure
│   ├── __init__.py
│   └── routes
│       ├── __init__.py
│       └── metrics_router.py
├── LICENSE
├── logging.ini
├── logs.log
├── main.py
├── monitoring
│   └── datadog.yml
├── README.md
├── requirements.txt
└── tests
    ├── conftest.py
    ├── __init__.py
    └── test_metrics.py
```

# Local Environment 

## Requirements 

* Docker
* Docker-compose

## Environment variables

To run this application you need to define the following environment variables:

```
API_KEY = YOUR_METRICS_SERVICE_APIKEY

USERS_SERVICE_API_KEY = YOUR_USERS_SERVICE_API_KEY
COURSES_SERVICE_API_KEY = YOUR_COURSES_SERVICE_API_KEY
PAYMENTS_SERVICE_API_KEY = YOUR_PAYMENTS_SERVICE_API_KEY
EXAMS_SERVICE_API_KEY = YOUR_EXAMS_SERVICE_API_KEY

USERS_SERVICE_URL = PRODUCTIVE_USERS_SERVICE_URL 
COURSES_SERVICE_URL = PRODUCTIVE_COURSES_SERVICE_URL
EXAMS_SERVICE_URL = PRODUCTIVE_EXAMS_SERVICE_URL
PAYMENTS_SERVICE_URL = PRODUCTIVE_PAYMENTS_SERVICE_URL
```

## Build and Deploy Services

```docker-compose up -d --build```

This command deploys the service:

* `metricsservice_web`: Web Service

## Stop services

```docker-compose stop```

## Down services and remove containers, networks, volumes and images created by 'up'

```docker-compose down```

## To run tests

```docker-compose exec web pytest .```


You can try it out at <https://https://staging-metrics-service.herokuapp.com/docs>