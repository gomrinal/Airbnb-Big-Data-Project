


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly 
import cufflinks
#get_ipython().run_line_magic('matplotlib', 'inline')

i=0
# In[2]:


cityArr=['Vancouver','Torronto','Montreal']
stateArr=['BC','ON','QC']
data=['ListingsVan.csv','ListingsTor.csv','ListingsMon.csv']
output=['ClVanListings.csv','ClTorListings.csv','ClMonListings.csv']


# In[3]:

city= cityArr[i]
state= stateArr[i]
df=pd.read_csv(data[i])


# In[4]:


df=df.drop(columns=["listing_url",'neighbourhood','property_type','is_business_travel_ready','space','host_acceptance_rate','reviews_per_month','has_availability','neighborhood_overview','host_location','host_listings_count',"scrape_id","last_scraped","summary","description","experiences_offered","notes","transit","access","interaction","house_rules","thumbnail_url","medium_url","picture_url","xl_picture_url","host_url","host_name","host_since","host_about","host_response_time","host_thumbnail_url","host_picture_url","host_neighbourhood","street","neighbourhood_cleansed","neighbourhood_group_cleansed","zipcode","market","smart_location","country_code","country","bed_type","square_feet","weekly_price","monthly_price","minimum_minimum_nights","maximum_minimum_nights","minimum_maximum_nights","maximum_maximum_nights","minimum_nights_avg_ntm","maximum_nights_avg_ntm","calendar_updated", "availability_30","availability_60", "availability_90","calendar_last_scraped", "number_of_reviews_ltm","first_review","last_review","license","jurisdiction_names","calculated_host_listings_count_entire_homes","calculated_host_listings_count_private_rooms","calculated_host_listings_count_shared_rooms"
],axis=1)


# In[5]:


def CorrectResponseRate(x):
    try:
        return(int(x[:-1])/100)
    except:
        return(0)


# In[6]:


df['host_response_rate']=df['host_response_rate'].apply(lambda x : CorrectResponseRate(x))


# In[7]:


def CorrectHostVerifications(x):
    arr= x.split(',')
    return(len(arr))


# In[8]:


df['host_verifications']= df['host_verifications'].apply(lambda x: CorrectHostVerifications(x))


# In[9]:


df['city']=city


# In[10]:


df['state']=state


# In[11]:


def CorrectAmenities(x):
    score=0
    x=x.lower()
    if 'tv' in x:
        score=score+1
    if 'kitchen' in x:
        score=score+1
    if 'internet' in x:
        score=score+1
    if 'gym' in x:
        score=score+1
    if 'breakfast' in x:
        score=score+1
    if 'washer' in x:
        score=score+1
    if 'extinguisher' in x:
        score=score+1
    if 'parking' in x:
        score=score+1
    if 'wheelchair' in x:
        score=score+1
    if 'smoke' in x:
        score=score+1
    return(score)


# In[12]:


df['amenities']= df['amenities'].apply(lambda x : CorrectAmenities(x))


# In[13]:


def CorrectPrice(x):
    num=''
    for i in x:
        if i in '0123456789.':
            num=num+i
        else:
            pass
    return(float(num))


# In[14]:


df['price']= df['price'].apply(lambda x : CorrectPrice(x))


# In[15]:


def CorrectSecurityDeposit(x):
    if x==-1:
        return(-1.0)
    else:
        try:
            return(CorrectPrice(x))
        except:
            return(-1)
      


# In[16]:


df['security_deposit']=df['security_deposit'].fillna(-1)
df['security_deposit']= df['security_deposit'].apply(lambda x : CorrectSecurityDeposit(x))
df[df['security_deposit']==-1]['security_deposit']=df['security_deposit'].mean()


# In[17]:


def CorrectCleaningFee(x):
    if x==-1:
        return(-1.0)
    else:
        try:
            return(CorrectPrice(x))
        except:
            return(-1)


# In[18]:


df['cleaning_fee']=df['cleaning_fee'].fillna(-1)
df['cleaning_fee']= df['cleaning_fee'].apply(lambda x : CorrectCleaningFee(x))
df[df['cleaning_fee']==-1]['cleaning_fee']=df['cleaning_fee'].mean()


# In[19]:


def CorrectExtraPeople(x):
    if x==-1:
        return(-1.0)
    else:
        try:
            return(CorrectPrice(x))
        except:
            return(-1)


# In[20]:


df['extra_people']= df['extra_people'].apply(lambda x : CorrectExtraPeople(x))


# In[21]:


df['review_scores_rating']=df['review_scores_rating'].fillna(-1)
df[df['review_scores_rating']==-1]['review_scores_rating']= df['review_scores_rating'].mean()
df['review_scores_rating']=df['review_scores_rating']/10


# In[22]:


rev=['review_scores_checkin','review_scores_communication','review_scores_location','review_scores_value','review_scores_accuracy','review_scores_cleanliness']
for element in rev:
    df[element]=df[element].fillna(-1)
    df[df[element]==-1][element]= df[element].mean()


# In[23]:


def CorrectCancellationPolicyScore(x):
    opt=['strict_14_with_grace_period', 'moderate', 'flexible']
    if x ==opt[0]:
        return(0)
    elif x==opt[1]:
        return(1)
    else:
        return(2)


# In[24]:


df['cancellation_policy']= df['cancellation_policy'].apply(lambda x : CorrectCancellationPolicyScore(x))


# In[25]:


boolFeatures=["require_guest_phone_verification",'host_is_superhost',"instant_bookable","host_identity_verified","host_has_profile_pic","require_guest_profile_picture","requires_license","is_location_exact"]


# In[26]:


def CorrectBoolFeatures(x):
    if x=='t':
        return(1)
    else:
        return(0)


# In[27]:


for element in boolFeatures:
    
    df[element]= df[element].apply(lambda x : CorrectBoolFeatures(x))
    


# In[28]:


df=df.dropna(axis = 0, how ='any')


# In[29]:


df.to_csv('output/'+output[i])


# In[ ]:




