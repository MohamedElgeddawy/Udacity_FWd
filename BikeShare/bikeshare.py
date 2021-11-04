import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city=input("Select city which you want to see its data : chicago, new york city or washington\n ").lower()

    while city not in ['chicago','new york city','washington']:
        city=input("Sorry, your input should be: chicago new york city or washington\n").lower()



    # get user input for month (all, january, february, ... , june)
    months=['january','february','march','april','may','june','all']
    #month=input('\n\nPlease select all months by typing---> all \n or one month by typing \n january as--->1 \n february as--->2 \n maech as--->3 \n appril as -->4 \n may as -->5 \n june as -->6 \n\n\n  ')
    month=input('Which Month (january , february , march , april , may , june or all)?\n  ').lower()

    while month not in months:
        print("invalid input")
        month=input('\nyour input should be->(january, february, march, april, may, june or all)\n\n ').lower()
        # get user input for day of week (all, monday, tuesday, ... sunday)
    days=[ 'saturday', 'sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']

    day=input('Which Day (saturday , sunday , monday , tuesday , wednesday , thursday , friday or all)  \n ').lower()
    while day not in days:
        print("invalid input")
        day=input(' your input should be->(saturday , sunday , monday , tuesday , wednesday , thursday , friday or all \n) ').lower()

    return city,month,day

def load_data(city, month, day):


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

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



    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month--->
    the_most_common_month=df['month'].mode()[0]
    print("The most common month--->",the_most_common_month)


    # display the most common day of week
    the_most_common_day_of_week=df['day_of_week'].mode()[0]
    print("The most common day of week--->",the_most_common_day_of_week)



    # display the most common start hour
    the_most_common_start_hour=df['hour'].mode()[0]
    print("The most common start hour--->",the_most_common_start_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('Common start station-->', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print('Common end station-->', common_end_station)


    # display most frequent combination of start station and end station trip
    df["combination station"] = df["Start Station"]+ '-' + df["End Station"]
    common_combination_station =df["combination station"].mode()[0]
    print('Common combination station-->', common_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total travel time--->', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('The mean oftravel time--->', mean_travel_time)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types=df['User Type'].value_counts()
    print('The counts of user types---> \n', counts_of_user_types)
    if city != 'washington':
        # Display counts of gender
        counts_of_gender=df['Gender'].value_counts()
        print('The counts of gender---> \n', counts_of_gender)
        # Display earliest, most recent, and most common year of birth
        earliest_year =df['Birth Year'].min()
        print('The earliest year--->',int(earliest_year))
        most_recent_year = df['Birth Year'].max()
        print('The most recent year of birth--->',int(most_recent_year))
        most_common_year=df['Birth Year'].min()
        print('The most common Year--->',int(most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def  display_raw_data(city) :

    print('\n May you want to have a look of Data \n')
    display_raw = input ('if you want to see first 5 rows?Please enter yes or no.\n')
    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city] , chunksize=5):
                print(chunk)

                display_raw = input('if you want to see another 5 rows?Please enter yes or no.\n')
                if display_raw != 'yes':
                    print('Thank You')
                    break
            break
        except KeyboardInterrupt:
            print('Thank you')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
