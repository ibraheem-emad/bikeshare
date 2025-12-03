# by ibrahim khatib

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH = [
              "january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december", "all"
            ]

DAY = [
    "monday", "tuesday", "wednesday", 
    "thursday", "friday", "saturday", "sunday", "all"]


# comment 1
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
    city = input("Would you like to see data for Chicago, New York City or Washington?: ").lower()
    while city not in CITY_DATA:
        city = input("your previous city entery doesn't exist in the database, try again: ").lower()
    
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("enter the name of the month you would like to filter by, if you dont want to filter by month type 'all': ").lower()
    while month not in MONTH:
        month = input("your previous month entery is incorrect, try again: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("enter the name of the day of week you would like to filter by, if you dont want to filter by a day of week type 'all': ").lower()
    while day not in DAY:
        day = input("your previous day entery is incorrect, try again: ").lower()

    print('-'*40)
    return city, month, day

# comment 2
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
    
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day'] = df['Start Time'].dt.day_name().str.lower()
    df['start_hour'] = df['Start Time'].dt.hour

    if month != 'all':
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day]
        
    return df


def time_stats(df , month , day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    if month == "all":
        common_month = df['month'].mode()[0]
        print("Most common month: ", common_month)

    # TO DO: display the most common day of week
    
    if day == "all":
        common_day = df['day'].mode()[0]
        print("Most common day of week: ", common_day)

    # TO DO: display the most common start hour
    
    common_hour = df['start_hour'].mode()[0]
    print("Most common start hour: ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start = df['Start Station'].mode()[0]
    print("Most commonly used start station: ", common_start)

    # TO DO: display most commonly used end station
    
    common_end = df['End Station'].mode()[0]
    print("Most commonly used end station: ", common_end)

    # TO DO: display most frequent combination of start station and end station trip
    
    common_route = (df['Start Station'] + " --> " + df['End Station']).mode()[0]
    print("Most frequent combination of start station and end station trip: ", common_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel = df['Trip Duration'].sum()
    print("Total travel time (in seconds): ", total_travel)

    # TO DO: display mean travel time
    
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time (in seconds): ", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n", user_types.to_string())

    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:\n", gender_counts.to_string())

    else:
        print("\nGender data not available for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df.columns:

        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode()[0])
        print("\nEarliest year of birth:", earliest)
        print("Most recent year of birth:", most_recent)
        print("Most common year of birth:", most_common)
        
    else:
        print("\nBirth Year data not available for this city.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
   
    i = 0
    
    decesion = input("do you want to see the first 5 rows of data? (yes, no): ").lower()
    while decesion not in ("yes", "no"):
        decesion = input("please enter yes or no: ").lower()
    
    if decesion == "yes":
        rows = df.head(5)
        print(rows.to_string(index=False))
        i += 5
        
        while i < df.shape[0]:
            decesion = input("Do you want to see the next 5 rows of data? Enter 'yes' or 'no': ").lower()
            while decesion not in ("yes", "no"):
                decesion = input("please enter yes or no: ").lower()
                
            if decesion == "no":
                break
            
            rows = df[i:i + 5]
            
            print(rows.to_string(index=False))
            i += 5
            
            if i >= df.shape[0]:
                print("there is no rows left!")
                break
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df , month , day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
