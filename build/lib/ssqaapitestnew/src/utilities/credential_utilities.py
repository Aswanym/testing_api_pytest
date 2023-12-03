import os

class CredentialUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_api_credentials():

        wc_api_key = os.environ.get('WC_KEY')
        wc_api_secret = os.environ.get('WC_SECRET')

        if not wc_api_key or not wc_api_secret:
            raise Exception('The api credentials WC_KEY and WC_SECRET must be set in the environment')
        else:
            wc_api_cred = {
                'wc_api_key': wc_api_key,
                'wc_api_secret': wc_api_secret
            }

            return wc_api_cred

    @staticmethod
    def get_db_credentials():

        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')

        if not db_user or not db_password:
            raise Exception('The db credentials db_user and DB_PASSWORD must be set in the environment')
        else:
            db_cred = {
                'db_user': db_user,
                'db_password': db_password
            }

            return db_cred
