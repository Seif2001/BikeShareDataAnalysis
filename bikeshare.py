import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all', 'january', 'february', 'march', 'april', 'may','june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    while True:
        city = input('Enter the city you want explored: ').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('Invalid city')
         

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input('Enter the month you want explored: ')
        month = month.lower()
        if month in months:
            break
        else:
            print('Invalid month')
         


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the day you want explored: ')
        day = day.lower()   
        if day in days:
            break   
        else:
            print('Invalid month')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        month = months.index(month)
        df = df[df['month'] == month]
    if day != 'all':
        day = day.title()
        df = df[df['day'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    most_common_month = months[most_common_month]
    print('The most common month was: {}' .format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]

    print('The most common day was: {}' .format(most_common_day))

    # TO DO: display the most common start hour
    ser = pd.Series(df['Start Time'].dt.hour)
    most_common_hour = ser.mode()[0]

    print('The most common hour was: {}' .format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_mode = df['Start Station'].mode()[0]
    print('The most common start station was: {}' .format(start_station_mode))
    # TO DO: display most commonly used end station
    end_station_mode = df['End Station'].mode()[0]
    print('The most common end station was: {}' .format(end_station_mode))
    

    # TO DO: display most frequent combination of start station and end station trip
    comb_station_col = df['Start Station'] +' to '+ df['End Station']
    comb_station_mode = comb_station_col.mode()[0]
    print('The most common trip was: {}' .format(comb_station_mode))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    duration_sum = df['Trip Duration'].sum()
    print('The total travel time was: {}' .format(duration_sum))

    # TO DO: display mean travel time
    duration_avg = df['Trip Duration'].mean()
    print('The average travel time was: {}' .format(duration_avg))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The user counts were:\n{}'.format(user_types.to_string()))
    

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        
        gender_types = df['Gender'].value_counts()
        print('The gender counts were:\n{}' .format(gender_types.to_string()))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        
        earliest_year = df['Birth Year'].min()
        most_year = df['Birth Year'].max()
        year_mode = df['Birth Year'].mode()[0]
        print('The earliest year of birth was {}, the most recent year of birth was {}, and the most common year of birth was {}.' .format(earliest_year,             most_year, year_mode))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
