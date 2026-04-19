"""Unit tests for Docker API — verifies all 12 SYNO.Docker.* namespaces are covered."""

import json
import unittest
from unittest.mock import MagicMock, patch

from synology_api.docker_api import Docker


def _make_docker():
    """Create a Docker instance with mocked auth/session."""
    with patch('synology_api.docker_api.base_api.BaseApi.__init__', return_value=None):
        docker = Docker.__new__(Docker)

    # Mock the API lists with all 12 Docker endpoints
    api_list = {
        'SYNO.Docker.Container': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Docker.Container.Log': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Docker.Container.PkgProfile': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Docker.Container.Profile': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Docker.Container.Resource': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Docker.Image': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Docker.Log': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Docker.Migrate': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Docker.Network': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Docker.Project': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Docker.Registry': {'path': 'entry.cgi', 'maxVersion': 2},
        'SYNO.Docker.Utils': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.System.Utilization': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    docker.gen_list = api_list
    docker.request_data = MagicMock(return_value={'success': True, 'data': {}})
    return docker


class TestDockerContainerApi(unittest.TestCase):
    """Tests for SYNO.Docker.Container methods."""

    def setUp(self):
        self.docker = _make_docker()

    def test_containers(self):
        self.docker.containers()
        self.docker.request_data.assert_called_once()
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Container')
        self.assertEqual(args[0][2]['method'], 'list')

    def test_get_container(self):
        self.docker.get_container('mycontainer')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'get')
        self.assertEqual(args[0][2]['name'], 'mycontainer')

    def test_start_container(self):
        self.docker.start_container('mycontainer')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'start')

    def test_stop_container(self):
        self.docker.stop_container('mycontainer')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'stop')

    def test_restart_container(self):
        self.docker.restart_container('mycontainer')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'restart')

    def test_delete_container(self):
        self.docker.delete_container('mycontainer', force=True)
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'delete')
        self.assertEqual(args[0][2]['force'], 'true')

    def test_create_container(self):
        profile = {'name': 'test', 'image': 'nginx:latest'}
        self.docker.create_container(profile)
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'create')
        self.assertEqual(json.loads(args[0][2]['profile']), profile)

    def test_signal_container(self):
        self.docker.signal_container('mycontainer', signal=9)
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'signal')
        self.assertEqual(args[0][2]['signal'], 9)

    def test_export_container_settings(self):
        self.docker.export_container_settings('mycontainer', '/docker')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Container.Profile')
        self.assertEqual(args[0][2]['method'], 'export')

    def test_export_container(self):
        self.docker.export_container('mycontainer', '/docker')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Container')
        self.assertEqual(args[0][2]['method'], 'export')

    def test_docker_stats(self):
        self.docker.docker_stats()
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'stats')


class TestDockerContainerLogApi(unittest.TestCase):
    """Tests for SYNO.Docker.Container.Log."""

    def setUp(self):
        self.docker = _make_docker()

    def test_get_logs(self):
        self.docker.get_logs(name='nginx', limit=100, sort_dir='ASC')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Container.Log')
        self.assertEqual(args[0][2]['method'], 'get')
        self.assertEqual(args[0][2]['name'], 'nginx')
        self.assertEqual(args[0][2]['limit'], 100)
        self.assertEqual(args[1].get('method'), 'post')


class TestDockerContainerPkgProfileApi(unittest.TestCase):
    """Tests for SYNO.Docker.Container.PkgProfile."""

    def setUp(self):
        self.docker = _make_docker()

    def test_get_pkg_profile(self):
        self.docker.get_pkg_profile('syno-package-container')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Container.PkgProfile')
        self.assertEqual(args[0][2]['method'], 'get')

    def test_list_pkg_profiles(self):
        self.docker.list_pkg_profiles()
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Container.PkgProfile')
        self.assertEqual(args[0][2]['method'], 'list')


