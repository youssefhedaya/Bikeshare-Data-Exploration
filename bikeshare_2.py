import time
import pandas as pd
import numpy as np
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while(True):
        print("Available Cities: Chicago, New York City, Washington")
        city = input("Please specify City: ").lower().replace(" ","")
        if city == "chicago":
            break
        if city == 'newyorkcity' or city == "newyork":
            city = "new york city"
            break
        if city == 'washington':
            break




    # TO DO: get user input for month (all, january, february, ... , june)
    while(True):
        month = input("Please specify a month from January to June: ").lower().replace(" ","")
        if month == "all" or month == "january" or month == "february" or month == "march" or month == "april" or month == "may" or month == "june":
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):
        day = input("Please specify day: ").lower()
        if day == "all" or day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "fridat" or day == "saturday" or day == "sunday":
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
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
       # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        print(month)

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]




    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    print("Most common month: ",months[df['month'].mode()[0]-1])


    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    print("Most common day of the week: ", df['day'].mode()[0])

    # TO DO: display the most common start hour
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
    most_station = df['Start Station'].mode()[0]
    print("Most commonly used start station:",most_station)


    # TO DO: display most commonly used end station
    most_station = df['End Station'].mode()[0]
    print("Most commonly used end station: ",most_station)

    # TO DO: display most frequent combination of start station and end station trip
    print("Most frequent combination of start station and end station trip:",(df['Start Station'] + ' and ' + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])


    # TO DO: display total travel time
    df['Travel Time'] =  df['End Time'] - df['Start Time']
    print("Total travel time:",df['Trip Duration'].sum()//60, "minutes")



    # TO DO: display mean travel time
    print("Mean travel time: ",df['Trip Duration'].mean()//60,"minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print("Counts of user types:",user_types)


    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("Counts of gender:",gender)
    except:
        print("Gender not available")



    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("Earliest date of birth:",df['Birth Year'].min())
        print("Most recent date of birth:",df['Birth Year'].max())
        print("Most common date of birth:",df['Birth Year'].mode())
    except:
        print("Birth year not available")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
        start_loc = 0
        if view_data == 'yes':
            while True:
                end_loc = start_loc + 5
                print(df.iloc[start_loc:end_loc])
                start_loc += 5
                view_display = input("Do you wish to continue?: ").lower()
                if view_display == 'no':
                    break
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
