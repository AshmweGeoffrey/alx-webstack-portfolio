from flask import Blueprint, jsonify, request
from models.sale_weekly import sale_weekly
from . import api
from datetime import datetime, timedelta
# api endpoint to get all sales,order by time_stamp
@api.route('/sales', methods=['GET'])
def get_sales():
    from_date=request.args.get('from')
    to_date=request.args.get('to')
    print(from_date)
    print(to_date)
    if from_date and to_date:
        order = "WHERE time_stamp BETWEEN '{}' AND '{}' ORDER BY time_stamp DESC".format(from_date, to_date)
    else:
        # Calculate last Monday's date
        today = datetime.now()
        # Find last Monday (if today is Wednesday, get the Monday of the same week)
        last_monday = today - timedelta(days=today.weekday() + 1) if today.weekday() >= 0 else today
        # Format the last Monday to a string (assuming your timestamp is in 'YYYY-MM-DD' format)
        last_monday_str = last_monday.strftime('%Y-%m-%d')
        # Modify the order to select from last Monday to now
        order = "WHERE time_stamp >= '{}' ORDER BY time_stamp DESC".format(last_monday_str)
    sale_weekly_1= sale_weekly().select_all(order)
    return jsonify(sale_weekly_1)
