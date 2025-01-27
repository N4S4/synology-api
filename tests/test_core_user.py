import datetime
import json
from unittest import TestCase
import unittest
from synology_api.core_user import User
from synology_api.exceptions import CoreError
import os, pathlib, random, string, time

def parse_config(config_path) -> dict[str, str]:
    with open(config_path, 'r') as config_file:
        config_data = json.load(config_file)
    return config_data

def generate_test_passwords(password_policy, username):
    strong_policy = password_policy.get('strong_password', {})
    
    correct = generate_correct_password(strong_policy, username)
    incorrect = generate_incorrect_password(strong_policy, username)
    
    return correct, incorrect

def generate_correct_password(policy, username):
    min_length = policy.get('min_length', 8) if policy.get('min_length_enable', False) else 8
    included_numeric = policy.get('included_numeric_char', False)
    included_special = policy.get('included_special_char', False)
    mixed_case = policy.get('mixed_case', False)
    exclude_username = policy.get('exclude_username', False)
    
    # Characters to be included
    required_chars = []
    if included_numeric:
        required_chars.append(random.choice(string.digits))
    if mixed_case:
        required_chars.append(random.choice(string.ascii_uppercase))
        required_chars.append(random.choice(string.ascii_lowercase))
    else:
        required_chars.append(random.choice(string.ascii_letters))
    if included_special:
        required_chars.append(random.choice(string.punctuation))
    
    # Determine remaining length needed
    remaining_length = max(min_length - len(required_chars), 0)
    
    # Generate allowed characters for remaining
    allowed_chars = []
    if included_special:
        allowed_chars += list(string.punctuation)
    allowed_chars += list(string.ascii_letters)
    if included_numeric:
        allowed_chars += list(string.digits)
    
    # Generate remaining characters
    remaining_chars = [random.choice(allowed_chars) for _ in range(remaining_length)]
    all_chars = required_chars + remaining_chars
    random.shuffle(all_chars)
    password = ''.join(all_chars)
    
    # Ensure password does not contain username
    if exclude_username and username.lower() in password.lower():
        return generate_correct_password(policy, username)
    
    return password

def generate_incorrect_password(policy, username):
    min_length = policy.get('min_length', 8)
    min_length_enable = policy.get('min_length_enable', False)
    included_numeric = policy.get('included_numeric_char', False)
    included_special = policy.get('included_special_char', False)
    mixed_case = policy.get('mixed_case', False)
    exclude_username = policy.get('exclude_username', False)
    
    # Try to violate min_length first if enabled
    if min_length_enable:
        # Generate password with min_length -1, try to meet other conditions
        new_policy = policy.copy()
        new_policy['min_length_enable'] = False  # Temporarily disable to generate
        password = generate_correct_password(new_policy, username)
        password = password[:max(min_length -1, 1)]
        if len(password) < min_length:
            return password
    
    # Next, violate included_numeric if enabled
    if included_numeric:
        # Generate password without numeric
        new_policy = policy.copy()
        new_policy['included_numeric_char'] = False
        password = generate_correct_password(new_policy, username)
        if not any(c.isdigit() for c in password):
            return password
    
    # Next, violate mixed_case if enabled
    if mixed_case:
        # Generate all lowercase
        new_policy = policy.copy()
        new_policy['mixed_case'] = False
        password = generate_correct_password(new_policy, username).lower()
        if password.islower():
            return password
    
    # Next, violate exclude_username if enabled
    if exclude_username:
        # Include username in password
        password = generate_correct_password(policy, username)
        insert_pos = random.randint(0, len(password))
        password = password[:insert_pos] + username + password[insert_pos:]
        return password
    
    # Fallback: violate min_length even if not enabled
    password = generate_correct_password(policy, username)
    return password[:-1]

def generate_username():
    # Generate 4-6 random lowercase letters
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(4, 6)))
    
    # Generate 2-4 random digits
    numbers = ''.join(random.choice(string.digits) for _ in range(random.randint(2, 4)))
    
    # Combine letters and numbers
    return letters + numbers

