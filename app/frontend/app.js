const chat = document.getElementById("chat");
const form = document.getElementById("ask-form");
const input = document.getElementById("question");

function addMessage(role, text) {
  const div = document.createElement("div");
  div.className = `msg ${role}`;
  div.textContent = text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
  return div;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const question = input.value.trim();
  if (!question) return;

  addMessage("user", question);
  input.value = "";
  const pending = addMessage("assistant", "Thinking...");

  try {
    const res = await fetch("/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });
    if (!res.ok) throw new Error(`Request failed: ${res.status}`);
    const data = await res.json();
    pending.textContent = data.answer;
    if (data.sources?.length) {
      const sourceLine = document.createElement("div");
      sourceLine.className = "sources";
      sourceLine.textContent = "Pages: " + data.sources.map(s => s.page_number).join(", ");
      pending.appendChild(sourceLine);
    }
  } catch (err) {
    pending.textContent = "Error: " + err.message;
  }
});
