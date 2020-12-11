
def PrototypeModel():
    import numpy as np
    import statsmodels.api as sm
    from scipy import stats
    import statsmodels.formula.api as smf
    import pandas as pd
    from pathlib import Path

    file = Path(__file__).parent / "Output/df.xlsx"
    data = pd.read_excel(file)
    df = data.iloc[:,[0,2,4,7,8]]
    formula = 'df.iloc[:,1]~df.iloc[:,4]+df.iloc[:,3]'
    model = smf.glm(formula = formula, data = df, family = sm.families.Binomial())
    result = model.fit()
    print(result.summary())
    print(result.pvalues)
    predictions = result.predict()
    print(predictions)

def NationalModel():
    import numpy as np
    import statsmodels.api as sm
    from scipy import stats
    import statsmodels.formula.api as smf
    import pandas as pd
    from pathlib import Path

    file = Path(__file__).parent / "Output/Nation_Covid_MLData.xlsx"
    data = pd.read_excel(file)
    ndf = data.iloc[0:22,[0,2,3,5,11,15]]
    formula = 'ndf[["hospitalizedCurrently"]]~ndf[["totalTestResults"]]+ndf[["positive"]]+ndf[["negative"]]'
    model = smf.glm(formula = formula, data = ndf, family = sm.families.Binomial())
    result = model.fit()
    print(result.summary())
    print(result.pvalues)
    predictions = result.predict()
    print(predictions)

def StateModel():
    import numpy as np
    import statsmodels.api as sm
    from scipy import stats
    import statsmodels.formula.api as smf
    import pandas as pd
    from pathlib import Path

    file = Path(__file__).parent / "Output/State_Covid_MLData.xlsx"
    data = pd.read_excel(file)
    sdf = data.iloc[0:22,[0,2,4,7,8]]
    formula = 'sdf[["hospitalizedCurrently"]]~sdf[["totalTestResults"]]+sdf[["positive"]]+sdf[["negative"]]'
    model = smf.glm(formula = formula, data = sdf, family = sm.families.Binomial())
    result = model.fit()
    print(result.summary())

def Disclaimer():
    print("This is a proof of concept so take results with a pinch of salt.")
    print("If the Deviance/Df Residuals on the Results table and Person chi2") 
    print("are high that means the values are not highly accurate but fear not")
    print("because better and more data means better models!")

def Models():
    print("Looking at national data")
    NationalModel()
    print("------------------------")
    print("")
    print("")
    print("------------------------")
    print("Looking at state data")
    StateModel()
    print("------------------------")
    print("")
    print("")
    print("------------------------")
    Disclaimer()

Models()