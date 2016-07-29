from pymongo import MongoClient

client = MongoClient()
my_collection = client.my_database.my_collection

my_dict = {'name': 'Contact Name'}

def Name('Contact Name'):
    my_object =  db.my_collection.findOne({'name': 'Contact Name')
    if my_object is None:
    return 'Not Found'
    
  """Finds and returns an object matching the primary key.
     Returns none if not found.
  """

def update_object(new_object):
    my_collection.update({'name': 'Contact Name'}, my_object)
    if my_object = 
  """Updates an object if it exists, inserts if it does not exist.
  """

def remove_object(primary_key):
  """Deletes the object matching primary_key.
     Returns True if deleted, False if not found.
  """
