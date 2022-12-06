from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.test import TestCase


class TestMigrations(TestCase):
    """
    Test the effect of applying a migration
    Adapted from https://github.com/open-formulieren/open-forms/blob/e64c9368264d3f662542866e2d7d5ba15e0f265c/src/openforms/utils/tests/test_migrations.py
    """

    app = None
    migrate_from = None
    migrate_to = None

    def setUp(self):
        assert self.migrate_from and self.migrate_to and self.app, (
            "TestCase '%s' must define migrate_from, migrate_to and app properties"
            % type(self).__name__
        )
        self.migrate_from = [(self.app, self.migrate_from)]
        self.migrate_to = [(self.app, self.migrate_to)]
        executor = MigrationExecutor(connection)
        old_apps = executor.loader.project_state(self.migrate_from).apps

        # Reverse to the original migration
        executor.migrate(self.migrate_from)

        self.setUpBeforeMigration(old_apps)

        # Run the migration to test
        executor = MigrationExecutor(connection)
        executor.loader.build_graph()  # reload.
        executor.migrate(self.migrate_to)

        self.apps = executor.loader.project_state(self.migrate_to).apps

    def setUpBeforeMigration(self, apps):
        pass
