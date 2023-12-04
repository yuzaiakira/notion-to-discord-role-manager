from notion_client import Client

from config import I_TOKEN, DATABASE_ID

notion = Client(auth=I_TOKEN)


# retrieve a database
async def fetch_notion_data():
    """Fetch notion page data from API

    Returns:
        dict: Notion databases data
    """
    try:
        return notion.databases.query(**{"database_id": DATABASE_ID})
    except Exception as e:
        print(f"An error occurred while fetching data from Notion: {e}")
        return None
    
    
async def get_user_data():
    """Yields Notion data from API for each user by querying the Notion database.


    Yields:
        dict: A dictionary containing user data.
    """
    output = await fetch_notion_data()
    
    if output:
        for page in output["results"]:
            roles = [role['name'] for role in page['properties']['roles']['multi_select']]
            user_data = {
                'user_name': page['properties']['user name']['title'][0]['text']['content'],
                'user_id': int(page['properties']['user id']['rich_text'][0]['text']['content']),
                'roles': roles
            }
            yield user_data
