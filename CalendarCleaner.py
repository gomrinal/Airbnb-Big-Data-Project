import pandas as pd



i=2

Input=["CalendarVan.csv","CalendarTor.csv","CalendarMon.csv"]
Output=["ClCalendarVan.csv","ClCalendarTor.csv","ClCalendarMon.csv"]

inputFile = Input[i]
outputFile= Output[i]

cal= pd.read_csv(inputFile)
print(cal.shape)
def ExtractPrice(x):
    val=''
    try:
        
        for i in x:
            if i in '123456789.':
                val=val+i
            else:
                pass
        return(float(val))
    except:
        return(0)
    
def CorrectAvailable(x):
    if x=='t':
        return(1)
    else:
        return(0)
        
cal= cal.drop(columns=['minimum_nights','maximum_nights','adjusted_price'],axis=1)
cal['date']=pd.to_datetime(cal['date'])
cal['price']= cal['price'].apply(lambda x: ExtractPrice(x))
cal[cal['price']==0]['price']= cal['price'].mean()
cal['available']= cal.available.apply(lambda x: CorrectAvailable(x))

cal.to_csv("output/"+outputFile)
