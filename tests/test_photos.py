"""Unit tests for Synology Photos request contracts."""

import json
import unittest
from unittest.mock import MagicMock, patch

from synology_api.photos import Photos


def _make_instance():
    """Create a Photos instance with mocked auth/session."""
    with patch('synology_api.photos.base_api.BaseApi.__init__', return_value=None):
        instance = Photos.__new__(Photos)

    instance.photos_list = {
        'SYNO.Foto.Browse.Item': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.FotoTeam.Browse.Item': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.request_data = MagicMock(
        return_value={'success': True, 'data': {'list': []}})
    return instance


class TestPhotos(unittest.TestCase):
    """Tests for Photos methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_list_item_in_folders_requires_folder_id(self):
        with self.assertRaisesRegex(ValueError, 'folder_id is required'):
            self.instance.list_item_in_folders(limit=10)

    def test_list_item_in_folders_requires_positive_limit(self):
        with self.assertRaisesRegex(ValueError, 'limit must be greater than 0'):
            self.instance.list_item_in_folders(folder_id=123, limit=0)

    def test_list_item_in_folders_sends_personal_space_request(self):
        response = self.instance.list_item_in_folders(
            folder_id=123,
            offset=5,
            limit=25,
            type='photo',
            additional=['thumbnail'],
        )

        self.assertEqual(response, {'success': True, 'data': {'list': []}})
        self.instance.request_data.assert_called_once_with(
            'SYNO.Foto.Browse.Item',
            'entry.cgi',
            {
                'version': 1,
                'method': 'list',
                'offset': 5,
                'limit': 25,
                'folder_id': 123,
                'sort_by': 'filename',
                'sort_direction': 'desc',
                'type': 'photo',
                'additional': json.dumps(['thumbnail']),
            },
        )

    def test_list_item_in_team_folders_sends_team_space_request(self):
        self.instance.list_item_in_team_folders(
            folder_id=456,
            offset=10,
            limit=50,
            sort_by='takentime',
            sort_direction='asc',
            type='video',
            passphrase='secret',
            additional=['thumbnail', 'resolution'],
        )

        self.instance.request_data.assert_called_once_with(
            'SYNO.FotoTeam.Browse.Item',
            'entry.cgi',
            {
                'version': 1,
                'method': 'list',
                'offset': 10,
                'limit': 50,
                'folder_id': 456,
                'sort_by': 'takentime',
                'sort_direction': 'asc',
                'type': 'video',
                'passphrase': 'secret',
                'additional': json.dumps(['thumbnail', 'resolution']),
            },
        )


if __name__ == '__main__':
    unittest.main()
