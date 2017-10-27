from orator import DatabaseManager, Model

config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'mysql',
        'database': 'test',
        'user': 'root',
        'password': 'root',
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)

