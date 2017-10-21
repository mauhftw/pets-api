from orator.seeds import Seeder
from .create_pets_seed import CreatePetsSeed


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
	self.call(CreatePetsSeed)
