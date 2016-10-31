import httplib2
import os

from apiclient import discovery, errors
from apiclient.http import MediaFileUpload

import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive.file'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'FishIntoSky'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to ', credential_path
    return credentials

def createFolderInRoot(service, folderName):
	body = {
		'title': folderName,
		'description': 'Daily backup folder',
		'mimeType': 'application/vnd.google-apps.folder'
	}
	
	results = service.files().insert (
		body=body,
	).execute ()
	
	print '[createFolderInRoot] ', results

	return results.get('id')

def uploadFileToFolder(service, filename, title, mime_type, folderId)	:
	media_body = MediaFileUpload(filename, mimetype=mime_type, resumable=True)

	if not folderId:
		print '[uploadFileToFolder] invalid folderId (%s), return' % (folderId,)
	
	parents = [{
		'id' : folderId,
		'kind': 'drive#fileLink'# "drive#parentReference",
	}]

	body = {
		'title': title,
		'description': title,
		'mimeType': mime_type,
		'parents' : parents
	}

	results = service.files().insert(
		body=body,
		media_body=media_body,
		convert=False,
		useContentAsIndexableText=False
	).execute ()
	
	print '[uploadFileToFolder] ', results
	
def demo():
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('drive', 'v2', http=http)

	# folderId = createFolderInRoot(service, 'fishBoBo')
	BACKUP_FOLDER_ID = u'0B-8dkW850O9RZlgtbkw0T00wckU'
	uploadFileToFolder(service, '3.mp4', 'video/mp4', BACKUP_FOLDER_ID)

if __name__ == '__main__':
	demo()