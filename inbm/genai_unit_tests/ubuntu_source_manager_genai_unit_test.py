import sys
sys.path.append('/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/')
sys.path.append('/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/')
sys.path.append('/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/dispatcher/')
sys.path.append('/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/dispatcher/source/')
sys.path.append('/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm-lib/')
import pytest
from unittest.mock import patch, MagicMock
from dispatcher.source.ubuntu_source_manager import UbuntuApplicationSourceManager, ApplicationAddSourceParameters
from unittest.mock import patch, mock_open
from dispatcher.source.ubuntu_source_manager import UbuntuApplicationSourceManager, ApplicationSourceList
from dispatcher.source.ubuntu_source_manager import UbuntuApplicationSourceManager, ApplicationRemoveSourceParameters, SourceError
from dispatcher.source.ubuntu_source_manager import UbuntuApplicationSourceManager, SourceError, ApplicationUpdateSourceParameters
from dispatcher.source.ubuntu_source_manager import UbuntuOsSourceManager, SourceParameters, SourceError
from dispatcher.source.ubuntu_source_manager import UbuntuOsSourceManager, SourceError
from dispatcher.source.ubuntu_source_manager import UbuntuApplicationSourceManager, SourceError, ApplicationRemoveSourceParameters

sys.path.insert(0, '../')
sys.path.insert(0, '../../../')
sys.path.insert(0, '../../')
sys.path.insert(0, '../../../../')
sys.path.insert(0, './')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm/dispatcher-agent/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm-lib/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm/dispatcher-agent/dispatcher/source/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm-lib/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/dispatcher/source/')
#DO NOT DELETE THIS LINE - TestUbuntuApplicationSourceManagerList
'''
ADD HUMAN FEEDBACK BELOW:

'''
class TestUbuntuApplicationSourceManagerList:
    @pytest.mark.parametrize('file_content, expected_output', [
        # Test with one source
        (["deb http://archive.ubuntu.com/ubuntu/ focal universe"], 
         [ApplicationSourceList(name="sources.list", sources=["deb http://archive.ubuntu.com/ubuntu/ focal universe"])]),
        
        # Test with multiple sources
        (["deb http://archive.ubuntu.com/ubuntu/ focal universe", "deb-src http://archive.ubuntu.com/ubuntu/ focal universe"], 
         [ApplicationSourceList(name="sources.list", sources=["deb http://archive.ubuntu.com/ubuntu/ focal universe", "deb-src http://archive.ubuntu.com/ubuntu/ focal universe"])]),
        
        # Test with no sources
        ([], [ApplicationSourceList(name="sources.list", sources=[])]),  # Fixed this line
        
        # Test with comments and empty lines
        (["# This is a comment", "", "deb http://archive.ubuntu.com/ubuntu/ focal universe"], 
         [ApplicationSourceList(name="sources.list", sources=["deb http://archive.ubuntu.com/ubuntu/ focal universe"])]),
    ])
    @patch('glob.glob')
    @patch('builtins.open', new_callable=mock_open)
    def test_list(self, mock_open, mock_glob, file_content, expected_output):
        # Mock the glob.glob call to return a single file
        mock_glob.return_value = ["sources.list"]
        
        # Mock the open call to return the file content
        mock_open().readlines.return_value = file_content
        
        # Create an instance of the class under test
        manager = UbuntuApplicationSourceManager(None)
        
        # Call the method under test
        result = manager.list()
        
        # Assert that the result is as expected
        assert result == expected_output

sys.path.insert(0, '../')
sys.path.insert(0, '../../../')
sys.path.insert(0, '../../')
sys.path.insert(0, '../../../../')
sys.path.insert(0, './')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm/dispatcher-agent/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm-lib/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm/dispatcher-agent/dispatcher/source/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm-lib/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/dispatcher/source/')
#DO NOT DELETE THIS LINE - TestUbuntuApplicationSourceManagerRemove
'''
ADD HUMAN FEEDBACK BELOW:
    Add more cases to test 
'''
class TestUbuntuApplicationSourceManagerRemove:
    @pytest.fixture
    def manager(self):
        return UbuntuApplicationSourceManager(MagicMock())

    @pytest.mark.parametrize('gpg_key_name, source_list_file_name, remove_file_return_value, expected_exception', [
        # Test case: Removing a source file that exists and a GPG key that exists
        ('existing_key', 'existing_file', True, None),

        # Test case: Removing a source file that does not exist and a GPG key that exists
        ('existing_key', 'nonexistent_file', False, SourceError),

        # Test case: Removing a source file that exists and a GPG key that does not exist
        ('nonexistent_key', 'existing_file', True, None),

        # Test case: Removing a source file that does not exist and a GPG key that does not exist
        ('nonexistent_key', 'nonexistent_file', False, SourceError),

        # Test case: Removing a source file with invalid name
        ('existing_key', '..', True, SourceError),
    ])
    @patch('dispatcher.source.ubuntu_source_manager.remove_file')
    def test_remove(self, mock_remove_file, manager, gpg_key_name, source_list_file_name, remove_file_return_value, expected_exception):
        # Mock the remove_file function to return the specified return value
        mock_remove_file.return_value = remove_file_return_value

        parameters = ApplicationRemoveSourceParameters(gpg_key_name=gpg_key_name, source_list_file_name=source_list_file_name)

        if expected_exception is not None:
            with pytest.raises(expected_exception):
                manager.remove(parameters)
        else:
            manager.remove(parameters)

            # Verify that the remove_file function was called with the correct arguments
            mock_remove_file.assert_any_call(f'/usr/share/keyrings/{gpg_key_name}')
            mock_remove_file.assert_any_call(f'/etc/apt/sources.list.d/{source_list_file_name}')

