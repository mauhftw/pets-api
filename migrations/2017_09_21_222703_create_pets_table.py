from orator.migrations import Migration


class CreatePetsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
	with self.schema.create('pets') as table:
		table.increments('id').unique()
		table.string('name')
		table.string('type')
		table.integer('age')
		table.string('specie')
		table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
	self.schema.drop('pets')
