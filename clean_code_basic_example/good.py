from typing import List


class InfectedPatient:
    MAX_NUMBER_OF_ORGANISMS = 1000

    def __init__(self):
        self.number_of_viruses = 0
        self.number_of_bacteria = 0

    def is_microorganism_level_to_high(self) -> bool:
        too_much_bacteria = self.number_of_bacteria >= self.MAX_NUMBER_OF_ORGANISMS
        too_much_viruses = self.number_of_viruses >= self.MAX_NUMBER_OF_ORGANISMS
        return too_much_bacteria or too_much_viruses

    def populate_patient_microorganisms(self, microorganisms: List[(int, int)]):
        for number_of_viruses, number_of_bacteria in microorganisms:
            self.number_of_viruses += number_of_viruses
            self.number_of_bacteria += number_of_bacteria

    def display_status(self):
        if self.is_microorganism_level_to_high():
            print('There are a lot of virus or bacteria in this patient')
        else:
            print('Patient is fine')


def main(patient_microorganisms: List[(int, int)]):
    patient = InfectedPatient()
    patient.populate_patient_microorganisms(patient_microorganisms)
    patient.display_status()