sys.path.insert(0, '../')
sys.path.insert(0, '../../../')
sys.path.insert(0, '../../')
sys.path.insert(0, '../../../../')
sys.path.insert(0, './')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm/dispatcher-agent/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm-lib/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm/dispatcher-agent/dispatcher/source/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm-lib/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/dispatcher/source/')
#DO NOT DELETE THIS LINE - TestUbuntuOsSourceManagerAdd
'''
ADD HUMAN FEEDBACK BELOW:

'''
class TestUbuntuOsSourceManagerAdd:
    @pytest.fixture
    def manager(self):
        return UbuntuOsSourceManager()

    @pytest.mark.parametrize('sources', [
        (['http://example.com']),
        (['http://example.com', 'http://example2.com']),
        (['http://example.com/path/to/repo']),
        (['http://example.com/path/to/repo', 'http://example2.com/path/to/another/repo']),
    ])
    def test_add_sources(self, manager, sources):
        # Mock the open function
        with patch('builtins.open', mock_open()) as m:
            params = SourceParameters(sources=sources)
            manager.add(params)
            m.assert_called_once_with('/etc/apt/sources.list', 'a')
            handle = m()
            for source in sources:
                handle.write.assert_any_call(f"{source}\n")

    @pytest.mark.parametrize('sources', [
        (['http://example.com']),
    ])
    def test_add_sources_os_error(self, manager, sources):
        # Mock the open function to raise an OSError
        with patch('builtins.open', mock_open()) as m:
            m.side_effect = OSError
            params = SourceParameters(sources=sources)
            with pytest.raises(SourceError):
                manager.add(params)

    @pytest.mark.parametrize('sources', [
        (['http://localhost/path/to/repo']),
        (['http://192.168.1.100/path/to/repo']),
        (['ftp://example.com/path/to/repo']),
        (['file:///path/to/repo']),
        (['http://user:password@example.com/path/to/repo']),
        (['http://example.com:8080/path/to/repo']),
        (['http://example.com/path/to/repo?query=string']),
        (['http://example.com/path/to/repo#fragment']),
    ])
    def test_add_sources_edge_cases(self, manager, sources):
        # Mock the open function
        with patch('builtins.open', mock_open()) as m:
            params = SourceParameters(sources=sources)
            manager.add(params)
            m.assert_called_once_with('/etc/apt/sources.list', 'a')
            handle = m()
            for source in sources:
                handle.write.assert_any_call(f"{source}\n")

sys.path.insert(0, '../')
sys.path.insert(0, '../../../')
sys.path.insert(0, '../../')
sys.path.insert(0, '../../../../')
sys.path.insert(0, './')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm/dispatcher-agent/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm-lib/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm/dispatcher-agent/dispatcher/source/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm-lib/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/dispatcher/source/')
#DO NOT DELETE THIS LINE - TestUbuntuOsSourceManagerList
'''
ADD HUMAN FEEDBACK BELOW:
    generate few more test scenarios. 
'''
class TestUbuntuOsSourceManagerList:
    @pytest.mark.parametrize('file_content, expected_output', [
        # Test with valid sources
        ("deb http://archive.ubuntu.com/ubuntu/ bionic main\n"
         "deb-src http://archive.ubuntu.com/ubuntu/ bionic main\n", 
         ["deb http://archive.ubuntu.com/ubuntu/ bionic main", 
          "deb-src http://archive.ubuntu.com/ubuntu/ bionic main"]),
        # Test with comments and empty lines
        ("# Comment\n"
         "\n"
         "deb http://archive.ubuntu.com/ubuntu/ bionic main\n", 
         ["deb http://archive.ubuntu.com/ubuntu/ bionic main"]),
        # Test with no sources
        ("# Comment\n"
         "\n", 
         []),
    ])
    @patch('builtins.open', new_callable=mock_open)
    def test_list(self, mock_open, file_content, expected_output):
        # Mock the file read
        mock_open.return_value.__enter__.return_value.readlines.return_value = file_content.splitlines(True)
        manager = UbuntuOsSourceManager()
        assert manager.list() == expected_output

    @pytest.mark.parametrize('os_error', [PermissionError, FileNotFoundError])
    @patch('builtins.open', new_callable=mock_open)
    def test_list_os_error(self, mock_open, os_error):
        # Mock the file read to raise an OSError
        mock_open.side_effect = os_error
        manager = UbuntuOsSourceManager()
        with pytest.raises(SourceError):
            manager.list()

