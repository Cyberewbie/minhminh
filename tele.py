from telethon import TelegramClient, events, sync

# Replace these with your own values from https://my.telegram.org
api_id = 123456      # Your API ID (integer)
api_hash = 'your_api_hash_here'  # Your API hash (string)
session_name = 'my_session'      # This will create a .session file locally

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    # Print incoming message
    print(f"Message from {sender.username or sender.id}: {event.text}")

    # Reply to the message (optional)
    await event.reply('Hello! I got your message.')

def main():
    client.start()  # This will prompt for your phone number and code if no session exists
    print("Client started. Waiting for messages...")
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
