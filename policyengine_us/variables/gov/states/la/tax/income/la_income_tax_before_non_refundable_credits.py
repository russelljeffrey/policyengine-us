from policyengine_us.model_api import *


class la_income_tax_before_non_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Louisiana income tax before non-refundable credits"
    defined_for = StateCode.LA
    unit = USD
    definition_period = YEAR
    reference = "https://www.legis.la.gov/legis/Law.aspx?d=101946"

    def formula(tax_unit, period, parameters):
        income = tax_unit("la_taxable_income", period)
        filing_status = tax_unit("filing_status", period)
        status = filing_status.possible_values
        p = parameters(period).gov.states.la.tax.income.main
        return select(
            [
                filing_status == status.SINGLE,
                filing_status == status.JOINT,
                filing_status == status.SEPARATE,
                filing_status == status.WIDOW,
                filing_status == status.HEAD_OF_HOUSEHOLD,
            ],
            [
                p.single.calc(income),
                p.joint.calc(income),
                p.separate.calc(income),
                p.widow.calc(income),
                p.head_of_household.calc(income),
            ],
        )
