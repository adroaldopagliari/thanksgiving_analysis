
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


data = pd.read_csv('thanksgiving.csv',encoding="Latin-1")


# In[4]:


data.head()


# In[5]:


data.columns


# In[6]:


data['Do you celebrate Thanksgiving?'].value_counts()


# In[7]:


data = data[data['Do you celebrate Thanksgiving?'] == 'Yes']


# In[8]:


data.head()


# In[9]:


data['Do you celebrate Thanksgiving?'].value_counts()


# In[10]:


data['What is typically the main dish at your Thanksgiving dinner?'].value_counts()


# In[11]:


data[data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"]["Do you typically have gravy?"]


# In[13]:


apple_isnull = data['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple'].isnull()


# In[14]:


apple_isnull


# In[28]:



ate_pies = (pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"])
&
pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"])
 &
 pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"])
)

ate_pies.value_counts()


# In[53]:


def parse_age_int(age):
    if pd.isnull(age):
        return None
    else:
        new_str = age.split(' ')    
        new_str = new_str[0]
        new_str = new_str.replace("+", "")
        new_int = int(new_str)
        return new_int
        


# In[54]:


data["int_age"] = data["Age"].apply(parse_age_int)
data["int_age"].describe()


# Our analysis uses the minor value in ages, so the values can be far of reality, although the data is balanced.

# In[55]:


def parse_wage_float(wage):
    if pd.isnull(wage):
        return None    
    else:
        new_str = wage.split(' ')    
        new_str = new_str[0]
        if new_str == 'Prefer':
            return None
        else:
            new_str = new_str.replace(",", "")
            new_str = new_str.replace("$", "")
            new_int = float(new_str)
            return new_int


# In[56]:


data["int_income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(parse_wage_float)
data["int_income"].describe()


# Once again we considered only the minor value of incomes, so this distribuition tends to downside.

# In[57]:


data[data["int_income"] < 150000]["How far will you travel for Thanksgiving?"].value_counts()


# In[58]:


data[data["int_income"] > 150000]["How far will you travel for Thanksgiving?"].value_counts()


# The local of thanksgiving is conditioned by the incomes. How low this value is there's more chance to go to parents house. If the income is high the local is the own house.

# In[59]:


data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_age"
)


# In[60]:


data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_income"
)


# If you are younger probably will attend the friendsgiving.
