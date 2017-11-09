
# coding: utf-8

# In[102]:

#Name: Sean Marino
#Program: Video Game Recommendation System
#Description: This program was designed to provide the user with average ratings,
#cosine similarities, and video game recommendations based on the data provided.

from collections import defaultdict
import pandas as pd


# In[103]:

#Create the columns for User, Video Game, and Rating and pass in the txt file containing the data

u_columns = ['user_id', 'item_id', 'rating']
data = pd.read_csv('/Users/seanmarino/Desktop/HW3/rating.txt', sep=' ', names=u_columns, encoding='latin-1')


# In[104]:

#Ensures that the data was passed in with appropriate column headers
data.head()


# In[84]:

#Passes the data into a dataframe
gameData = pd.DataFrame(data)


# In[85]:

gameData.head()


# In[86]:

#Finds the average rating for the following user
gameData.groupby(by='user_id')['rating'].mean().sort_values(ascending=False).head(20)
averageRating = gameData[gameData['user_id'] == 'U868476845'].mean()
print('Average Rating for User U868476845:', averageRating)


# In[87]:

#Provides the number of users and video games in the data set

users = gameData['user_id'].unique()
len(users)


# In[88]:

games = gameData['item_id'].unique()
len(games)


# In[89]:

#Creates a testing set and a base set of data
testcols = ['user_id', 'item_id', 'rating']
initialRatings = pd.read_csv('/Users/seanmarino/Desktop/HW3/rating.txt', sep=' ', names=r_cols, encoding='latin-1')
testRatings = pd.read_csv('/Users/seanmarino/Desktop/HW3/rating.txt', sep=' ', names=r_cols, encoding='latin-1')
initialRatings.shape, testRatings.shape


# In[90]:

import graphlab as gl


# In[91]:

#Move training data into an Sframe
trainingData = gl.SFrame(initialRatings)
testingData = gl.SFrame(testRatings)


# In[92]:

print(trainingData)


# In[93]:

#Uses graphlabs item similarity function to calculate cosine similaritys between users

model = gl.item_similarity_recommender.create(trainingData, user_id='user_id', item_id='item_id', target='rating', similarity_type='cosine')


# In[106]:

#Uses graphlabs recommend function to recommend video games to the specified user

similarGames = model.recommend(users=['U868476845'], k=10)
similarGames.print_rows(num_rows=200)


# In[101]:

#The following functions find the users with the highest cosine similarity to user U868476845

userModel = gl.factorization_recommender.create(trainingData, user_id='user_id', item_id='item_id', target='rating')
similarUsers = m.get_similar_users(users=['U868476845'], k=5)
similarUsers.print_rows(num_rows=200)


# In[ ]:



