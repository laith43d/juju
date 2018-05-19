from orator.migrations import Migration


class Users(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('username', 64).unique()
            table.string('name', 120)
            table.string('email', 120).unique()
            table.string('password', 128)
            table.string('password_again', 128)
            table.text('roles')
            table.boolean('is_active').default(True)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
