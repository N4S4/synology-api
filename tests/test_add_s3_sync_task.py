from unittest import TestCase
import unittest
from synology_api.cloud_sync import CloudSync
from setup_tests import parse_config
import os, pathlib
import json
import time

class TestSynologyCloudSync(TestCase):
    config: dict[str, str]

    def setUp(self):
        self.config = parse_config(
            os.path.realpath(
                os.path.join(
                    pathlib.Path(__file__).parent.resolve(),
                    './resources/config-test.json'
                )
            )
        )

    def sign_in(self) -> CloudSync:
        return CloudSync(
            ip_address=self.config["synology_ip"],
            port=self.config["synology_port"],
            username=self.config["synology_user"],
            password=self.config["synology_password"],
            secure=bool(self.config["synology_secure"]), cert_verify=False,
            dsm_version=int(self.config["dsm_version"]), debug=True,
            otp_code=self.config["otp_code"]
        )

    def test_sign_in(self):
        cs = self.sign_in()
        self.assertIsNotNone(cs)
        self.assertIsNotNone(cs.session)
        self.assertIsNotNone(cs.session.sid)
        self.assertIsNot(cs.session.sid, '')

    def test_create_s3_task_list(self):
        # Sign in to the Synology CloudSync service
        cs = self.sign_in()
        try:
            # Get the list of connections
            conns = cs.get_connections()
            self.assertIsNotNone(conns, "Connections should not be None")

            # Get the first connection from the list
            conn = conns['data']['conn'][0]
            self.assertIsNotNone(conn, "First connection should not be None")

            # Extract the connection ID
            conn_id = conn['id']

            # Add a new S3 sync task
            task = cs.create_sync_task_s3(
                conn_id=conn_id,
                local_path='/userData/1',
                cloud_path='/1',
            )
            # Save the task details to a JSON file for debugging purposes
            # json.dump(task, open('task.json', 'w'), indent=4)

            # Verify that the task was created successfully
            self.assertTrue(task[1]['data']['result'][0]['success'], "Task creation should be successful")

            # Find the session id
            list_sessions = task[1]['data']['result'][1]['data']['sess']

            # Find the largest sess_id in the list
            sess_id = max(sess['sess_id'] for sess in list_sessions)

            # Sleep for 5 seconds before removing the session id
            print(f"Sleeping for 5 seconds before removing session id: {sess_id}")
            time.sleep(5)

            # Remove the session
            task_remover = cs.task_remove(conn_id=conn_id, sess_id=sess_id)
            # Verify that the task was removed successfully
            self.assertTrue(task_remover['success'], "Task removal should be successful")
        finally:
            # Ensure logout is called to clean up the session
            cs.logout()

if __name__ == '__main__':
    unittest.main()
