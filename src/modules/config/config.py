class Config:
    def __init__(self, file_path):
        self.env_vars = self.load_environment_variables(file_path)

    def load_environment_variables(self, file_path):
        env_variables = {}

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and '=' in line:
                    key, value = line.split('=', 1)
                    env_variables[key] = value

        return env_variables

    def get_host(self):
        return self.env_vars.get('host')

    def get_user(self):
        return self.env_vars.get('user')

    def get_password(self):
        return self.env_vars.get('password')

    def get_prefix_table(self):
        return self.env_vars.get('prefixTable')