sys.path.insert(0, '../')
sys.path.insert(0, '../../../')
sys.path.insert(0, '../../')
sys.path.insert(0, '../../../../')
sys.path.insert(0, './')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm/dispatcher-agent/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm-lib/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm/dispatcher-agent/dispatcher/source/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm-lib/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/dispatcher/source/')
#DO NOT DELETE THIS LINE - TestUbuntuOsSourceManagerRemove
'''
ADD HUMAN FEEDBACK BELOW:

'''
class TestUbuntuOsSourceManagerRemove:
    @pytest.fixture
    def manager(self):
        return UbuntuOsSourceManager()

    @pytest.mark.parametrize('sources, file_content, expected_content', [
        (['deb http://archive.ubuntu.com/ubuntu/ bionic main'], 'deb http://archive.ubuntu.com/ubuntu/ bionic main\n', ''),
        (['deb http://archive.ubuntu.com/ubuntu/ bionic main'], 'deb http://archive.ubuntu.com/ubuntu/ bionic universe\n', 'deb http://archive.ubuntu.com/ubuntu/ bionic universe\n'),
        (['deb http://archive.ubuntu.com/ubuntu/ bionic main'], '', ''),
    ])
    def test_remove(self, manager, sources, file_content, expected_content):
        # Mocking the open function
        mock_file = mock_open(read_data=file_content)
        with patch('builtins.open', mock_file):
            manager.remove(SourceParameters(sources=sources))
            if expected_content:
                mock_file().write.assert_called_once_with(expected_content)
            else:
                mock_file().write.assert_not_called()

    @pytest.mark.parametrize('sources, file_content', [
        (['deb http://archive.ubuntu.com/ubuntu/ bionic main'], 'deb http://archive.ubuntu.com/ubuntu/ bionic main\n'),
        (['deb http://archive.ubuntu.com/ubuntu/ bionic main'], 'deb http://archive.ubuntu.com/ubuntu/ bionic universe\n'),
        (['deb http://archive.ubuntu.com/ubuntu/ bionic main'], ''),
    ])
    def test_remove_os_error(self, manager, sources, file_content):
        # Mocking the open function to raise an OSError
        mock_file = mock_open(read_data=file_content)
        mock_file.side_effect = OSError
        with patch('builtins.open', mock_file):
            with pytest.raises(SourceError):
                manager.remove(SourceParameters(sources=sources))

sys.path.insert(0, '../')
sys.path.insert(0, '../../../')
sys.path.insert(0, '../../')
sys.path.insert(0, '../../../../')
sys.path.insert(0, './')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm/dispatcher-agent/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm-lib/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/intel-inb-manageability/intel-inb-manageability/inbm/dispatcher-agent/dispatcher/source/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm-lib/')
sys.path.insert(0, '/home/runner/GITHUB_ACTION_RUNNERS/_work/genai_ag_intel-inb-manageability/genai_ag_intel-inb-manageability/inbm/dispatcher-agent/dispatcher/source/')
#DO NOT DELETE THIS LINE - TestUbuntuOsSourceManagerUpdate
'''
ADD HUMAN FEEDBACK BELOW:

'''
class TestUbuntuOsSourceManagerUpdate:
    @pytest.fixture
    def manager(self):
        return UbuntuOsSourceManager()

    @pytest.mark.parametrize('sources, file_contents, exception_expected', [
        # Test with normal sources
        (['deb http://archive.ubuntu.com/ubuntu/ focal universe', 'deb-src http://archive.ubuntu.com/ubuntu/ focal universe'], 
         ['deb http://archive.ubuntu.com/ubuntu/ focal universe\n', 'deb-src http://archive.ubuntu.com/ubuntu/ focal universe\n'], 
         False),
        # Test with empty sources
        ([], [], False),
        # Test with special characters in sources
        (['deb http://archive.ubuntu.com/ubuntu/ focal universe # special char', 'deb-src http://archive.ubuntu.com/ubuntu/ focal universe # special char'], 
         ['deb http://archive.ubuntu.com/ubuntu/ focal universe # special char\n', 'deb-src http://archive.ubuntu.com/ubuntu/ focal universe # special char\n'], 
         False),
        # Test with OSError when trying to open file
        (['deb http://archive.ubuntu.com/ubuntu/ focal universe'], ['deb http://archive.ubuntu.com/ubuntu/ focal universe\n'], True)
    ])
    def test_update(self, manager, sources, file_contents, exception_expected):
        parameters = SourceParameters(sources=sources)
        mock_file = mock_open()
        with patch('builtins.open', mock_file):
            if exception_expected:
                mock_file.side_effect = OSError('Mocked OSError')
                with pytest.raises(SourceError):
                    manager.update(parameters)
            else:
                manager.update(parameters)
                mock_file.assert_called_once_with('/etc/apt/sources.list', 'w')
                for file_content in file_contents:
                    mock_file().write.assert_any_call(file_content)

if __name__ == '__main__':
    pytest.main()