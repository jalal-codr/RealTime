# import os
# from pymongo import MongoClient
# from dotenv import load_dotenv

# load_dotenv()

# #Data base connection

# mongo_uri=os.getenv("MONGO_URI")

# client = MongoClient(
#     mongo_uri,
#     tls=True,
#     tlsAllowInvalidCertificates=True
#     )

# db=client.db