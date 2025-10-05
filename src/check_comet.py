import os
from dotenv import load_dotenv

load_dotenv()

workspace = os.getenv('COMET_WORKSPACE')
project = os.getenv('COMET_PROJECT_NAME')
api_key = os.getenv('COMET_API_KEY')

print(f"Workspace: {workspace}")
print(f"Project: {project}")
print(f"API Key: {'*' * 10 + api_key[-4:] if api_key else 'Not set'}")
print(f"\nExperiments URL: https://www.comet.com/{workspace}/{project}")
print(f"\nDirect links from logs:")
print("1. gpt-4o: https://www.comet.com/sidhant-garg/testing/50c5d7acf3f04a20a1587d21c9686d25")
print("2. gpt-4o-mini: https://www.comet.com/sidhant-garg/testing/9a0245def9b94dfb8c5e644172b1757d")
print("3. gpt-4-turbo: https://www.comet.com/sidhant-garg/testing/269e3fbff9ca443b9304cbd2b5a17033")
print("4. gpt-4: https://www.comet.com/sidhant-garg/testing/e800baf20eae42ac9215e89a0de0e509")
print("5. gpt-3.5-turbo: https://www.comet.com/sidhant-garg/testing/bad26522fa7e438795e8cedd95832116")
