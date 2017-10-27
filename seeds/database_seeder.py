from orator.seeds import Seeder
from create_pets_seeder import CreatePetsSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
	self.call(CreatePetsSeeder)
	self.call(CreateUserSeeder)

