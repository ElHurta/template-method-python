from researchGuideline import *
from universityA import UniversityA
from universityB import UniversityB

def client_call(research_guideline: ResearchGuideline):
    research_guideline.templateMethod();

if __name__ == '__main__':
    print("University A:")
    client_call(UniversityA())

    print("University B:")
    client_call(UniversityB())
    