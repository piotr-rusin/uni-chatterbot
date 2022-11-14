from __future__ import print_function

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

"""
Creates the batch_update the user has access to.
Load pre-authorized user credentials from the environment.
TODO(developer) - See https://developers.google.com/identity
for guides on implementing OAuth2 for the application.
    """
creds, _ = google.auth.default()


class GoogleSheets:
    def __init__(self):
        self.service = build('sheets', 'v4', credentials=creds)

    def get_values(self, spreadsheet_id, _range):
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id,
                range=_range).execute()
            rows = result.get('values', [])
            print(f"{len(rows)} rows retrieved")
            return result
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

    def append_values(self, spreadsheet_id, _range, _values):
        try:
            body = {
                'values': _values
            }
            request = self.service.spreadsheets().values().append(
                spreadsheetId=spreadsheet_id,
                range=_range,
                insertDataOption="OVERWRITE",
                responseDateTimeRenderOption="FORMATTED_STRING",
                responseValueRenderOption="FORMATTED_VALUE",
                valueInputOption="USER_ENTERED",
                body=body
            )
            result = request.execute()
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

        return result.get('updates', [])


google_sheets = GoogleSheets()