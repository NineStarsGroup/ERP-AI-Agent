import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
# For Pinecone v3 serverless index creation
PINECONE_CLOUD = os.getenv("PINECONE_CLOUD", "aws")
PINECONE_REGION = os.getenv("PINECONE_REGION", "us-west-2")
# Legacy environment var (v2 SDK) is not used by v3
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
DATABASE_URL = os.getenv("DATABASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 