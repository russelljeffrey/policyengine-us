from policyengine_us.model_api import *


class wv_low_income_exemption(Variable):
    value_type = float
    entity = TaxUnit
    label = "West Virginia low income exemption"
    defined_for = StateCode.WV
    unit = USD
    definition_period = YEAR
    reference = "https://code.wvlegislature.gov/11-21-10/"

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.wv.tax.income.exemptions.low_income