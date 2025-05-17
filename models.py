from datetime import datetime
import pandas as pd
class Policyholder:
    def __init__(self, customer_id, name, age, policy_type, sum_insured, city):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.policy_type = policy_type
        self.sum_insured = sum_insured
        self.city = city
        self.claims = []

    def add_claim(self, claim):
        self.claims.append(claim)

    def total_claim_amount(self):
        return sum(claim.claim_amount for claim in self.claims)


    def claim_frequency_last_year(self, reference_date):
        reference_date = reference_date.date()
        return sum(
        1 for claim in self.claims
        if (reference_date - (
            claim.date.date() if hasattr(claim.date, "date") else claim.date
        )).days <= 365)



class Claim:
    def __init__(self, claim_id, date, amount, premium_collected, paid_amount, rejection_remarks):
        self.claim_id = claim_id
        self.date = date
        self.claim_amount = amount
        self.premium_collected = premium_collected
        self.paid_amount = paid_amount
        self.rejection_remarks = rejection_remarks
        self.status = "Rejected" if rejection_remarks else "Approved"

    def is_pending(self):
        return self.paid_amount == 0 and not self.rejection_remarks
