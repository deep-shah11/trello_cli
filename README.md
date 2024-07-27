
# Trello CLI Card Creator

This Python script allows you to create a Trello card via the command line using Trello's API. You can optionally add labels and comments to the card.

## Prerequisites

- Python 3
- `requests` library

Install the `requests` library using pip if you haven't already:

```bash
pip install requests
```

## Setup

### API Key and Token

You need a Trello API key and token to use this script. Visit this [blog post](https://www.merge.dev/blog/trello-api-key) to understand how to get your API key and token.

### List ID

You also need the ID of the Trello list where you want to create the card. Visit this [blog post](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.trello/#templates-and-examples) to find the List ID or essentially any other IDs you might need such as Card IDs, Member IDs, etc.

## Usage

### Setting API Key and Token

You can either set your API key and token directly in the script ***trello_cli.py*** for one-time setup:

```python
API_KEY = 'your_api_key'
TOKEN = 'your_auth_token'
```

Or you can include them every time in the CLI command.

### Command Line Arguments

The script accepts several command-line arguments to customize the Trello card creation. Below are the available options:

```bash
python3 trello_cli.py -id LIST_ID [-key API_KEY] [-tok TOKEN] [-n NAME] [-d DESC] [-p POS] [-l LABELS] [-c COMMENT] [-ln LABEL_NAME] [-lc LABEL_COLOR] [-m MEMBERS] [-sd START] [-dd DUE] [-dc DUE_COMPLETE] [-u URL_SOURCE] [-f FILE_SOURCE] [-mt MIME_TYPE] [-ics CARD_SOURCE] [-kfs KEEP_FROM_SOURCE] [-add ADDRESS] [-loc LOCATION_NAME] [-coord COORDINATES]
```

#### Required Arguments:

- `-id`, `--idList`: The ID of the Trello list

#### Optional Arguments:

- `-key`, `--api_key`: The API key of the Trello account
- `-tok`, `--auth_token`: The OAuth token of the Trello account
- `-n`, `--name`: The name of the Trello card
- `-d`, `--desc`: The description of the Trello card
- `-p`, `--pos`: The position of the Trello card in the list - top, bottom, or a position number
- `-l`, `--idLabels`: The IDs of the labels to be added (space-separated)
- `-c`, `--comment_text`: The comment text
- `-ln`, `--label_name`: The name of the new label to create on the card
- `-lc`, `--label_color`: The color of the new label to create on the card
- `-m`, `--idMembers`: The IDs of the members to be added (space-separated)
- `-sd`, `--start`: The start date for the card
- `-dd`, `--due`: The due date for the card
- `-dc`, `--dueComplete`: The due complete flag for the card
- `-u`, `--urlSource`: The URL source for the card (starting with http:// or https://)
- `-f`, `--fileSource`: The file source for the card (binary)
- `-mt`, `--mimeType`: The mime type for the card (max 256 characters)
- `-ics`, `--idCardSource`: The ID of a card to copy into the new card
- `-kfs`, `--keepFromSource`: Properties to copy from the source card (comma-separated)
- `-add`, `--address`: For use with/by the Map View
- `-loc`, `--locationName`: For use with/by the Map View
- `-coord`, `--coordinates`: For use with/by the Map View. Should take the form latitude,longitude

### Example Command

To create a card with the name "Test Card" and description "This is a test card", run:

```bash
python3 trello_cli.py -id your_list_id -n "Test Card" -d "This is a test card" -key your_api_key -tok your_token
```

## API Documentation

Refer to the [Trello API documentation](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post) for more details on the available endpoints and parameters.

## Next Development Steps

1. **Error Handling**: Implement better error handling to manage API failures, invalid inputs, and other issues.
2. **Unit Tests**: Could write unit tests to make sure that the script works as expected.
3. **CLI Interface**: Improve the CLI interface to make it more user-friendly and add more detailed help messages. Additionally, can also add mode select functionality to select the Component that we want to add/ update/ delete (eg. boards, cards, labels, etc.).
4. **Logging**: Add logging to the script to help with debugging.
5. **Config File**: Allow users to set their API key, token, and other default settings in a configuration file, or set it in a config file ourselves when user enters it once.

## Additional Trello API Functionality

1. **Card Updates**: Add functionality to update existing cards with new details, labels, or comments.
2. **Board Management**: Add functionality to create, update, and delete Trello boards separately.
3. **List Management**: Add functionality to create, update, and delete lists from within boards separately.
4. **Label Management**: Add functionality to include creating, updating, and deleting labels separately.
5. **Comment Handling**: Improve comment handling by adding functionality for editing and deleting comments.

Similarly, we can go on to create an almighty Trello CLI that extends all the API functionalities provided by the Trello REST APIs. 