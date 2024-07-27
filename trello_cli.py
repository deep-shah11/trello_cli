import requests
import argparse


API_KEY = 'your_api_key'
TOKEN = 'your_auth_token'


class TrelloClient:
    def __init__(self, api_key, token):
        self.api_key = api_key
        self.token = token
        self.base_url = 'https://api.trello.com/1'

    def create_card(self, args):
        url = f"{self.base_url}/cards"

        query = {
            'key': self.api_key,
            'token': self.token,
            'idList': args.idList
        }

        optional_params = ['name', 'desc', 'pos', 'idLabels', 'idMembers', 'start', 'due', 'dueComplete',
                           'urlSource', 'fileSource', 'mimeType', 'idCardSource', 'keepFromSource',
                           'address', 'locationName', 'coordinates']

        for param in optional_params:
            value = getattr(args, param, None)
            if value is not None:
                print(param, value)
                query[param] = value

        response = requests.post(url, params=query)
        return response.json()

    def add_label(self, card_id, label_name, label_color):
        url = f"{self.base_url}/cards/{card_id}/labels"
        query = {
            'key': self.api_key,
            'token': self.token,
            'name': label_name,
            'color': label_color
        }
        response = requests.post(url, params=query)
        return response.json()

    def add_comment(self, card_id, comment_text):
        url = f"{self.base_url}/cards/{card_id}/actions/comments"
        query = {
            'key': self.api_key,
            'token': self.token,
            'text': comment_text
        }
        response = requests.post(url, params=query)
        return response.json()


def str_or_float(value):
    try:
        return value if (value == 'top' or value == 'bottom') else float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Invalid value: {value}. Must be 'top', 'bottom', or a position number (float).")


def str_character_check(value):
    if len(value) > 256:
        raise argparse.ArgumentTypeError(f"Invalid value: {value}. Must be less than 256 characters.")
    return value


def url_check(value):
    if not value.startswith('http'):
        raise argparse.ArgumentTypeError(f"Invalid value: {value}. Must start with 'http'.")
    return value


def kfs_check(*value):
    for item in value:
        if item not in ['all', 'attachments', 'checklists', 'customFields', 'comments', 'due', 'start', 'labels',
                        'members', 'start', 'stickers']:
            raise argparse.ArgumentTypeError(
                f"Invalid value: {value}. Must be 'all', 'attachments', 'checklists', 'customFields', "
                f"'comments', 'due', 'start', 'labels', 'members', 'start', 'stickers'.")
    return value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a card to a Trello board.")

    parser.add_argument('-id', '--idList', type=str, required=True, help="The ID of the Trello list")

    # Optional arguments
    parser.add_argument('-key', '--api_key', type=str, help="The API key the Trello account")
    parser.add_argument('-tok', '--auth_token', type=str, help="The OAuth token of the Trello account")

    parser.add_argument('-n', '--name', type=str, help="The name of the Trello card")
    parser.add_argument('-d', '--desc', type=str, help="The description of the Trello card")

    parser.add_argument('-p', '--pos', type=str_or_float,
                        help="The position of the Trello card in the list - top, bottom, or a position number")
    parser.add_argument('-l', '--idLabels', type=str, nargs='+',
                        help="The IDs of the Labels to be added (space-separated)")

    parser.add_argument('-c', '--comment_text', type=str, help="The comment text")
    parser.add_argument('-ln', '--label_name', type=str, help="The name of the new label to create on the card")
    parser.add_argument('-lc', '--label_color', type=str, help="The color of the new label to create on the card")

    parser.add_argument('-m', '--idMembers', type=str, nargs='+',
                        help="The IDs of the Members to be added (space-separated)")
    parser.add_argument('-sd', '--start', type=str, help="The start date for the card")
    parser.add_argument('-dd', '--due', type=str, help="The due date for the card")
    parser.add_argument('-dc', '--dueComplete', type=bool, help="The due complete flag for the card")

    parser.add_argument('-u', '--urlSource', type=url_check,
                        help="The URL source for the card (starting with http:// or https://)")
    parser.add_argument('-f', '--fileSource', type=str, help="The file source for the card (binary)")
    parser.add_argument('-mt', '--mimeType', type=str_character_check,
                        help="The mime type for the card (max 256 characters)")
    parser.add_argument('-ics', '--idCardSource', type=str,
                        help="The ID of a card to copy into the new card")
    parser.add_argument('-kfs', '--keepFromSource', type=kfs_check, nargs='+',
                        help="If using idCardSource you can specify which properties to copy over. 'all' or "
                             "comma-separated list of: attachments,checklists,customFields,comments,due,start,labels,"
                             "members,start,stickers")

    parser.add_argument('-add', '--address', type=str, help="For use with/by the Map View")
    parser.add_argument('-loc', '--locationName', type=str, help="For use with/by the Map View")
    parser.add_argument('-coord', '--coordinates', type=str,
                        help="For use with/by the Map View. Should take the form latitude,longitude")

    args = parser.parse_args()

    if args.api_key is not None and args.auth_token is not None:
        API_KEY = args.api_key
        TOKEN = args.auth_token

    trello_client = TrelloClient(API_KEY, TOKEN)

    card = trello_client.create_card(args=args)
    print(f"Card created: {card}")

    if args.label_name is not None and args.label_color is not None:
        label = trello_client.add_label(card['id'], args.label_name, args.label_color)
        print(f"New Label created and added: {label}")

    if args.comment_text is not None:
        comment = trello_client.add_comment(card['id'], args.comment_text)
        print(f"Comment added: {comment}")
