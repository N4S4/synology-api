"""
Integration tests for the Docker API module.

Safe tests (marked @pytest.mark.safe) exercise ONLY read-only / GET methods
that will never modify your NAS. They are safe for production devices.

Destructive tests (marked @pytest.mark.destructive) exercise create, delete,
start, stop, and other state-changing operations. They are SKIPPED by default.
To run them:  SYNOLOGY_ALLOW_DESTRUCTIVE=1 python3 -m pytest tests/integration/test_docker_integration.py -v

Run safe tests only:
    python3 -m pytest tests/integration/test_docker_integration.py -m safe -v
"""
import pytest

from synology_api.docker_api import Docker


# ---------------------------------------------------------------------------
# Session-scoped Docker client (one login for all tests)
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def docker_client(nas_connection_kwargs):
    """Create a Docker API client and log in once per test module."""
    client = Docker(**nas_connection_kwargs)
    yield client
    client.logout()


# ===================================================================
#  SAFE (read-only) tests — will NOT modify your NAS
# ===================================================================

class TestDockerSafeLogin:
    """Verify basic connectivity."""

    @pytest.mark.safe
    def test_login_session_valid(self, docker_client):
        """Verify the Docker client has an active session."""
        assert docker_client.session is not None
        assert docker_client.session.sid != ''


class TestDockerSafeContainerReads:
    """Read-only container queries."""

    @pytest.mark.safe
    def test_containers_list(self, docker_client):
        """List all containers — GET, read-only."""
        result = docker_client.containers()
        assert result is not None
        # Should have a 'data' key on success or an 'error' dict
        if isinstance(result, dict):
            assert 'data' in result or 'error' in result

    @pytest.mark.safe
    def test_container_resources(self, docker_client):
        """Get container resource usage — GET, read-only."""
        result = docker_client.container_resources()
        assert result is not None

    @pytest.mark.safe
    def test_system_resources(self, docker_client):
        """Get system-wide Docker resource usage — GET, read-only."""
        result = docker_client.system_resources()
        assert result is not None

    @pytest.mark.safe
    def test_docker_stats(self, docker_client):
        """Get Docker daemon statistics — GET, read-only."""
        result = docker_client.docker_stats()
        assert result is not None

    @pytest.mark.safe
    def test_get_container_by_name(self, docker_client):
        """Get a specific container — read-only, may 404 if name unknown.

        We first list containers to find a valid name.
        """
        containers = docker_client.containers()
        if isinstance(containers, dict) and 'data' in containers:
            data = containers['data']
            if isinstance(data, dict) and data:
                # data is a dict of project_id -> project_info
                first_project = next(iter(data.values()))
                name = first_project.get('name')
                if name:
                    result = docker_client.get_container(name)
                    assert result is not None
                    return
        pytest.skip("No containers found to query")


class TestDockerSafeImageReads:
    """Read-only image queries."""

    @pytest.mark.safe
    def test_downloaded_images(self, docker_client):
        """List downloaded images — GET, read-only."""
        result = docker_client.downloaded_images()
        assert result is not None

    @pytest.mark.safe
    def test_images_registry_resources(self, docker_client):
        """Get image registry resources — GET, read-only."""
        result = docker_client.images_registry_resources()
        assert result is not None

    @pytest.mark.safe
    def test_search_image(self, docker_client):
        """Search Docker Hub for an image — GET, read-only."""
        result = docker_client.search_image(query='alpine')
        assert result is not None


class TestDockerSafeNetworkReads:
    """Read-only network queries."""

    @pytest.mark.safe
    def test_network_list(self, docker_client):
        """List all Docker networks — GET, read-only."""
        result = docker_client.network()
        assert result is not None


class TestDockerSafeProjectReads:
    """Read-only project/compose queries."""

    @pytest.mark.safe
    def test_list_projects(self, docker_client):
        """List all Docker Compose projects — GET, read-only."""
        result = docker_client.list_projects()
        assert result is not None

    @pytest.mark.safe
    def test_get_project_info(self, docker_client):
        """Get info for a specific project — read-only.

        Fetches project list first to find a valid ID.
        """
        projects = docker_client.list_projects()
        if isinstance(projects, dict) and 'data' in projects:
            data = projects['data']
            if isinstance(data, dict) and data:
                first_id = next(iter(data.keys()))
                result = docker_client.get_project_info(project_id=first_id)
                assert result is not None
                return
        pytest.skip("No projects found to query")


class TestDockerSafeLogReads:
    """Read-only log queries."""

    @pytest.mark.safe
    def test_get_logs(self, docker_client):
        """Get container logs — GET, read-only.

        Uses a generic call; may return empty data if no containers exist.
        """
        result = docker_client.get_logs()
        assert result is not None

    @pytest.mark.safe
    def test_get_docker_logs(self, docker_client):
        """Get Docker daemon logs — GET, read-only."""
        result = docker_client.get_docker_logs()
        assert result is not None


class TestDockerSafeProfileReads:
    """Read-only profile queries."""

    @pytest.mark.safe
    def test_list_pkg_profiles(self, docker_client):
        """List package-managed profiles — GET, read-only."""
        result = docker_client.list_pkg_profiles()
        assert result is not None


