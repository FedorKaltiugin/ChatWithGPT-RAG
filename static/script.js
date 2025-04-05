// Send message to the server and update chat UI
async function sendMessage() {
    const input = document.getElementById("message");
    const chatBox = document.getElementById("chat-box");

    const msg = input.value.trim();
    if (!msg) return;

    // Display user's message in the chat box
    const userMessage = document.createElement("div");
    userMessage.classList.add("message", "user");
    userMessage.textContent = `You: ${msg}`;
    chatBox.appendChild(userMessage);

    input.value = "";

    // Send user input to the backend via POST request
    const response = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: msg})
    });

    const data = await response.json();

    // Display bot's reply in the chat box
    const botMessage = document.createElement("div");
    botMessage.classList.add("message", "bot");
    botMessage.textContent = `Bot: ${data.reply}`;
    chatBox.appendChild(botMessage);

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
}
