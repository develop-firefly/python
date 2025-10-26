def get_current_user():
    """
    Method to get the currently logged on user
    Input: None
    Output: UPN-ID of the currently logged on user
    Note: This function requires dbutils to be available in the environment. So run it in a Databricks notebook.
    """
    return (dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get())
