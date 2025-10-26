import datetime
import calendar

str_threshold_dt='08/29/2023'
end_threshold_dr_interval = 7

def desired_ts(str_threshold_dt):
    """
    Method to get the desired timestamp based on the threshold date
    Input: str_threshold_dt - Threshold date in 'MM/DD/YYYY' format
    Output: Epoch Timestamp
    """
    # split the date into variables
    str_mm, str_dd, str_y4 = str_threshold_dt.split('/')[0], str_threshold_dt.split('/')[1], str_threshold_dt.split('/')[-1]
    # Conver the standard input date format to URC time and generate the start and end timestamps
    str_time_tuple = datetime.datetime(int(str_y4), int(str_mm), int(str_dd))
    end_time_tuple = str_time_tuple + datetime.timedelta(days=end_threshold_dr_interval)
    # Conver the UTC time to epoch and add additional zeros to match the length of databricks modification timestamp
    str_file_load_epoch=str(calendar.timegm(str_time_tuple.timetuple())) + '000'
    end_file_load_epoch=str(calendar.timegm(end_time_tuple.timetuple())) + '000'
    return str_file_load_epoch, end_file_load_epoch