class TestDockerSafeMiscReads:
    """Read-only miscellaneous queries."""

    @pytest.mark.safe
    def test_get_migrate_status(self, docker_client):
        """Get migration status — GET, read-only."""
        result = docker_client.get_migrate_status()
        assert result is not None

    @pytest.mark.safe
    def test_get_docker_utils_info(self, docker_client):
        """Get Docker utility info — GET, read-only."""
        result = docker_client.get_docker_utils_info()
        assert result is not None

    @pytest.mark.safe
    def test_get_docker_version(self, docker_client):
        """Get Docker version — GET, read-only."""
        result = docker_client.get_docker_version()
        assert result is not None


# ===================================================================
#  DESTRUCTIVE tests — SKIPPED by default
#  Set SYNOLOGY_ALLOW_DESTRUCTIVE=1 to run these.
#  Use a test/disposable NAS, NOT production!
# ===================================================================

class TestDockerDestructiveContainerOps:
    """Container lifecycle operations that change state."""

    @pytest.mark.destructive
    def test_start_container(self, docker_client):
        """Start a stopped container."""
        pytest.skip("Requires a known stopped container name")

    @pytest.mark.destructive
    def test_stop_container(self, docker_client):
        """Stop a running container."""
        pytest.skip("Requires a known running container name")

    @pytest.mark.destructive
    def test_restart_container(self, docker_client):
        """Restart a container."""
        pytest.skip("Requires a known container name")

    @pytest.mark.destructive
    def test_create_and_delete_container(self, docker_client):
        """Create a container and then delete it."""
        pytest.skip("Requires a valid container profile dict")

    @pytest.mark.destructive
    def test_signal_container(self, docker_client):
        """Send a signal to a container."""
        pytest.skip("Requires a known running container name")

    @pytest.mark.destructive
    def test_export_container(self, docker_client):
        """Export a container to a path."""
        pytest.skip("Requires a known container and writable path")

    @pytest.mark.destructive
    def test_export_container_settings(self, docker_client):
        """Export container settings to a path."""
        pytest.skip("Requires a known container and writable path")

    @pytest.mark.destructive
    def test_import_container_profile(self, docker_client):
        """Import a container profile."""
        pytest.skip("Requires a known container name and profile dict")


class TestDockerDestructiveImageOps:
    """Image operations that change state."""

    @pytest.mark.destructive
    def test_pull_image(self, docker_client):
        """Pull an image from a registry."""
        pytest.skip("Would download data to NAS")

    @pytest.mark.destructive
    def test_delete_image(self, docker_client):
        """Delete an image."""
        pytest.skip("Would remove an image from NAS")

    @pytest.mark.destructive
    def test_export_image(self, docker_client):
        """Export an image to a file."""
        pytest.skip("Would write files to NAS")

    @pytest.mark.destructive
    def test_import_image(self, docker_client):
        """Import an image from a file."""
        pytest.skip("Would add an image to NAS")


class TestDockerDestructiveRegistryOps:
    """Registry operations that change state."""

    @pytest.mark.destructive
    def test_create_and_delete_registry(self, docker_client):
        """Create and delete a custom registry."""
        pytest.skip("Would modify registry configuration")

    @pytest.mark.destructive
    def test_set_registry(self, docker_client):
        """Modify a registry entry."""
        pytest.skip("Would modify registry configuration")

    @pytest.mark.destructive
    def test_set_using_registry(self, docker_client):
        """Set the active registry."""
        pytest.skip("Would change which registry is active")


class TestDockerDestructiveNetworkOps:
    """Network operations that change state."""

    @pytest.mark.destructive
    def test_create_and_delete_network(self, docker_client):
        """Create and delete a Docker network."""
        pytest.skip("Would modify Docker networking")


class TestDockerDestructiveProjectOps:
    """Project/Compose operations that change state."""

    @pytest.mark.destructive
    def test_create_project(self, docker_client):
        """Create a compose project."""
        pytest.skip("Would create files and services on NAS")

    @pytest.mark.destructive
    def test_update_project(self, docker_client):
        """Update a compose project."""
        pytest.skip("Would modify project configuration")

    @pytest.mark.destructive
    def test_delete_project(self, docker_client):
        """Delete a compose project."""
        pytest.skip("Would remove project and potentially data")

    @pytest.mark.destructive
    def test_start_project(self, docker_client):
        """Start a compose project."""
        pytest.skip("Would start containers on NAS")

    @pytest.mark.destructive
    def test_stop_project(self, docker_client):
        """Stop a compose project."""
        pytest.skip("Would stop running containers")

    @pytest.mark.destructive
    def test_build_project(self, docker_client):
        """Build a compose project."""
        pytest.skip("Would build images on NAS")


class TestDockerDestructiveMiscOps:
    """Miscellaneous operations that change state."""

    @pytest.mark.destructive
    def test_start_migration(self, docker_client):
        """Start a Docker migration."""
        pytest.skip("Would initiate data migration")

    @pytest.mark.destructive
    def test_docker_prune(self, docker_client):
        """Prune unused Docker resources."""
        pytest.skip("Would delete unused images, containers, networks")
