API_HOST = {
    'test': 'http://localhost/mysite/wp-json/wc/v3/',
    'dev': '',
    'prod': '',
}

WOO_API_HOST = {
    'test': 'http://localhost/mysite/',
    'dev': '',
    'prod': '',
}

DB_HOST = {
    'machine1': {
        "test": {
            "host": "localhost",
            "database": "mysite",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
        "dev": {
            "host": "host.docker.internal",
            "database": "mysite",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
        "prod": {
            "host": "host.docker.internal",
            "database": "mysite",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },

    },
    'docker': {
        "test": {
            "host": "host.docker.internal",
            "database": "mysite",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
        "dev": {
            "host": "host.docker.internal",
            "database": "mysite",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
        "prod": {
            "host": "host.docker.internal",
            "database": "mysite",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
    },
    'machine2': {
        "test": {
            "host": "localhost",
            "database": "mysite",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
        "dev": {
            "host": "host.docker.internal",
            "database": "mysite",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
        "prod": {
            "host": "host.docker.internal",
            "database": "mysite",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
    }
}
