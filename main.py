from anki.deck import AnkiDecks
from anki.cards import AnkiCards

import asyncio
import os
import json
from dotenv import load_dotenv
from agent.helper_functions import print_ascii_art
from hume import HumeVoiceClient, MicrophoneInterface, VoiceSocket


message_counter = 0
answered = True
tool_call_id = None
tool_type = None


# Handler for when the connection is opened
def on_open():
    # Print a welcome message using ASCII art
    print_ascii_art("Say hello to EVI, Hume AI's Empathic Voice Interface!")


# Function to get the top N emotions based on their scores
def get_top_n_emotions(prosody_inferences, number):
    # Sort the inferences by their scores in descending order
    sorted_inferences = sorted(
        prosody_inferences.items(), key=lambda item: item[1], reverse=True
    )
    # Return the top N inferences
    return sorted_inferences[:number]


# Handler for when the connection is closed
def on_close():
    # Print a closing message using ASCII art
    print_ascii_art("Thank you for using EVI, Hume AI's Empathic Voice Interface!")


async def main() -> None:
    # Handler for incoming messages
    async def on_message(message):
        global message_counter, answered, tool_call_id, tool_type
        # Increment the message counter for each received message
        message_counter += 1
        msg_type = message["type"]

        # Start the message box with the common header
        message_box = f"\n{'='*60}\n" f"Message {message_counter}\n" f"{'-'*60}\n"

        # Add role and content for user and assistant messages
        if msg_type in {"user_message", "assistant_message"}:
            role = message["message"]["role"]
            content = message["message"]["content"]
            message_box += f"role: {role}\n" f"content: {content}\n" f"type: {msg_type}\n"

            # Add top emotions if available
            if "models" in message and "prosody" in message["models"]:
                scores = message["models"]["prosody"]["scores"]
                num = 3
                # Get the top N emotions based on the scores
                top_emotions = get_top_n_emotions(prosody_inferences=scores, number=num)

                message_box += f"{'-'*60}\nTop {num} Emotions:\n"
                for emotion, score in top_emotions:
                    message_box += f"{emotion}: {score:.4f}\n"
        elif msg_type == "tool_call":
            paras = json.loads(message["parameters"])
            ankicards.answerCards(paras["questionId"], paras["performance"])
            if tool_call_id is None and tool_type is None:
                answered = True
                tool_call_id = message["tool_call_id"]
                tool_type = message["tool_type"]
                message_box += f"tool_call \n"
            await socket.send_tool_response(
                content="you are pretty good at this!",
                tool_call_id=tool_call_id,
                tool_type="function",
            )
        elif msg_type != "audio_output":
            for key, value in message.items():
                message_box += f"{key}: {value}\n"
        else:
            message_box += f"type: {msg_type}\n"

        message_box += f"{'='*60}\n"
        # Print the constructed message box
        print(message_box)


    # ================================================ #
    #                     ANKI PART                    #
    # ================================================ #

    # fetch desk
    ankidesk = AnkiDecks()
    ankidesk.fetch_decks()

    # choose deck
    current_deck = {"name": "CalHacks", "id": 1719082606356}

    # fetch cards
    ankicards = AnkiCards(current_deck)
    ankicards.fetch_cards()

    # Handler for when an error occurs
    def on_error(error):
        # Print the error message
        print(f"Error: {error}")

    # Asynchronous handler for user input
    async def user_input_handler(socket: VoiceSocket):
        global answered, tool_call_id, tool_type
        while True:
            if answered:
                answered = False
                if tool_call_id is not None and tool_type is not None:
                    await socket.send_tool_response(
                        content="you are pretty good at this!",
                        tool_call_id=tool_call_id,
                        tool_type="function",
                    )
                    tool_call_id = None
                    tool_type = None
                resp = ankicards.fetch_card_info()
                resp_str = "When you are ready for next round of questions, say 'next' to continue, else keep silent.\n1"
                for card in resp:
                    resp_str += f"Question: {card['question']}  "
                    resp_str += f"Answer: {card['answer']}  "
                    resp_str += f"Question ID: {card['questionId']} \n"
                await socket.send_text_input(resp_str)

            else:
                # Asynchronously get user input to prevent blocking other operations
                user_input = await asyncio.to_thread(
                    input, "Type a message to send or 'Q' to quit: "
                )
                if user_input.strip().upper() == "Q":
                    # If user wants to quit, close the connection
                    print("Closing the connection...")
                    await socket.close()
                    break
                else:
                    # Send the user input as text to the socket
                    await socket.send_text_input(user_input)

    try:
        # ================================================ #
        #                    HUME PART                     #
        # ================================================ #

        # Retrieve the Hume API key from the environment variables
        load_dotenv()
        HUME_API_KEY = os.getenv("HUME_API_KEY")
        HUME_SECRET_KEY = os.getenv("HUME_SECRET_KEY")
        HUME_CONFIG_ID = os.getenv("HUME_CONFIG_ID")

        # Connect and authenticate with Hume
        client = HumeVoiceClient(
            HUME_API_KEY,
            HUME_SECRET_KEY,
        )

        async with client.connect_with_handlers(
            config_id=HUME_CONFIG_ID,
            on_open=on_open,  # Handler for when the connection is opened
            on_message=on_message,  # Handler for when a message is received
            on_error=on_error,  # Handler for when an error occurs
            on_close=on_close,  # Handler for when the connection is closed
            enable_audio=False,  # Flag to enable audio playback (True by default)
        ) as socket:
            # Start the microphone interface in the background; add "device=NUMBER" to specify device
            microphone_task = asyncio.create_task(
                MicrophoneInterface.start(
                    socket,
                    device=1,
                )
            )

            # Start the user input handler
            user_input_task = asyncio.create_task(user_input_handler(socket))

            # The gather function is used to run both async tasks simultaneously
            await asyncio.gather(microphone_task, user_input_task)
    except Exception as e:
        # Catch and print any exceptions that occur
        print(f"Exception occurred: {e}")


asyncio.run(main())