class TestDockerContainerProfileApi(unittest.TestCase):
    """Tests for SYNO.Docker.Container.Profile."""

    def setUp(self):
        self.docker = _make_docker()

    def test_get_container_profile(self):
        self.docker.get_container_profile('nginx')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Container.Profile')
        self.assertEqual(args[0][2]['method'], 'get')

    def test_import_container_profile(self):
        profile = {'name': 'test'}
        self.docker.import_container_profile('nginx', profile)
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'import')
        self.assertEqual(args[1].get('method'), 'post')


class TestDockerContainerResourceApi(unittest.TestCase):
    """Tests for SYNO.Docker.Container.Resource."""

    def setUp(self):
        self.docker = _make_docker()

    def test_container_resources(self):
        self.docker.container_resources()
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Container.Resource')
        self.assertEqual(args[0][2]['method'], 'get')


class TestDockerImageApi(unittest.TestCase):
    """Tests for SYNO.Docker.Image."""

    def setUp(self):
        self.docker = _make_docker()

    def test_downloaded_images(self):
        self.docker.downloaded_images(limit=10, offset=5)
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Image')
        self.assertEqual(args[0][2]['method'], 'list')
        self.assertEqual(args[0][2]['limit'], 10)

    def test_pull_image(self):
        self.docker.pull_image('nginx', tag='alpine')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'pull')
        self.assertEqual(args[0][2]['repository'], 'nginx')
        self.assertEqual(args[0][2]['tag'], 'alpine')

    def test_delete_image(self):
        self.docker.delete_image('nginx', tag='latest')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'delete')

    def test_export_image(self):
        self.docker.export_image('nginx', path='/docker/exports')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'export')
        self.assertEqual(args[0][2]['path'], '/docker/exports')

    def test_import_image(self):
        self.docker.import_image('/docker/nginx.tar')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'import')
        self.assertEqual(args[1].get('method'), 'post')

    def test_get_image(self):
        self.docker.get_image('nginx', tag='alpine')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'get')


class TestDockerLogApi(unittest.TestCase):
    """Tests for SYNO.Docker.Log (daemon-level)."""

    def setUp(self):
        self.docker = _make_docker()

    def test_get_docker_logs(self):
        self.docker.get_docker_logs(limit=25, keyword='error')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Log')
        self.assertEqual(args[0][2]['method'], 'get')
        self.assertEqual(args[0][2]['keyword'], 'error')

    def test_get_docker_logs_defaults(self):
        self.docker.get_docker_logs()
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['offset'], 0)
        self.assertEqual(args[0][2]['limit'], 50)
        self.assertNotIn('keyword', args[0][2])


class TestDockerMigrateApi(unittest.TestCase):
    """Tests for SYNO.Docker.Migrate."""

    def setUp(self):
        self.docker = _make_docker()

    def test_get_migrate_status(self):
        self.docker.get_migrate_status()
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Migrate')
        self.assertEqual(args[0][2]['method'], 'get')

    def test_start_migration(self):
        self.docker.start_migration()
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'start')


class TestDockerNetworkApi(unittest.TestCase):
    """Tests for SYNO.Docker.Network."""

    def setUp(self):
        self.docker = _make_docker()

    def test_network_list(self):
        self.docker.network()
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Network')
        self.assertEqual(args[0][2]['method'], 'list')

    def test_create_network(self):
        self.docker.create_network(
            'mynet', subnet='172.28.0.0/16', gateway='172.28.0.1')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'create')
        self.assertEqual(args[0][2]['name'], 'mynet')
        self.assertEqual(args[0][2]['subnet'], '172.28.0.0/16')

    def test_delete_network(self):
        self.docker.delete_network('mynet')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'delete')

    def test_get_network(self):
        self.docker.get_network('bridge')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'get')


