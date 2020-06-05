import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! \n Choose from the following \n a.Chicago\nb.New York\nc.Washington\n')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('Which city data do you want to explore (options a,b or c)? \n ')
    
    while (city != 'a' and city != 'b' and city != 'c'):
        
        print('\nInvalid input , please choose from the options a.Chicago , b.New York , c.Washington\n')
        city = input('Which city data do you want to explore (options a,b or c)? \n ')
    
    print('From the choices ,a.Chicago , b.New York , c.Washington\n , We will look into the data of city ', city)
    
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input('\nWhich month data do you wish to look into ( all months or specifically from january to june) ? ').lower()
    
    if month not in ['january','february','march','april','may','june'] :
        print('Please enter a valid month ( all months or specifically from january to june)')
        month = input('\nWhich month data do you wish to look into ( all months or specifically from january to june) ? ').lower()
    
    
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input('Which day of the week data do you wish to look into ( all days of the week or specifically monday to sunday? )').lower()
    
    if day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        print('Please enter a valid day of teh week ( all days of the week or specifically monday to sunday? )')
        day = input('Which day of the week data do you wish to look into ( all days of the week or specifically monday to sunday? )').lower()
    
    print('Let us look into',month)
    print('Let us look into',day)

    if (city == 'a'):
        city = 'chicago'
    elif(city == 'b'):
        city = 'new york city'   
    else:
        city = 'washington'
        
    
    print('-'*40)
    return city, month, day

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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    view_display = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_display == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month:

   
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)
    

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Start Day:', popular_day)

    # TO DO: display the most common start hour

    # find the most popular hour:
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station

    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    df['Count']=df.groupby(['Start Station','End Station'])['End Station'].transform('size')
    count_max = df['Count'].max()
    df1 = df[ count_max == df['Count'].values]
    #df1 = df1[['Start Station','End Station']]
    #df1 = np.unique(df1)
    #print(df1)
    print('Most frequent Combination occures when start station is and end station are ', df1[['Start Station','End Station']])
    
    #print('The Combination are ', \n df1['Combi'].unique())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['diff'] = df['End Time'] - df['Start Time']
    
    df['diff'] = df['diff']/np.timedelta64(1,'s')
    print('Travel time in seconds',df['diff'])
    
    # TO DO: display mean travel time

    mean_travel_time = np.mean(df['diff'])
    print('The mean travel time in seconds \n ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(city , df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print('The count of user types are \n ',user_types)

    # TO DO: Display counts of gender

    if (city == 'chicago' or city =='new_york'):
        gender_count = df['Gender'].value_counts()
        print('The count of gender types are \n ',gender_count)
    
    # TO DO: Display earliest, most recent, and most common year of birth

    if (city == 'chicago' or city =='new_york'):
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        popular_birth_year = df['Birth Year'].mode()[0]
        
        print('The earliest birth year is', earliest_birth_year)
        print('The recent birth year is', recent_birth_year)
        print('The common birth year ', popular_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(city , df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
