from orator.seeds import Seeder


class CreatePetsSeed(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('pets').insert({
            'name': 'john',
	    'type': 'mammal',
	    'specie': 'dog',
            'age': '13'
        })
	