class TestDockerProjectApi(unittest.TestCase):
    """Tests for SYNO.Docker.Project."""

    def setUp(self):
        self.docker = _make_docker()

    def test_list_projects(self):
        self.docker.list_projects()
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Project')
        self.assertEqual(args[0][2]['method'], 'list')

    def test_get_project_info(self):
        self.docker.get_project_info('abc-123')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'get')
        self.assertEqual(args[0][2]['id'], 'abc-123')

    def test_create_project(self):
        yaml_content = 'version: "3"\nservices:\n  web:\n    image: nginx\n'
        self.docker.create_project(
            'myproject', '/docker/myproject', yaml_content)
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'create')
        self.assertEqual(args[0][2]['content'], yaml_content)

    def test_update_project(self):
        self.docker.update_project('abc-123', 'version: "3"')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'update')

    def test_delete_project(self):
        self.docker.delete_project('abc-123', preserve_content=True)
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'delete')
        self.assertEqual(args[0][2]['preserve_content'], 'true')

    def test_start_project(self):
        self.docker.start_project('abc-123')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'start')

    def test_stop_project(self):
        self.docker.stop_project('abc-123')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'stop')

    def test_build_project(self):
        self.docker.build_project('abc-123')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'build')


class TestDockerRegistryApi(unittest.TestCase):
    """Tests for SYNO.Docker.Registry."""

    def setUp(self):
        self.docker = _make_docker()

    def test_images_registry_resources(self):
        self.docker.images_registry_resources()
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Registry')
        self.assertEqual(args[0][2]['method'], 'get')

    def test_search_image(self):
        self.docker.search_image('nginx')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'search')
        self.assertEqual(args[0][2]['q'], 'nginx')

    def test_create_registry(self):
        self.docker.create_registry(
            'GHCR', 'https://ghcr.io', username='user', password='pass')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'create')
        self.assertEqual(args[0][2]['url'], 'https://ghcr.io')
        self.assertEqual(args[0][2]['username'], 'user')

    def test_set_registry(self):
        self.docker.set_registry('GHCR', 'https://ghcr.io')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'set')

    def test_delete_registry(self):
        self.docker.delete_registry('GHCR')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'delete')

    def test_set_using_registry(self):
        self.docker.set_using_registry('Docker Hub')
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'using')

    def test_get_image_tags(self):
        self.docker.get_image_tags('nginx', limit=25)
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'tags')
        self.assertEqual(args[0][2]['version'], 2)
        self.assertEqual(args[0][2]['limit'], 25)


class TestDockerUtilsApi(unittest.TestCase):
    """Tests for SYNO.Docker.Utils."""

    def setUp(self):
        self.docker = _make_docker()

    def test_get_docker_utils_info(self):
        self.docker.get_docker_utils_info()
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][0], 'SYNO.Docker.Utils')
        self.assertEqual(args[0][2]['method'], 'get')

    def test_docker_prune(self):
        self.docker.docker_prune()
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'prune')

    def test_get_docker_version(self):
        self.docker.get_docker_version()
        args = self.docker.request_data.call_args
        self.assertEqual(args[0][2]['method'], 'version')


class TestDockerApiCoverage(unittest.TestCase):
    """Meta-test: verify all 12 SYNO.Docker.* namespaces are covered."""

    def test_all_namespaces_covered(self):
        """Every SYNO.Docker.* API namespace must be referenced in at least one method."""
        import inspect
        required_namespaces = {
            'SYNO.Docker.Container',
            'SYNO.Docker.Container.Log',
            'SYNO.Docker.Container.PkgProfile',
            'SYNO.Docker.Container.Profile',
            'SYNO.Docker.Container.Resource',
            'SYNO.Docker.Image',
            'SYNO.Docker.Log',
            'SYNO.Docker.Migrate',
            'SYNO.Docker.Network',
            'SYNO.Docker.Project',
            'SYNO.Docker.Registry',
            'SYNO.Docker.Utils',
        }

        source = inspect.getsource(Docker)
        for ns in required_namespaces:
            with self.subTest(namespace=ns):
                self.assertIn(f"'{ns}'", source,
                              f"Namespace {ns} not found in Docker class source")

    def test_method_count(self):
        """Ensure we have a healthy number of public methods."""
        public_methods = [m for m in dir(Docker)
                          if not m.startswith('_') and callable(getattr(Docker, m))]
        # We expect 30+ public methods (including inherited logout)
        self.assertGreaterEqual(len(public_methods), 30,
                                f"Expected 30+ public methods, found {len(public_methods)}: {public_methods}")


if __name__ == '__main__':
    unittest.main()
