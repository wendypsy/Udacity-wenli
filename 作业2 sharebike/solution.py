
# coding: utf-8

# In[21]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#df = pd.read_csv(CITY_DATA['chicago'])  
#print(df.head())
#print(df.head(10))
#start_time = time.time()
#print(start_time)


# In[29]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input( 'Would you like to see data for chicago, new york city, washington?\n')
    city=city.lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    time_period = input('\nWould you like to filter the data by month, day,both, or not at'
                        ' all? Type "none" for no time filter.\n')
    if time_period=='both':
        month = input('\nWhich month?all,january, february, march, april, may, or june?\n')
        month = month.lower()
        day = input('\nWhich day? all,monday, tuesday,wednesday,thursday,friday,saturday,sunday？\n')
        day = day.lower()
    elif time_period=='month':
        month = input('\nWhich month?all,january, february, march, april, may, or june?\n')
        month = month.lower()
        day='all'
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    elif time_period=='day':
        day = input('\nWhich day? all,monday, tuesday,wednesday,thursday,friday,saturday,sunday？\n')
        day = day.lower()
        month='all'
    else:
        month='all'
        day='all'
            
    #month = input('\nWhich month?all,january, february, march, april, may, or june?\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #day = input('\nWhich day? all,monday, tuesday,wednesday,thursday,friday,saturday,sunday？\n')

    
    print('-'*40)
    return city, month, day
#print(get_filters())


# In[30]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])   
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name 
    
    if month!='all':
        """transfer the input months to the number of 1-6"""
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]
        
    if day!='all':
        df=df[df['day_of_week']==day.title()]
    return df
#print(load_data('chicago','march','friday'))


# In[31]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    # TO DO: display the most common month   
    start_time = time.time()
    #print(start_time)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #print(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    #print(df['month'])
    #print(df['month'].mode())
    #month_types= df['month'].value_counts()
    popular_month = df['month'].mode()[0]
    

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_weekday = df['day_of_week'].mode()[0]

    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    count_hour=df['hour'].count()
    popular_hour = df['hour'].mode()[0]

    #print(month_types)
    #return popular_month,popular_weekday,popular_hour
    print("Most popular hour:{},count:{}".format(popular_hour,count_hour))
    print(popular_month,popular_weekday,popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#print(time_stats('chicago'))


# In[32]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    #df = pd.read_csv(CITY_DATA[city])
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
        
    # TO DO: display most commonly used start station   
    #start_station_types = df['Start Station'].value_counts()    
    popular_start_station = df['Start Station'].mode()[0]  
    count_start_station=df['Start Station'].count()

    # TO DO: display most commonly used end station
    #end_station_types = df['End Station'].value_counts()  
    popular_end_station = df['End Station'].mode()[0]  
    count_end_station = df['End Station'].count()
    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+df['End Station']
    most_frequent_combination=df['combination'].mode()[0]  
    count_frequent_combination=df['combination'].count() 
    #print(station_stats('chicago'))
    #print(station_stats(df))
    
    print("Start Station:{},Count:{},End Station:{},Count:{}".format(popular_start_station,count_start_station,popular_end_station,count_end_station))  
    print("popular trip:{},Count:{}".format(most_frequent_combination,count_frequent_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[33]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum() 
    count_travel_time=df['Trip Duration'].count() 

    # TO DO: display mean travel time
    mean_travel_time =df['Trip Duration'].mean()
    #return total_travel_time,mean_travel_time
    #print(trip_duration_stats(df))
    print("Total Duration:{},Count:{},Averager Duration:{}".format(total_travel_time,count_travel_time,mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#print(trip_duration_stats('chicago'))    


# In[34]:


def user_types(df):
    """Displays statistics on bikeshare users."""
    
    #df=pd.read_csv(CITY_DATA[city])
    print('\nCalculating User Types...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_gender(df):
    # TO DO: Display counts of gender
    print('\nCalculating Gender...\n')
    start_time = time.time()
    gender_types = df['Gender'].value_counts()
    print(gender_types)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: Display earliest, most recent, and most common year of birth
    #birth_year_types = df['Birth Year'].value_counts()
    
def user_birth_year(df):
    print('\nCalculating earliest, most recent, and most common year of birth...\n')
    start_time = time.time()
    earliest_birth_year=df['Birth Year'].max()
    oldest_birth_year=df['Birth Year'].min()   
    most_common_birth_year=df['Birth Year'].mode()[0]
    print("earliest_birth_year:{},oldest_birth_year:{},most_common_birth_year:{}".format(earliest_birth_year,oldest_birth_year,most_common_birth_year))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    #return user_types,gender_types,earliest_birth_year,oldest_birth_year,most_common_birth_year

    #print(user_stats('chicago'))
    #print(user_stats(df))

    


# In[35]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_types(df)
        if city!='washington':
            user_gender(df)
            user_birth_year(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

