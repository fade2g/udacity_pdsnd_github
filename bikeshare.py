import time
import datetime

import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
MONTH_DICT = {0: 'all', 1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
DAYS_OF_WEEK_DICT = {0: 'all', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                     7: 'Sunday'}


def get_city():
    """
    Asks a user to enter the name of the city to be analysed. Allowed cities are limited to the available data
    :return: (str) The name of the city to be analysed
    """
    success = False
    city = None
    while not success:
        print('Which city should be analyzed? Choice of ' + ', '.join(CITY_DATA.keys()))
        city = input('City? ')
        if city.lower() not in CITY_DATA.keys():
            print('The city name you entered is not correct. Please try again')
        else:
            success = True

    return city.lower()


def get_month():
    """
    Asks a user to enter the month to be analysed,
    :return: (int) 0 for all months, otherwise 1 to 6 for the number of the month (January to June)
    """
    success = False
    month = None
    while not success:
        print('Which month should be analyzed?')
        for key in MONTH_DICT:
            print('{0}: {1}'.format(key, MONTH_DICT[key]))
        month = input('Month? ')
        if not month.isnumeric() or int(month) not in MONTH_DICT.keys():
            print('The month must be one of {0} Please try again'.format(', '.join(map(str, MONTH_DICT.keys()))))
        else:
            success = True

    return int(month)


def get_day_of_week():
    """
    Asks a user for the day of the week to be analysed (e.g. only thuesdays or all days)
    :return: (int) 0 for no day of week filter, 1 to 7 for Monday to Sunday
    """
    print('Which day of the week shall be analyzed?')
    for key in DAYS_OF_WEEK_DICT:
        print('{0}: {1}'.format(key, DAYS_OF_WEEK_DICT[key]))
    day_of_week = input('Day of week? ')
    if not day_of_week.isnumeric() or int(day_of_week) not in MONTH_DICT.keys():
        print('The day of the week must be one of {0}. Please try again'.format(
            ', '.join(map(str, DAYS_OF_WEEK_DICT.keys()))))
    else:
        success = True

    return int(day_of_week)


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_city()

    # get user input for month (all, january, february, ... , june)
    month_number = get_month()
    month = MONTH_DICT[month_number]

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_the_week_number = get_day_of_week()
    day = DAYS_OF_WEEK_DICT[day_of_the_week_number]

    print('-' * 40)
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
    df = pd.read_csv(f'data/{CITY_DATA[city]}',
                     parse_dates=['Start Time', 'End Time'],
                     date_format={1: '%Y-%m-%d %H:%M:%S'})

    month_number = list(MONTH_DICT.keys())[list(MONTH_DICT.values()).index(month)]
    if month_number > 0:
        df = df[(df['Start Time'] >= pd.Timestamp(2017, month_number, 1))
                & (df['Start Time'] < pd.Timestamp(2017, (month_number + 1), 1))]

    weekday_number = list(DAYS_OF_WEEK_DICT.keys())[list(DAYS_OF_WEEK_DICT.values()).index(day)]
    if weekday_number > 0:
        df = df[(df['Start Time']
                 .apply(lambda x: x.isoweekday() == weekday_number))]

    return df


def _find_mode_and_count_for_column(df, col):
    """
    Calculates the mode of a column and also returns the number of rides for the corresponding mode
    :param df: DataFrame that contains the column
    :param col: (str) Name of the column
    :return:
    """

    # The value in the column, that occurs the most
    mode_value = df[col].mode()[0]
    # Now determine the number of rows that the mode has
    occurrences_count = df[(df[col] == mode_value)][col].count()
    return mode_value, occurrences_count


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()
    df_start = df[['Start Time']].copy()
    df_start['month'] = df_start['Start Time'].dt.strftime('%Y-%m')
    df_start['day of week'] = df_start['Start Time'].apply(lambda x: x.isoweekday())
    df_start['hour of day'] = df_start['Start Time'].dt.hour

    month, month_count = _find_mode_and_count_for_column(df_start, 'month')
    print(f'  Most frequently travelled month is \'{month}\' with {month_count} rides')

    day_of_week, day_of_week_count = _find_mode_and_count_for_column(df_start, 'day of week')
    print(
        f'  Most frequently travelled day of week ist \'{DAYS_OF_WEEK_DICT[day_of_week]}\' with {day_of_week_count} rides')

    hour, hour_count = _find_mode_and_count_for_column(df_start, 'hour of day')
    print(f'  Most frequently travelled hour of day is \'{hour}\' with {hour_count} rides')

    print(f"\n  Calculation took {(time.time() - start_time):.2f} seconds.")
    print('  ' + '-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()
    df_start = df[['Start Station', 'End Station']].copy()
    df_start['Combined'] = (df_start[['Start Station', 'End Station']]
                            .apply(lambda single_row: ' -> '.join(single_row.values), axis=1))

    start, start_count = _find_mode_and_count_for_column(df_start, 'Start Station')
    print(f'  Most commonly used station \'{start}\' has {start_count} departures')

    start_end, start_end_count = _find_mode_and_count_for_column(df_start, 'Combined')
    print(f'  Most commonly used start-end-combination \'{start_end}\' has {start_end_count} rides')

    print(f"\n  Calculation took {(time.time() - start_time):.2f} seconds.")
    print('  ' + '-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total = datetime.timedelta(seconds=int(total_travel_time))
    print(f'  Total travel time is {str(total)}.')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'  The mean travel time is {mean_travel_time:.2f} seconds or {mean_travel_time / 60:.2f} minutes.')

    print(f"\n  Calculation took {(time.time() - start_time):.2f} seconds.")
    print('  ' + '-' * 40)


def _user_stats(df, cols):
    """
    Internal function that groups the dataframe by the cols and displays the results of occurrences
    :param df: Data Frame to be analyzes
    :param cols: String containing the columns, by which the dataframe shall be grouped
    :return:
    """
    print(f'Statistics for Attribute \'{cols}\'')
    total_rides = df[cols].count()
    for name, group in df.groupby(by=[cols])[cols]:
        print(
            f'  Gender \'{name[0]}\' has {group.count()} ({group.count() / total_rides * 100:.1f}%) rides of {total_rides} total rides')


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...')
    start_time = time.time()

    _user_stats(df, 'User Type')

    if 'Gender' in df.columns:
        print()
        _user_stats(df, 'Gender')

    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        print()
        print('Statistics for birth year:')
        # Store calculations in a dict to allow iterating over the result
        year_stats = {
            'earliest': int(df['Birth Year'].min()),
            'most recent': int(df['Birth Year'].max()),
            'most common': int(df['Birth Year'].mode()[0])
        }
        for key, value in year_stats.items():
            print(f'  {key.capitalize()} year: {value}')

    print(f"\n  Calculation took {(time.time() - start_time):.2f} seconds.")
    print('  ' + '-' * 40)


def handle_statistics(df):
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)


def _get_possible_answer(question, possible_answers):
    answer = None
    while True:
        answer = input(f'{question} Possible are: {", ".join(possible_answers)}\n')
        if answer.lower() in possible_answers:
            break

        print('Please type one of the allowed values.')

    return answer.lower()


def handle_raw(df):
    pd.set_option('display.max_columns', 200)
    page_size = 5
    start_pos = 0
    more = None
    while more != 'quit':
        print(df[start_pos:(start_pos + page_size)])
        more = _get_possible_answer(f'Enter \'+\' for the next {page_size} rows. \'quit\' will exit.', ['+', 'quit'])
        if more == '+':
            start_pos += page_size


def main():
    while True:
        city, month, day = get_filters()

        print(f'Load data for city \'{city}\' for month \'{month}\' and day of week \'{day}\'')
        df = load_data(city, month, day)

        raw = _get_possible_answer('Do you want to see inspect data?', ['yes', 'no'])
        if raw == 'yes':
            print(f'Display raw data for city \'{city}\' for month \'{month}\' and day of week \'{day}\'')
            handle_raw(df)
        elif raw == 'no':
            print(f'Calculate statistics for city \'{city}\' for month \'{month}\' and day of week \'{day}\'')
            handle_statistics(df)
        else:
            print('Only \'yes\' or \'no\' are accepted')

        restart = _get_possible_answer('\nWould you like to restart?', ['yes', 'no'])
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
