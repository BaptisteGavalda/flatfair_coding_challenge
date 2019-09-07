class OrganisationUnit:
    def __init__(self, name, OrganisationUnitConfig):
        self.name = name
        self.OrganisationUnitConfig = OrganisationUnitConfig

class OrganisationUnitConfig:
    has_fixed_membership_fee = True
    def __init__(self, membership_fee = 0):
        self.fixed_membership_fee = membership_fee
        if membership_fee > 0:
            self.has_fixed_membership_fee = True
        else:
            self.has_fixed_membership_fee = False

def calculate_membership_fee(rent_amount, rent_period, organisation_unit):
    fee = 0
    return (fee)

if __name__ == "__main__":
    pass