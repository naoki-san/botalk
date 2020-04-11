<template>
  <div>
    <ul>
      <li v-for="message in messages" :key="message.timestamp">
        {{ message.body }} name: {{ message.name }}
      </li>
    </ul>
    <input v-model="message" />
    <button v-on:click="sendTextMessage">Send</button>
    <button v-on:click="startVoiceInput">Voice</button>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      message: "",
      messages: []
    };
  },
  methods: {
    sendMessage: async function(message) {
      this.messages.push({
        name: "Me",
        body: message,
        timestamp: Date.now()
      });

      const data = { message };
      const response = await fetch("http://localhost:5000/message", {
        method: "POST",
        headers: {
          "Content-Type": "application/json; charset=utf-8"
        },
        body: JSON.stringify(data)
      });
      const json = await response.json();

      const synth = window.speechSynthesis;
      const utterThis = new SpeechSynthesisUtterance(json.message);
      synth.speak(utterThis);

      this.messages.push({
        name: "Bot",
        body: json.message,
        timestamp: Date.now()
      });
    },
    sendTextMessage: function() {
      this.sendMessage(this.message);
      this.message = "";
    },
    startVoiceInput: function() {
      const recognition = new window.webkitSpeechRecognition();
      recognition.lang = 'en-US';
      recognition.onresult = event => {
        const message = event.results[0][0].transcript;
        this.sendMessage(message);
      };
      recognition.start();
    }
  }
};
</script>

<style scoped></style>
