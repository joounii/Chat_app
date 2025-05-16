import os
from dotenv import load_dotenv
from google import genai
import tkinter as tk

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

def get_answer(content):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=content,
    )

    return(response.text)

def send_message():
    user_text = input_entry.get()
    if user_text:
        # Display the user's message
        user_label = tk.Label(chat_frame, text=f"You: {user_text}", anchor="w", justify="left")
        user_label.pack(padx=10, pady=5, fill="x")

        # AI response
        # ai_response = "Gemini: " + get_answer(user_text)
        ai_response = "Gemini: " + "gemini will answer here"
        ai_label = tk.Label(chat_frame, text=ai_response, anchor="w", justify="left", bg="#f0f0f0")
        ai_label.pack(padx=10, pady=5, fill="x")

        # Clear the input field
        input_entry.delete(0, tk.END)

def _on_mousewheel(event):
    chat_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Create the main window
window = tk.Tk()
window.title("Chat")

# Create a frame to hold the chat messages (for scrolling later)
chat_frame = tk.Frame(window)
chat_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Create a scrollbar for the chat frame (optional but good for longer chats)
scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side="right", fill="y")

# Configure the chat frame to use the scrollbar
chat_canvas = tk.Canvas(chat_frame, yscrollcommand=scrollbar.set)
chat_canvas.pack(side="left", fill="both", expand=True)
scrollbar.config(command=chat_canvas.yview)
chat_canvas.bind('<Configure>', lambda e: chat_canvas.configure(scrollregion = chat_canvas.bbox("all")))

inner_frame = tk.Frame(chat_canvas)
chat_canvas.create_window((0, 0), window=inner_frame, anchor="nw")
chat_frame = inner_frame # Update chat_frame to be the inner frame

# Bind mouse wheel events to the canvas
chat_canvas.bind("<MouseWheel>", _on_mousewheel)
chat_canvas.bind("<Button-4>", lambda event: chat_canvas.yview_scroll(-1, "units")) # For Linux
chat_canvas.bind("<Button-5>", lambda event: chat_canvas.yview_scroll(1, "units"))  # For Linux

# Create the input field
input_entry = tk.Entry(window)
input_entry.pack(padx=10, pady=5, fill="x")

# Create the send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
