"""By US State 2010-2014, identify energy source growing most quickly in percentage of total BTU consumption"""
import pandas as pd
dfMain=pd.read_csv('Energy Census and Economic Data US 2010-2014.csv')

df=dfMain[['State','CoalC2010','CoalC2011','CoalC2012','CoalC2013','CoalC2014',
'FossFuelC2010','FossFuelC2011','FossFuelC2012','FossFuelC2013','FossFuelC2014',
'GeoC2010','GeoC2011','GeoC2012','GeoC2013','GeoC2014',
'HydroC2010','HydroC2011','HydroC2012','HydroC2013','HydroC2014',
'NatGasC2010','NatGasC2011','NatGasC2012','NatGasC2013','NatGasC2014',
'LPGC2010','LPGC2011','LPGC2012','LPGC2013','LPGC2014']][:50]

dfCoal=df[['State','CoalC2010','CoalC2011','CoalC2012','CoalC2013','CoalC2014']]
dfFossFuel=df[['State','FossFuelC2010','FossFuelC2011','FossFuelC2012','FossFuelC2013','FossFuelC2014']]
dfGeo=df[['State','GeoC2010','GeoC2011','GeoC2012','GeoC2013','GeoC2014',]]
dfHydro=df[['State','HydroC2010','HydroC2011','HydroC2012','HydroC2013','HydroC2014']]
dfNatGas=df[['State','NatGasC2010','NatGasC2011','NatGasC2012','NatGasC2013','NatGasC2014']]
dfLPCG=df[['State','LPGC2010','LPGC2011','LPGC2012','LPGC2013','LPGC2014']]

CoalAvgChange=[sum([dfCoal.loc[i][j]/dfCoal.loc[i][j-1] for j in range(2,6)])/4 for i in range(50)]
FossFuelAvgChange=[sum([dfFossFuel.loc[i][j]/dfFossFuel.loc[i][j-1] for j in range(2,6)])/4 for i in range(50)]
GeoAvgChange=[sum([dfGeo.loc[i][j]/dfGeo.loc[i][j-1] for j in range(2,6)])/4 for i in range(50)]
HydroAvgChange=[sum([dfHydro.loc[i][j]/dfHydro.loc[i][j-1] for j in range(2,6)])/4 for i in range(50)]
NatGasAvgChange=[sum([dfNatGas.loc[i][j]/dfNatGas.loc[i][j-1] for j in range(2,6)])/4 for i in range(50)]
LPCGAvgChange=[sum([dfLPCG.loc[i][j]/dfLPCG.loc[i][j-1] for j in range(2,6)])/4 for i in range(50)]
StateEnergyTrends=[[CoalAvgChange[i],FossFuelAvgChange[i],GeoAvgChange[i],HydroAvgChange[i],
                    NatGasAvgChange[i],LPCGAvgChange[i]] for i in range(50)]

changeLeader=[]
typeLeader=[]
for state in StateEnergyTrends:
    growing=max([state[i] for i in range(6)])
    shrinking=min([state[i] for i in range(6)])
    if abs(1-growing)>abs(1-shrinking):
        changeLeader.append(round((growing-1)*100,2))
        slot=state.index(max([state[i] for i in range(6)]))
        if slot==0:
            typeLeader.append('Coal')
        elif slot==1:
            typeLeader.append('Fossil Fuel')
        elif slot==2:
            typeLeader.append('Geothermal')
        elif slot==3:
            typeLeader.append('Hydroelectric')
        elif slot==4:
            typeLeader.append('Natural Gas')
        else:
            typeLeader.append('Liq. Petroleum Gas')
    else:
        changeLeader.append(round((shrinking-1)*100,2))
        slot=state.index(min([state[i] for i in range(6)]))
        if slot==0:
            typeLeader.append('Coal')
        elif slot==1:
            typeLeader.append('Fossil Fuel')
        elif slot==2:
            typeLeader.append('Geothermal')
        elif slot==3:
            typeLeader.append('Hydroelectric')
        elif slot==4:
            typeLeader.append('Natural Gas')
        else:
            typeLeader.append('Liq. Petroleum Gas')
   
dfSlim=df[['State']]
dfSlim['ChangeLeader']=pd.Series(changeLeader).values           
dfSlim['typeLeader']=pd.Series(typeLeader).values 
dfSlim=dfSlim.sort_values(by='ChangeLeader',ascending=False)
dfSlim=dfSlim.set_index(['State'])

print(dfSlim)
