from orator.migrations import Migration


class Users(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('username', 64).unique()
            table.string('name', 128)
            table.string('email', 128)
            table.string('password', 64)
            table.string('password_again', 64)
            table.text('roles')
            table.boolean('is_active').default(True)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
