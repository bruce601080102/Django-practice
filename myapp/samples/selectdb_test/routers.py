class MyAppRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'myapp' and model._meta.model_name == 'otherdb':
            return 'other_database'
        return 'default'

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'myapp' and model_name == 'otherdb':
            return db == 'other_database'
        return db == 'default'