from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now() + timedelta(hours=8)
    
    day_num = int(now.strftime("%j"))
    week_num = now.isocalendar()[1]
    
    # Logic for your custom duties
    # Day is Odd -> ayy, Even -> ism
    if day_num % 2 != 0:
        is_day_odd = "Odd day"
        neko_status = "Ayy" 
    else: 
        is_day_odd = "Even day"
        neko_status = "Ism"
    
    # Week is Even -> ayy, Odd -> ism
    if week_num % 2 != 0:
        is_week_odd = "Odd week"
        wipey_status = "Ism" 
    else: 
        is_week_odd = "Even week"
        wipey_status = "Ayy"

    context = {
        "full_date_time": now.strftime("%B %d, %Y | %H:%M"),
        "day_of_year": day_num,
        "is_day_odd": is_day_odd,
        "week_number": week_num,
        "is_week_odd": is_week_odd,
        "neko_status": neko_status,
        "wipey_status": wipey_status
    }
    
    return render_template('index.html', data=context)

if __name__ == '__main__':
    app.run(debug=True, port=8080)