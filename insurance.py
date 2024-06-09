class Insurance:
    
    def __init__(self, coverage_percentage):
        self.coverage_percentage = coverage_percentage / 100

    def calculate_payment(self, total_bill):
        insurance_coverage = total_bill * self.coverage_percentage
        patient_payment = total_bill - insurance_coverage
        return patient_payment