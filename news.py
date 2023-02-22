import pyrogram
import requests
import datetime

NEWS_API_KEY = "VtVQhAqTe6tqVihjinWz3Qxw7akRE5Wm"

app = pyrogram.Client("mybot", api_id=10816184, api_hash="54fcbe09fa0ea55509bf88bd04a9aff0", bot_token="5568157345:AAHs36IOywVMJ3RB1DOoXHLW3yO5LnOQg9k")


# Function to get time and date of Kolkata in 12 hour format
def get_kolkata_time():
    # Set the timezone to Asia/Kolkata
    kolkata_tz = pytz.timezone('Asia/Kolkata')
    # Get the current time in Kolkata
    kolkata_time = datetime.datetime.now(kolkata_tz)
    # Format the time string in 12-hour format
    kolkata_time_str = kolkata_time.strftime('%I:%M %p, %d %B %Y')
    # Return the time string
    return kolkata_time_str

# Command handler for /time command
@app.on_message(pyrogram.filters.command("time"))
def send_time(client, message):
    # Get the current time in Kolkata
    kolkata_time = get_kolkata_time()
    # Send the time string as a reply to the message
    message.reply_text(f"Current time in Kolkata: {kolkata_time}")



def get_news_headlines():
    url = f"https://api.nytimes.com/svc/topstories/v2/world.json?api-key={NEWS_API_KEY}"
    response = requests.get(url)
    news = response.json()
    headlines = [article["title"] for article in news["articles"]]
    return headlines

@app.on_message(pyrogram.filters.command("news"))
def news(client, message):
    headlines = get_news_headlines()
    if len(headlines) > 0:
        message.reply_text("\n\n".join(headlines))
    else:
        message.reply_text("Sorry, could not fetch any news headlines.")

app.run()
