import sys
sys.path.append('/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/')
sys.path.append('/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/')
sys.path.append('/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm-lib/')
sys.path.append('/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/dispatcher/')
import pytest
from unittest.mock import MagicMock, patch, mock_open
from dispatcher.downloader import _check_if_valid_file
from dispatcher.dispatcher_exception import DispatcherException
from unittest.mock import Mock, patch
from dispatcher.downloader import download
from dispatcher.packagemanager.local_repo import DirectoryRepo
from inbm_common_lib.utility import CanonicalUri

#DO NOT DELETE THIS LINE - TestCheckIfValidFile
'''
ADD HUMAN FEEDBACK BELOW:

'''
class TestCheckIfValidFile:

    @pytest.mark.parametrize('file_name, repo_path, file_type, expected_exception', [
        # Test case: Valid file type, no exception expected
        ("file.txt", "/path/to/repo", "text", None),
        # Test case: Invalid file type, DispatcherException expected
        ("file.exe", "/path/to/repo", "exe", DispatcherException),
        # Test case: File does not exist, DispatcherException expected
        ("nonexistent.txt", "/path/to/repo", None, DispatcherException),
        # Test case: File name is empty, DispatcherException expected
        ("", "/path/to/repo", None, DispatcherException),
    ])
    def test_check_if_valid_file(self, file_name, repo_path, file_type, expected_exception):
        # Mocking the repo object
        repo = MagicMock()
        repo.get_repo_path.return_value = repo_path

        # Mocking the validate_file_type function
        with patch('inbm_common_lib.utility.validate_file_type') as mock_validate_file_type, \
             patch('builtins.open', new_callable=mock_open, read_data=b"data"):
            # If file_type is None, the file does not exist, so raise a FileNotFoundError
            if file_type is None:
                mock_validate_file_type.side_effect = FileNotFoundError
            # If file_type is "exe", the file type is invalid, so raise a TypeError
            elif file_type == "exe":
                mock_validate_file_type.side_effect = TypeError

            # If an exception is expected, check if it is raised
            if expected_exception is not None:
                with pytest.raises(expected_exception):
                    _check_if_valid_file(file_name, repo)
            # If no exception is expected, check if the function runs without raising an exception
            else:
                try:
                    _check_if_valid_file(file_name, repo)
                except Exception as e:
                    pytest.fail(f"Unexpected exception raised: {e}")

#DO NOT DELETE THIS LINE - TestDownload
'''
ADD HUMAN FEEDBACK BELOW:

'''
class TestDownload:
    @pytest.mark.parametrize('uri_value, username, password, umask, enough_space, get_status, raises_exception', [
        # Test case: Successful download
        ("http://example.com/file.txt", "username", "password", 22, True, 200, False),
        # Test case: URI is not a CanonicalUri object
        ("not a CanonicalUri object", "username", "password", 22, True, 200, True),
        # Test case: Not enough space for the download
        ("http://example.com/file.txt", "username", "password", 22, False, 200, True),
        # Test case: Download fails
        ("http://example.com/file.txt", "username", "password", 22, True, 404, True),
    ])
    def test_download(self, uri_value, username, password, umask, enough_space, get_status, raises_exception):
        # Mock the DispatcherBroker object
        dispatcher_broker = Mock()
        # Mock the IRepo object
        repo = Mock()
        repo.get_repo_path.return_value = "/path/to/repo"
        # Create the CanonicalUri object
        uri = CanonicalUri(uri_value)
        # Mock the is_enough_space_to_download function
        with patch('dispatcher.packagemanager.package_manager.is_enough_space_to_download', return_value=enough_space):
            # Mock the get function
            with patch('dispatcher.packagemanager.package_manager.get', return_value=Mock(status=get_status)):
                if raises_exception:
                    with pytest.raises(DispatcherException):
                        download(dispatcher_broker, uri, repo, username, password, umask)
                else:
                    download(dispatcher_broker, uri, repo, username, password, umask)
                    dispatcher_broker.telemetry.assert_called_with('OTA Download Successful')

if __name__ == '__main__':
    pytest.main()