class TestCoreUser(TestCase):
    
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
        self.user = User(
            ip_address=self.config["synology_ip"],
            port=self.config["synology_port"],
            username=self.config["synology_user"],
            password=self.config["synology_password"],
            secure=bool(self.config["synology_secure"]),
            cert_verify=False,
            dsm_version=int(self.config["dsm_version"]),
            debug=True,
            otp_code=self.config["otp_code"]
        )

    def api_response_base_assert(self, response: dict, success: bool = True):
        self.assertIsNotNone(response)
        if success:
            self.assertIsNotNone(response['data'])
            self.assertTrue(response['success'])
        else:
            self.assertIsNone(response['data'])
            self.assertIsNotNone(response['error'])
            self.assertFalse(response['success'])
        

    def test_core_user(self):

        self.assertIsNotNone(self.user)
        self.assertIsNotNone(self.user.session)
        self.assertIsNotNone(self.user.session.sid)
        self.assertIsNot(self.user.session.sid, '')
        
        password_policy_response = self.user.get_password_policy()
        
        password_policy = password_policy_response['data']
        
        username_policy_response = self.user.get_username_policy()
        self.api_response_base_assert(username_policy_response)
        
        test_username = generate_username()

        
        correct_pass, incorrect_pass = generate_test_passwords(password_policy, test_username)
        
        # Test create user with correct password
        create_response = self.user.create_user(
            name=test_username,
            password=correct_pass,
            email=f"{test_username}@test.com"
        )
        
        self.api_response_base_assert(create_response)
        
        # Test get user
        get_user_response = self.user.get_user(name=test_username)
        
        self.api_response_base_assert(get_user_response)
        self.assertIsNotNone(get_user_response['data']['users'][0]['name'])
        self.assertEqual(get_user_response['data']['users'][0]['name'], test_username)
        self.assertIsNotNone(get_user_response['data']['users'][0]['name'])
        
        self.assertIsNotNone(get_user_response['data']['users'][0]['uid'])
        self.assertNotEqual(get_user_response['data']['users'][0]['uid'], 0)
        
        # Test affect groups to user
        assign_groups_response = self.user.affect_groups(name=test_username, join_groups=['admnistrators'])
        self.api_response_base_assert(assign_groups_response)
        
        # Test affect groups to user status
        assign_groups_status_response = self.user.affect_groups_status(task_id=assign_groups_response['data']['task_id'])
        self.api_response_base_assert(assign_groups_status_response)
        
        while assign_groups_status_response['data']['finish'] == False:
            assign_groups_status_response = self.user.affect_groups_status(task_id=assign_groups_response['data']['task_id'])
            self.api_response_base_assert(assign_groups_status_response)
            time.sleep(1)
        
        # Test leave groups to user
        leave_groups_response = self.user.affect_groups(name=test_username, leave_groups=['admnistrators'])
        self.api_response_base_assert(leave_groups_response)
        
        # Test leave groups to user status
        leave_groups_status_response = self.user.affect_groups_status(task_id=leave_groups_response['data']['task_id'])
        self.api_response_base_assert(leave_groups_status_response)
        
        while leave_groups_status_response['data']['finish'] == False:
            leave_groups_status_response = self.user.affect_groups_status(task_id=leave_groups_response['data']['task_id'])
            self.api_response_base_assert(leave_groups_status_response)
            time.sleep(1)
            
        # Test confirm password of the current user
        confirm_response = self.user.password_confirm(password=self.config["synology_password"])
        self.api_response_base_assert(confirm_response)
        
        # Test update user
        new_test_username = generate_username()
        update_response = self.user.modify_user(name=test_username, new_name=new_test_username)
        
        self.api_response_base_assert(update_response)

        # Delete user
        delete_response = self.user.delete_user(name=new_test_username)
        self.api_response_base_assert(delete_response)
        
        # Test create user with incorrect password
        try:
            create_response = self.user.create_user(
                name=test_username,
                password=incorrect_pass,
                email=f"{test_username}@test.com",
            )
        except Exception as e:
            self.assertIsNotNone(e)
            self.assertIsInstance(e, CoreError, "Exception has to be Core Error")
        
        # Test create user with incorrect username
        try:
            create_response = self.user.create_user(
                name='admin',
                password=correct_pass
            )
        
        except Exception as e:
            self.assertIsNotNone(e)
            self.assertIsInstance(e, CoreError, "Exception has to be Core Error")
        
        

        
if __name__ == '__main__':
    unittest.main()