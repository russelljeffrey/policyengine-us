from policyengine_us.model_api import *


class wv_low_income_exemption(Variable):
    value_type = float
    entity = TaxUnit
    label = "West Virginia low income exemption"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.WV

    def formula(tax_unit, period, parameters):
        # First get their filing status.
        filing_status = tax_unit("filing_status", period)

        # Then get the WV Exemptions part of the parameter tree.
        p = parameters(period).gov.states.wv.tax.income.exemptions.low_income

        # Get their regular exemption amount based on their filing status.
        return p.max_amount[filing_status]