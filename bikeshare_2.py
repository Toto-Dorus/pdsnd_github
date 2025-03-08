import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    User is asked to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    month = 'all'
    day = 'all'

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        try:
            city = input('Would you like to see data from Chicago, New York oder Washington?\n').lower()
            if city in ['chicago', 'new york', 'washington']:
                if city == 'new york':
                    city = 'new york city'
                print(f"Looks like you want to hear about {city.title()}! If this is not true, restart the program now.\n")
                break
            else:
                print("invalid input, try again")
        except:
            print("invalid input, try again")



        # get user input for filter type (month, day, both, none)
    while True:
        try:
            filter = input('Would you like to filter the data by month, day, both or not at all? Type \"none\" for no time filter.\n').lower()
            if filter in ['month', 'day', 'both', 'none']:
                print(f"We will make sure to filter by {filter}\n")
                break
            else:
                print("invalid input, try again")
        except:
            print("invalid input, try again")
        
        # get user input for month (january, february, ... , june)



        
    if filter in ['month', 'both']:
        while True:
            try:
                month = input('Which Month? January, February, March, April, May or June? Please type out the full month name.\n').lower()
                if month in ['january', 'february', 'march', 'april', 'may' 'june']:
                    print(f"We will show data for the month of {month.title()}\n")
                    break
                else:
                    print("invalid input, try again to choose a month")
            except:
                print("invalid input, try again to choose a month again")


        # get user input for day of week (all, monday, tuesday, ... sunday)
                
    if filter in ['day', 'both']:
        while True:
            try:
                day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday? Please type out the full day name.\n').lower()
                if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday' 'saturday', 'sunday']:
                    print(f"We will show data only for {day.title()}s")
                    break
                else:
                    print("invalid input, try again to choose a day again")
            except:
                print("invalid input, try again to choose a day again")


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month  = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
        
    # filter by day of week if applicable
    if day != 'all':
            
        # filter by month to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    popular_month = df['month'].mode()[0]
    print(f"What is the most popular month for traveling?\n{months[popular_month-1]}\n")
    
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(f"What is the most popular day for traveling?\n{popular_day.title()}\n")

    # display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print(f"What is the most popular hour of the day to start your travels?\nBetween {popular_hour}:00 and {00 if popular_hour == 23 else popular_hour+1}:00 \n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print(f"What is the most popular station to start from?\n{popular_start.title()}\n")

    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print(f"What is the most popular station to end your trip?\n{popular_end.title()}\n")


    # display most frequent combination of start station and end station trip
    popular_trip = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().idxmax()
    popular_trip_count   = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().max()
    print(f"What is the most popular trip from start to end?\nStart Station: {popular_trip[0]}    End Station: {popular_trip[1]}    Trip Count:{popular_trip_count}\n")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_time = df['End Time'] - df['Start Time']
    total_time = trip_time.sum()
    print(f"What was the total traveling time?\n{total_time.days} days, {total_time.seconds//3600} hours, {total_time.seconds % 3600//60} minutes and {total_time.seconds % 60} seconds\n")


    # display mean travel time
    avg_time = trip_time.mean()
    print(f"What was the average time per trip?\n{avg_time.seconds//3600} hours, {avg_time.seconds % 3600//60} minutes and {avg_time.seconds % 60} seconds\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print(f"What is the breakdown of users?\n{user_types}\n")
    
    # Display counts of gender
    print("What is the breakdown of gender?")
    if 'Gender' in df:
        print(df['Gender'].value_counts(),"\n")
    else:
        print("No gender data to share\n")

    # Display earliest, most recent, and most common year of birth
    print("What is the oldest, youngest and most popular year of birth?")
    if 'Birth Year' in df:
        print(f"Oldest year of birth: {int(df['Birth Year'].min())}")
        print(f"Youngest year of birth: {int(df['Birth Year'].max())}")
        print(f"Most popular year of birth: {int(df['Birth Year'].mode()[0])}\n")
    else:
        print("No birth year data to share\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def provide_raw_data(df):
    """Displays raw Data."""

    show_init = input('\nWould you like to see the raw data? Enter yes or no.\n').lower()
    if show_init[0] == 'y':
        i = 0
        while True:
            print(df[i:i+5])
            i += 5
            show_more = input('\nWould you like to see next raw data? Enter yes or no.\n').lower()
            if show_more[0] != 'y':
                break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        provide_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break




if __name__ == "__main__":
	main()
