# Make sure you replace the API and or APP key below with the ones for your account

from checks import AgentCheck

class HelloCheck(AgentCheck):
    def check(self, instance):
        self.gauge('hello.world', 1)