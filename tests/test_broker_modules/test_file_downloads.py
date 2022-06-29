from lib.modules.live_data_fetch.API_client import API
import settings
import os

def test_scrip_master_download():
    """Test downloading of scrip master file.
    """
    api = API()
    api.fetch_scrip_master()
    if not os.path.exists(settings.SCRIP_MASTER_FILE):
        raise Exception("Scrip master file could not be downloaded")