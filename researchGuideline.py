
from abc import ABC, abstractmethod

class ResearchGuideline(ABC):

    def templateMethod(self):
        self.step1()
        self.step2()
        self.step3()
        self.step4()

    def step1(self):
        pass

    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass

    def step4(self):
        pass