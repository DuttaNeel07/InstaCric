from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from notifypy import Notify

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

print("\nOpening live match page")

driver.get("https://www.cricketworld.com/cricket/live")

time.sleep(5)

competitions = driver.find_elements(
    By.CLASS_NAME,
    "competition"
)

print("Competitions Found:", len(competitions))

ipl_link = ""

for comp in competitions:

    try:

        heading = comp.find_element(
            By.TAG_NAME,
            "h2"
        )

        heading_text = heading.text.strip()

        print("\nTournament:")
        print(heading_text)

        if "Indian Premier League" in heading_text:

            print("\nIPL FOUND")

            match = comp.find_element(
                By.CLASS_NAME,
                "match-row"
            )

            ipl_link = match.get_attribute("href")

            print("IPL LINK:")
            print(ipl_link)

            break

    except Exception as e:

        print("Competition Error:", e)

if ipl_link == "":

    print("\nNo IPL live match found")

    driver.quit()

    exit()

old_events = ""

while True:

    try:

        print("\nRefreshing IPL match page")

        driver.get(ipl_link)

        time.sleep(5)

        recent_div = driver.find_element(
            By.CLASS_NAME,
            "live-info4"
        )

        spans = recent_div.find_elements(
            By.TAG_NAME,
            "span"
        )

        print("\nEvents Found:", len(spans))

        events = []

        for span in spans:

            text = span.text.strip()

            span_class = span.get_attribute("class")

            event = {
                "text": text,
                "class": span_class
            }

            events.append(event)

        print("\nALL EVENTS:")

        for e in events:

            print(e)

        current_events = str(events)

        if current_events != old_events:

            print("\nNEW UPDATE DETECTED")

            if len(events) > 0:

                latest_event = events[0]

                latest_text = latest_event["text"]

                latest_class = latest_event["class"]

                print("\nLATEST EVENT:")
                print("Text :", latest_text)
                print("Class:", latest_class)

                if "run4" in latest_class:

                    print("\nFOUR!")

                    notification = Notify()

                    notification.title = "🏏 FOUR"

                    notification.message = "Boundary scored"

                    notification.send()

                elif "run6" in latest_class:

                    print("\nSIX!")

                    notification = Notify()

                    notification.title = "🏏 SIX"

                    notification.message = "Maximum scored"

                    notification.send()

                elif "wicket" in latest_class.lower():

                    print("\nWICKET!")

                    notification = Notify()

                    notification.title = "🏏 WICKET"

                    notification.message = "Batsman Out"

                    notification.send()
                else:

                    print("\nNormal ball event")

            old_events = current_events

        else:

            print("\nNo new updates")

        print("\nWaiting 10 seconds...\n")

        time.sleep(10)

    except Exception as e:

        print("\nERROR:", e)

        print("\nRetrying in 15 seconds...\n")

        time.sleep(15)