import requests,time,json
from datetime import datetime

known_list=[]
while True:
    date = datetime.now().strftime("%d-%m-%Y")
    url=f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=294&date={date}"

    r = requests.get(url)
    # print(r.text)

    with open("data.json","w") as f:
        f.write(json.dumps(r.json(), indent=2))

    data = r.json()['centers']
    for center in data:
        for session in center['sessions']:
            if not session['session_id'] in known_list:
                known_list.append(session['session_id'])
                now = datetime.now().strftime("%d-%m-%Y,%H:%M,%A")
                with open("log.csv","a") as f:
                    f.write(f"{center['name']},{center['address']},{session['date']},{session['available_capacity']},{session['min_age_limit']},{session['vaccine']},{now}\n")


    time.sleep(5)