import time
import datetime as dt
import pandas as pd
import numpy as np

# Project requirements:
# 1.
# Anticipate raw input errors like using improper upper or lower case,
# typos, or users misunderstanding what you are expecting
# 2. Statistics needed:
# i. Most common month, day of week, hour of day
# ii. Most common start station, end station, start and end trip
# iii. Total travel time, average travel time
# iv. Counts of each user type, counts of each gender (nyc and chicago),
# earliest, most recent, and most common year of birth (nyc and chicago)
# 3.
# Your script also needs to prompt the user whether they would like want
# to see the raw data. If the user answers 'yes,' then the script should print
# 5 rows of the data at a time, then ask the user if they would like to see
# 5 more rows of the data. The script should continue prompting and printing
# the next 5 rows at a time until the user chooses 'no,' they do not want any
# more raw data to be displayed.
#4.
#Project has been submitted and passed

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
    print('Hello! Let\'s explore some US bikeshare data!')

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    while True:
        try:
            # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
            # TO DO: get user input for month (all, january, february, ... , june)
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            city = input('Would you like to see data for Chicago, New York City, or Washington: ')
            month = input('Would you like to filter by which month of the year, January, February, ..., June, or include all: ')
            day = input('Would you like to filter by which day of the week, Monday, Tuesday, ..., Sunday, or include all: ')

            if city.lower() in CITY_DATA and (month.lower() in months or month.lower() == 'all') and (day.lower() in days or day.lower() == 'all'):

                break

            else:

                if city.lower() not in CITY_DATA:
                    print('You have entered an incorrect city or an invalid input. Please ensure you typed the full name of the city.')

                if month.lower() not in months and month.lower() != 'all':
                    print('You have entered an invalid month or an invalid input. Please ensure you typed the full name of the month.')

                if day.lower() not in days and day.lower() != 'all':
                    print('You have entered an invalid day of the week or an invalid input. Please ensure you typed the full name of the day of the week.')

        except KeyboardInterrupt:
            print('You have stopped the program.')
            break

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
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])
    month = month.lower()
    day = day.lower()

    # convert the Start Time and End Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    # 0 is a monday
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    # TO DO: display the most common month
    most_common_month = months[df['month'].mode()[0] - 1]
    most_common_month_ct = df['month'].value_counts().max()
    print('Most common month is {}.'.format(most_common_month.title()))
    print('The count of {} is {}.'.format(most_common_month.title(), most_common_month_ct))

    # TO DO: display the most common day of week
    most_common_day = days[df['day_of_week'].mode()[0]]
    most_common_day_ct = df['day_of_week'].value_counts().max()
    print('Most common day of week is {}.'.format(most_common_day.title()))
    print('The count of {} is {}.'.format(most_common_day.title(), most_common_day_ct))

    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    most_common_hour_ct = df['Start Time'].dt.hour.value_counts().max()
    print('Most common hour is {}.'.format(most_common_hour))
    print('The count of hour {} is {}.'.format(most_common_hour, most_common_hour_ct))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_stn = df['Start Station'].mode()[0]
    most_common_start_stn_ct = df['Start Station'].value_counts().max()
    print('Most common start station is {}.'.format(most_common_start_stn))
    print('The count of {} is {}.'.format(most_common_start_stn, most_common_start_stn_ct))

    # TO DO: display most commonly used end station
    most_common_end_stn = df['End Station'].mode()[0]
    most_common_end_stn_ct = df['End Station'].value_counts().max()
    print('Most common end station is {}.'.format(most_common_end_stn))
    print('The count of {} is {}.'.format(most_common_end_stn, most_common_end_stn_ct))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Combo'] = df['Start Station'] + '**' + df['End Station']
    most_common_start_end = df['Start End Combo'].mode()[0]
    most_common_start_end_cnt = df['Start End Combo'].value_counts().max()
    print('Most common start-end stations are {}.'.format(most_common_start_end))
    print('The count of {} is {}.'.format(most_common_start_end, most_common_start_end_cnt))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['Travel Time'] = (df['End Time'] - df['Start Time']).dt.seconds

    # TO DO: display total travel time
    total_travel_time = df['Travel Time'].sum()
    print('Total travel time in seconds is {}.'.format(total_travel_time))

    # TO DO: display mean travel time
    average_travel_time = df['Travel Time'].mean()
    print('Average travel time in seconds is {}.'.format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    if city.lower() == 'washington':
        print('{} does not have gender of year of birth information.'.format(city.title()))
    else:
    # TO DO: Display counts of gender
        print('Gender counts are:\n')
        print(df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest year of birth is {}'.format(df['Birth Year'].min()))
        print('The most recent year of birth is {}'.format(df['Birth Year'].max()))
        print('The most common year of birth is {}'.format(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def sample_prompt(df):
    """Prompts the user if they would like to view data samples 5 at a time"""
    while True:

        decision = input('Would you like to see 5 lines of data? Enter yes or no: ')
        counter = 0

        if decision.lower() != 'yes' and decision.lower() != 'no':
            print('Please enter either yes or no only.')
        elif decision.lower() != 'yes':
            break
        else:
            print(df[counter:(counter + 5)][:])
            counter += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        sample_prompt(df)

        restart = input('\nWould you like to restart? Enter yes or no:\n')
        if restart.lower() != 'yes':
            break

    return df

if __name__ == "__main__":
	df = main()
