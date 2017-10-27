from orator.seeds import Seeder


class CreateUserSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
# see password hashing
        self.db.table('users').insert({
        'email': 'admin@admin.com',
	    'password': '123456',
        })

