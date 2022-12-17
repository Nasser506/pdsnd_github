import time
import pandas as pd
import numpy as np

# Dictionary contains city and its corresponding csv file name
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
#this change is made for github project to add commit .
Myname ="Nasser" 

# this function is to select the filters to be applied it's very important
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid
    # inputs Take the inputs from the user
    city = input("\nPlease enter a city from the following: 1.chicago 2.new york city 3.washington\n").lower()

    # while loop to make sure that the user entered the correct name of city (option)
    while (city not in CITY_DATA.keys()):
        city = input("\nPlease enter a city from the following: 1.chicago 2.new york city 3.washington\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    #
    months = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
    month = input(
        '\nPlease enter month from the folloiwng to filter by:\n\njanuary, february, march, april, may, june\n\nnote:type "all" for no month filtering\n').title()
    # while loop to make sure that the user entered the correct name of month
    while (month not in months):
        month = input(
            'Please enter month from the folloiwng to filter by\njanuary, february, march, april, may, june\ntype "all" for no month filtering\n').title()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = input('\nPlease enter day of the week to filter by\ntype "all" for no day filtering\n').title()
    # while loop to make sure that the user entered the day name in the correct way
    while (day not in days):
        day = input('\nPlease enter a correct day of the week to filter by\ntype "all" for no day filtering\n').title()

    print('\nyour choice was :\ncity: {}\nmonth: {}\nday: {}\n'.format(city, month, day))
    print('-' * 40)

    return city, month, day


# Function to load the selected csv file
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

    # creating data frame from csv
    df = pd.read_csv(CITY_DATA[city])

    # converting Start Time row into datetime data type
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracting month and week day from 'Start Time' row
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of Week'] = df['Start Time'].dt.day_name()

    # filter by month
    if month != 'All':
        df = df[df['Month'] == month]

    # filter by day
    if day != 'All':
        df = df[df['Day of Week'] == day.title()]

    # Returns the selected file as a dataframe (df) with relevant columns
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
       Args: df : the data frame
       Returns: Nothing
       """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    # displaying Most common month using pandas mode() method
    print('\nMost common month is: ', df['Month'].mode()[0])

    # TO DO: display the most common day of week

    # displaying Most common day using pandas mode() method
    print('\nMost common day is: ', df['Day of Week'].mode()[0])

    # TO DO: display the most common start hour

    # Extracting Hour column from 'Start Time' column
    df['Hour'] = df['Start Time'].dt.hour

    # displaying Most common start Hour using pandas mode() method
    hr = df['Hour'].mode()[0]

    # to convert 24 hour format into 12 hour format
    if hr <= 12:
        print('\nMost common start hour is: {} AM'.format(hr))
    else:
        print('\nMost common start hour is: {} PM'.format(hr % 12))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
       Args: df : the data frame
       Returns: Nothing
       """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    # displaying Most commonly used start station using pandas mode() method
    print('\nMost commonly used start station is: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station

    # displaying Most commonly end station using pandas mode() method
    print('\nMost commonly end station is: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip

    # Creating a new calculated column for 'Start & End' stations
    df['Start & End'] = df['Start Station'].str.cat(df['End Station'], sep=' --> ')

    # displaying Most frequent combination of start station and end station trip using pandas mode() method
    print('\nMost frequent combination of start station and end station trip is: ', df['Start & End'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
       Args: df : the data frame
       Returns: Nothing
       """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    # displaying total travel time using sum() method
    print('\nTotal travel duration is: ', df['Trip Duration'].sum())

    # TO DO: display mean travel time

    # displaying average travel time using mean() method
    print('\nAverage travel duration is: ', df['Trip Duration'].mean())

    # extra statistics
    # what is the largest and smallest duration of travel time

    print('\nLargest travel duration is: ', df['Trip Duration'].max())
    print('\nSmallest travel duration is: ', df['Trip Duration'].min())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users.
       Args: df : the data frame
       Returns: Nothing
       """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    # displaying counts of user types using value_counts() method
    print('\nCounts of user types: \n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # displaying counts of gender using value_counts() method
    # handling any error would show up because 'washington' csv file has no Gender column
    try:
        print('\nCounts of gender: \n', df['Gender'].value_counts())
    except:
        print('\nSorry, Whasington has no "Gender" informations')

    # TO DO: Display earliest, most recent, and most common year of birth

    # displaying earliest, most recent, and most common year of birth
    # handling any error would show up because 'washington' csv file has no Birth Year column
    try:
        oldest = int(df['Birth Year'].min())
        youngest = int(df['Birth Year'].max())
        most = int(df['Birth Year'].mode())
        print('\nOldest User/Customer year of birth is: ', oldest)
        print('\nYoungest User/Customer year of birth is: ', youngest)
        print('\nMost common User/Customer year of birth is: ', most)
    except:
        print('\nSorry, Whasington has no "year of birth" informations')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)



def display_raw_data(city):
    """Show 5 records from the selected city.
    Asks user to type if he wants to show raw data or not

    Args:
        (df): the data frame of the selected city.
    Returns:
        Nothing.
    """
    df = pd.read_csv(CITY_DATA[city])
    answers = ['no','yes']
    user_input = ''

    #counter to use later in displaying raw data with df.head() method
    i = 0

    #if the user wants to see more records
    while user_input not in answers:
        print("\nDo you wanna see raw data records?")
        print("\nPlease type: Yes or No\n")
        user_input = input().lower()

        #displaying 5 records of raw data if user says yes using df.head() method
        if user_input == "yes":
            print(df.head())
        elif user_input not in answers:
            print("\nPlease enter a right answer.")

    #Another loop to ask the user if he wants more data to be displayed
    while user_input == 'yes':
        print("\nDo you wanna see MORE raw data records?\n")
        i += 5
        user_input = input().lower()
        #If yes -> display more 5 records, else -> break
        if user_input == "yes":
             print(df[i:i+5])
        elif user_input != "yes":
             break

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

    display_raw_data(city)

#Main function to call all the previous functions

if __name__ == "__main__":
	main()