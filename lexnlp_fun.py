import lexnlp
import lexnlp.extract.en.acts
import lexnlp.extract.en.conditions
import lexnlp.extract.en.constraints
import lexnlp.extract.en.copyright
import lexnlp.extract.en.dates
import lexnlp.extract.en.money
import lexnlp.extract.en.trademarks
import lexnlp.extract.en.regulations


import nltk
# Only use it onece and then comment out

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


class lexnlp_entity():
    def __init__(self,data):
        self.data = data

    def acts(self):
        Acts = lexnlp.extract.en.acts.get_act_list(self.data)
        return Acts


    def conditioons(self):
        Condition =list(lexnlp.extract.en.conditions.get_conditions(self.data))
        return Condition

    def constraints(self):
        Constraint = list(lexnlp.extract.en.constraints.get_constraints(self.data))
        
        return Constraint

    def copyrights(self):
        Copyright = list(lexnlp.extract.en.copyright.get_copyright(self.data))
        return Copyright

    def date_time(self):
        x = list(lexnlp.extract.en.dates.get_dates(self.data))
        return x

    def get_money(self):
        Z = list(lexnlp.extract.en.money.get_money(self.data))
        return Z

    def trademark(self):
        xy = list(lexnlp.extract.en.trademarks.get_trademarks(self.data))
        return xy

    def regulation(self):
        x =list(lexnlp.extract.en.trademarks.get_trademarks(self.data))
        return x

# data02 = "source array and spread diagram, summary of sea and weather conditions and complete   operational statistics will also be provided.      5.3 2 hard copies and 4 electronic copies of the final operations report on CDs, within 30 days of the   completion of the Services in the Contractor’s standard format.         6 DATA DELIVERY      The Contractor shall deliver the field tapes, observer’s reports and other pertinent field data to the   Company's address for notices as provided in Clause 13 of Annexure A or such other destination as the   Company may direct.          7 PRE-PLOTS       At least 2 weeks before the commencement of the Services, the Contractor shall supply pre-plots of the   program sail lines based on coordinates supplied by the company for the Survey programs.  These pre-   plots shall be provided digitally and in the form of maps and coordinate printouts, using the geodetic   reference system and mapping projection specified in Annexure D.         8 NAVIGATION DATA      The Contractor shall ensure that navigation data shall be recorded digitally. Post-plotted navigat"

# # lexji = lexnlp_entity()

# xy = lexnlp_entity(data02)
# print(xy.acts())
# print(xy.conditioons())
# print(xy.constraints())

