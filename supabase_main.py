from supabase.client import create_client, Client

from config import SUPABASE_URL, SUPABASE_KEY

class Supabase:
    def __init__(self):
        self.supabase : Client = create_client(supabase_key=SUPABASE_KEY, supabase_url=SUPABASE_URL)


    def get_table(self, name : str):
        return self.supabase.table(name)

    def insert(self, table : str, data):
        self.get_table(table).insert(json=data).execute()