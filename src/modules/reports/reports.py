from abc import ABC, abstractmethod

class ReportTemplate(ABC):
    def generate_report(self):
        data = self.collect_data()
        report = self.format_report(data)
        self.save_report(report)

    def collect_data(self):
        actions = {}
        with open('logs.txt', 'r') as log_file:
            for line in log_file:
                parts = line.split(": ")
                if len(parts) >= 2:
                    timestamp = parts[0]
                    action = parts[1].strip()
                    if action in actions:
                        actions[action] += 1
                    else:
                        actions[action] = 1
        sorted_actions = dict(sorted(actions.items(), key=lambda item: item[1], reverse=True))
        return sorted_actions

    @abstractmethod
    def format_report(self, data):
        pass

    @abstractmethod
    def save_report(self, report):
        pass