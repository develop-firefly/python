fgp = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']


def latest_file_load(path):
    """
    Method to fetch only the latest filesnames based on the date parameterm and filter specific fiels
    Input: Landing zone path
    Output: List of lists containing filenames, filesizes, filepathcs as Record count in the file
    Note: This function requires dbutils to be available in the environment. So run it in a Databricks notebook.
    """
    # Create an empty list to hold the filtered values.
    filelist = []
    # Iterate over all the files present in the landing zone
    for fd in dbutils.fs.ls(path):
        # Iterate over all the fiels presend in the landing location
        # Filter specfic files
        # Only consider .txt files
        # Filter any files where the modification timestamp is greater than defined threshold and less than the interval date
        if (any(_ in fd.name for _ in fgp) and fd.name.endswith('.txt')) and int(desired_ts(str_threshold_dt)[0]) <= fd.modificationTime <= int(desired_ts(str_threshold_dt)[-1]):
            # Append the filtered values to the list
            filelist.append([fd.name, fd.size, fd.path, (((spark.read.load('text', fd.path)).toPandas()).shape[0]-1)])
    return filelist
